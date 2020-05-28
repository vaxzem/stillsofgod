#!/usr/bin/env python3
import os

import tweepy


def get_env():
    secrets = 'CONSUMER_KEY', 'CONSUMER_SECRET', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET'
    return {s: os.getenv(s, "Environment variable doesn't exist.") for s in secrets}


def authenticate():
    env_info = get_env()
    auth = tweepy.OAuthHandler(env_info['CONSUMER_KEY'], env_info['CONSUMER_SECRET'])
    auth.set_access_token(env_info['ACCESS_TOKEN'], env_info['ACCESS_TOKEN_SECRET'])
    return tweepy.API(auth)


def main():
    api = authenticate()
    print(api.me())  # Should print out user information if authentication worked properly.


if __name__ == '__main__':
    main()