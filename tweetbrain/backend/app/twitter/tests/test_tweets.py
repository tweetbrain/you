from ..twitter_user import TwitterUser


user = TwitterUser("lopez__11")

def test_get_user():
    print(user.num_of_tweets)

def test_hashtags():
    print(user.get_top_hastags())

def test_get_top_words():
    top = user.get_top_words()
    print(top)
    print('\n')
