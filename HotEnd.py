import wiringpi2
from datetime import datetime

class HotEnd:
	controlPin = 0
	curTemp = 0

	def __init__(self, controlPin):
		wiringpi2.wiringPiSetupPhys()
		self.controlPin = controlPin
		wiringpi2.pinMode(self.controlPin,1)
		print ("[{0}] HotEnd Configured on pin {1}".format(datetime.now(),controlPin))

	def heat(self):
		wiringpi2.digitalWrite(self.controlPin,1)

	def coolDown(self, direction1):
		wiringpi2.digitalWrite(self.controlPin,0)