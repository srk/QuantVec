# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('beacon_utils.py').read(),
    re.M
    ).group(1)

setup(
    name = "beacon_utils",
    py_modules=['beacon_utils'],
    version = version,
    author='Prof. Steven R. Kirk, BEACON Research Group',
    author_email='stevenrkirk@gmail.com',
    description = "beacon_utils",
    url = 'https://www.beaconresearch.org',
    )