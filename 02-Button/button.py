# button.py
# Written by Zachary Ferguson.
# A program for the Raspberry Pi that reads the state of a button and controls 
# the state of a LED.

# Import the necessary files for GPIO use and sleeping the program.
import RPi.GPIO as GPIO

# Constant for the pin to which the LED is plugged attached.
LED_PIN = 25
# Constant for the pin to which the button is plugged attached.
BUTTON_PIN = 24

# Setup the GPIO pins for an output on LED_PIN.
def setup():
	print("Setting up GPIO")
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED_PIN, GPIO.OUT)   # Set the LED pin as an output.
	GPIO.setup(BUTTON_PIN, GPIO.IN) # Set the button pin as an input.
	print("Done Setup\n\nPush the Button.")

# Loop function for the program that reads the state of the button then writes 
# the state to the LED. 
def loop():
	# Get the state of the button.
	buttonState = GPIO.input(BUTTON_PIN)
	 # Set the LED to the same state as the button.
	GPIO.output(LED_PIN, buttonState)
	
# Main function for the script. 
# Sets up then loops then cleans up.
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