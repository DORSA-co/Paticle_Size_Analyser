from distutils.core import setup, Extension
from Cython.Build import cythonize
import os
import numpy

#python setupCythons.py build_ext --inplace
cython_madules = [ 'backend\\Processing\\utiltsCython.pyx',
                  ]

for madule in cython_madules:
    setup(ext_modules = cythonize(madule, build_dir = os.path.split(madule)[0]), 
            include_dirs=[numpy.get_include()],
            
             )


