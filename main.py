import argparse
from datetime import datetime, timedelta
import logging
import sys

import requests
import twitter
import tweepy
from secrets import consumer_key, consumer_secret_key, access_token, access_token_secret, bearer_token


tweeter_obj = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret_key,
                            access_token=access_token, access_token_secret=access_token_secret,
                            wait_on_rate_limit=True)



LOGGING_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

# LAX is good for testing
LOCATIONS = [
    #('SFO', 5446),
    #('LAX', 5180),
     ('RIC', 14981),
     ('TPA', 8020),
     ('IOW', 16461)
]

DELTA = 50  # Weeks

SCHEDULER_API_URL = 'https://ttp.cbp.dhs.gov/schedulerapi/locations/{location}/slots?startTimestamp={start}&endTimestamp={end}'
TTP_TIME_FORMAT = '%Y-%m-%dT%H:%M'

NOTIF_MESSAGE = 'New appointment slot open at {location}: {date}'
MESSAGE_TIME_FORMAT = '%A, %B %d, %Y at %I:%M %p'

def tweet(message):

    try:
        tweeter_obj.create_tweet(text=message)
    except twitter.TwitterError as e:
        if len(e.message) == 1 and e.message[0]['code'] == 187:
            logging.info('Tweet rejected (duplicate status)')
        else:
            raise

def check_for_openings(location_name, location_code, test_mode=True):
    start = datetime.now()
    end = start + timedelta(weeks=DELTA)

    url = SCHEDULER_API_URL.format(location=location_code,
                                   start=start.strftime(TTP_TIME_FORMAT),
                                   end=end.strftime(TTP_TIME_FORMAT))
    try:
        results = requests.get(url).json()  # List of flat appointment objects
    except requests.ConnectionError:
        logging.exception('Could not connect to scheduler API')
        sys.exit(1)

    for result in results:
        if result['active'] > 0:
            logging.info('Opening found for {}'.format(location_name))

            timestamp = datetime.strptime(result['timestamp'], TTP_TIME_FORMAT)
            message = NOTIF_MESSAGE.format(location=location_name,
                                           date=timestamp.strftime(MESSAGE_TIME_FORMAT))
            if test_mode:
                print(message)
            else:
                logging.info('Tweeting: ' + message)
                tweet(message)
            return  # Halt on first match

    logging.info('No openings for {}'.format(location_name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', '-t', action='store_true', default=False)
    parser.add_argument('--verbose', '-v', action='store_true', default=False)
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(format=LOGGING_FORMAT,
                            level=logging.INFO,
                            stream=sys.stdout)

    logging.info('Starting checks (locations: {})'.format(len(LOCATIONS)))
    for location_name, location_code in LOCATIONS:
        check_for_openings(location_name, location_code, args.test)

if __name__ == '__main__':
    main()
