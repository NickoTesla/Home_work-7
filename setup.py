from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='A tool to clean up a folder by moving files into subfolders based on their extensions',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': ['clean-folder=clean_folder.clean:main'],
    },
)
