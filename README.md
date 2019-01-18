# CMake Setuptools

A small library of `setuptools` extensions to ease building python packages which have a cmake component.

## Install

`pip install cmake_setuptools`

## Usage

```python
from setuptools import setup
from cmake_setuptools import *

setup(name='mypackage',
      description='',
      version='0.0.0.dev0',
      ext_modules=[CMakeExtension('make_target')],
      cmdclass={'build_ext': CMakeBuildExt}
      )
```