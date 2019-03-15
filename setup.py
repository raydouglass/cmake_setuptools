from setuptools import setup, find_packages
from cmake_setuptools import __version__

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='cmake_setuptools',
      description='Provides some usable cmake related build extensions',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Ray Douglass',
      url='https://github.com/raydouglass/cmake_setuptools',
      version=__version__,
      install_requires=['setuptools', 'wheel'],
      license="Apache 2.0",
      packages=find_packages(),
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Build Tools'
      ],
      entry_points={
          'console_scripts': [
              'rename-wheel=cmake_setuptools.utils:rename_package_wheel_main'
          ]
      }
      )
