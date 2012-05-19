# -*- coding: utf-8 -*-
from distutils.core import setup, Extension

module1 = Extension('dmhash', sources = ['dmhash.c'])

setup (name = 'dmhash',
       version = '1.0',
       author = u'Zhang Ping',
       author_email = 'zhangping@dvnchina.com',
       maintainer = u'Zhang Ping',
       maintainer_email = 'zhangping@dvnchina.com',
       url = 'www.dvnchina.com',
       license = 'http://www.gnu.org/licenses/gpl.txt',
       platforms = ['Linux'],
       description = 'dmhash',
       long_description = "dm hash",
       classifiers = "alpha",
       ext_modules = [module1])
