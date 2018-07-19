import os
from setuptools import setup
 
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
 
# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name = 'playingcard',
    version = '0.1.0',
    packages = ['playingcard'],
    include_package_data = True,
    license = 'BSD License',
    description = 'A playing card model used to play card games.',
    long_description = README,
    test_suite='tests',
    url = 'http://www.example.com/',
    author = 'Gordon Collins',
    author_email = 'gordon.collins@excella.com',
    classifiers =[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)