# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 19:29:32 2018

@author: larsjohan
"""

length_meters=640

length_inch=length_meters/0.0254
length_feet=length_inch/12
length_yards=length_feet/3
length_miles=length_yards/1760

print """
A length of %g meters is equal to

%g inches
%g feet
%g yards
%g miles
""" %(length_meters, length_inch, length_feet, length_yards, length_miles)