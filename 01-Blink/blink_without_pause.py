# blink_without_pause.py
# created by Zachary Ferguson
# A program for the Raspberry Pi that blinks an led. Does so without using 
# the time.pause function.

# Import the necessary files for GPIO use and getting the current time.
import RPi.GPIO as GPIO
import time

# Constant for the pin the LED is plugged in on.
LED_PIN = 25

# Boolean for if the LED is currently on.
ledState = False

# The time in milliseconds of the last switch.
previousTime = 0

# Amount of time in milliseconds between LED state switches.
delayTime = 1000

# Setup the GPIO pins for an output on LED_PIN.
def setup():
	print "Setting up GPIO"
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED_PIN, GPIO.OUT)
	previousTime = time.time() # Initialize the start time.

# Loop through the blink cycle, Off -> Sleep(2) -> On -> Sleep(2) -> Off.
# Ends in the off state, but without a sleep after.
def loop():
	currentTime = time.time() # The current time in milliseconds.
	# If enough time has passed since the last switch.
	if(currentTime-previousTime >= delayTime):
		previousTime = currentTime
		ledState = not ledState
		# Switch the state of the LED.
		GPIO.output(LED_PIN, ledState)
		print "LED is %s" % ("ON" if ledState else "OFF")

# Main function for blink. Sets up then loops then cleans up.
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