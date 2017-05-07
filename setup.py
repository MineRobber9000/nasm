#!/usr/bin/env python

from setuptools import setup

with open("README.rst") as readme:
    long_description = readme.read()

install_requires = []

setup(
    name='nasm',
    version='0.1.0',
    description='A tool for generating 6502 assembly',
    long_description=long_description,
    author='Robert Miles',
    author_email='milesrobert374@gmail.com',
    url='https://github.com/MineRobber9000/nasm',
    keywords='6502 languages',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=['nasm'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'nasm=nasm.console:main',
        ],
    }
)
