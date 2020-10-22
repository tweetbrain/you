'''
This is where we define schemas.

These schemas model the response of our API
'''

from pydantic import BaseModel, AnyHttpUrl, Json, Field





class Artist(BaseModel):
    name: str = Field(...,example="Eminem")
    url: AnyHttpUrl = Field(...,example="https://genius.com/artists/Eminem")
    header_image_url: AnyHttpUrl = Field(...,example="https://images.genius.com/a9f98b20f8aa7a32650a1dfa5f3de088.1000x445x1.jpg")
    image_url: AnyHttpUrl = Field(...,example="https://images.genius.com/f300798551b97fe030876123afb8c33a.805x805x1.jpg")
    is_verified: bool = Field(...,example=True)
    is_meme_verified: bool = Field(...,example=True)
    id: int = Field(...,example=45)

class Song(BaseModel):
    full_title: str = Field(..., example="Rap God by Eminem")
    title: str =  Field(..., example="Rap God")
    title_with_featured: str =  Field(..., example="Rap God")
    url: str = Field(...,example="https://genius.com/Eminem-rap-god-lyrics")
    header_image_thumbnail_url: AnyHttpUrl = Field(...,example="https://images.genius.com/5d3c94d2fdbdf669ff400fe02396bf53.300x182x1.jpg")
    header_image_url: AnyHttpUrl = Field(...,example="https://images.genius.com/5d3c94d2fdbdf669ff400fe02396bf53.828x502x1.jpg")
    song_art_image_thumbnail_url: AnyHttpUrl = Field(...,example="https://images.genius.com/058e2359838c93395c36119b48a2eff6.300x300x1.png")
    song_art_image_url: AnyHttpUrl = Field(...,example="https://images.genius.com/058e2359838c93395c36119b48a2eff6.1000x1000x1.png")
    id: int = Field(...,example=235729)

    primary_artist: Artist
