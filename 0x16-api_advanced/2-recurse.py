#!/usr/bin/python3
"""this script to return posts list in raddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Define function to print titles of first 10 hot posts"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return None
    data = res.json()
    hot_list.extend(data['data']['children'])
    after = data['data'].get('after')
    if after is not None:
        recurse(subreddit, hot_list, after)
        return hot_list
