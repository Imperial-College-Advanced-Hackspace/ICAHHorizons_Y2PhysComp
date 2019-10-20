# Session 2 Workbook - Physical Computing

<p align="center">
    <img src="images/ICAHLOGO.png" alt="ICAHLOGO" width="300">
</p>

# How to use this workbook & teams formation

Welcome back to the second session of the Physical Computing theme!

This week, the focus moves firmly to working in teams of 3 to 4 and doing exercises in your workbook together. All exercises happen on the actual Raspberry Pis.

Having formed teams, let's jump right in at the deep end!

# Physical Computing and the gpiozero library

Ultimately, we want you to control a physical contraption with your Raspberry Pi. For this, we'll use the General Purpose Input/Output (GPIO) pins on the side of your Pi. Their layout is shown below. Don't worry too much about it all for now, we will show you how to connect things up. Just one thing to remember: **Never connect a 5V pin directly to any other pin of the Raspberry Pi, particularly the Ground pin!**

<p align="center">
    <img src="images/RPi_pin_layout.svg" alt="pin" width="200">
    <figcaption align="center">Raspberry Pi pin layout</figcaption>
</p>

## Using a breadboard

An electronics breadboard are great units for prototyping or making quick temporary circuits and they generally require no soldering. If you are not sure how a certain circuit will react, its best to prototype it out and usually this is done using a breadboard.

Some of you who have previously worked with electronics may have already seen a breadboard. They come in different sizes and configurations but generally are very similar. A breadboard will always have a DIP ravine in the centre of the breadboard. This is so that you can place IC chips in the middle with pins on either side. Also your breadboard may have a set of rails running along the top and bottom. Lets have a look at a small breadboard:

<p align="center">
    <img src="images/medium_breadboard.jpg" alt="Medium Breadboard" width="600">
    <figcaption align="center">Medium sized breadboard with exposed pins</figcaption>
</p>

So on the left is the top side of the board where you would place your components and on the right is the bottom side of the board. Usually a breadboard has some backing on it so you cannot see the exposed metal components but we have peeled it off here so you can see the inner workings of the breadboard. Now the metal lines you can see are actually rows of pins as shown in the image below and each of these metal rows have clips at the top that are just under the plastic surface of the breadboard. When you plug in a wire or a leg of a component it is held in place by these metal clips.

<p align="center">
    <img src="images/breadboard_pins.JPG" alt="Breadboard metal pins" width="300">
    <figcaption align="center">Metal pins inside the breadboard</figcaption>
</p>

As you can see you have vertical rows and horizontal rows of these metal clips. The vertical rows are used for common rails such as 5V and GND. Note that the vertical rows running on both sides are not connected, traditionally on simple circuits you would run a wire from each side bridging these to allow for rails on either side of the breadboard making it easier when building your circuits. The horizontal rows are for placing your components and allowing for multiple connections off one pin. Note the horizontal rows are not connected in the middle. This is so that you can place IC chips in the middle allowing for half the pins to be on either side and not be bridged across.

<p align="center">
    <img src="images/breadboard_bridge.jpg" alt="Bridged rails" width="500">
</p>
<p align="center">
    <img src="images/breadboard_ravine.jpg" alt="Breadboard DIP ravine" width="500"
</p>
<p align="center">
  <figcaption align="center">Top: Bridging rails on either side of breadboard. Bottom: DIP ravine to place IC</figcaption>
</p>

<p align="center">
    <img src="images/verticalpower.png" alt="Vertical power rails" width="500"
</p>
<p align="center">
    <img src="images/horizontalrows.png" alt="Horizontal breadboard connections" width="500"
</p>
<p align="center">
    <img src="images/horizontalwithIC.png" alt="Breadboard with IC DIP ravine" width="500"
</p>

## Working with files on the Pi

As you know we do not have a screen connected to the Raspberry Pi right now, which may confuse some of you for the next bit. Lets say we wanted to write some code and run it on the Pi. How would we do this? There are two ways we can use here, either we write the file on our own laptops in a text editor and copy it over, or we write it directly on the pi in the terminal. 

### Copying a file over to the Raspberry Pi

As some of you may find it is nicer to work within a known code editor that you are comfortable with. Once you have made this file on your laptop you can then copy this over to the Raspberry Pi and run it. So lets try this, create a simple text file called blinky.py on the Desktop on your laptop.

Now lets copy your file over to the Raspberry Pi. We can do this using SCP (Secure File Copy). Don't forget to connet to your RPi network again before trying the next steps.

If you are using Mac/Linux then you do not require any extra software. Simply open a terminal and change directory to the Desktop and type:

```scp blinky.py pi@192.168.4.2:/home/pi/horizons```

If you are using Windows then you will need the program PuTTy which we mentioned in the previous lesson. You can download it [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html). Download the MSI('Windows Installer') and install it.

Once you have installed PuTTy you can open the command prompt in Windows and change directory to the Desktop. Now use the pscp command to transfer the file.

```pscp -scp blinky.py pi@192.168.4.2:/home/pi/horizons```

Now if you ssh into your Raspberry Pi and list the files in the Desktop folder you will see your text file has been copied across!

### Using a file editor on the Raspberry Pi

If you wanted you could also create and edit a file directly on the RPi. Lets try this. First SSH into the RPi:

```ssh pi@192.168.4.2```

Then change directory to the horizons folder. 

```
cd /home/pi/horizons
```

Now we are going to use one of the built in file editors for Linux systems called Nano. It is a very nice and easy terminal text editor. So to run it type:

```nano blinky.py```

This will open a text editor in your terminal as shown below:

<p align="center">
    <img src="images/nano_terminal.PNG" alt="Nano in the terminal" width="800">
    <figcaption align="center">Nano in the terminal</figcaption>
</p>

Note that within this text editor you cannot just click where you want to go but have to move there using the keypad on your keyboard. Then you can type whatever you need so lets try typing ```Hello World!``` at the top of the file and to exit you click <kbd>CTRL</kbd>+<kbd>X</kbd> on your keyboard. Click <kbd>y</kbd> and <kbd>Enter</kbd> to save it under the same file name.

Now we know what a Raspberry Pi is and how to copy files to it.

## Using the gpiozero library

The [gpiozero library](https://gpiozero.readthedocs.io/en/stable/) enables us to control the GPIO pins on our Pi. We start off with `import gpiozero`. The gpiozero library provides us with a lot functionality to interface with the GPIO pins and provides us with ready to use objects for LEDs, sensors and actuators. 

### Switching an LED

Connect an LED via a resistor to the Ground (GND) and GPIO pin 17 (GP17). Note that the shorter wire of the LED needs to connect to ground.

<p align="center">
    <img src="images/gpiozero_led.png" alt="Connecting an LED" width="800">
    <figcaption align="center">Connecting an LED to the Pi</figcaption>
</p>

To keep everything a little organised lets create a directory where we can keep all our code:

```
cd /home/pi/
mkdir Horizons
cd Horizons
```

Run:

```python
import gpiozero
import time

red = gpiozero.LED(17)

while True:
    red.on()
    time.sleep(1)
    red.off()
    time.sleep(1)
```

Note how we also imported the `time` library to allow the program to sleep for one second.

### Dimming an LED

Keep the same connection, and run the below code. Note how we use the PWMLED object to control the LED. PWM stands for [**P**ulse **W**idth **M**odulation](https://www.arduino.cc/en/Tutorial/PWM), which rapidly blinks the LED and controls its brightness by switching it on and off for different amounts of times.

```python
from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0  # off
    sleep(1)
    led.value = 0.5  # half brightness
    sleep(1)
    led.value = 1  # full brightness
    sleep(1)
```

Note how in this case we have used the syntax `from <library> import <thing>` to import the `PWMLED` and `sleep` functions directly. This allowed us to skip repeatedly writing `time.sleep()` etc.

### Using an ultrasonic distance sensor

Here we have the very common HC-SR04 ultrasonic sensor which is great for measuring distances. It has a range of 2cm to 400cm (but works best from around 10cm to 250cm). The sensors have a transmitter, a receiver and a control circuit. From the code you can simply call the ```get_distance()``` function and it will return the distance as a string. To get the distance a timer is started and the transmitter sends out a pulse, which bounces off a surface and then returns to the receiver. The time is taken again and we now know how long the pulse took to go and come back from the surface infront of the sensor. With some quick maths we can then calculate the distance of the object!

To get started wire the sensor as shown below. For this we need a breadboard, because the sensor's "Echo" returns a 5V signal, which is too much for the Pi's GPIO pins. To solve this, we have to build a small [voltage divider](https://en.wikipedia.org/wiki/Voltage_divider) to bring the signal from 5V down to 3.3V.

<p align="center">
    <img src="images/gpiozero_distance_sensor.png" alt="Connecting an ultrasonic distance sensor" width="800">
    <figcaption align="center">Connecting a distance sensor to the Pi</figcaption>
</p>

Then execute the following code.

```python
from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=4, queue_len=10)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(0.5)
```

You can stop the program by pressing <kbd>CTRL</kbd>+<kbd>C</kbd>.

You can find many more ways of using gpiozero [here](http://gpiozero.readthedocs.io/en/stable/recipes.html).

## Exercises

Feel free to team up for these challenges. We only have a limited amount of each sensor.

1. Write a program that flashes an LED at a frequency set by the user.

1. Using gpiozero's [PWMLED object](http://gpiozero.readthedocs.io/en/stable/recipes.html#led-with-variable-brightness), write a program that repeatedly dims the LED from zero to full brightness, abruptly re-sets it to zero brightness and repeats. This is called a sawtooth wave.

    <p align="center">
        <img src="images/Sawtooth.gif" alt="pin" width="300">
        <figcaption align="center">A sawtooth wave</figcaption>
    </p>

1. Write a program that blinks an LED if it detects an object closer than 20cm from the distance sensor.

1. Write a program that accepts user input like "HELLOCANYOUHEARME" (all upper case and no whitespace), and translates this into an LED flashing the corresponding Morse Code.

   You will need to translate letters into dots and dashes according to the Morse alphabet. It is best to use a Python dictionary to translate between letters and Morse symbols. This can be found [here](https://raw.githubusercontent.com/raspberrypilearning/morse-code-virtual-radio/master/code/morse_lookup.py), and the timing rules for International Morse Code [here](https://github.com/raspberrypilearning/morse-code-virtual-radio/blob/master/worksheet.md#decode-the-morse-as-you-go).

1. Write a program that makes use of a line sensor (we have a few here today, so you will need to team up, depending on who is at this stage) and notifies the user whenever a black line is detected. Try to avoid repeatedly printing out whatever the line sensor sees. Instead, only notify the user when there is a change (no line &#8646; line). You will want to [wire it up correctly and familiarise yourself with the LineSensor interface](http://gpiozero.readthedocs.io/en/stable/api_input.html#line-sensor-trct5000) in gpiozero.


# May we introduce...

So we've been busy this last week to assemble you a little vehicle. May we introduce the **ICAH-101 bot**. It is based on Imperial College Robotics Society's [Robotics 101 course](http://101.icrs.io/), which you can read up on here if you want to find out more. Note that for our robot we do not use a bare bones circuit like in that tutorial but instead we are using a motor shield which you will connect soon.

<p align="center">
    <img src="images/bot_motor_hat.jpg" alt="ICAH-101 bot" width="800">
    <figcaption align="center">The ICAH-101 bot</figcaption>
</p>

For the rest of this theme, you will be working with this robot.

It has the following capabilities:

* **Driving around!** The two wheels on either side can be independently controlled, so you can make it go forward, backward and steer left or right, with either just one wheel spinning, or both spinning in opposite direction.

* **Blinking an LED!** (Yay...) This is a good way to check the functioning of the GPIO pins in general. We'll get to that in the first exercise.

* **Detecting a forward-facing distance.** This uses the HC-SR04 ultrasound sensor we met in the last session. Note that it detects a distance straight ahead of the robot.

* **Detecting brightness changes in the floor surface**, using 2 TCRT5000 **line sensors**. Why are they called line sensors? Because a natural application for reading brightness changes is to follow a black line on bright ground.

We won't be focussed on the electronic setup of the robot in this session, but if you want to find out more about how we actually control the motors, do have a look at the [explanation in the 101 course](http://101.icrs.io/lesson-2) ("Motor Driver"). Note that we are using a different circuit here using a RPi Motor HAT but essentially the premise is the same. There is a H-Bridge on the HAT that is used to control the motors turning them clockwise or counterclockwise. However in our Motor HAT we also have a controller IC that we interface with it using I2C. I2C (Inter-integrated Circuit) protocol is a method of communication that allows for multiple slave devices (e.g. sensors) that all communicate to one master. It is only intended for short lengths and requires only 2 lines, the data signal and the clock signal. Unfortunately I2C is outside the scope of this lesson but you can find out more about it [here](https://learn.sparkfun.com/tutorials/i2c).

# Connecting and setting up the Motor HAT

First of all shutdown the Raspberry Pi safely. To do this SSH into the raspberry pi and in the terminal type:

```
sudo shutdown now
```

Eventually the RPi will shutdown and then you can add the motor hat to the RPi. As you may have noticed the hat has connectors soldered on to it that have very long pins. This is so you can use jumper wires with the hat still connected. In fact if you wanted you could put multiple motor hats on top of each other. Now plug in the RPi and motor hat into the connector on the breadboard.

Now connect the motor wires, one motor to the M1 terminals and one motor to the M2 temrinals. Finally we need to connect the power for the motors. This is on the top left corner of the shield. Connect one black wire from the negative terminal to the GND rail on the breadboard and one red wire from the positive terminal on the shield to the 5V rail on the breadboard. This can all be seen in the image below. Now turn your pi on.

<p align="center"><img src="images/pi_motorshield_wiring.jpg" alt="Motor Shield Wiring" width="800"><figcaption align="center">how to wire up the motor shield</figcaption></p>

To use this HAT you will need to [install the software](https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git) with it. To do this you will need to download the library on your laptop and then copy the folder over. To do this go to the below link and click on clone or download -> download ZIP.

**[ADAFRUIT LIBRARY](https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git)**

Now we have downloaded the files we can copy them over to the Raspberry Pi:

1. Open a command prompt window (Windows) or Terminal (Linux/MAC OS).
2. Change to the directory where you downloaded the library zip file.
3. Copy the file accross using the following command:
```
pscp -scp -r <name_of_zip_file> pi@192.168.4.2:/home/pi/horizons
```
4. Open PuTTy and SSH into the Raspberry Pi.
5. Go to the horizons directory:
```
cd /home/pi/horizons/
```
6. Install the library usingthe setup command:
```
sudo python setup.py install
```

And thats it! Its installed now and we can start using the library. Try going to the examples folder and running the RobotTest.py example. **NOTE: This will move the robot so make sure you hold it up or ensure the robot does not run away from you!**

```
cd examples
python RobotTest.py
```

To close the program type <kbd>CTRL</kbd>+<kbd>C</kbd>.

# Exercises

1. Have a look at your robot and [the Raspberry Pi pin layout](http://gpiozero.readthedocs.io/en/stable/_images/pin_layout.svg) (the bottom is where the USB ports are, and it is also on your desktop background). Connect an LED into the breadboard and to one of the pins on the pi and get it to blink.

2. Driving the robot around.
 Now to drive the robot around we will use one of the example classes created by Adafruit for the motor HAT. To do this copy the file Robot.py into our Horizons folder. (Try pressing tab to auto-complete the names).

 ```
 cd /home/pi/Horizons/
 cp Adafruit-Motor-HAT-Python-Library/examples/Robot.py .
 ```

 Now lets create a file that lets us import this Robot class and drive the robot around:

 ```python
 import time
 import Robot

 LEFT_TRIM = 0
 RIGHT_TRIM = 0

 my_robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

 my_robot.forward(150, 1.0)   # Move forward at speed 150 for 1 second. Speed is a value between 0 and 255
 my_robot.left(200, 0.5) # Spin left at speed 200 for 0.5 seconds.

 # Spin in place slowly for a few seconds.
 my_robot.right(100)  # No time is specified so the robot will start spinning forever.
 time.sleep(2.0)   # Pause for a few seconds while the robot spins (you could do other processing here though!).

 my_robot.backward(100,2)

 my_robot.stop()      # Stop the robot from moving.
 ```

   The above creates an instance of adafruit's `Robot` object, called `my_robot`. As we create it, we tell it the correct GPIO pins for controlling the left and the right motor.

   Armed with this knowledge, `my_robot` knows exactly what signals to put out onto the pins if it is asked to move the robot forward, backward, left or right. The great thing is that we can leave the nitty-gritty of _how_ to move in either direction to the internal workings of the adafruit library. It just presents us with handy shortcut commands called left(), right(), forward() and backward().

   To do a motion at less than full speed, you can give it a speed parameter. For example `my_robot.forward(122)` moves the robot forward at half of the full speed.

   You can find all the commands that you can send to the Robot object in the Robot.py file we copied earlier. Note that there is a handy `stop()` function that saves you from writing things like `my_robot.forward(0)`.

3. Moving out of the way when there is an obstacle in front of the robot.
 In this exercise, we stop the robot when there is an obstacle in front of it, using the ultrasonic distance sensor. Optionally, you can set it on a new course until it detects another obstacle, thus going on until its battery is depleted.

   Remember [the distance sensing code from last time](https://github.com/till-h/ICAHHorizons_Y2PhysComp/blob/master/session%201/Session%201%20Workbook%20-%20Physical%20Computing.md#using-an-ultrasonic-distance-sensor)? You will first need to wire up the sensor, including the voltage divider, as per the last session's instructions. We will once more give you a "large" and a "small" resistor to build the voltage divider.  

   A sample flowchart for the robot control is shown below - but do try out your own ideas!

   <p align="center">
      <img src="images/obstacle_flowchart.png" alt="Obstacle avoidance" width="600">
      <figcaption align="center">A possible way to deal with obstacles.</figcaption>
   </p>

4. Stopping the robot when it crosses a black line.
 <p align="center"><img src="images/TCRT5000.jpg" alt="The TCRT5000 line sensor module" width="300"><figcaption align="center">The TCRT5000 line sensor module</figcaption></p>
 Instead of the ultrasonic sensor, you can use what's called a line sensor to detect an abrupt change in brightness of the ground. If we use this together with a black marker tape stuck onto a white paper, or similar, it is the perfect way to detect markings on the ground. Let's use it to stop if our robot crosses a black line! 
 In order to use the line sensor, you need to import the `LineSensor` object from gpiozero.

   ```python
   from gpiozero import LineSensor
   
   sensor = LineSensor(21) # if we connect the sensor's data pin to GPIO pin 21
   
   while True:
   	 if sensor.pin.state:
   	 	 print("No line detected.")
   	 else:
   	     print("Line detected.")
   ```

   Physically, you connect it up as follows:

   * Connect the sensor's VCC to a 3V3 pin on the Pi.
   * Connect the sensor's GND to a Ground pin on the Pi.
   * Connect the sensor's OUT to a free GPIO pin on the Pi.

   Again, feel free to change the code to a more interesting behaviour, if you have time.

5. Driving the robot around in a black square.
Finally, you can use the previous exercise to drive the robot around within a box. Can you make it go as closely as possible around the inside of the perimeter? I.e., constantly keep probing to one side?
