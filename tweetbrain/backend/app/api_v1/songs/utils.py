from ....twitter.twitter_user import TwitterUser
from ....genius.match import Match

match = Match()
def match_with_top_songs(twitter_handle: str):
    user = TwitterUser(twitter_handle)
    top_songs = user.get_top_songs()
    songs = match.search_songs(top_songs[0][0])

    return songs["hits"][0]["results"]
