import mimetypes
from pathlib import Path
from typing import Type

from fastapi import HTTPException
from starlette import status
from starlette.responses import Response


from geopy.geocoders import Nominatim
from geopy import distance




def apply_cache_headers(response: Response) -> None:
    cache_params = (
        "immutable",
        "public",
        f"max_age={60 * 60}",
    )

    response.headers["Cache-Control"] = ",".join(cache_params)


def static_response(
    file_name: str,
    *,
    binary: bool = False,
    response_cls: Type[Response] = Response,
) -> Response:
    def get_file_path_safe() -> Path:
        file_path = Path(file_name).resolve()
        if not file_path.is_file():
            raise HTTPException(
                detail=f"file {file_name!r} not found",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return file_path

    def calc_mode() -> str:
        return "rb" if binary else "r"

    def calc_media_type() -> str:
        return mimetypes.guess_type(file_name)[0] or "text/plain"

    file_path = get_file_path_safe()
    mode = calc_mode()
    media_type = calc_media_type()

    with file_path.open(mode) as stream:
        content = stream.read()
        return response_cls(content=content, media_type=media_type)


def get_distance(locA, locB):
    # use haversine forumla
    city_A = (locA[0], locA[1])
    city_B = (locB[0], locB[1])
    return round(distance.distance(city_A, city_B).km)


def get_latlongs(location):
    geolocator = Nominatim(user_agent='API_KEY')
    result = geolocator.geocode(location)
    return result.latitude, result.longitude



