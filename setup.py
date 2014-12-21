#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import mypersonal
version = mypersonal.__version__

setup(
    name='mypersonal',
    version=version,
    author='',
    author_email='btanne6@gmail.com',
    packages=[
        'mypersonal',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['mypersonal/manage.py'],
)
