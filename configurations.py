AUTHOR = u'Hendra'
SITENAME = u"hndr.me"
SITESUBTITLE = u"My blog. Consists of mostly broken english and rubbish"
SITEURL = 'http://hndr-blog.herokuapp.com'
TIMEZONE = "Asia/Kuala_Lumpur"

DEFAULT_CATEGORY = ('randoms')
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')
DEFAULT_DATE = ('fs')

THEME = "themes/Cait"

OUTPUT_PATH = ('output/')
PATH = ('content/')

INDEX_URL = ('blog')
INDEX_SAVE_AS = (INDEX_URL+'/index.html')

ARTICLE_URL = (INDEX_URL+'/{slug}')
ARTICLE_SAVE_AS = (ARTICLE_URL+'/index.html')

page_dir = 'pages'
PAGE_URL = (page_dir+'/{slug}')
PAGE_SAVE_AS = (PAGE_URL+'/index.html')

DEFAULT_PAGINATION = 5

DISQUS_SITENAME = ('hndrblog')
GOOGLE_ANALYTICS = ('UA-40075063-1')

MENUITEMS = (('Blog', INDEX_URL),
             ('Contact', 'contact'),
             ('Projects', page_dir+'/projects'))

SOCIAL = (('twitter', 'https://twitter.com/_hdra'),
          ('facebook', 'https://www.facebook.com/b011010000110010101101110011001000111001001100001'),
          ('google-plus', 'https://plus.google.com/118295715125687342506'),
          ('github', 'https://github.com/hdra'),)

CONTACT_EMAIL = "hendra2392@gmail.com"
CONTACTS = (('facebook', 'https://www.facebook.com/b011010000110010101101110011001000111001001100001'),
            ('twitter', 'https://twitter.com/_hdra'),)

RELATIVE_URLS = False
