# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:47:26 2020

@author: lars-johan.brannmark
"""

from pysketcher import *

class Person(Shape):
    def __init__(self, head_center, head_radius, arms_angle=20):
        R = head_radius   #Radius of head
        hc = head_center  #Center of head
        alpha = arms_angle*pi/180
        
        head = Circle(center=hc, radius=R)       
        torso = Triangle((hc[0],hc[1]-R),(hc[0]-R,hc[1]-R-4*R),(hc[0]+R,hc[1]-R-4*R))

        arm_1 = Line((hc[0]+R/4.0,hc[1]-R-R),(hc[0]+R/4.0+4*R*cos(alpha),hc[1]-R-R+4*R*sin(alpha)))
        arm_2 = Line((hc[0]-R/4.0,hc[1]-R-R),(hc[0]-R/4.0-4*R*cos(alpha),hc[1]-R-R+4*R*sin(alpha)))
        
        arms = Composition({'arm_1': arm_1, 'arm_2': arm_2})
        
        leg = Line((hc[0],hc[1]-R-4*R), (hc[0],hc[1]-R-4*R-6*R))
        
        leg_1 = leg.copy()
        leg_1.rotate(-15,(hc[0],hc[1]-R-4*R))
        leg_2 = leg.copy()
        leg_2.rotate(15, (hc[0],hc[1]-R-4*R))
        
        legs = Composition({'leg_1': leg_1, 'leg_2': leg_2})
        
        person = Composition({'head': head, 'torso': torso, 'arms': arms, 'legs':legs})
        
        self.shapes = {'person': person}

if __name__ == '__main__':  
    R = 0.12
    hc = (1.0, 2.0)
    p = Person(hc, R)
    drawing_tool.set_coordinate_system(xmin=hc[0]-1.0, xmax=hc[0]+1.0, ymin=hc[1]-2.5, ymax=hc[1]+0.5)
    p.draw()
    drawing_tool.display()
    s = raw_input('Press enter:')
