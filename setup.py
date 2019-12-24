# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in abacus_first_solutions/__init__.py
from abacus_first_solutions import __version__ as version

setup(
	name='abacus_first_solutions',
	version=version,
	description='Abacus First Solutions',
	author='AFS',
	author_email='afs@afs.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
