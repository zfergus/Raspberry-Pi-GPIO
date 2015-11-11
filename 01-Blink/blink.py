# blink.py
# Written by Zachary Ferguson.
# A program for the Raspberry Pi that blinks a LED.

# Import the necessary files for GPIO use and sleeping the program.
import RPi.GPIO as GPIO
from time import sleep

# Constant for the pin to which the LED is plugged attached.
LED_PIN = 25

# Setup the GPIO pins for an output on LED_PIN.
def setup():
	print("Setting up GPIO")
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED_PIN, GPIO.OUT)

# Loop through the blink cycle, Off -> Sleep(2) -> On -> Sleep(2) -> Off.
# Ends in the off state, but without a sleep after.
def loop():
	# LED OFF
	GPIO.output(LED_PIN, False)
	print("LED is OFF")
	sleep(1)
	
	# LED ON
	GPIO.output(LED_PIN, True)
	print("LED is ON")
	sleep(1)
	
	# LED OFF; NO SLEEP
	GPIO.output(LED_PIN, False)

# Main function for blink. Sets up then loops then cleans up.
def main():
	try:
		setup()
		while True:
			loop()
	except (KeyboardInterrupt, SystemExit):
		print("\nCleaning up GPIO")
		GPIO.cleanup()
		print("Exiting")
		exit()
	
# If being run directly.
if __name__=="__main__":
	main()