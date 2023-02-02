#!/usr/bin/python3
"""Queries the Reddit API and
returns a list containing the
titles of all hot articles for
a given subreddit.

If no results are found for the
given subreddit, the function
should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Returns a list containing the titles of all hot articles
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My Reddit API Client"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        hot_posts = data.get('data').get('children')
        after = data.get('data').get('after')
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        return None
