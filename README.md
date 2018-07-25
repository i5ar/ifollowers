iFollowers
==========

A *followers* tracking script for Twitter.

> This script was made for fun in my spare time.

There are a ton of spammers on Twitter, many of them will follow you for a few days.  
With this script you can track them down and block them forever.

### Installation and required packages

- Install <a href="https://www.python.org/" target="_blank">Python</a> if not already in your operating system;
    - Install the PyPA recommended tool <a href="https://pip.pypa.io/" target="_blank">pip</a> for installing Python packages;
        - Install <a href="https://pythonhosted.org/Markdown/" target="_blank">Markdown</a>:

                pip install markdown
        - Install <a href="http://www.tweepy.org/" target="_blank">Tweepy</a>:

                pip install tweepy

### Use

Save the script [*main.py*](https://github.com/i5ar/ifollowers/blob/master/main.py) and the module [*ioauth.py*](https://github.com/i5ar/ifollowers/blob/master/ioauth.py) in the same directory, then open your terminal and run `python main.py`. It will list and save all your **Current followers** so next time you are going to run the script it will be able to list:
- **Previous followers**;
- **New followers**;
- **Unfollowers**.

> Before to run the script you need to **Create New App** at <a href="https://apps.twitter.com/" target="_blank">Twitter Application Management</a> to get your **Keys and Access Tokens**:
- Owner;
- Consumer Key;
- Consumer Secret;
- Access Token;
- Access Token Secret;

##### Note
Since Release v0.0.3 iFollowers uses Tweepy package so it does not allow to run the script twice in less than 15 minutes. If you get an error, please try again after 15 minutes.

This script is meant to be used in respect of Twitter [Following rules and best practices](https://support.twitter.com/entries/68916-following-rules-and-best-practices).
I take no responsibility or liability for any damages including damages arising from use or loss of use, data, or profits.

> Please, come back to check new and awesome releases! Any contribution or suggestion will be greatly appreciated.

### Changelog
*Release Version 0.2.0*
*Release Date - 01th May, 2017*

- Add backward compatibility
- Cleaning

*Release Version 0.0.8*
*Release Date - 05th July, 2015*

- Add database to store OAuth keys and access tokens

*Release Version 0.0.5*
*Release Date - 16th April, 2015*

- Add style.

*Release Version 0.0.4*
*Release Date - 28th December, 2014*

- Add OAuth modules;
- Change `.md` file extension to `.dat` to store IDs.

*Release Version 0.0.3*
*Release Date - 27th December, 2014*

- Add *Tweepy* package;
- Remove *BeautifulSoup* package;
- Remove `icleaner.py` to rename static pages.

*Release Version 0.0.2*
*Release Date - 22th December, 2014*

- Add `icleaner.py` to rename static pages with the static page date.

*Release Version 0.0.1*
*Release Date - 21th December, 2014*

 - Having some fun with *BeautifulSoup* coding `ifollowers.py`.

### TODO

- Binary;

[Python]: https://www.python.org/
[pip]: https://pip.pypa.io/
[Tweepy]: http://www.tweepy.org/
[BeautifulSoup]: http://www.crummy.com/software/BeautifulSoup/
[Markdown]: https://pythonhosted.org/Markdown/
