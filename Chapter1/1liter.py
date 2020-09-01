# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 23:49:34 2018

@author: larsjohan
"""

rho_iron = 7.8
rho_air =  0.0012
rho_gasoline = 0.67
rho_ice = 0.9
rho_humanbody = 1.03
rho_silver = 10.5
rho_platinum = 21.4

print """
Mass of 1 liter iron: %g g
Mass of 1 liter air: %g g
Mass of 1 liter gasoline: %g g
Mass of 1 liter ice: %g g
Mass of 1 liter humanbody: %g kg
Mass of 1 liter silver: %g kg
Mass of 1 liter platinum: %g kg
""" % (1e3*rho_iron, 1e3*rho_air, 1e3*rho_gasoline, 1e3*rho_ice, rho_humanbody, rho_silver, rho_platinum)