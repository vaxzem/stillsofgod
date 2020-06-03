#!/usr/bin/env python3

import os
import random
import time

import tweepy


def authenticate():
    """Handles main authentication for Twitter account.

    Returns:
        API instance.
    """

    secrets = (
        'CONSUMER_KEY',
        'CONSUMER_SECRET',
        'ACCESS_TOKEN',
        'ACCESS_TOKEN_SECRET'
    )
    env_info = {s: os.getenv(s, "Environment variable doesn't exist.") for s in secrets}

    auth = tweepy.OAuthHandler(
        env_info['CONSUMER_KEY'],
        env_info['CONSUMER_SECRET']
    )
    auth.set_access_token(
        env_info['ACCESS_TOKEN'],
        env_info['ACCESS_TOKEN_SECRET']
    )

    return tweepy.API(auth)


def main():
    api = authenticate()
    # Upload a random image from the list of the directory's contents.
    pictures = os.listdir(os.chdir('tog_images'))
    while True:
        api.update_with_media(random.choice(pictures))
        time.sleep(3600)


if __name__ == '__main__':
    main()
