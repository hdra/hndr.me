#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Hendra'
SITENAME = u"hndr (dot) me"
SITESUBTITLE = u"My blog. Consists of mostly broken english and rubbish"
TIMEZONE = "Asia/Kuala_Lumpur"

DEFAULT_CATEGORY = 'randoms'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

THEME = "themes/Cait"
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

DEFAULT_PAGINATION = 8

DISQUS_SITENAME = 'hndrblog'
GOOGLE_ANALYTICS = 'UA-40075063-1'

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('Blog', INDEX_URL),
                    ('Contact', 'contact'),
                    ('Projects', page_dir+'/projects'))

SOCIAL = (('twitter', 'https://twitter.com/_hdra'),
          ('google-plus', 'https://plus.google.com/118295715125687342506'),
          ('github', 'https://github.com/hdra'),)

CONTACT_EMAIL = "hendra2392@gmail.com"
CONTACTS = (('github', 'https://github.com/hdra'),
            ('twitter', 'https://twitter.com/_hdra'),)

# STATIC_PATHS = (('extra/favicon.ico', 'favicon.ico'),
#                  ('extra/humans.txt', 'humans.txt'),
#                  ('extra/CNAME', 'CNAME'),
#                  ('extra/robots.txt', 'robots.txt'),)

STATIC_PATHS =   ['extra/favicon.ico',
                 'extra/humans.txt',
                 'extra/CNAME',
                 'extra/robots.txt']
