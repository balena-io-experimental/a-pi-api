import RPi.GPIO as GPIO
import connexion

if __name__ == '__main__':
	app = connexion.App('a-pi-api')
	app.add_api('v0/spec.yml')
	app.run(host='0.0.0.0', port=80)
