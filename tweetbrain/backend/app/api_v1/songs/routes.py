from fastapi import Depends, APIRouter,Request

from . import utils



router = APIRouter()


@router.get("/match")
async def match_song(
    request: Request, handle: str
):
    result = utils.match_with_top_words(handle)
    return result
