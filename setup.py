from setuptools import setup, find_packages
from os import path
setup(
    name='clean_folder',
    version='1.0.0',
    description='A tool to clean up a folder by moving files into subfolders based on their extensions',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['clean-folder=clean_folder.clean:main'],
    },
)
