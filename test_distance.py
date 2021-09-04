import httpx

from my_own_project.asgi import Points

url = "http://localhost:8000/distance"

sample = Points(start='London', end='Minsk')

r = httpx.post(url, json=sample.dict())
print(r)
print(r.json())
