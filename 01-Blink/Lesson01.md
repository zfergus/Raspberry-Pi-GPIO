# Lesson 01 - Blink

When learning a new programming language you print out the simple phrase
"Hello, World!" When learning a new graphics library you draws a point on the
screen. In electronics, you blinks an LED! This first lesson is exactly that,
setting up the GPIO programming environment and learning how to turn a LED on
and off.

## Setup

### What you need:

* Raspberry Pi (any model)
* Any color LED
* 220 ohm resistor
* Jumper Cables (female to male if not using a pi cobbler)
* Bread Board
* (Optional) [Pi Cobbler](https://goo.gl/LhVmEg)


### Setting up your Environment

In order to start using the GPIO pins in your python scripts, you first need to
install the GPIO library, RPi.GPIO. This module allows you to interact with the
GPIO pin through function calls. The library is written in Python 2, but is
compatible with Python 3, the version of Python used in these lessons.

To start with you need to update your repository list in order to get the newest
version. Do this by opening a terminal prompt and enter the following command:
```bash
sudo apt-get update
```
Now that your repository list is up to date, you can first install the Python
Development toolkit. This toolkit is required by RPi.GPIO.

Install the tool kit by entering the following command in your terminal:
```shell
sudo apt-get install python-dev
```
Finally, to install the GPIO module enter the following command:
```bash
sudo apt-get install python-rpi.gpio
```
Confirm any prompts by entering `Y`.

Now you should have RPi.GPIO installed and updated, and you are ready to make
your first project.

### The GPIO

// description of the GPIO layout

#### Raspberry Pi A/B rev2:

|        |    |    |        |
| ------:|:--:|:--:| ------ |
|   3.3V |  1 |  2 |     5V |
|  GPIO2 |  3 |  4 |     5V |
|  GPIO3 |  5 |  6 |    GND |
|  GPIO4 |  7 |  8 | GPIO14 |
|    GND |  9 | 10 | GPIO15 |
| GPIO17 | 11 | 12 | GPIO18 |
| GPIO27 | 13 | 14 |    GND |
| GPIO22 | 15 | 16 | GPIO23 |
|   3.3V | 17 | 18 | GPIO24 |
| GPIO10 | 19 | 20 |    GND |
|  GPIO9 | 21 | 22 | GPIO25 |
| GPIO11 | 23 | 24 |  GPIO8 |
|    GND | 25 | 26 |  GPIO7 |

#### Raspberry Pi A+/B+/2:

|        |    |    |        |
| ------:|:--:|:--:| ------ |
|    DNC | 27 | 28 |    DNC |
|  GPIO5 | 29 | 30 |    GND |
|  GPIO6 | 31 | 32 | GPIO12 |
| GPIO13 | 33 | 34 |    GND |
| GPIO19 | 35 | 36 | GPIO16 |
| GPIO26 | 37 | 38 | GPIO12 |
|    GND | 39 | 40 | GPIO21 |

### The Circuit
<center>
    <img src = "../illustrations/Lesson01_Blink.png" title="Circuit Diagram"/>
</center>
<br>
The circuit of this lesson is a fairly simple one. First, use a jumper cable to
connect GPIO pin 25 to the anode of the LED. The LED pictured above is a 505nm
LED but any color LED will work. Next, connect the cathode of the LED to one of
the resistors pins. The resistor regulates the amount of current that flows
through the LED, preventing the LED or the Pi from being damaged. The resistor
used here is a 220 ohm resistor, but any resistor, up to 1K ohm, will work.
Finally, connect the free pin of the resistor to the ground pin on the
Raspberry's GPIO.

## The Code

```python
# Import the necessary files for GPIO use and sleeping the program.
import RPi.GPIO as GPIO
from time import sleep
```

The first thing needed is to import the proper GPIO files and as well as the
time class for pausing execution. Importing RPi.GPIO allows the program to
access to the GPIO functions necessary to control the GPIO. By importing it as
GPIO it is easier to reference later. From time the sleep function is imported
in order to pause execution while the LED is on or off.

```python
# Constant for the pin to which the LED is plugged attached.
LED_PIN = 25
```

Next, a global variable is declared for the pin number on the Raspberry Pi's
GPIO to which the LED is connected.

```python
# Setup the GPIO pins for an output on LED_PIN.
def setup():
    print("Setting up GPIO")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
```

The setup functions initializes the GPIO and sets the LED_PIN to an output.
The function GPIO.setmode sets the way in which the GPIO pins are referenced.
[[1]](#references) This program uses BCM which allows us to refer to pins by
their label rather than their board numbers. GPIO.setup is used to specify a pin
number and whether the pin should be used as output, GPIO.OUT, or input,
GPIO.IN.

```python
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
```

The loop function is the core of the code. This function is looped indefinitely,
turning the LED on and off. It uses the function GPIO.ouput to write
out to a pin, setting it high or low. The function takes two arguments: the
pin number, and a boolean for the state to put the pin in. False indicated low
and True indicated high. The first line turns off the LED then the sleep
function waits one second before continuing execution. The second call to output
turns on the LED and, again, the call to the sleep function pauses execution for
one second. The last call to GPIO.output is just to make sure loop never leaves
with the LED in the on state.

```python
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
```

Finally, the main controlling function of the program, main. Main simply calls
the setup function and then loops indefinitely over the loop function. All of
this is inside of a try-except block so that it can catch any KeyboardInterrupt
or SystemExit. By catching these exceptions the program can clean up the GPIO,
ensuring the GPIO and LED are turned off, and exit cleanly. GPIO.cleanup sets
the pins to low and frees them up for other programs to use later on.
[[2]](#references)

```python
# If being run directly.
if __name__ == "__main__":
    main()
```

Lastly is a bit of python magic that allow the program to either run directly or
to be import by another python script with out running main automatically. The
if statement check if this script is being run directly and if so calls main,
beginning the blink loop.

The script in its entirety can be viewed [here](./blink.py).

### Running the Code
To run the code simply open a terminal prompt and navigate to the directory you
saved your script in. Once in the correct directory, enter the following to run
the program:
```bash
sudo python3 blink.py
```
Where blink.py is the name of your script. Note that sudo is needed because
you need super user privileges to interface with the GPIO.

Also note, the above command runs the code using Python 3. If you want to run
the code in Python 2 enter the following:
```bash
sudo python blink.py
```
Note, for this example the script will run in either 2 or 3, but there is no
guarantee that future lessons will be so nice. To avoid any complications simply
use python3.

## More

[Blink without sleeping](./blink_without_sleep.py) - An alternative program that
blinks a LED without using the time.sleep function.

## Next

[Lesson 02: Buttons](../02-Button/Lesson02.md)

## References

1. Read more [here](http://goo.gl/RpTCBO) for more information about
GPIO.setmode and the different ways to reference GPIO's.
2. Read more [here](http://goo.gl/YZDurf) about why and how to use GPIO.cleanup.
