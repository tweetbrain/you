from fastapi import Depends, APIRouter,Request

from . import utils
from ..schemas import Song


router = APIRouter()


@router.get("/match", response_model=Song)
async def match_song(
    request: Request, handle: str = "MontellFish"
):
    result = utils.match_with_top_words(handle)
    return result
