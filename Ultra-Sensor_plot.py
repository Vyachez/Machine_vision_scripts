# please see readme for instructions
import time
import math
import matplotlib
import matplotlib.pyplot as plt
import sys
# all distance dimensions measured in "cm"

# dot vectors arrays
test_c = []
test_r = test_c
test_l = test_c

# VAR setting quantity of dots for sampling (central sensor range in cm)
dot_quant = 150

# FIXED distance of side sensors relatively to central
Cpoint = 0
Rpoint = 7.9
Lpoint = Rpoint * -1

# FIXED dimensions from central sensors to boards of frame
r_side = 11.7
l_side = 10

# VAR - TUNABLE distance which side sensors should cross upfront
r_dist = 32
l_dist = 32

# VAR robot width/passing corridor
width_corr = 50

# VAR setting distance which side sensor should cover from center (wider that sensive corridor)
ss_vis = 70

# FIXED sensor operation angle
range_ang = 15

# calc distance from central sensor to sides of corridor
r_board = l_side + ((width_corr - (r_side + l_side))/2)
l_board = r_side + ((width_corr - (r_side + l_side))/2)

# calculations of sensor "triangle" sides for side sensor angles finding
r_leg = width_corr - ((l_side - Rpoint) + ((width_corr - (r_side + l_side))/2))
l_leg = width_corr - ((r_side - Rpoint) + ((width_corr - (r_side + l_side))/2))

# angle calculations depending on requirements of distance
r_ang = math.degrees(float(math.atan(float(r_dist/r_leg))))
l_ang = math.degrees(float(math.atan(float(l_dist/l_leg))))

# creating array of test vectors depending on desired length
def test_len(q):
    k = 0
    for i in range(q):
        k = k + 1
        test_c.append(k)
    return test_c

# creating right sensor vector dots on y axis
def gettin_yr(dist, ang):
    yr_list = []
    for i in range(len(dist)):
        a = float(dist[i]) * math.sin(math.radians(float(ang)))
        yr_list.append(float("{0:.2f}".format(a)))
    return yr_list

# creating left sensor vector dots on y axis
def gettin_yl(dist, ang):
    yl_list = []
    for i in range(len(dist)):
        a = float(dist[i]) * math.sin(math.radians(float(ang)))
        yl_list.append(float("{0:.2f}".format(a)))
    return yl_list

# creating central sensor vector dots on y axis
def gettin_yc(dist):
    yc_list = []
    for i in range(len(dist)):
        a = float(dist[i])
        yc_list.append(float("{0:.2f}".format(a)))
    return yc_list

# creating right sensor vector dots on x axis   
def gettin_xr(dist, ang):
    xr_list = []
    for i in range(len(dist)):
        b1 = Rpoint - abs(float(dist[i]) * math.cos(math.radians(float(ang))))
        xr_list.append(float("{0:.2f}".format(b1)))
    return xr_list

# creating left sensor vector dots on x axis
def gettin_xl(dist, ang):
    xl_list = []
    for i in range(len(dist)):
        b2 = Lpoint + abs(float(dist[i]) * math.cos(math.radians(float(ang))))
        xl_list.append(float("{0:.2f}".format(b2)))
    return xl_list

# creating central sensor vector dots on x axis
def gettin_xc(dist):
    xc_list = []
    for i in range(len(dist)):
        a = 0
        xc_list.append(float("{0:.2f}".format(a)))
    return xc_list

# red borders of corridor on plot
def borders(length, side):
    lst = []
    for i in range(length):
        lst.append(side)
    return lst

# central sensor range markup
def ranges(length, ang):
    ang = ang/2
    a = length * math.tan(math.radians(float(ang)))
    x1 = 0
    y1 = 0
    x2 = -1 * a
    y2 = length
    x3 = a
    y3 = length
    points = [[x1, y1], [x2, y2], [x3, y3]]
    return points

# side sensors range markup
def ranges_sl(ang, range_ang, s_vis, corr_point):
    half_ang = range_ang/2
    aux_ang2 = ang - half_ang
    aux_ang1 = ang + half_ang
    x_vis = s_vis + corr_point
    m_cath = x_vis/math.cos(math.radians(float(ang)))
    h_aux = m_cath/math.cos(math.radians(float(half_ang)))
    x_sens1 = h_aux*math.cos(math.radians(float(aux_ang1)))
    y_sens1 = h_aux*math.sin(math.radians(float(aux_ang1)))
    x_sens2 = h_aux*math.cos(math.radians(float(aux_ang2)))
    y_sens2 = h_aux*math.sin(math.radians(float(aux_ang2)))
    x1 = corr_point*-1
    y1 = 0
    x2 = x_sens1 - corr_point
    y2 = y_sens1
    x3 = x_sens2 - corr_point
    y3 = y_sens2
    points = [[x1, y1], [x2, y2], [x3, y3]]
    return points

def ranges_sr(ang, range_ang, s_vis, corr_point):
    half_ang = range_ang/2
    aux_ang2 = ang - half_ang
    aux_ang1 = ang + half_ang
    x_vis = s_vis + corr_point
    m_cath = x_vis/math.cos(math.radians(float(ang)))
    h_aux = m_cath/math.cos(math.radians(float(half_ang)))
    x_sens1 = h_aux*math.cos(math.radians(float(aux_ang1)))
    y_sens1 = h_aux*math.sin(math.radians(float(aux_ang1)))
    x_sens2 = h_aux*math.cos(math.radians(float(aux_ang2)))
    y_sens2 = h_aux*math.sin(math.radians(float(aux_ang2)))
    x1 = corr_point
    y1 = 0
    x2 = x_sens1*-1 + corr_point
    y2 = y_sens1
    x3 = x_sens2*-1 + corr_point
    y3 = y_sens2
    points = [[x1, y1], [x2, y2], [x3, y3]]
    return points

# func for printing central triangle parameters in console
def ranges_p(length, ang):
    ang = ang/2
    a = length * math.tan(math.radians(float(ang)))
    x3 = a
    y3 = length
    print "Cathet b: ", y3
    print "Cathet a: ", x3
    print "Angle: ", ang
    
# generating test array of dots 
test_len(dot_quant)

# generating triangles of sensor ranges
triangle_c = ranges(dot_quant, range_ang)
triangle_r = ranges_sr(r_ang, range_ang, ss_vis, Rpoint)
triangle_l = ranges_sl(l_ang, range_ang, ss_vis, Rpoint)

# generating pieces of x dots
xr = gettin_xr(test_r, r_ang)
xl = gettin_xl(test_l, l_ang)
xc = gettin_xc(test_c)

x = xl + xc + xr 

# generating pieces of y dots
yr = gettin_yr(test_r, r_ang)
yl = gettin_yl(test_l, l_ang)
yc = gettin_yc(test_c)

y = yl + yc + yr

# creating borders on plot
xr_line = borders(dot_quant, r_board)
xl_line = borders(dot_quant, l_board*-1)
yr_line = test_c
yl_line = test_c

# setting axis
minx = min(x)
maxx = max(x)+100
maxy = max(y)+100

#printing block
print "Angle right: ", r_ang
print "Angle left: ", l_ang
print "Right cathetus: ", r_leg
print "Left cathetus: ", l_leg
print "Right board", r_board
print "Left board", l_board
ranges_p(dot_quant, range_ang)

# building plot
fig = plt.figure()
ax = fig.add_subplot(111)

tri_c = matplotlib.patches.Polygon(triangle_c, closed=True, fill=False, hatch='/', edgecolor="g")
ax.add_patch(tri_c)

tri_r = matplotlib.patches.Polygon(triangle_r, closed=True, fill=False, hatch='/', edgecolor="m")
ax.add_patch(tri_r)

tri_l = matplotlib.patches.Polygon(triangle_l, closed=True, fill=False, hatch='/', edgecolor="m")
ax.add_patch(tri_l)

ax.plot(x, y, 'bo', xr_line, yr_line, 'r--', xl_line, yl_line, 'r--')
ax.axis([0, int(maxx), 0, int(maxy)])
ax.grid(True)


plt.show()
