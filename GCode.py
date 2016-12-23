import wiringpi2

class GCode:
	def __init__(self, stepPin, dirPin):
		#initial a Bipolar_Stepper_Moter objects by assigning the pins
		wiringpi2.wiringPiSetupPhys()

		self.stepPin = stepPin
		self.dirPin = dirPin
		self.stepsInFullRound = 400

		wiringpi2.pinMode(self.stepPin,1)
		wiringpi2.pinMode(self.dirPin,1)
		print "Gcode Parser Configured"


