# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:44:58 2019

@author: larsjohan
"""

#Name,  distance in light years, apparent brightness, luminosity
data = [
('Alpha Centauri A',    4.3,  0.26,      1.56),
('Alpha Centauri B',    4.3,  0.077,     0.45),
('Alpha Centauri C',    4.2,  0.00001,   0.00006),
("Barnard's Star",      6.0,  0.00004,   0.0005),
('Wolf 359',            7.7,  0.000001,  0.00002),
('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
('Sirius A',            8.6,  1.00,      23.6),
('Sirius B',            8.6,  0.001,     0.003),
('Ross 154',            9.4,  0.00002,   0.0005),
]

data_dist = sorted(data,key=lambda obj: obj[1])
data_bright = sorted(data,key=lambda obj: obj[2])
data_lum = sorted(data,key=lambda obj: obj[3])

print '%-20s' % ('Name'),
print '%-12s' % ('Distance')
for item in data_dist:
    print '%-20s' % item[0],
    print '%-12.1f'   % item[1]

print '--------------------------------'

print '%-20s' % ('Name'),
print '%-12s' % ('Brightness')
for item in data_bright:
    print '%-20s' % item[0],
    print '%-12.6f'   % item[2]
    
print '--------------------------------'

print '%-20s' % ('Name'),
print '%-12s' % ('Luminosity')
for item in data_lum:
    print '%-20s' % item[0],
    print '%-12.6f'   % item[3]