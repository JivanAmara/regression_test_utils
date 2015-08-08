import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='regression-test-utils',
    version='0.1',
    packages=['regression_test_utils'],
    include_package_data=True,
    description='Facilitates fairly easy creation of regression tests.',
    long_description=README,
    url='https://github.com/JivanAmara/regression_test_utils',
    author='Jivan Amara',
    author_email='Development@JivanAmara.net',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = [
        'jsonpickle',
    ],
)

