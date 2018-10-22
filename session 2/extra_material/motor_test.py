import time
import Robot

LEFT_TRIM = 0
RIGHT_TRIM = 0

my_robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

my_robot.forward(150, 1.0)   # Move forward at speed 150 for 1 second. 
Speed is a value between 0 and 255
my_robot.left(200, 0.5) # Spin left at speed 200 for 0.5 seconds.

# Spin in place slowly for a few seconds.
my_robot.right(100)  # No time is specified so the robot will start 
spinning forever.
time.sleep(2.0)   # Pause for a few seconds while the robot spins (you could do other processing here though!).

my_robot.backward(100,2)

my_robot.stop()      # Stop the robot from moving.
