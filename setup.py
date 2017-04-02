"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from xudo import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=xudo', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'xudo',
    version = __version__,
    description = 'A command line program for docker',
    long_description = long_description,
    url = 'https://github.com/ostralyan/xudo',
    author = 'Luke Xu',
    author_email = 'lukecxu@gmail.com',
    license = 'MIT License',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt', 'requests'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'xudo=xudo.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)