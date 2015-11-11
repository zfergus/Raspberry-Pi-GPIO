# CharLCD.py
# Written by Zachary Ferguson.
# A class for a character liquid crystal display. Uses the 4-bit communication 
# standard.

class CharLCD:
	
	# Commands
	LCD_CLEARDISPLAY = 0x01
	LCD_NEWLINE = 0xC0
	
	def __init__(self, regsel_pin, clk_pin, data_pins):
		# Save the pins to fields of this instance.
		self.regsel_pin = regsel_pin
		self.clk_pin    = clk_pin
		self.data_pins  = data_pins
		
		# Setup the pins using RPi.GPIO.
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.regsel_pin, GPIO.OUT)
		GPIO.setup(self.clk_pin, GPIO.OUT)
		for pin in self.data_pins:
			GPIO.setup(pin, GPIO.OUT)
			
		# Clear the LCD's screen.
		self.clear()
	
	def clear(self):
		write(LCD_CLEARDISPLAY)
		
	def cmd(self, bits, char_mode = False):
		return
		
	def message(self, str):
		for c in str:
			if c == '\n':
				self.cmd(LCD_NEWLINE) # Next Line Command
			else:
				self.cmd(ord(c), True);