mkproject
=========
`mkproject` is a simple console script that generate a basic python project structure.

Installation
------------

    python setup.py install

Ussage
------

Type `mkproject PROJECT_NAME` on a shell. It should create the following project structure.

    CHANGES.txt
    LICENSE.txt
    MANIFEST.in
    README.md
    setup.py
    bin/
    docs/
    PROJECT_NAME/
      __init__.py
      tests/
        __init__.py
        PROJECT_NAME_tests.py

### Where:

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

file: `PROJECT_NAME_tests.py`

    from nose.tools import *
    import PROJECT_NAME

    def setup():
        print "SETUP!"

    def teardown():
        print "TEAR DOWN!"

    def test_basic():
        print "I RAN!"
