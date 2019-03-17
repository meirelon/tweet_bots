# tweet_bots

Insert any public Twitter handle and markovify will build a model to generate fake tweets.

## Getting Started

```
git clone https://github.com/meirelon/tweet_bots.git
cd tweet_bots
pip install -r requirements.txt
```

## Example
### CLI
Save a twitter bot model locally
```
python tweetBot.py --twitter_handle=elonmusk
```
Inside Python Terminal
```
from tweetBot import tweetBot
bot = tweetBot('elonmusk')
bot.make_short_sentence(140)
```
