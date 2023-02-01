#!/usr/bin/pyhon3
"""
This queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """ Prints titles of first 10 hot posts """
    headers = {'User-Agent': 'Python/requests'}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for i, post in enumerate(data["data"]["children"]):
            title = post["data"]["title"]
            print(f"{i+1}. {title}")
    else:
        print("None")
