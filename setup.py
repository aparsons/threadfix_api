from distutils.core import setup


setup(
    name='threadfix_api',
    packages=['threadfix_api'],
    version='1.0.0',
    description='An API wrapper to facilitate interactions to and from ThreadFix.',
    author='Adam Parsons',
    author_email='adam@aparsons.net',
    url='https://github.com/aparsons/threadfix_api',
    download_url='',
    license='MIT',
    install_requires=['requests'],
    keywords=['threadfix', 'api', 'http'],
)
