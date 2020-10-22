from ...twitter.twitter_user import TwitterUser
from ...genius.match import Match

match = Match()
def match_with_top_words(twitter_handle: str):
    user = TwitterUser(twitter_handle)
    top_words = user.get_top_words()
    songs = match.search_songs(top_words[0][0])



    return songs["hits"][0]["result"]
