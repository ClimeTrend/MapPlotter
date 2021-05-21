#!/bin/env python
#
# MapPlotter tool
#
# Last rev: 2021
from __future__ import print_function, division

import sys, os, numpy as np

from setuptools import setup, find_packages

with open('README.md') as f:
	readme = f.read()

# Main setup
setup(
	name="MapPlotter",
	version="2.0.0",
    long_description=readme,
    url='https://github.com/ArnauMiro/MEP.git',
    packages=find_packages(exclude=('Examples', 'doc')),
	install_requires=['numpy','matplotlib','cartopy','datetime','netCDF4']
)