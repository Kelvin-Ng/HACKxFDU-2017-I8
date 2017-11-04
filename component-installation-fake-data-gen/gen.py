#!/usr/bin/env python3

import sys
import math
import random

def cap_value(val, l, r):
    #return min(r, max(l, val))
    #return val
    if val < l:
        return l
    elif val > r:
        return r
    else:
        return val

width = 2
height = 1

# angle (in rad) of workers from +x axis
theta_l = -0.927295218
theta_r =  0.927295218

# distance of workers from center
#r_l = 1.229837388
r_l = 1.285739087
r_r = 1.341640786

# pos of rect
x_l = -0.2
x_r =  0.2
y_l = -0.2
y_r =  0.2

# rot of rect
phi_l = -0.231823804
phi_r =  0.231823804

# variances

r_sigma = 0.1
theta_sigma = 0.1
x_sigma = 0.1
y_sigma = 0.1
phi_sigma = 0.1

num_frames = 200

rect_cur_x = random.uniform(x_l, x_r)
rect_cur_y = random.uniform(y_l, y_r)
rect_cur_phi = random.uniform(phi_l, phi_r)

l_cur_r = random.uniform(r_l, r_r)
l_cur_theta = math.pi - random.uniform(theta_l, theta_r)
r_cur_r = random.uniform(r_l, r_r)
r_cur_theta = random.uniform(theta_l, theta_r)

with open(sys.argv[1], 'w') as f:
    for i in range(num_frames):
        l_cur_x = l_cur_r * math.cos(l_cur_theta)
        l_cur_y = l_cur_r * math.sin(l_cur_theta)
        r_cur_x = r_cur_r * math.cos(r_cur_theta)
        r_cur_y = r_cur_r * math.sin(r_cur_theta)

        f.write('{},{},{},{},{},{},{}\n'.format(rect_cur_x, rect_cur_y, rect_cur_phi, l_cur_x, l_cur_y, r_cur_x, r_cur_y))

        rect_cur_x = cap_value(random.gauss(rect_cur_x, x_sigma), x_l, x_r)
        rect_cur_y = cap_value(random.gauss(rect_cur_y, y_sigma), y_l, y_r)
        rect_cur_phi = cap_value(random.gauss(rect_cur_phi, phi_sigma), phi_l, phi_r)

        l_cur_r = cap_value(random.gauss(l_cur_r, r_sigma), r_l, r_r)
        l_cur_theta = cap_value(random.gauss(l_cur_theta, theta_sigma), math.pi - theta_r, math.pi - theta_l)
        r_cur_r = cap_value(random.gauss(r_cur_r, r_sigma), r_l, r_r)
        r_cur_theta = cap_value(random.gauss(r_cur_theta, theta_sigma), theta_l, theta_r)


