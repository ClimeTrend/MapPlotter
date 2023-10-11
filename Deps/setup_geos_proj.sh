#!/bin/bash
#
# Script to setup GEOS and PROJ
# for CARTOPY.
#
# Specially thought for the Github pipelines
#
# Arnau Miro, Elena Terzic (2023)


## Install geos libraries
GEOS_VERS=3.7.2
GEOS_DIR="geos-${GEOS_VERS}"
GEOS_TAR="${GEOS_DIR}.tar.bz2"
curl --output ${GEOS_TAR} "http://download.osgeo.org/geos/${GEOS_TAR}"
tar xf $GEOS_TAR && cd $GEOS_DIR
cd ../

# Configure 
mkdir build
cd build
cmake ../$GEOS_DIR \
	-DCMAKE_BUILD_TYPE=Release \
	-DGEOS_ENABLE_TESTS=OFF \
	-DGEOS_BUILD_SHARED=ON \
	-DGEOS_BUILD_STATIC=ON 

# Build
read -s -p "Please check install configuration and press [enter]..."
make -j $(getconf _NPROCESSORS_ONLN)
make install
cd ../ && rm -rf build $GEOS_DIR $GEOS_TAR


## Install proj libraries
PROJ_VERS=5.2.0
PROJ_DATV=1.8
PROJ_DIR=proj-$PROJ_VERS
PROJ_TAR=$PROJ_DIR.tar.gz
PROJ_DATG=proj-datumgrid-$PROJ_DATV.zip

curl --output $PROJ_TAR https://download.osgeo.org/proj/$PROJ_TAR
tar xvf $PROJ_TAR && cd $PROJ_DIR

curl --output $PROJ_DATG https://download.osgeo.org/proj/$PROJ_DATG
unzip $PROJ_DATG -d data/

./configure 
read -s -p "Please check install configuration and press [enter]..."
make -j $(getconf _NPROCESSORS_ONLN)
make install
cd ../ && rm -rf $PROJ_DIR $PROJ_TAR


## Install cartopy and pyepsg
pip install cartopy pyepsg
pip uninstall shapely
pip install --no-binary :all: shapely