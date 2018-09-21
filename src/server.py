"""
Bootstrapper script for instantiating a server

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

import RPi.GPIO as GPIO
import connexion
from flask import redirect

if __name__ == '__main__':
	# Create a basic server
	app = connexion.App('a-pi-api')
	# Populate it with the API
	app.add_api('v0/spec.yml')
	# Provide a redirect to the UI
	def gotoUI():
		return redirect('/v0/ui/#/pins')
	app.add_url_rule('/', view_func=gotoUI)
	# Run the server
	app.run(host='0.0.0.0', port=80)
