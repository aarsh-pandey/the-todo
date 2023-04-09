from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

classifiers = [
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
]

setup(
    name='the-todo',
    version='0.1.0a1',
    url='https://github.com/aarsh-pandey/the-todo',
    description='A simple command line todo application',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Aarsh Pandey',
    classifiers=classifiers,
    packages=find_packages(),
    install_requires=["termcolor"],
    zip_safe=False
)
