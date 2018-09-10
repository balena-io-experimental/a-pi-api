"""
A library of functions for interacting with the pins on an RPi3.
The documentation for each function resides in spec.yml, the swagger
spec

Copyright 2018 Andrew Lucas

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
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

def get(id):
	# This pin is in output-ish mode, so set it up and read its emit,
	# which logically is the `HIGH` or `LOW` mode configured
	if GPIO.gpio_function(int(id)) == GPIO.OUT:
		GPIO.setup(int(id), GPIO.OUT)
		mode = "HIGH" if GPIO.input(int(id)) == GPIO.HIGH else "LOW"
	# This pin is not an output, so set it up and note that it is `IN`
	else:
		GPIO.setup(int(id), GPIO.IN)
		mode = "IN"
	# Pass to upstream the id, mode and retrieved value of the pin
	return {
		"id": str(id),
		"mode": mode,
		"value": "HIGH" if GPIO.input(int(id)) == GPIO.HIGH else "LOW"
	}

def put(id, pin):
	# Set the pin to output high
	if pin['mode'] == 'HIGH':
		GPIO.setup(int(id), GPIO.OUT, initial=GPIO.HIGH)
	# Set the pin to output low
	elif pin['mode'] == 'LOW':
		GPIO.setup(int(id), GPIO.OUT, initial=GPIO.LOW)
	# Set the pin to input
	elif pin['mode'] == 'IN':
		GPIO.setup(int(id), GPIO.IN)
	# Return the pin
	return get(id)
