# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in barcode_batch/__init__.py
from barcode_batch import __version__ as version

setup(
	name='barcode_batch',
	version=version,
	description='Barcode Batch',
	author='vinhnguyen.t090@gmail.com',
	author_email='vinhnguyen.t090@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
