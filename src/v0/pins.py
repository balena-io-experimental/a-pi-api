"""
A library of functions for interacting with the pins on an RPi3.
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


import RPi.GPIO as GPIO
from . import pin
GPIO.setmode(GPIO.BOARD)

AVAILABLE_PINS = frozenset((
	3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21,
	22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40,
))

def get():
	return list(pin.get(p) for p in AVAILABLE_PINS)

def patch(pins):
	return list(pin.put(p['id'], p) for p in pins)
