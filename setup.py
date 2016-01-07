#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pyduino-includes',
    description="Basic SNAPpy includes for the Synapse Pyduino wireless meshing development board",
    maintainer='Tyler Crumpton',
    maintainer_email='tyler.crumpton@synapse-wireless.com',
    url='https://git.synapse-wireless.com/tyler.crumpton/pyduino-includes',
    packages=['PyduinoIncludes'],
    install_requires=['vcversioner'],
    vcversioner={
        'version_module_paths': ['PyduinoIncludes/_version.py'],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
    ],
)
