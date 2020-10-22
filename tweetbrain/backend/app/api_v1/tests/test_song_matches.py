from ....twitter.twitter_user import TwitterUser
from ....genius.match import Match


user = TwitterUser("MontellFish")
matcher = Match()

def test_basic_match():
    query = ""
    top_words = user.get_top_words()
    word_limit = 1

    for index, word_freq in enumerate(top_words):
        query += word_freq[0] + " "

        if index >= word_limit - 1:
            break

    print(query)
    print(matcher.search_song(query))
