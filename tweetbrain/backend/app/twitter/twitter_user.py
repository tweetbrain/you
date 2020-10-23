import re
import tweepy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


from ..config import Config

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("stopwords")
nltk.download("punkt")


class TwitterUser:

    auth = tweepy.AppAuthHandler(Config.CONSUMER_KEY, Config.CONSUMER_SECRET)

    #Construct the API instance
    api = tweepy.API(auth, wait_on_rate_limit=True) # create an API object

    # create tokenizer that gets words (only alphabetical words)
    tokenizer = RegexpTokenizer(r'\w+')


    stopwords = set(stopwords.words('english'))
    stopwords.update({
        "https",
        "http"
    })

    def __init__(self, handle: str):
        self.handle = handle
        self.user = self.api.get_user(handle)
        self.bio = self.user.description
        self.timeline = self.user.timeline(count=200)
        self.num_of_tweets = len(self.timeline)
        self.verified = self.user.verified
        self.stopwords.add(handle)


    def get_top_words(self, limit: int = 10, word_len_min: int = 2) -> list:
        '''
        Return top common words from tweets
        '''
        all_words = list()

        for tweet in self.timeline:
            # print(tweet.text, "\n-----\n\n\n")
            words = self.tokenizer.tokenize(tweet.text)
            for word in words:
                if len(word) > word_len_min and word not in self.stopwords:
                    all_words.append(word.lower())

        word_distribution = nltk.FreqDist(all_words)
        top_words = word_distribution.most_common(limit)
        return top_words


    def get_top_hashtags(self, limit: int = 10, word_len_min: int = 2) -> list:
        '''
        Return top common hashtags from tweets
        '''
        all_words = list()

        for tweet in self.timeline:
            # print(tweet.text, "\n-----\n\n\n")
            words = re.findall(r"(\#[a-zA-Z]+\b)(?!;)", tweet.text)
            for word in words:
                if len(word) > word_len_min and word not in self.stopwords:
                    all_words.append(word.lower())

        word_distribution = nltk.FreqDist(all_words)
        hashtags = word_distribution.most_common(limit)
        return hashtags


    def get_verified_users(self):
        '''
        Return top verified users that self retweeted
        '''
        verified_users = list()
        for tweet in self.user.timeline(count=25):

            status = self.api.get_status(tweet.id, tweet_mode="extended")
            if hasattr(status, "retweeted_status"):  # Check if Retweet
                try:
                    handl = re.search(r"(\@[a-zA-Z]+\b)", tweet.text)
                    try:
                        h = handl.group()
                        h = h.split('@')[1]

                        auth = tweepy.AppAuthHandler(Config.CONSUMER_KEY, Config.CONSUMER_SECRET)
                        api = tweepy.API(auth, wait_on_rate_limit=True)  # create an API object
                        usr = api.get_user(h)

                        if usr.verified:
                            verified_users.append(h)

                    except IndexError:
                        print()

                except AttributeError:
                    print()

        word_distribution = nltk.FreqDist(verified_users)
        fin = word_distribution.most_common(5)
        return fin
