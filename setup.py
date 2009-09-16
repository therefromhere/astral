# Copyright 2009, Simon Kennedy, python@sffjunkie.co.uk
# Distributed under the terms of the MIT License.

from distutils.core import setup

setup(name='astral',
    version='0.01',
    description='Calculations for the position of the sun.',
    long_description='Sun calculations for dawn, sunrise, solar noon, sunset, dusk, solar elevation, solar azimuth and rahukaalam.',
    author='Simon Kennedy',
    author_email='python@sffjunkie.co.uk',
    url="http://www.sffjunkie.co.uk/odds.html",
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['astral']
)
