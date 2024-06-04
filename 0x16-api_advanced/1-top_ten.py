#!/usr/bin/python3
"""this script to return posts list in raddit"""
import requests


def top_ten(subreddit):
    """Define function to print titles of first 10 hot posts"""
    headers = {'User-Agent': 'Mozilla/5.0'}

    if subreddit is None:
        return None
    
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    
    res = requests.get(url, headers=headers, allow_redirects=False)
    
    if res.status_code != 200:
        return None
    
    data = res.json().get('data', {})
    children = data.get('children', [])
    
    for post in children[:10]:
        print(post['data']['title'])
