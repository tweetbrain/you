from fastapi import FastAPI
from starlette.requests import Request

from .api_v1.songs import routes as songs_routes


tags_metadata = [
    {
        "name": "tweetbrain REST API",
        "description": "Send us your tweets programatically ;)",
        "externalDocs": {
            "description": "More about tweetbrain",
            "url": "https://docs.tweetbrain.tisuela.com/",
        },
    }
]

app = FastAPI(
    title="Tweet Brain API",
    version="v1.0-beta",
    openapi_tags=tags_metadata,
    redoc_url="/docs",
    docs_url="/",
)


@app.get("/hello")
async def hello(request: Request):
    return {"message": "Hello World"}


app.include_router(songs_routes.router, prefix="/songs", tags=["songs"])
