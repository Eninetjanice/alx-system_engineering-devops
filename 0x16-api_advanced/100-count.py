#!/usr/bin/python3
"""GET to api"""
import requests
import string


def recurse(subreddit, word_list, after="", dic={}):
    """recursive function"""
    headers = {'User-Agent': 'Reddit API test'}
    params = {'limit': 100, 'after': after}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        after = data['data']['after']
        posts = data['data']['children']

        word_count = {}
        for word in word_list:
            word_count[word.lower()] = 0

        for post in posts:
            title = post['data']['title']
            for punc in string.punctuation:
                title = title.replace(punc, ' ')
            words = title.lower().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1

        if after:
            count_words(subreddit, word_list, after)

        for k, v in sorted(word_count.items(), key=lambda item: item[0]):
            sorted_words = (k, v)
        sorted_words.sort(key=lambda x: x[1], reverse=True)

        for word, count in sorted_words:
            if count > 0:
                print(f'{word}: {count}')
    else:
        return
