mkproject
=========
A simple template for python projects.

Ussage
------

Type `mkproject C:\DEV\PROJECT_NAME` on a shell and it should create the following directory structure.

    setup.py
    PROJECT_NAME/
      __init__.py
    bin/
    docs/
    tests/
      PROJECT_NAME_tests.py
      __init__.py

Where:

file: `setup.py`

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    config = {
        'description': 'My Project',
        'author': 'My Name',
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'My email.',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['PROJECT_NAME'],
        'scripts': [],
        'name': 'PROJECT_NAME'
    }

    setup(**config)

file: `NAME_tests.py`

    from nose.tools import *
    import PROJECT_NAME

    def setup():
        print "SETUP!"

    def teardown():
        print "TEAR DOWN!"

    def test_basic():
        print "I RAN!"
