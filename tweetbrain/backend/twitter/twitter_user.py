import tweepy

from ..config import Config


class TwitterUser:

    auth = tweepy.AppAuthHandler(Config.CONSUMER_KEY, Config.CONSUMER_SECRET)

    #Construct the API instance
    api = tweepy.API(auth, wait_on_rate_limit=True) # create an API object


    def __init__(self, handle: str):
        self.handle = handle
        self.user = self.api.get_user(handle)
        self.bio = self.user.description
        self.timeline = self.user.timeline(count=200)
        self.num_of_tweets = len(self.timeline)
