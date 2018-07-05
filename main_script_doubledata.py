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
from filters import *

prm = parameters.Parameters()


def init_params(): #Defines initial parameters used throughout.
    prm.set_filepath('C:\\Users\\agonzal2\\DocSyncUoE\\Important Documents\\VGAT159 Analysis Seizures\\')
    prm.set_filename('E17.txt')
    prm.set_excelpath('D:\\ERUK\\Evans Recordings\\180314\\')
    prm.set_excelname('171221_VGATCRE_150_Day_39b.xls')
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
#data=data[::2] #####These 2 lines let you down sample data and plot it.
#plt.plot(data)
#prm.set_filename('E9.txt')
#data2=load_file(prm.get_filepath() + prm.get_filename()) #######load file
#plt.plot(data2)
#filtered_data=lowpass(data, prm.get_sampling_rate, 30, 255)  #### Function to filter data.
#filtered_data2=lowpass(data2, prm.get_sampling_rate, 1, 100)
plot_all((data)-38000, prm.get_sampling_rate(), 'k') #######Function to plot the data file.
#plot_all((data2+1000), prm.get_sampling_rate(), 'b')
#plot_all(filtered_data, prm.get_sampling_rate(), 'b') #######Function to plot filtered data file.
#plot_all(filtered_data2, prm.get_sampling_rate()) #######Function to plot filtered data file.



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



