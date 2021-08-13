#!/usr/bin/env python
from os.path import exists
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='patsylearn',
      version="0.0.1",
      description='Scikit-lean Patsy adaptor',
      url='http://github.com/amueller/patsylearn/',
      maintainer='Andreas Mueller',
      maintainer_email='t3kcit@gmail.com',
      license='BSD',
      keywords='scikit-learn patsy formula machine-learning',
      packages=['patsylearn'],
      long_description=(open('README.md').read() if exists('README.rst') else''),
      requirements=requirements,
)
