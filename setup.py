from setuptools import setup, find_packages
from cmake_setuptools import __version__

setup(name='cmake_setuptools',
      description='Provides some usable cmake related build extensions',
      author='Ray Douglass',
      url='https://github.com/raydouglass/cmake_setuptools',
      version=__version__,
      install_requires=['setuptools'],
      license="Apache 2.0",
      packages=find_packages())
