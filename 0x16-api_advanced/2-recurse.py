#!/usr/bin/python3
"""recursive function returns list of titles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers={"User-Agent": "myself"},
                            allow_redirects=False,
                            params={"limit": 100, 'after': after})
    data = response.json().get("data")
    hot_list += ([(x.get('data').get('title')) for x in data.get("children")])
    after = data.get("after")

    if (after is not None):
        return recurse(subreddit, hot_list, after)
    return hot_list
