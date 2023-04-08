from setuptools import setup, find_packages

setup(
    name='the-todo',
    version='0.1',
    description='A simple command line todo application',
    packages=find_packages(),
    install_requires=["termcolor"],
    zip_safe=False
)