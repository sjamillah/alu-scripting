#!/usr/bin/python3

"""A recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords"""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """Function to count_words
    """

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'Mozilla/5.0 \
(Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})

    if request.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                for i, keyword in enumerate(word_list):
                    if keyword.lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']

        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            sorted_counts = sorted(zip(word_list, count), key=lambda x: (-x[1], x[0].lower()))
            for keyword, keyword_count in sorted_counts:
                if keyword_count > 0 and word_list.index(keyword) not in save:
                    print(f"{keyword.lower()}: {keyword_count}")
        else:
            count_words(subreddit, word_list, after, count)
