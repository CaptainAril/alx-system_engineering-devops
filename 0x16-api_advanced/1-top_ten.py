#!/usr/bin/python3
"""Query Reddit API."""


def top_ten(subreddit):
    """Queries Reddit API and prints the titles of the first 10 hot post
    listed for a given subreddit."""
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 10}
    header = {'user-agent': 'User 1.0'}

    r = requests.get(url, params=params, headers=header, allow_redirects=False)

    if r.status_code != 200:
        print(None)
    else:
        children = r.json().get('data').get('children')
        for child in children:
            print(child.get('data').get('title'))
