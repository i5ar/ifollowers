#!/usr/bin/env python

# Twitter Application Management [1]
# [1]: https://apps.twitter.com/

class DynamicTwitterOAuth(object):
    '''Define Dynamic OAuth '''
    def __init__(self, owner, consumer_key, consumer_secret, access_token, access_token_secret):
        '''Initialize dynamic OAuth'''
        self.owner = owner
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.static_isar = "iSar"
        
    def printargs(self):
        '''Print'''
        print(self.static_isar)

'''
isar_dynamic_oauth = DynamicTwitterOAuth(
    '', # Owner
    '', # Consumer Key
    '', # Consumer Secret
    '', # Access Token
    '') # Access Token Secret

owner = isar_dynamic_oauth.owner
consumer_key = isar_dynamic_oauth.consumer_key
consumer_secret = isar_dynamic_oauth.consumer_secret
access_token = isar_dynamic_oauth.access_token
access_token_secret = isar_dynamic_oauth.access_token_secret

print(isar_dynamic_oauth.owner)
print(isar_dynamic_oauth.consumer_key)
print(isar_dynamic_oauth.consumer_secret)
print(isar_dynamic_oauth.access_token)
print(isar_dynamic_oauth.access_token_secret)

isar_dynamic_oauth.printargs()
'''

version = '0.0.4'

'''
if __name__ == '__main__':
    Main()
'''