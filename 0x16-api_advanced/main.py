#!/usr/bin/python3
"""
0-main
"""
import sys
import json

if __name__ == '__main__':
    number_of_subcribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{}".format(number_of_subcribers(sys.argv[1])))
