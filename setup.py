#!/usr/bin/env python
#
# MapPlotter tool
#
# Last rev: 2021
from __future__ import print_function, division

import sys, os, numpy as np

from setuptools import setup, find_packages
from MapPlotter import __VERSION__

with open('README.md') as f:
	readme = f.read()

# Main setup
setup(
	name               = "MapPlotter",
	version            = __VERSION__,
	author             = 'Arnau Miro, Elena Terzić',
	author_email       = 'arnau.miro@upc.edu, elena.terzic@proton.me',
	maintainer         = 'Arnau Miro',
	maintainer_email   = 'arnau.miro@upc.edu',
    long_description   = readme,
    url                = 'https://github.com/ArnauMiro/MapPlotter',
    packages           = find_packages(exclude=('Examples', 'doc')),
	install_requires   = ['numpy','matplotlib','cartopy','cmocean','datetime','netCDF4'],
	scripts            = ['bin/map_plotter']
)