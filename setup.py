#!/usr/bin/env python

from distutils.core import setup
from comrunner import __version__

setup(name='ComRunner',
      version=__version__,
      description='Commandline runner utility',
      long_description='Commandline runner utility',
      author='Guillaume Dugas',
      author_email='dugas.guillaume@gmail.com',
      download_url='https://github.com/gdugas/comrunner/archive/0.1.zip',
      py_modules=['comrunner'],
      url='https://github.com/gdugas/comrunner/archive/0.1.zip',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators'
      ]
     )
