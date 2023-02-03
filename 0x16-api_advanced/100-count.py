#!/usr/bin/python3
"""Query Reddit API."""
import requests


def count_words(subreddit, word_list, before=None, count={}):
    """Queries Reddit API, parses the title of all hot articles, and prints
    a sorted count of given keywords."""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 100, 'after': before}
    header = {'user-agent': 'User 1.0'}

    r = requests.get(url, params=params, headers=header, allow_redirects=False)
    if r.status_code != 200:
        return
    else:
        after = r.json().get('data').get('after')

        children = r.json().get('data').get('children')
        for child in children:
            for word in word_list:
                times = len([x for x in child.get('data').get('title')
                            .lower().split() if x == word.lower()])
                if count.get(word.lower()):
                    count[word.lower()] += times
                else:
                    count[word.lower()] = times

    if after is None:
        if len(count) == 0:
            return

        sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[1]))
        for k, v in sorted_count:
            if v != 0:
                print('{}: {}'.format(k, v))
    else:
        count_words(subreddit, word_list, before=after, count=count)
