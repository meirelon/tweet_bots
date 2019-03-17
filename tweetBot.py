import argparse
from datetime import datetime
import pickle

from twitter_scraper import get_tweets
import markovify

def tweetBot(twitter_handle):
    tweets = '\n'.join([t['text'] for t in get_tweets(twitter_handle, pages=25)])
    return markovify.Text(tweets)

def main(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--twitter_handle',
                        dest='twitter_handle',
                        default = None,
                        help='Insert Twitter Handle')

    args, _ = parser.parse_known_args(argv)

    bot = tweetBot(args.twitter_handle)
    with open('bots/{}_{}.pkl'.format(args.twitter_handle.lower(), datetime.now().strftime("%Y%m%d")), "wb") as f:
        pickle.dump(bot, f)

if __name__ == '__main__':
    main()
