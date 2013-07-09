try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': '$name',
    'description': '$name description.',
    'author': 'Cesar Saez',
    'author_email': 'cesarte@gmail.com',
    'url': 'https://www.github.com/csaez/$name',
    'version': '0.1.0',
    'install_requires': ['nose'],
    'packages': ['$name'],
    'scripts': []
}

setup(**config)
