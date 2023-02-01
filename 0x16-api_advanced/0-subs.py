#!/usr/bin/python3
"""Reddit API query."""


def number_of_subscribers(subreddit):
    """Reddit API query that returns the number of total subscribers
    to a given subreddit."""
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'user'}

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0
    return r.json().get('data').get('subscribers')
