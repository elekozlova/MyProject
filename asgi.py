import folium
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

@app.get("/map")
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("map1.html")


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
    map = folium.Map(location=get_latlongs(points.start) , zoom_start = 8, tiles = "cartodbpositron")
    for coordinates in [get_latlongs(points.start), get_latlongs(points.end)]:
        folium.Marker(location=coordinates, icon=folium.Icon(color = 'cadetblue',icon="cloud")).add_to(map)
    map.save("map1.html")
    return result

@app.get("/map")
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("map1.html")












