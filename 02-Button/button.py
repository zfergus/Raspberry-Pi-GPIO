# button.py
# created by Zachary Ferguson
# A program for the Raspberry Pi that reads the state of a switch and controls 
# the state of a LED.

# Import the necessary files for GPIO use and sleeping the program.
import RPi.GPIO as GPIO

# Constant for the pin the LED is plugged in on.
LED_PIN = 25

# Setup the GPIO pins for an output on LED_PIN.
def setup():
	print "Setting up GPIO"
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED_PIN, GPIO.OUT)

# Loop function for the program that reads the state of the switch then writes 
# this state to the LED.
def loop():
	return

# Main function for the script. 
# Sets up then loops then cleans up.
def main():
	try:
		setup()
		while True:
			loop()
	except (KeyboardInterrupt, SystemExit):
		GPIO.cleanup()
		raise
	
# If being run directly.
if __name__=="__main__":
	main()