import lyricsgenius

from ..config import Config

class Match:
    api = lyricsgenius.Genius(Config.GENIUS_ACCESS_TOKEN)
    def __init__(self):
        pass


    def search_song(self, query: str):
        return self.api.search_songs(query)
