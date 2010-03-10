"""
Copyright 2009 Myles Braithwaite <me@mylesbraithwaite.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from setuptools import setup, find_packages

setup(
	name = "http2pg",
	version = "0.1",
	url = "http://github.com/myles/http2pg",
	license = "Apache 2.0",
	description = "Get an HTTP request (in SQL) sends it to PostgreSQL and reply's in JSON.",
	
	author = "Myles Braithwaite",
	author_email = "me@mylesbraithwaite.com",
	
	packages = [
		'http2pg',
	],
	
	install_requires = [
		'distribute',
		'web.py'
	],
	
	# entry_points = {
	# 	'console_scripts': [],
	# },
	
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
	],
)