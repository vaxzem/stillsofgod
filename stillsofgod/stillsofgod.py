#!/usr/bin/env python3
import os

import tweepy


def authenticate():
    """Handles main authentication for Twitter account.

    Returns:
        API instance.
    """
    secrets = 'CONSUMER_KEY', 'CONSUMER_SECRET', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET'

    env_info = {s: os.getenv(s, "Environment variable doesn't exist.") for s in secrets}

    auth = tweepy.OAuthHandler(
        env_info['CONSUMER_KEY'], env_info['CONSUMER_SECRET']
    )
    auth.set_access_token(
        env_info['ACCESS_TOKEN'], env_info['ACCESS_TOKEN_SECRET']
    )

    return tweepy.API(auth)


def main():
    api = authenticate()
    print(api.me())  # Should print out user information if authentication worked properly.


if __name__ == '__main__':
    main()