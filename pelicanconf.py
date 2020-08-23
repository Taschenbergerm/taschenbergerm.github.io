#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marvin Taschenberger'
SITENAME = 'Marvin Taschenberger '
SITEURL = ''
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
RELATIVE_URLS = True

PATH = 'content'
OUTPUT_PATH = 'output'
TIMEZONE = 'Europe/Berlin'
GITHUB_URL = 'http://github.com/taschenbergerm/'
DEFAULT_LANG = 'en'
REVERSE_CATEGORY_ORDER = True
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
PLUGIN_PATHS = ['/home/marvin/Projects/Blogs/pelican-plugins']
PLUGINS = [
    'assets',
    # 'ace_editor',
    # 'auto_pages',
    'pelican_comment_system',
    'sitemap',
    'gravatar']
    
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )


STATIC_PATHS = [
    'images',
    ]

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/taschenberger-marvin-94531bb2/'),)
          
# PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
DEFAULT_PAGINATION = 10

THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# Custom Home page
# DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
# PAGINATED_DIRECT_TEMPLATES = (('blog',))
# TEMPLATE_PAGES = {'home.html': 'index.html',}
