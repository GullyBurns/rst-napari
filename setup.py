from setuptools import setup
import os
import sys

setup(
    name='ontomatch',
    version='1.0.0',
    packages=['ontomatch',
              'ontomatch.data',
              'ontomatch.mentions',
              'ontomatch.text',
              'ontomatch.utils'],
    package_dir={'ontomatch': 'Python/ontomatch'},
    url='https://github.com/chanzuckerberg/rst-napari',
    license='MIT',
    author='Sunil Mohan',
    author_email='smohan@chanzuckerberg.com',
    description='Code for finding ontology term matches in natural language descriptions.',
    install_requires=[
        'nltk>=3.5', 'pygtrie==2.4.2', 'Unidecode>=1.3.4', 'numpy'
    ]
)