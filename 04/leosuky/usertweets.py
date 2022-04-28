from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', 'id_str created_at text')


class UserTweets(object):

    def __init__(self, handle, max_id=None):
        """Get handle and optional max_id.
        Use tweepy.OAuthHandler, set_access_token and tweepy.API
        to create api interface.
        Use _get_tweets() helper to get a list of tweets.
        Save the tweets as data/<handle>.csv"""
        # ...
        self.handle = handle
        self.max_id = max_id

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        self.api = tweepy.API(auth)
        
        self._tweets = list(self._get_tweets())
        print(f'There are {len(self._tweets)} number of tweets')
        self.output = self._save_tweets()

    def _get_tweets(self):
        """Hint: use the user_timeline() method on the api you defined in init.
        See tweepy API reference: http://docs.tweepy.org/en/v3.5.0/api.html
        Use a list comprehension / generator to filter out fields
        id_str created_at text (optionally use namedtuple)"""
        tweets = (self.api).user_timeline(
            screen_name=self.handle,
            count= NUM_TWEETS,
            since_id = self.max_id
        )

        return tweets

    def _save_tweets(self):
        """Use the csv module (csv.writer) to write out the tweets.
        If you use a namedtuple get the column names with Tweet._fields.
        Otherwise define them as: id_str created_at text
        You can use writerow for the header, writerows for the rows"""

        if not os.path.exists(DEST_DIR):
            os.makedirs(DEST_DIR)

        filepath = f'./{DEST_DIR}/{self.handle}.{EXT}'

        with open(filepath, 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['id_str', 'created_at', 'text'])
            for tweet in self._tweets:
                writer.writerow([tweet.id_str, tweet.created_at, tweet.text])

        return filepath

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, pos):
        return (self._tweets)[pos]


if __name__ == "__main__":

    for handle in ('pybites', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()