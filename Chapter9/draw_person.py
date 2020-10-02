# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:39:28 2020

@author: lars-johan.brannmark
"""

from pysketcher import *

w = 2.0           #Width of coordinate system
h = 2.5           #Height of coordinate system
R = 0.12          #Radius of head
hc = (1.0, 1.82)  #Center of head
alpha = 30.0/180*pi

drawing_tool.set_coordinate_system(xmin=0, xmax=w, ymin=-0.1, ymax=h)

head = Circle(center=hc, radius=R)
head.draw()

body = Triangle((hc[0],hc[1]-R),(hc[0]-R,hc[1]-R-4*R),(hc[0]+R,hc[1]-R-4*R))
body.draw()

leg = Line((hc[0],hc[1]-R-4*R), (hc[0],hc[1]-R-4*R-6*R))

leg_1 = leg.copy()
leg_1.rotate(-15,(hc[0],hc[1]-R-4*R))
leg_1.draw()

leg_2 = leg.copy()
leg_2.rotate(15, (hc[0],hc[1]-R-4*R))
leg_2.draw()

arm_1 = Line((hc[0]+R/4.0,hc[1]-R-R),(hc[0]+R/4.0+4*R*cos(alpha),hc[1]-R-R+4*R*sin(alpha)))
arm_1.draw()

arm_2 = Line((hc[0]-R/4.0,hc[1]-R-R),(hc[0]-R/4.0-4*R*cos(alpha),hc[1]-R-R+4*R*sin(alpha)))
arm_2.draw()

drawing_tool.display()
s = raw_input('Press enter:')