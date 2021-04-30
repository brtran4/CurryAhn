"""
Index server python package configuration.

Nilay Muchhala  <nilaym@umich.edu>
Aneeqa Fatima   <aneeqaf@umich.edu>
"""

from setuptools import setup

setup(
    name='curryahn',
    version='0.1.0',
    packages=['curryahn'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'bs4',
        'Flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'requests',
        'selenium',
    ],
    python_requires='>=3.6',
)
