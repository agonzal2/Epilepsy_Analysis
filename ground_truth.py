# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:31:24 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
This script allows one to generate sine waves and replace values in them to test effect on PSDs.
"""
from matplotlib.pyplot import *
from numpy import *
from initial_processes import *
from math import *
import scipy.fftpack
from scipy import signal
from power_spectrum import *

sampling_rate = 512
fake_data_index_length=5120
oscillation_freq = 8
data_amplitude=400
optogenetics_duration=0.03 #seconds


def ground_truth_induction_saturation(sampling_rate, oscillation_freq, fake_data_index_length, data_amplitude, optogenetics_duration):
    
    x = np.arange(fake_data_index_length) #make array of data points.
    timelength = fake_data_index_length/sampling_rate  
    timeforplot = linspace(0, timelength, fake_data_index_length) #time axis for plotting
    ground_truth_data = np.sin(2*np.pi * oscillation_freq * x / Fs)*data_amplitude #sine wave
    intervals=1/oscillation_freq #this figures out where to introduce the gaps.
    index_jumps=intervals*sampling_rate
    index_jumps_integer=int(index_jumps)
    opto_index=optogenetics_duration*sampling_rate 
    opto_index_int=int(opto_index)

    
    for n in range(0, 79):#For loop introduces induction gap. 
        t=n*index_jumps_integer+13
        ground_truth_data[t:t+opto_index_int]=400

    return ground_truth_data, timeforplot



ground_truth_data, timeforplot= ground_truth_induction_saturation(sampling_rate, oscillation_freq, fake_data_index_length, data_amplitude, optogenetics_duration)

#plot(timeforplot, ground_truth_data) #Plot ground truth data with these points.
#xlabel('fake_data_index_length(n)')
#ylabel('voltage(V)')
#show()

psd(ground_truth_data, 'hamming', sampling_rate) ###Plot PSD for ground truth data.