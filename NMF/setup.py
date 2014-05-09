########################################################
# setup.py 
# setup script to build extension model for UIPCC_core 
# Author: Jamie Zhu <jimzhu@GitHub>
# Created: 2014/4/20
# Last updated: 2014/5/3
########################################################


import sys
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import shutil

print('Build extension modules...')
print('==============================================')

ext_modules = [Extension('NMF',
				['src/NMF_core/NMF.pyx', 'src/NMF_core/NMF_core.cpp'],
				language='c++'
              )]

setup(
	name = 'Extended Cython module for NMF',
	cmdclass = {'build_ext': build_ext},
	ext_modules = ext_modules
)

shutil.move('NMF.so', 'src/NMF.so')
print('==============================================')
print('Build done.\n')

