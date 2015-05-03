#!/usr/bin/env python

# Twitter Application Management [1]
# [1]: https://apps.twitter.com/
class DynamicTwitterOAuth(object):
    '''Define Dynamic OAuth '''
    def __init__(self):
        '''Initialize dynamic OAuth'''
        #self.owner = input('Owner: ')
        self.consumer_key = input('Consumer Key: ')
        self.consumer_secret = input('Consumer Secret: ')
        self.access_token = input('Access Token: ')
        self.access_token_secret = input('Access Token Secret: ')

        self.static_isar = "iSar"

    def printargs(self):
        '''Print'''
        print(self.static_isar)

'''Dynamic Twitter OAuth
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

'''
if __name__ == '__main__':
    Main()
'''
