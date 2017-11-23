# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:17:18 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
from numpy import *
import parameters
import matplotlib.pyplot as plt
prm = parameters.Parameters()

def load_file(file):  #Opens text files.
    print("Opening file" + file)
    data=loadtxt(file)
    
    return data
    

def sub_time_data(data, start_time, end_time, sampling_rate): #Gets time axis and data of specific times.
    
    prm.set_filelength(len(data))
    filelength=prm.get_filelength()
    timelength=filelength/sampling_rate
    time_axis = linspace(start_time, end_time, ((end_time-start_time)*sampling_rate))
    
    index_start = start_time*sampling_rate
    index_end = end_time*sampling_rate
    sub_data = data[index_start:index_end]
    
    return time_axis, sub_data


def plot_all(data, sampling_rate):  #This allows for an initial plot of all the ddata.
    
    timemax=len(data)
    timelength = timemax/sampling_rate
    
    timeforplot = linspace(0, timelength, timemax)
    plt.plot(timeforplot, data)
    
    return
    

