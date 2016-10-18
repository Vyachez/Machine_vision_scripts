# Machine_vision_scripts
Scripts using sensors data to command robotics

# Sensor_decision_alg.py

This algorythm depicts the work of decision making mechanism for robot based on
3 ultra-range sensors allocated at diferent angel in front panel of robot to cover obstacles
in front of robot, from left and right.

To test the algorythm just run it in python idle;
enter distance in cm.

Algorythm will request sensors (in test case you should enter data instead of sensor)
to get distance and verify it couple of times
depending on how close obstacle is.

There are 3 checking algorythms - strong, light and medium.

After algorythm "ensures" the distance is correct - it will make decision for robot
to move in right direction, avoiding obstacle.

# Ultra-Sensor_plot.py

Algorythm allows to build the plot of 3 sensor
vision depending on angles of sensors locations
relatively to eahc other:

VAR - means variable to change depending on your conditions

VAR setting quantity of dots for sampling (sensor range in cm)
dot_quant = 150

FIXED distance of side sensors relatively to central
(this figures static due to pecularity of sensor locations for this example)
Cpoint = 0
Rpoint = 7.9
Lpoint = Rpoint * -1
r_side = 11.7
l_side = 10

VAR - TUNABLE distance which side sensors should cross upfront
r_dist = 32
l_dist = 32

VAR robot width/passing corridor
width_corr = 50

VAR setting distance which side sensor should cover from center (wider that sensive corridor)
ss_vis = 70
