#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Dedi Purwanto"
SITENAME = u"Dedi Purwanto"
SITEURL = 'http://kecebongsoft.com'
SITETAGLINE = u""
FOOTERTEXT = u"&copy; Dedi Purwanto. "

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG='en'

LINKS = (
         )

DEFAULT_PAGINATION = 5

PERMALINK_STRUCTURE = '{date:%Y}/{date:%m}/'
ARTICLE_URL = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_URL = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_URL = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_URL = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE
ARTICLE_SAVE_AS = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_SAVE_AS = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_SAVE_AS = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_SAVE_AS = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE

REVERSE_ARCHIVE_ORDER = True

FEED_DOMAIN = 'http://kecebongsoft.com'

THEME = 'notmyidea'

PAGE_EXCLUDES = (
            'env',
            'themes',
            'posts',
        )

ARTICLE_EXCLUDES = (
            'env',
            'themes',
            'pages',
        )

#DISQUS_SITENAME = 'kecebongsoft'
THEME = 'themes/pelican-theme-cebong'
GITHUB_URL = 'https://kecebongsoft.github.com'
