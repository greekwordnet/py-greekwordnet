from setuptools import setup, find_packages
from os import path

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='greekwordnet',
    version='0.0.1-post1',
    packages=find_packages(),
    url='https://greekwordnet.chs.harvard.edu',
    license='GNU General Public License v3.0',
    author='William Michael Short',
    author_email='w.short@exeter.ac.uk',
    description='A light-weight wrapper for the Ancient Greek WordNet API',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
