#!/usr/bin/python3
"""this script to return numbers of subs in raddit"""
import requests


def number_of_subscribers(subreddit):
    """define function"""
    headers = {'User-Agent': 'Mozilla/5.0'}

    if subreddit is None:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    return res.json()['data']['subscribers']
