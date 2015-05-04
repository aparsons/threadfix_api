from setuptools import setup

from threadfix_api import __version__ as version


setup(
    name='threadfix_api',
    packages=['threadfix_api'],
    version=version,
    description='An API wrapper to facilitate interactions to and from ThreadFix.',
    author='Adam Parsons',
    author_email='adam@aparsons.net',
    url='https://github.com/aparsons/threadfix_api',
    download_url='https://github.com/aparsons/threadfix_api/tarball/' + version,
    license='MIT',
    install_requires=['requests'],
    keywords=['threadfix', 'api', 'http'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
