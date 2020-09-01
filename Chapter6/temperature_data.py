# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:16:02 2020

@author: lars-johan.brannmark
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#Function for reading .htm file content into dictionary that maps city name to
# name of .txt file
def read_fnamedict(filename):
    with open(filename,'r') as infile:
        text = infile.read().split("tab-stops:list .5in'><b>")[1:]
        return {word[0:word.find('</b>')].replace(' ( ',''): 
            word[word.find('/gsod/')+6:word.find('.txt"')+4] for word in text}

#Function for reading the temperature data .txt file of a specific city, into
# a dictionary containing the city name (a string), time (a datetime array) and
# temperature (a float array) 
def read_citytempdict(fnamedict, cityname):
    tempdata = np.genfromtxt('city_temp\\' + fnamedict[cityname])
    date = np.array([datetime(int(row[2]),int(row[0]),int(row[1])) for row in tempdata])
    temp = tempdata[:,-1]
    return {'name': cityname, 'date': date, 'temp': temp}

#Plot function that takes a list of city temperature dictionaries as input
def plot_citytemp(citydata):
    plt.figure()
    for city in list(citydata):
        plt.plot(city['date'], city['temp'], label=city['name'])
    plt.xlabel('date')
    plt.ylabel('temperature')
    plt.legend()

fname = 'city_temp\citylistWorld.htm'
fnamedict = read_fnamedict(fname)
citynames = ['London', 'Calcutta', 'Yerevan', 'Singapore']
citylist = [read_citytempdict(fnamedict, name) for name in citynames]
plot_citytemp(citylist)
