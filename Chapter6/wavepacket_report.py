# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:29:25 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

#Wavepacket function from Exercise 5.33
def f(x, t):
    return np.exp(-(x - 3*t)**2)*np.sin(3*np.pi * (x - t))

###############################################################################
# Generate three figures of the wavepacket at three different times
x = np.linspace(-6, 6, 1000)
t_values = np.array([-1, 0, 1])

plt.close('all')

plt.figure(1)
plt.plot(x,f(x,t_values[0]))
plt.axis([x[0], x[-1], -1, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('t=%d'%t_values[0])
plt.savefig('./wavepacket_fig1.png')
plt.show()

plt.figure(2)
plt.plot(x,f(x,t_values[1]))
plt.axis([x[0], x[-1], -1, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('t=%d'%t_values[1])
plt.savefig('./wavepacket_fig2')
plt.show()

plt.figure(3)
plt.plot(x,f(x,t_values[2]))
plt.axis([x[0], x[-1], -1, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('t=%d'%t_values[2])
plt.savefig('./wavepacket_fig3')
plt.show()

plt.close('all')
###############################################################################
# Generate html page containing the code for Exercise 5.33, along with the
# three plots generated above, and the animation produced in Exercise 5.33.
with open('Exercise_6_15.html','w') as outfile:
    outfile.write('<html>\n<body>\n')
    outfile.write('<h1>Python code for the solution of Exercise 5.33</h1>\n<pre>\n')
    with open('..\Chapter5\plot_wavepacket_movie.py','r') as infile:
        for line in infile.readlines():
            outfile.write(line)
    outfile.write('\n</pre>\n<hr>\n')
    outfile.write('<h1>Plots of wavepacket for t=%d, t=%d and t=%d </h1>\n' 
                  %(t_values[0],t_values[1],t_values[2]))  
    outfile.write('<img src="./wavepacket_fig1.png">\n')
    outfile.write('<img src="./wavepacket_fig2.png">\n')
    outfile.write('<img src="./wavepacket_fig3.png">\n')
    outfile.write('<hr><h1>Wavepacket animation</h1>')
    outfile.write('<img src="./movie1.gif">\n')
    outfile.write('</html>\n</body>')

      