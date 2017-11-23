# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:26:07 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
import glob
import os
import parameters
import matplotlib.pyplot as plt
from numpy import *
from initial_processes import *
from power_spectrum import *
import scipy.fftpack
from scipy import signal

prm = parameters.Parameters()


def init_params(): #Defines initial parameters used throughout.
    prm.set_filepath('D:\\ERUK\\Wireless_Opto\\171120_VGATCRE_150_Day_3\\')
    prm.set_sampling_rate(512)
    prm.set_filename('vgatcre_150_day3.txt')
    prm.set_starttime(100)
    prm.set_endtime(200)
    prm.set_windowtype('hamming')
        

def main (): #runs stuff.
    
    init_params()
    
    
    
    
    
init_params()

data=load_file(prm.get_filepath() + prm.get_filename()) #######load file

#plot_all(data, prm.get_sampling_rate()) #######plot all


#time_axis, sub_data=sub_time_data(data, prm.get_starttime(), prm.get_endtime(), prm.get_sampling_rate())
#########get sub-data with time

psd(sub_data, prm.get_windowtype(), prm.get_sampling_rate()) #########plot psd of subdata 

#plt.plot(time_axis, sub_data) ##########plot sub-data



