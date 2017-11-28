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
    prm.set_filepath('E:\\ERUK\Wireless_Opto\\171127_VGATCRE_150_Day_10\\')
    prm.set_filename('171127_vgatcre_150_day_10.txt')
    prm.set_excelpath('E:\\ERUK\\Wireless_Opto\\171127_VGATCRE_150_Day_10\\PSD Analysis_black_control_blue_opto\\')
    prm.set_excelname('171127_VGATCRE_150_Day_10.xls')
    prm.set_sampling_rate(512)
    prm.set_starttime(1036) #using as experiment
    prm.set_endtime(1046)   
    prm.set_starttime2(994) #using as control.
    prm.set_endtime2(1004)
    prm.set_windowtype('hamming')
        

def main (): #runs stuff.
    
    init_params()
    
    
init_params()
data=load_file(prm.get_filepath() + prm.get_filename()) #######load file
plot_all(data, prm.get_sampling_rate()) #######Function to plot the data file.


#analysis_times=import_spreadsheet(prm.get_excelpath() + prm.get_excelname()) #This together with Excel spreadsheet
#allows you to analyse specified times in the data.
#
#multiple_psds(analysis_times, data) # Function to plot the multiple psds based on import_spreadsheet. 








#time_axis, sub_data1=sub_time_data(data, prm.get_starttime(), prm.get_endtime(), prm.get_sampling_rate())
#########get sub-data with time

#time_axis, sub_data2=sub_time_data(data, prm.get_starttime2(), prm.get_endtime2(), prm.get_sampling_rate())

#psd(sub_data, prm.get_windowtype(), prm.get_sampling_rate()) #########plot psd of subdata 


#psd_2chan(sub_data1, sub_data2, prm.get_windowtype(), prm.get_sampling_rate())


#plt.plot(time_axis, sub_data) ##########plot sub-data



