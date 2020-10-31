from ..twitter_user import TwitterUser


user = TwitterUser("rozayrj")

def test_get_user():
    print(user.num_of_tweets)

def test_get_Verified():
    people = user.get_verified_users()
    for p in people:
        print(p)

def test_getBio():
    print(user.bio)


def test_hashtags():
    tag = user.get_top_hashtags()
    for t in tag:
        print(t)

def test_get_top_words():
    top = user.get_top_words()
    for t in top:
        print(t)