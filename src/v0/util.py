"""
Utility functions for monitoring and changing the server status
The documentation for each function resides in spec.yml, the swagger
spec

Copyright 2018 resin.io

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import connexion
import hashlib
from os import environ

def status():
	return {
		'status': 'OK'
	}

def checkAuth():
	"""
	Checks the authorization header against the most secure method
	provided in the environment variables.
	Returns a string (truthy) describing the auth passed, or False.
	"""
	if('AUTH_SHA256' in environ):
		# The SHA256 of `test` is
		# `9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08`
		if 'Authorization' not in connexion.request.headers:
			return False
		hash = hashlib.sha256(connexion.request.headers['Authorization'].encode('utf-8')).hexdigest()
		return 'SHA256' if hash == environ['AUTH_SHA256'].lower() else False
	elif('AUTH_SHA1' in environ):
		# The SHA1 of `test` is
		# `A94A8FE5CCB19BA61C4C0873D391E987982FBBD3`
		if 'Authorization' not in connexion.request.headers:
			return False
		hash = hashlib.sha1(connexion.request.headers['Authorization'].encode('utf-8')).hexdigest()
		return 'SHA1' if hash == environ['AUTH_SHA1'].lower() else False
	elif('AUTH_MD5' in environ):
		# The MD5 of `test` is
		# `098F6BCD4621D373CADE4E832627B4F6`
		if 'Authorization' not in connexion.request.headers:
			return False
		hash = hashlib.md5(connexion.request.headers['Authorization'].encode('utf-8')).hexdigest()
		return 'MD5' if hash == environ['AUTH_MD5'].lower() else False
	elif('AUTH_PLAIN' in environ):
		if 'Authorization' not in connexion.request.headers:
			return False
		hash = connexion.request.headers['Authorization']
		return 'PLAIN' if hash == environ['AUTH_PLAIN'] else False
	elif('AUTH_NONE' in environ):
		return 'NONE'
	else:
		return False
