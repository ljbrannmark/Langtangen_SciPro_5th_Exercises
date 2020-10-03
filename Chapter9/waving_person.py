# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 00:33:45 2020

@author: lars-johan.brannmark
"""
import numpy as np
from pysketcher import *

from DrawPerson import Person

def rotate_arms(fig, deg_step):
    arm_1_c = (fig['arms']['arm_1']['line'].x[0], fig['arms']['arm_1']['line'].y[0])
    arm_2_c = (fig['arms']['arm_2']['line'].x[0], fig['arms']['arm_2']['line'].y[0])
    fig['arms']['arm_1'].rotate(deg_step, arm_1_c)
    fig['arms']['arm_2'].rotate(-deg_step, arm_2_c)
    
def wave_arms(t, fig):
    angle_step = 1.0*(2.0*(round(t)%2)-1.0)
    rotate_arms(fig, angle_step)

R = 0.12
hc = (1.0, 2.0)
drawing_tool.set_coordinate_system(xmin=hc[0]-1.0, xmax=hc[0]+1.0, ymin=hc[1]-2.5, ymax=hc[1]+0.5)

fig = Person(hc, R, arms_angle=0)

tp = np.linspace(0, 2, 50, endpoint=False)
time_step = tp[1]-tp[0]
files = animate(fig, tp, wave_arms, moviefiles=True,
                pause_per_frame=time_step)

files_wildcard = files.split('%')[0] + '*.png'
from scitools.std import movie
movie(files_wildcard, encoder='html', output_file='vehicle1')
