#!/usr/bin/python3
"""returns the first 10 hot posts listed fro a given subredit"""

import requests


def top_ten(subreddit):
    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers={"User-Agent": "myself"},
                            allow_redirects=False, params={"limit": 10})
    data = response.json().get("data")
    [print(x.get("data").get('title')) for x in data.get('children')]
