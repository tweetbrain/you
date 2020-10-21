from ..twitter_user import TwitterUser


user = TwitterUser("MontellFish")
def test_get_user():

    print(user.num_of_tweets)



def test_get_top_words():
    user = TwitterUser("MontellFish")
    top = user.get_top_words()
    print(top)
