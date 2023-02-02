#!/usr/bin/python3
"""
This queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """ Prints titles of first 10 hot posts """
    headers = {'User-Agent': 'Python/requests'}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?"
    payload = {'limit': '10'}
    response = requests.get(url, headers=headers, params=payload,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if data.get('data') and data.get('data').get('children'):
            hot_posts = data.get('data').get('children')
            for post in hot_posts:
                if post.get('data') and post.get('data').get('title'):
                    print(post.get('data').get('title'))
    else:
        print("None")
