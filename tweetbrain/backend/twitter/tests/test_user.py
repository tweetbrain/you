from ..twitter_user import TwitterUser



def test_get_user():
    user = TwitterUser("MontellFish")
    print(user.num_of_tweets)
