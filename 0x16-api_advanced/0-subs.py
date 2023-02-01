#!/usr/bin/python3
"""
Queries the Reddit API and return the num of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """ Returns num of subscribers or 0 if subreddit is invalid"""
    headers = {'User-Agent': 'Python/requests'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
