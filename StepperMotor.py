import wiringpi2
from datetime import datetime

class Stepper:
	stepPin = 0 #pin numbers
	dirPin = 0
	curPos = 0
	def __init__(self, stepPin, dirPin):
		#initial a Bipolar_Stepper_Moter objects by assigning the pins
		wiringpi2.wiringPiSetupPhys()

		self.stepPin = stepPin
		self.dirPin = dirPin
		self.stepsInFullRound = 400

		wiringpi2.pinMode(self.stepPin,1)
		wiringpi2.pinMode(self.dirPin,1)
		print ("[{0}] Stepper Configured on stepPin: {1}; dirPin:{2}".format(datetime.now(),stepPin, dirPin))

	def move(self, direction1, delay):
		# direction - 1 or 0
		# delay - in microseconds !!
		if direction1 == 1:
			wiringpi2.digitalWrite(self.dirPin, 1);
		else:
			wiringpi2.digitalWrite(self.dirPin, 0);
		wiringpi2.delayMicroseconds(2) # wait for setup direction state
		wiringpi2.digitalWrite(self.stepPin,0)
		wiringpi2.delayMicroseconds(int(delay//2))
		wiringpi2.digitalWrite(self.stepPin,1)
		wiringpi2.delayMicroseconds(int(delay//2))
	
	def step(self, direction1):
		# direction - 1 or 0
		if direction1 == 1:
			wiringpi2.digitalWrite(self.dirPin, 1);
			curPos=curPos+1
		else:
			wiringpi2.digitalWrite(self.dirPin, 0);
			curPos=curPos-1
		wiringpi2.delayMicroseconds(2) # wait for setup direction state
		wiringpi2.digitalWrite(self.stepPin,0)
		wiringpi2.delayMicroseconds(2)
		wiringpi2.digitalWrite(self.stepPin,1)
		wiringpi2.delayMicroseconds(2)
