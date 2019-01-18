from setuptools import setup, find_packages
from cmake_setuptools import __version__

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='cmake_setuptools',
      description='Provides some usable cmake related build extensions',
      long_description=long_description,
      author='Ray Douglass',
      url='https://github.com/raydouglass/cmake_setuptools',
      version=__version__,
      install_requires=['setuptools'],
      license="Apache 2.0",
      packages=find_packages())
