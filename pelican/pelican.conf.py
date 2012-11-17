#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Dedi Purwanto"
SITENAME = u"Dedi Purwanto"
SITEURL = 'http://kecebongsoft.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG='en'

SOCIAL =  (
            ('github','http://github.com/kecebongsoft'),
            ('twitter','http://twitter.com/kecebongsoft'),
            ('geekli.st','http://geekli.st/kecebongsoft'),
            ('julython 2012','http://julython.org/kecebongsoft'),
         )

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
