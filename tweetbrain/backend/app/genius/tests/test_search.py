from ..match import Match


matcher = Match()

def test_basic():
    result = matcher.search_songs("burger town")
    for hit in result["hits"]:
        print(hit["result"], "\n----\n\n")
