import argparse
from datetime import datetime, timedelta
import tweepy


class twitterApi:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
        self.access_token=access_token
        self.access_token_secret=access_token_secret


    def twitter_auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)

    def delete_tweets(self, before=None):
        api = self.twitter_auth()
        if before is None:
            before = datetime.now() - timedelta(days=365)
        tweets = [x for x in tweepy.Cursor(api.user_timeline).items()]
        for tweet in tweets:
            if tweet.created_at < before:
                tweet.destroy()

    def unfollow(self, screen_name):
        api = self.twitter_auth()
        following = api.friends_ids(screen_name)
        followers = api.followers_ids(screen_name)
        for f in following:
            if f not in followers:
                api.destroy_friendship(f)


def main(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--consumer_key',
                        dest='consumer_key',
                        default = None,
                        help='consumer key')
    parser.add_argument('--consumer_secret',
                        dest='consumer_secret',
                        default = None,
                        help='consumer secret')
    parser.add_argument('--access_token',
                        dest='access_token',
                        default = None,
                        help='access token')
    parser.add_argument('--access_token_secret',
                        dest='access_token_secret',
                        default = None,
                        help='access token secret')
    parser.add_argument('--screen_name',
                        dest='screen_name',
                        default = None,
                        help='screen name')

    args, _ = parser.parse_known_args(argv)

    twitter = twitterApi(args.consumer_key,
                         args.consumer_secret,
                         args.access_token,
                         args.access_token_secret)
    twitter.delete_tweets()
    if args.screen_name is not None:
        twitter.unfollow(args.screen_name)


if __name__ == '__main__':
    main()
