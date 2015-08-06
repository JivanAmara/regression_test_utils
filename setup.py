import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='test-utils',
    version='0.1',
    packages=['test-utils'],
    include_package_data=True,
    description='Automatically collects information for easy regression test creation.',
    long_description=README,
    url='https://github.com/JivanAmara/test_utils',
    author='Jivan Amara',
    author_email='Development@JivanAmara.net',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
