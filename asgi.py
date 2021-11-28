from fastapi import FastAPI, Body
from fastapi.responses import Response, FileResponse
from pydantic import BaseModel
from my_fun import apply_cache_headers
from my_fun import get_latlongs, get_distance
from my_fun import static_response


app = FastAPI()




@app.get("/")
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("my.html")

@app.get("/img")
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("image.jpg")


@app.get("/style")
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("style.css")


@app.get("/js")
async def _(response: Response):
    apply_cache_headers(response)
    return static_response("my.js")


class Points(BaseModel):
    start: str
    end: str


@app.post("/distance")
async def _(response: Response  , points: Points = Body(...)):
    result = get_distance(get_latlongs(points.start), get_latlongs(points.end))
    return result














