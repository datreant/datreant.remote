#! /usr/bin/python
"""Setuptools-based setup script for datreant.

For a basic installation just type the command::

  python setup.py install

"""

from setuptools import setup, find_packages

setup(name='datreant.remote',
      version='0.8.0-dev',
      description='Treants on remote machines',
      author='Joy Monteiro',
      author_email='',
      url = 'http://datreant.org/',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      packages=find_packages('src'),
      namespace_packages=['datreant'],
      package_dir={'': 'src'},
      scripts=[],
      license='BSD',
      long_description=open('README.rst').read(),
      install_requires=[]
      )
