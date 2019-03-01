from distutils.core import setup
from Cython.Build import cythonize

setup(name='opendht',
      ext_modules=cythonize("opendht.pyx"))
