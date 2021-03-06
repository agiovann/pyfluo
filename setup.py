#from distutils.core import setup, Extension #it's either this line (distutils) or the next (setuptools). both work, using setuptools because it supports develop mode
from setuptools import find_packages, setup, Extension
from distutils.sysconfig import get_python_inc
readme = open('README.txt').read()
import os
import numpy as np

incdir = os.path.join(get_python_inc(plat_specific=1), 'Numerical')

setup(	name = 'pyfluo',
		version = '2.0',
		author = 'Ben Deverett',
		author_email = 'bendeverett@gmail.com',
		url = 'https://github.com/bensondaled/pyfluo',
		description = 'A python library for Ca imaging data analysis.',
		long_description = readme,
		keywords = 'pyfluo fluorescence calcium ca imaging',
		packages = find_packages(),
		data_files = [	('', ['LICENSE.txt']),
						('', ['README.txt']),
												],
		install_requires = ['numpy', 'scipy', 'matplotlib'], 
        include_dirs = [incdir, np.get_include()]
        
        )
