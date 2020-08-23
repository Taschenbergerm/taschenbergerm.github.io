#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marvin Taschenberger'
SITENAME = 'Marvin Taschenberger '
SITEURL = ''
SITELOGO = SITEURL + "/images/marvin.png"
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
THEME = 'Flex'
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

COPYRIGHT_YEAR = 2020
MAIN_MENU = True
ADD_THIS_ID = "ra-77hh6723hhjd"
DISQUS_SITENAME = "yoursite"
# Enable i18n plugin.
PLUGINS = ["i18n_subsites"]
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}


# Default theme language.
I18N_TEMPLATES_LANG = "en"