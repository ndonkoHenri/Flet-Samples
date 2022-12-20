import json
from typing import Optional

import urllib3

# documentation available here : https://v2.jokeapi.dev/
JOKE_URL = 'https://v2.jokeapi.dev/joke/Programming,Christmas?blacklistFlags=nsfw,racist,sexist,explicit&safe-mode'


def fetch_joke() -> Optional[dict]:
    """ We fetch the joke, while taking into consideration possible errors. """
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', JOKE_URL)
    except Exception as ex:
        print(ex)
        return None
    return json.loads(r.data.decode('utf-8'))


def validate_joke(joke: dict) -> None:
    """ We want to validate the joke before rendering it"""
    assert isinstance(joke, dict), "Humm! Seems like the the joke is not of type Dict."
    assert joke['error'] is False, "An error occurred while fetching the joke!"


def render_joke(joke: dict) -> Optional[str]:
    try:
        validate_joke(joke)
        if joke.get('type') == 'single':
            joke_str = joke['joke']
        elif joke.get('type') == 'twopart':
            joke_str = f">> {joke['setup']} \n\n>> {joke['delivery']}"
        else:
            raise Exception(f'Unknown joke format {joke}')
    except Exception as ex:
        print(ex)
        return None

    return joke_str


def return_joke():
    return render_joke(
        fetch_joke()
    )


if __name__ == '__main__':
    print(render_joke(fetch_joke()))
