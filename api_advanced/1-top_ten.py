#!/usr/bin/python3
""" Prints the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
           json_data = response.json()
           children = json_data['data']['children']
           for post in children[:10]:
               print(post['data']['title'])
    else:
        print(None)
