#!/usr/bin/env python
#
# Example of how to use the MapPlotter class
# on a custom created figure and axes.
#
# Arnau Miro, Elena Terzic (2023)
from __future__ import print_function

import os, numpy as np, matplotlib.pyplot as plt
import MapPlotter as mp


## DATA PATHS ##
PATH     = os.path.dirname(os.path.abspath(__file__))
fname    = os.path.join(PATH,'CMEMS.2020.thetao.nc')
varname  = 'thetao'
lonname  = 'lon'
latname  = 'lat'
outfile  = 'example1.png'
outdpi   = 300


# Instance MapPlotter class
# This is needed in order to access the projection
plotter = mp.MapPlotter(projection='PlateCarree')

# Create matplotlib figures
fig  = plt.figure(figsize=(8,6),dpi=300,facecolor='w',edgecolor='k')
ax   = fig.add_subplot(1,1,1,projection=plotter.projection)

# Create basic parameters dictionary
params  = plotter.defaultParams()
# DPI
params['dpi']      = 100
# Set figure and axes
params['fig']      = fig
params['ax']       = ax
# Limits for the plot
params['xlim']     = [11, 21]
params['ylim']     = [39, 46]
# Which features need to be plotted?
params['features'] = ['coastline','continents','rivers','image']
params['img']      = 'https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73726/world.topo.bathy.200406.3x5400x2700.png'
# A bit of formatting on the title and axis
params['title']    = ['Temperature Map',{'weight':'bold','style':'italic'}]
params['xlabel']   = ['Longitude (deg)']
params['ylabel']   = ['Latitude (deg)']
# A bit of formatting on the colorbar
params['cmap']     = 'cmo.thermal'
params['bounds']   = [5,18]
params['label']    = {'label':'Temperature (deg C)','weight':None,'style':None}
print(params)

# Plot
plotter.plot_from_file(fname,varname,lonname,latname,iTime=0,iDepth=0,params=params)

# Save and show
plotter.save(outfile,dpi=outdpi)
plotter.show()