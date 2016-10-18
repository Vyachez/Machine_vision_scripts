import numpy
import random
import sys

# vars
x = 0
y = 0
z = 0

# coordinates
x1 = 150
x2 = 100
x3 = 70
x4 = 32
x5 = 15
x6 = 10

y3 = 35 ## ATTENTION - the value from sensor shall be calculated into cathet of triangle
y4 = 32
y5 = 15
y6 = 10

z3 = 35 ## ATTENTION - the value from sensor shall be calculated into cathet of triangle
z4 = 32
z5 = 15
z6 = 10

# robot speeds
speed1 = 200
speed2 = 150
speed3 = 100
speed4 = 50

# turn angles
ang6 = 60
ang9 = 90

# lists to compare
x_vals = []
y_vals = []
z_vals = []

# error admissible for sensor to avoid check
delta_sens = 5

times = 0
check_state = 0

count = []

switch = "on"

def go():
    global x
    global y
    global z
    global switch
    if switch == "on":
        x = int(raw_input("Enter center sensor: "))
        y = int(raw_input("Enter left sensor: "))
        z = int(raw_input("Enter right sensor: "))
        switch = raw_input("on/off? ")
    elif switch == "off":
        print "Turned sensors off..."
        sys.exit()
    else:
        return "Motors will be cutted due to wrong command"
        sys.exit()

go()

while switch == "on":

    # states of coordinates to evaluate
    stx1 = int(x > x1)
    stx2 = int(x <= x1 and x > x2)
    stx3 = int(x <= x2 and x > x3)
    stx4 = int(x <= x3 and x > x4)
    stx5 = int(x <= x4 and x > x5)
    stx6 = int(x <= x5 and x > x6)
    stx7 = int(x <= x6)

    sty1 = 0
    sty2 = 0
    sty3 = 0
    sty4 = int(y <= y3 and y > y4)
    sty5 = int(y <= y4 and y > y5)
    sty6 = int(y <= y5 and y > y6)
    sty7 = int(y <= y6)

    stz1 = 0
    stz2 = 0
    stz3 = 0
    stz4 = int(z <= z3 and z > z4)
    stz5 = int(z <= z4 and z > z5)
    stz6 = int(z <= z5 and z > z6)
    stz7 = int(z <= z6)

    finish = 0

    # robot actions
    def forward(fwd_sp_l, fwd_sp_c, fwd_sp_r, state):
        if state > 0 and (fwd_sp_l > 0 or fwd_sp_c > 0 or fwd_sp_r > 0):
            speed = (min(fwd_sp_l, fwd_sp_c, fwd_sp_r))    
            print "Moving forward with", speed, "speed"
            count.append(1)
        else:
            pass

    def backward(bcw_sp_l, bcw_sp_c, bcw_sp_r, state):
        if state > 0 and (bcw_sp_l > 0 or bcw_sp_c > 0 or bcw_sp_r > 0):
            print "Stopped"
            speed = (min(bcw_sp_l, bcw_sp_c, bcw_sp_r))    
            print "Moving backward with", speed, "speed for 4 seconds"
        else:
            pass

    def turn(ang_l, ang_c, ang_r, state):
        if state > 0 and (ang_l > 0 or ang_c > 0 or ang_r > 0):
            print "Stopped"
            t_ran = 0
            if (left[i] == 1 and centr[i] == 0 and right[i] == 0) or (left[i] == 1 and centr[i] == 1 and right[i] == 0):
                print "Turn Right at", ang_l, "degree"
            elif (left[i] == 0 and centr[i] == 0 and right[i] == 1) or (left[i] == 0 and centr[i] == 1 and right[i] == 1):
                print "Turn Left at", ang_r, "degree"
            else:
                t_ran = random.randint(0, 1)
                turn_n = ""
                if t_ran == 1:
                    turn_n = "Right"
                else:
                    turn_n = "Left"
                print "Turn", turn_n, "at", ang_c, "degree"
        else:
            pass

    command = [forward, backward, turn]

    # sensor check functions
    def addlist(times):
        global x
        global y
        global z
        for i in range(1, times+1):
            print "Forming list of data"
            print "Center sensor repeated", i,"/",times
            x = int(raw_input(": "))
            print "Left sensor repeated", i,"/",times
            y = int(raw_input(": "))
            print "Right sensor repeated", i,"/",times
            z = int(raw_input(": "))
            x_vals.append(x)
            y_vals.append(y)
            z_vals.append(z)

    def check(x_vals, y_vals, z_vals):
        global x
        global y
        global z
        print "Checking......"
        if max(x_vals) - min(x_vals) >= delta_sens\
            or max(y_vals) - min(y_vals) >= delta_sens\
            or max(z_vals) - min(z_vals) >= delta_sens:
            print "There is difference of one of sensors is more than 4"
            x = min(x_vals)
            y = min(y_vals)
            z = min(z_vals)
            return False
        else:
            print "Check passed - OK"
            x = min(x_vals)
            y = min(y_vals)
            z = min(z_vals)
            return True

    if (stx3 or stx4 or sty4 or stz4)\
       and not (sty5 or stz5 or sty6 or stz6 or sty7 or stz7):
        print "Light check"
        iter_times = 3
        check_times = 3
        for f in range(1, check_times+1):
            print "Check No ", f
            addlist(iter_times)
            fx = check(x_vals, y_vals, z_vals)
            x_vals = []
            y_vals = []
            z_vals = []
            if fx == True:
                print f, "check passed may proceed with algorithm"
                break
            else:
                check_state += 1
                print check_state
                print f
                print "Finding solution..."   
        if check_state >= check_times:
            print "Check failed", check_times, "times, but robot tries to avoid potential obstacle:"
            command[1](speed4, speed4, speed4, 1)
            command[0](speed4, speed4, speed4, 1)
            count = []
            finish = 1
            
    if stx5 or sty5 or stz5\
       and not (sty6 or stz6 or sty7 or stz7):
        print "Strong check"
        iter_times = 3
        check_times = 4
        for f in range(1, check_times+1):
            print "Check No ", f
            addlist(iter_times)
            fx = check(x_vals, y_vals, z_vals)
            x_vals = []
            y_vals = []
            z_vals = []
            if fx == True:
                print f, "check passed may proceed with algorithm"
                break
            else:
                check_state += 1
                print check_state
                print f
                print "Finding solution..."
        if check_state >= check_times:
            print "Check failed", check_times, "times, but robot tries to avoid potential obstacle:"
            command[1](speed4, speed4, speed4, 1)
            count = []
            finish = 1

    if stx6 or sty6 or stz6 or stx7 or sty7 or stz7:
        print "SUPER strong check"
        iter_times = 2
        check_times = 5
        for f in range(1, check_times+1):
            print "Check No ", f
            addlist(iter_times)
            fx = check(x_vals, y_vals, z_vals)
            x_vals = []
            y_vals = []
            z_vals = []
            if fx == True:
                print f, "check passed may proceed with algorithm"
                break
            else:
                check_state += 1
                print check_state
                print f
                print "Finding solution..."
        if check_state >= check_times:
            print "Check failed", check_times, "times ..."
            print "STOP BOT. Message - reboot sensor interface or place robot in more static environment"
            sys.exit()

    check_state = 0

    print x
    print y
    print z

    # states of coordinates to build
    stx1 = int(x > x1)
    stx2 = int(x <= x1 and x > x2)
    stx3 = int(x <= x2 and x > x3)
    stx4 = int(x <= x3 and x > x4)
    stx5 = int(x <= x4 and x > x5)
    stx6 = int(x <= x5 and x > x6)
    stx7 = int(x <= x6)

    sty1 = 0
    sty2 = 0
    sty3 = 0
    sty4 = int(y <= y3 and y > y4)
    sty5 = int(y <= y4 and y > y5)
    sty6 = int(y <= y5 and y > y6)
    sty7 = int(y <= y6)

    stz1 = 0
    stz2 = 0
    stz3 = 0
    stz4 = int(z <= z3 and z > z4)
    stz5 = int(z <= z4 and z > z5)
    stz6 = int(z <= z5 and z > z6)
    stz7 = int(z <= z6)
    
    left =  numpy.array([sty7, sty6, sty5, sty4, sty3, sty2, sty1])
    centr = numpy.array([stx7, stx6, stx5, stx4, stx3, stx2, stx1])
    right = numpy.array([stz7, stz6, stz5, stz4, stz3, stz2, stz1])

    fwd_sp_l = numpy.array([0,0,0,speed4,speed1,speed1,speed1])
    fwd_sp_c = numpy.array([0,0,0,speed4,speed3,speed2,speed1])
    fwd_sp_r = numpy.array([0,0,0,speed4,speed1,speed1,speed1])

    bcw_sp_l = numpy.array([speed4,0,0,0,0,0,0])
    bcw_sp_c = numpy.array([speed4,0,0,0,0,0,0])
    bcw_sp_r = numpy.array([speed4,0,0,0,0,0,0])

    ang_l = numpy.array([0,ang9,ang6,0,0,0,0])
    ang_c = numpy.array([0,ang9,ang6,0,0,0,0])
    ang_r = numpy.array([0,ang9,ang6,0,0,0,0])

    all_dir = left + centr + right

    print left
    print all_dir
    print right
    
    print finish

    for i in range(len(all_dir)):
        if (left[i] == 1 and left[1] == 1) or (right[i] == 1 and right[1] == 1)\
            or (left[i] == 1 and left[2] == 1) or (right[i] == 1 and right[2] == 1)\
            or (centr[i] == 1 and centr[1] == 1) or (centr[i] == 1 and centr[2] == 1)\
            and finish == 0:
            #print "cond1"
            command[2](ang_l[i], ang_c[i], ang_r[i], all_dir[i])
            break
        elif (left[0] == 1 or right[0] == 1 or centr[0] == 1) and finish == 0:
            #print "cond2"
            command[1](bcw_sp_l[i], bcw_sp_c[i], bcw_sp_r[i], all_dir[i])
            break
        else:
            #print "cond 3"
            if len(count) > 0:
                break
            elif len(count) == 0 and finish == 0:
                command[0](fwd_sp_l[i], fwd_sp_c[i], fwd_sp_r[i], all_dir[i])
            else:
                break

    count = []

    finish = 0
    
    go()

go()

#tested 07 Sept 2016 23.24 - WORKS
