#!/usr/bin/python3
"""number of subscribers for a given subredit"""

import requests


def number_of_subscribers(subreddit):
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "myself"},
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        return data.get("subscribers")
    else:
        return 0
