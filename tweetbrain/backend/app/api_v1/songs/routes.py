from fastapi import Depends, APIRouter

from . import utils








@router.get("/match")
async def match_song(
    request: Request, twitter_handle: str
):
    result = utils.match_with_top_songs(twitter_handle)
