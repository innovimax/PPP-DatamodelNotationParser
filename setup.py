#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='ppp_datamodel_notation_parser',
    version='0.1.8',
    description='A module parsing a human-writable representation of a question tree.',
    url='https://github.com/ProjetPP',
    author='Valentin Lorentz',
    author_email='valentin.lorentz+ppp@ens-lyon.org',
    license='MIT',
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Development Status :: 1 - Planning',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'ply',
        'ppp_datamodel>=0.6,<0.7',
        'ppp_libmodule>=0.7',
    ],
    packages=[
        'ppp_datamodel_notation_parser',
    ],
)
