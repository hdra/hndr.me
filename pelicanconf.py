#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Hendra'
SITENAME = u"HNDR.ME"
SITESUBTITLE = u"A nerd pretending to be a software engineer."
TIMEZONE = "Asia/Kuala_Lumpur"

SITEFOOTER = u'Contents is <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/us/">cc by-nc-sa</a>. All opinions are of my own.'

DEFAULT_CATEGORY = 'Uncategorized'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

SUMMARY_MAX_LENGTH = 15

THEME = "themes/pelican-cid"
TYPOGRIFY = True

OUTPUT_PATH = 'output'
PATH = 'content/'

INDEX_URL = 'blog'
INDEX_SAVE_AS = INDEX_URL+'/index.html'

ARTICLE_URL = INDEX_URL+'/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL+'/index.html'

page_dir = 'pages'
PAGE_URL = page_dir+'/{slug}'
PAGE_SAVE_AS = PAGE_URL+'/index.html'

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = 'hndrblog'
GOOGLE_ANALYTICS = 'UA-40075063-1'

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('Blog', INDEX_URL),)

SOCIAL = (('twitter', 'https://twitter.com/_hdra'),
          ('github', 'https://github.com/hdra'),)

CONTACT_EMAIL = "hendra2392@gmail.com"
CONTACTS = (('github', 'https://github.com/hdra'),
            ('twitter', 'https://twitter.com/_hdra'),)


EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}


STATIC_PATHS = ['extra/favicon.ico',
                'extra/humans.txt',
                'extra/CNAME',
                'extra/robots.txt']

PLUGIN_PATHS = ['./themes/pelican-cid/plugins']
PLUGINS = ['cid_filters']
