#!/usr/bin/env python

import os
import time
import glob
import markdown

import tweepy

# Dynamic Twitter OAuth
import ioauth
print('Version:', ioauth.version)

owner = input('Owner: ')
consumer_key = input('Consumer Key: ')
consumer_secret = input('Consumer Secret: ')
access_token = input('Access Token: ')
access_token_secret = input('Access Token Secret: ')

isar_dynamic_oauth = ioauth.DynamicTwitterOAuth(
    owner,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret )

'''
# Static Twitter OAuth
import ioauth_isar
print('Version:', ioauth_isar.version)

isar_static_oauth = ioauth_isar.StaticTwitterOAuth()

owner = isar_static_oauth.owner
consumer_key = isar_static_oauth.consumer_key
consumer_secret = isar_static_oauth.consumer_secret
access_token = isar_static_oauth.access_token
access_token_secret = isar_static_oauth.access_token_secret
'''

# Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

last_ls = []
for follower in tweepy.Cursor(api.followers, screen_name=owner).items():
    last_ls.append(follower.screen_name)
    #print (follower.screen_name)

'''
# Get Specific markdown file in case you'd like a specific last_ls
with open("", "rt") as in_md: # "_build\\markdown\\2014-12-27T175811.md"
    last_followers = in_md.read()
    last_ls = last_followers.split()
'''

# Make directories if they do not exist
if not os.path.exists('_build\\markdown'):
    os.makedirs('_build\\markdown')
if not os.path.exists('_build\\html'):
    os.makedirs('_build\\html')
if not os.path.exists('_build\\dat'):
    os.makedirs('_build\\dat')

# Create a name with current date and time
# Representing a time [4]
# [4]: http://bit.ly/1A2stqn
date_name = time.strftime("%Y-%m-%dT%H%M%S")
only_date_name = time.strftime("%Y-%m-%d")
date_name_path = '_build\\dat\\'+date_name+'.dat'

def head( header, ls ):
    hyphens = len(header)
    out_md.write(header + ' ['+str(len(ls))+']\n')
    i = 0
    while i < hyphens:
        out_md.write('-')
        i = i+1
    out_md.write('\n\n')

def followers( ls ):
    for i in ls:
        out_md.write('- ['+i+'](https://twitter.com/'+i+')\n')
    out_md.write('\n')


# File Input Output [1]
# [1]: http://bit.ly/1sWobRM
with open(date_name_path, "wt") as out_md: # "_build/markdown/iFollowers.md"
    for i in last_ls:
        out_md.write(i+'\n')
    out_md.write('\n')

with open("_build\\markdown\\iFollowers.md", "wt") as out_md:
    head( 'Last followers', last_ls )
    followers( last_ls )

with open("_build\\markdown\\iFollowers.md", "rt") as in_md:
    my_test = in_md.read()
    split_list_last = my_test.split()

# Get a list of files in markdown directory and sort last modified
dic = {}
for file in glob.glob("_build\\dat\\*.dat"):
    key = int(os.path.getmtime(file))   # Key
    dic[key] = file                     # Value
#print(dic)

ls = []
for key in dic.keys():
    ls.append(key)
sorted_ls = sorted(ls)

print('lengh: '+str(len(ls)))

if len(ls) > 1 :
    # Dictionary from list items
    first = (dic[sorted_ls[0]]) # '_build\markdown\2014-12-27T151122.md'
    last = (dic[sorted_ls[-1]]) # '_build\markdown\2014-12-27T151245.md'
    #print(str(len(ls)))
    #print('First static page: '+first)
    #print('Last static page: '+last)
    # Opening the older markdown file to read the old followers
    with open(first, "rt") as in_md: # "_build\markdown\2014-12-27_15-16.md"
        first_followers = in_md.read()
        #print(first_followers)

    with open("_build\\markdown\\iFollowers.md", "at") as out_md:

        first_ls = first_followers.split()
        head( 'First followers', first_ls )
        followers( first_ls )

        new_followers_ls = []
        for last in last_ls:
            if not last in first_ls:
                new_followers_ls.append(last)
        head( 'New followers', new_followers_ls )
        followers( new_followers_ls )

        unfollowers_ls = []
        for first in first_ls:
            if not first in last_ls:
                unfollowers_ls.append(first)
        head( 'Unfollowers', unfollowers_ls )
        followers( unfollowers_ls )

        # TODO second_last_ls
        second_last_ls = []

# Markdown Details [2]
# [2]: http://bit.ly/1weDnEg
#in_md = codecs.open("_build/markdown/ifollowers.md", mode="r", encoding="utf-8")
with open("_build\\markdown\\iFollowers.md", 'rt') as in_md:
    text = in_md.read()
    html = markdown.markdown(text)

with open("_build\\html\\"+only_date_name+"_iFollowers.html", "wt") as out_html:
    out_html.write(html)

# Open the file in a browser
cwd = os.getcwd()
os.system(cwd + "\\_build\\html\\"+only_date_name+"_iFollowers.html")
