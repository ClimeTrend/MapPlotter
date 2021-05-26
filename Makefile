# Compile MapPlotter
#   Compile with g++ or Intel C++ Compiler (/opt/intel/bin/icpc)
#   Compile with the most aggressive optimization setting (O3)
#   Use the most pedantic compiler settings: must compile with no warnings at all
#
# The user may override any desired internal variable by redefining it via command-line:
#   make CXX=g++ [...]
#   make OPTL=-O2 [...]
#   make FLAGS="-Wall -g" [...]
#
# David de la Torre / Arnau Miro
# November 2018

# Compilers
#
# Automatically detect if the intel compilers are installed and use
# them, otherwise default to the GNU compilers
PYTHON = python
PIP    = pip

# One rule to compile them all, one rule to find them,
# One rule to bring them all and in the compiler link them.
all:  requirements install
	@echo ""
	@echo "MapPlotter deployed successfully"


# Python
#
requirements: requirements.txt
	@${PIP} install -r $<

install: 
	@${PIP} install .

install_dev: 
	@${PIP} install -e .


# Clean
#
clean:
	-@cd MapPlotter; rm -rf __pycache__
uninstall: clean
	-@${PIP} uninstall MapPlotter
	-@rm -rf MapPlotter.egg-info