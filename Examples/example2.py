#!/usr/bin/env python
#
# Example of how to use the MapPlotter class
# from already loaded data.
#
# Arnau Miro, OGS (2019)
from __future__ import print_function

import os, numpy as np
import MapPlotter as mp


## DATA PATHS ##
PATH     = os.path.dirname(os.path.abspath(__file__))
fname    = os.path.join(PATH,'CMEMS.2020.thetao.nc')
outfile  = 'example2.png'
outdpi   = 300


# Instance MapPlotter class
plotter = mp.MapPlotter(projection='PlateCarree')

# Create basic parameters dictionary
params  = plotter.defaultParams()
# DPI
params['dpi']      = 100
# Limits for the plot
params['xlim']     = [-6, 37]
params['ylim']     = [30, 46]
# Which features need to be plotted?
params['features'] = ['coastline','continents','rivers','image']
params['img']      = 'https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73726/world.topo.bathy.200406.3x5400x2700.png'
# A bit of formatting on the title and axis
params['title']    = ['Temperature Map',{'weight':'bold','style':'italic'}]
params['xlabel']   = ['Longitude (deg)']
params['ylabel']   = ['Latitude (deg)']
# A bit of formatting on the colorbar
params['cmap']     = 'jet'
params['bounds']   = [5,18]
params['label']    = {'label':'Temperature (deg C)','weight':None,'style':None}
print(params)

# Load data
data = plotter.loadNC(fname,'thetao',mask_value=np.nan)[0,0,:,:]
lon  = plotter.loadNC(fname,'lon')
lat  = plotter.loadNC(fname,'lat')

# Plot
plotter.plot(lon,lat,data,params=params)

# Save and show
plotter.save(outfile,dpi=outdpi)
plotter.show()