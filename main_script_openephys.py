# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:26:07 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
import glob
import os
import parameters
from OpenEphys import *
import matplotlib.pyplot as plt
from numpy import *
from initial_processes import *
from power_spectrum import *
import scipy.fftpack
from scipy import signal
from filters import *

#This sets the parameters.
prm = parameters.Parameters()

###Parameters are defined here as objects but they use the parameters.py script.

def init_params(): #Defines initial parameters used throughout.
    prm.set_filepath('D:\\ERUK\\Tethered Recordings\\ERUK Animals\\180830\\2018-08-13_11-44-24\\')
    prm.set_filename('E17.txt')
    prm.set_excelpath('D:\\ERUK\\Tethered Recordings\\ERUK Animals\\180830\\')
    prm.set_excelname('180830_Stimulations_formated.xls')
    prm.set_sampling_rate(1000)
    prm.set_starttime(1036) #using as experiment
    prm.set_endtime(1046)   
    prm.set_starttime2(994) #using as control.
    prm.set_endtime2(1004)
    prm.set_windowtype('hamming')
    prm.set_stimfreq(10)
    
    
        

def main (): #runs everything but not in use yet
    
    init_params()
    
    
#This below initiates all the parameters.    
init_params()

##These two lines below load the data from OpenEphys and use the functions from Openephys.
data=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'CH', dtype = float, session = '0', source = '100')#######load file

data_adc=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'ADC', dtype = float, session = '0', source = '100')#######load file8

####This below is for filtering and plotting the data directly, but
###MNE will do a nicer job so don't use.

#filtered_data=lowpass(data, prm.get_sampling_rate, 30, 255)  #### Function to filter data.
#filtered_data2=lowpass(data2, prm.get_sampling_rate, 1, 100)
#plot_all((data)-38000, prm.get_sampling_rate(), 'k') #######Function to plot the data file.
#plot_all((data2+1000), prm.get_sampling_rate(), 'b')
#plot_all(filtered_data, prm.get_sampling_rate(), 'b') #######Function to plot filtered data file.
#plot_all(filtered_data2, prm.get_sampling_rate()) #######Function to plot filtered data file.



###This is to import analysis times from the spreadsheet.
analysis_times=import_spreadsheet(prm.get_excelpath() + prm.get_excelname()) #This together with Excel spreadsheet



####The line below allows us to plot and save Power spectrumes (PSDS) from a particular channel to a particular
####folder. See script in power_spectrum.
#multiple_psds(analysis_times, data[:,13]) # Function to plot the multiple psds based on import_spreadsheet. 


###This allows us to calculate a premilinary entrainment ratio from an individual channel. 
### It uses the basic functions in python and scipy, we should move to getting the data from MNE plots.

multiple_entrainmentratio(analysis_times, data[:,19])




###### Below are lines to plot the data directly, definitely ignore for now as plotting is better
#### and faster with MNE.

#emg=data[:,11]-data[:,10]
#plot_all(emg, prm.get_sampling_rate(), 'g')
#plot_all(data[:,3]+1000, prm.get_sampling_rate(), 'g')
#plot_all(data[:,9]+500, prm.get_sampling_rate(),'y')
#plot_all(data[:,9], prm.get_sampling_rate(),'r')
#plot_all(data[:,15], prm.get_sampling_rate(),'k')

#plot_all(data_adc[:,1]*1000+1000, prm.get_sampling_rate(), 'b')

#time_axis, sub_data1=sub_time_data(data, prm.get_starttime(), prm.get_endtime(), prm.get_sampling_rate())
#########get sub-data with time

#time_axis, sub_data2=sub_time_data(data, prm.get_starttime2(), prm.get_endtime2(), prm.get_sampling_rate())

#psd(sub_data, prm.get_windowtype(), prm.get_sampling_rate()) #########plot psd of subdata 


#psd_2chan(sub_data1, sub_data2, prm.get_windowtype(), prm.get_sampling_rate())


#plt.plot(time_axis, sub_data) ##########plot sub-data



