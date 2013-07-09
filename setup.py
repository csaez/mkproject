from setuptools import setup

setup(
    name="mkproject",
    version="0.1.0",
    packages=["mkproject"],
    package_data={"mkproject": ["templates/*.*"]},
    author="Cesar Saez",
    author_email="cesarte@gmail.com",
    description="A simple template for python projects.",
    url="http://csaez.blogspot.com",
    license="GNU General Public License (GPLv3)",
    entry_points={"console_scripts": ["mkproject = mkproject:main"]},
)
