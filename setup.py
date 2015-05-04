#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from threadfix_api import __version__ as version

with open('README.rst', 'r') as f:
    readme = f.read()

# Publish helper
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    #os.system('python setup.py sdist bdist_wheel upload -r pypitest')
    sys.exit(0)

setup(
    name='threadfix_api',
    packages=['threadfix_api'],
    version=version,
    description='An API wrapper to facilitate interactions with ThreadFix.',
    long_description=readme,
    author='Adam Parsons',
    author_email='adam@aparsons.net',
    url='https://github.com/aparsons/threadfix_api',
    download_url='https://github.com/aparsons/threadfix_api/tarball/' + version,
    license='MIT',
    install_requires=['requests'],
    keywords=['threadfix', 'api', 'security', 'software'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
