#!/usr/bin/env python
from builtins import input


# Twitter Application Management [1]
# [1]: https://apps.twitter.com/
class DynamicTwitterOAuth(object):
    """Define Dynamic OAuth."""

    def __init__(self):
        """Initialize dynamic OAuth."""
        # self.owner = input('Owner: ')
        self.consumer_key = input('Consumer Key: ')
        self.consumer_secret = input('Consumer Secret: ')
        self.access_token = input('Access Token: ')
        self.access_token_secret = input('Access Token Secret: ')

        self.static_isar = "iSar"

    def printargs(self):
        """Print args."""
        print(self.static_isar)
