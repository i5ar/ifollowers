#!/usr/bin/env python

ifollowers_info = {
    "name": "iFollowers",
    "author": "iSar",
    "version": (0, 0, 8),
    "python": (3, 4),
    "markdown": (2, 5, 2),
    "tweepy": (3, 1, 0),
    "description": "Followers tracking script for Twitter" }

import os
import time
import glob
import markdown
import tweepy
import sqlite3
import ioauth

owner = ''
# Check database
if os.path.isfile('ifollowers.db'):
    # Connect to the database and show the last account
    conn = sqlite3.connect('ifollowers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ifolloauth")
    fetch = c.fetchall()
    # Get first value of last row
    owner = fetch[-1][0]
    consumer_key = fetch[-1][1]
    consumer_secret = fetch[-1][2]
    access_token = fetch[-1][3]
    access_token_secret = fetch[-1][4]
    conn.close()
    newner = input('Please enter \"'+ owner +'\" or a new Owner: ') or owner
else:
    print('Please go to https://apps.twitter.com/ to Create New App;')
    print('Open Permissions tab and check Read only;')
    print('Open Keys and Access Token tab to copy your Application Settings.')
    newner = input('Owner: ')

if(newner != owner):
    # Dynamic Twitter OAuth
    isar_dynamic_oauth = ioauth.DynamicTwitterOAuth()
    #owner = isar_dynamic_oauth.owner
    consumer_key = isar_dynamic_oauth.consumer_key
    consumer_secret = isar_dynamic_oauth.consumer_secret
    access_token = isar_dynamic_oauth.access_token
    access_token_secret = isar_dynamic_oauth.access_token_secret
    # Database Twitter OAuth
    conn = sqlite3.connect('ifollowers.db')
    c = conn.cursor()
    # Create table if not exists
    c.execute("CREATE TABLE if not exists ifolloauth ('Owner' TEXT, 'Consumer Key' TEXT, 'Consumer Secret' TEXT, 'Access Token' TEXT, 'Access Token Secret' TEXT)")
    # Insert a row of data
    c.execute("INSERT INTO ifolloauth ('Owner', 'Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')"
              "VALUES (?, ?, ?, ?, ?)", (newner, consumer_key, consumer_secret, access_token, access_token_secret))
    conn.commit()
    conn.close()
elif(newner == ''):
    print('You must enter a valid owner')

# Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

last_ls = []
for follower in tweepy.Cursor(api.followers, screen_name=owner).items():
    last_ls.append(follower.screen_name)

# Make directories if they do not exist
if not os.path.exists('_build\\markdown'):
    os.makedirs('_build\\markdown')
if not os.path.exists('_build\\html'):
    os.makedirs('_build\\html')
if not os.path.exists('_build\\dat'):
    os.makedirs('_build\\dat')

# Time access and conversions
date_name = time.strftime("%Y-%m-%dT%H%M%S")
only_date_name = time.strftime("%Y-%m-%d")
date_name_path = '_build\\dat\\'+date_name+'.dat'

def head( header, ls ):
    '''Write markdown head'''
    hyphens = len(header)
    out_md.write(header + ' <i>'+str(len(ls))+'</i>\n')
    i = 0
    while i < hyphens:
        out_md.write('-')
        i += 1
    out_md.write('\n\n')

def followers( ls ):
    '''Write markdown list items'''
    i = 0
    for account in ls:
        i += 1
        out_md.write(str(i) +'. ['+ account +'](https://twitter.com/'+ account +')\n')
    out_md.write('\n')

# Write last followers in data file
with open(date_name_path, "wt") as out_md:
    for i in last_ls:
        out_md.write(i+'\n')
    out_md.write('\n')

# Write last followers in markdown file
with open("_build\\markdown\\last.md", "wt") as out_md:
    head( 'Last followers', last_ls )
    followers( last_ls )

# List data files
dic = {}
for file in glob.glob("_build\\dat\\*.dat"):
    key = int(os.path.getmtime(file))
    dic[key] = file
# List data files
ls = []
for key in dic.keys():
    ls.append(key)
sorted_ls = sorted(ls)

# Check if there are data files to compare in order to list first followers, new followers and unfollowers
if len(ls) > 1:
    # Get first data file from list
    first_data = dic[sorted_ls[0]]
    # Get last data file from list
    last_data = dic[sorted_ls[-1]]
    # Get previous data file from list
    previous_data = dic[sorted_ls[-2]]

    # Opening the older markdown file to read the first followers
    with open(previous_data, "rt") as in_md:
        first_followers = in_md.read()

    # Write first followers markdown list
    with open("_build\\markdown\\first.md", "wt") as out_md:
        first_ls = first_followers.split()
        head( 'First followers', first_ls )
        followers( first_ls )

    # Write new followers markdown list
    with open("_build\\markdown\\new.md", "wt") as out_md:
        new_followers_ls = []
        for last in last_ls:
            if not last in first_ls:
                new_followers_ls.append(last)
        head( 'New followers', new_followers_ls )
        followers( new_followers_ls )

    # Write unfollowers markdown list
    with open("_build\\markdown\\un.md", "wt") as out_md:
        unfollowers_ls = []
        for first in first_ls:
            if not first in last_ls:
                unfollowers_ls.append(first)
        head( 'Unfollowers', unfollowers_ls )
        followers( unfollowers_ls )

else:
    # Write last followers markdown list
    with open("_build\\markdown\\last.md", "wt") as out_md:
        head( 'Followers', last_ls )
        followers( last_ls )

    # Write empty first followers markdown list
    with open("_build\\markdown\\first.md", "wt") as out_md:
        out_md.write('')

    # Write empty new followers markdown list
    with open("_build\\markdown\\new.md", "wt") as out_md:
        out_md.write('')

    # Write empty unfollowers markdown list
    with open("_build\\markdown\\un.md", "wt") as out_md:
        out_md.write('')

# Template
html_header = '<!DOCTYPE html>' \
              '<html>' \
              '<head>' \
              '<title>iFollowers</title>' \
              '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' \
              '<meta name="A followers tracking script" content="" />' \
              '<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css" />' \
              '</head>' \
              '<body>'
html_footer = '</body>' \
              '</html>'

# Generate markdown
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

# Build the page
html_page = '<div class="col-md-3">'+ html_last +'</div>' \
            '<div class="col-md-3">'+ html_first +'</div>' \
            '<div class="col-md-3">'+ html_new +'</div>' \
            '<div class="col-md-3">'+ html_un +'</div>'

with open("_build\\html\\"+only_date_name+".html", "wt") as out_html:
    out_html.write(html_header + html_page + html_footer)

# Get current working directory
cwd = os.getcwd()
# Open the file in a browser
os.system(cwd + "\\_build\\html\\"+only_date_name+".html")
