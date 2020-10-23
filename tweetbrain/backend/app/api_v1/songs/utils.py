from ...twitter.twitter_user import TwitterUser
from ...genius.match import Match

match = Match()
def match_with_top_words(twitter_handle: str):
    user = TwitterUser(twitter_handle)
    top_words = user.get_top_words()
    songs = list()

    # list of words that return a song
    valid_words = list()
    valid_words_str = ""
    max_valid_words = 7

    index = 0
    max_index = 7
    while (len(valid_words_str.split()) < max_valid_words) and (index < max_index):
        songs.clear()
        query = f"{valid_words_str} {top_words[index][0]}"
        results = match.search_songs(query)

        for result in results["hits"]:
            if (result["type"] =="song"):
                songs.append(result["result"])

        if len(songs) > 0:
            valid_words_str = query


        index += 1




    results = list()


    print(valid_words_str, "WOWOWOWOWOW \n\n\n\n")
    return songs
