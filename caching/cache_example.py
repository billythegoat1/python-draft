from functools import lru_cache
import requests
from timeit import timeit

@lru_cache(maxsize=None)
def get_article(url):
    print("You are requesting a page ...\n")
    response = requests.get(url)

    return response.text

url = "https://www.datacamp.com/tutorial/decorators-python"

print(
    timeit(
    "get_article(url)",
    globals=globals(),
    number=1
)
)

print(
    timeit(
    "get_article(url)",
    globals=globals(),
    number=1
)
)