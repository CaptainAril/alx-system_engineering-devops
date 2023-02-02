#!/usr/bin/python3
"""Query Reddit API."""


def recurse(subreddit, hot_list=[], before=None):
    """Queries Reddit API and .returns a list containing the titles of all
    articles for a given subreddit."""
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 100, 'after': before}
    header = {'user-agent': 'User 1.0'}

    r = requests.get(url, params=params, headers=header, allow_redirects=False)

    if r.status_code != 200:
        return None
    else:
        after = r.json().get('data').get('after')

        children = r.json().get('data').get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
    if after is not None:
        hot_list = recurse(subreddit, hot_list=hot_list, before=after)

    return hot_list
