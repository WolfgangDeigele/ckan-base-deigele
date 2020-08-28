from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(
	name='ckanbase-deigele',
	version=version,
	description="CKAN base files",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Wolfgang Deigele',
	author_email='wolfgang.deigele@tum.de',
	url='',
	license='Affero General Public License (AGPL)',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.grouphierarchy'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	""",
)