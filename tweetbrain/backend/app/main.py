from fastapi import FastAPI
from starlette.requests import Request
from starlette.graphql import GraphQLApp

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
    docs_url="/api/v1",
)




@app.get("/hello")
async def hello(request: Request):
    return {"message": "Hello World"}
