#!/usr/bin/env python

ifollowers_info = {
    "name": "ifollowers",
    "author": "iSar",
    "version": (0, 0, 5),
    "python": (3, 4),
    "markdown": (2, 5, 2),
    "tweepy": (3, 1, 0),
    "description": "Followers tracking script for Twitter" }

import os
import time
import glob
import markdown
import tweepy

'''
# Dynamic Twitter OAuth
import ioauth

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

isar_static_oauth = ioauth_isar.StaticTwitterOAuth()

owner = isar_static_oauth.owner
consumer_key = isar_static_oauth.consumer_key
consumer_secret = isar_static_oauth.consumer_secret
access_token = isar_static_oauth.access_token
access_token_secret = isar_static_oauth.access_token_secret

# Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

'''
# Print followers
for follower in api.followers_ids(owner):
    print(api.get_user(follower).screen_name)
'''

last_ls = []
for follower in tweepy.Cursor(api.followers, screen_name=owner).items():
    last_ls.append(follower.screen_name)
    #print (follower.screen_name)

#last_ls = ['Leonardo', 'Raffaello', 'Donatello', 'Michelangelo']

'''
# Get Specific markdown file in case you'd like a specific last_ls
with open("_build\\markdown\\2014-12-27T175811.md", "rt") as in_md:
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

# Representing a time [4]
# [4]: http://bit.ly/1A2stqn
date_name = time.strftime("%Y-%m-%dT%H%M%S")
only_date_name = time.strftime("%Y-%m-%d")
date_name_path = '_build\\dat\\'+date_name+'.dat'

def head( header, ls ):
    hyphens = len(header)
    out_md.write(header + ' <i>'+str(len(ls))+'</i>\n')
    i = 0
    while i < hyphens:
        out_md.write('-')
        i += 1
    out_md.write('\n\n')

def followers( ls ):
    i = 0
    for account in ls:
        i += 1
        out_md.write(str(i) +'. ['+ account +'](https://twitter.com/'+ account +')\n')
    out_md.write('\n')

# File Input Output [1]
# [1]: http://bit.ly/1sWobRM
with open(date_name_path, "wt") as out_md: # "_build/markdown/iFollowers.md"
    for i in last_ls:
        out_md.write(i+'\n')
    out_md.write('\n')

# Write last followers
with open("_build\\markdown\\iFollowers.md", "wt") as out_md:
    head( 'Last followers', last_ls )
    followers( last_ls )

''' maybe to remove
# Read
with open("_build\\markdown\\iFollowers.md", "rt") as in_md:
    my_test = in_md.read()
    split_list_last = my_test.split()
'''

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

        # Append first followers
        first_ls = first_followers.split()
        head( 'First followers', first_ls )
        followers( first_ls )

        # Append new followers
        new_followers_ls = []
        for last in last_ls:
            if not last in first_ls:
                new_followers_ls.append(last)
        head( 'New followers', new_followers_ls )
        followers( new_followers_ls )

        # Append unfollowers
        unfollowers_ls = []
        for first in first_ls:
            if not first in last_ls:
                unfollowers_ls.append(first)
        head( 'Unfollowers', unfollowers_ls )
        followers( unfollowers_ls )

# Write last followers markdown list
with open("_build\\markdown\\last.md", "wt") as out_md:
    head( 'Last followers', last_ls )
    followers( last_ls )

# Write first followers markdown list
with open("_build\\markdown\\first.md", "wt") as out_md:
    head( 'First followers', first_ls )
    followers( first_ls )

# Write new followers markdown list
with open("_build\\markdown\\new.md", "wt") as out_md:
    head( 'New followers', new_followers_ls )
    followers( new_followers_ls )

# Write unfollowers markdown list
with open("_build\\markdown\\un.md", "wt") as out_md:
    head( 'Unfollowers', unfollowers_ls )
    followers( unfollowers_ls )

# Get current working directory
cwd = os.getcwd()

# Template
html_header = '<!DOCTYPE html>' \
              '<html>' \
              '<head>' \
              '<title>iFollowers</title>' \
              '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' \
              '<meta name="A followers tracking script" content="" />' \
              '<link rel="stylesheet" type="text/css" href="'+ cwd +'\\_build\\html\\css\\bootstrap.css" />' \
              '</head>' \
              '<body>'
html_footer = '</body>' \
              '</html>'

# Markdown Details [2]
# [2]: http://bit.ly/1weDnEg
with open("_build\\markdown\\last.md", 'rt') as in_md:
    last = in_md.read()
    html_last = markdown.markdown(last)
with open("_build\\markdown\\first.md", 'rt') as in_md:
    first = in_md.read()
    html_first = markdown.markdown(first)
with open("_build\\markdown\\new.md", 'rt') as in_md:
    new = in_md.read()
    html_new = markdown.markdown(new)
with open("_build\\markdown\\un.md", 'rt') as in_md:
    un = in_md.read()
    html_un = markdown.markdown(un)

'''
#in_md = codecs.open("_build/markdown/ifollowers.md", mode="r", encoding="utf-8")
with open("_build\\markdown\\iFollowers.md", 'rt') as in_md:
    iFollowers = in_md.read()
    html_page = markdown.markdown(iFollowers)
'''

# Build the page
html_page = '<div class="col-md-3">'+ html_last +'</div>' \
            '<div class="col-md-3">'+ html_first +'</div>' \
            '<div class="col-md-3">'+ html_new +'</div>' \
            '<div class="col-md-3">'+ html_un +'</div>'

with open("_build\\html\\"+only_date_name+"_iFollowers.html", "wt") as out_html:
    out_html.write(html_header + html_page + html_footer)

# Open the file in a browser
os.system(cwd + "\\_build\\html\\"+only_date_name+"_iFollowers.html")
