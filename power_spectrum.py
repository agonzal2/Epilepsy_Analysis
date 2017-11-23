# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:09:44 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""

import matplotlib.pyplot as plt
from numpy import *
import scipy.fftpack
from scipy import signal


def psd(sub_data, windowtype, samplingrate) :  # Calculates PSD, plots it.
    


    window=scipy.signal.get_window(windowtype, samplingrate)
    f, Pxx_den = signal.periodogram(sub_data, samplingrate, window, samplingrate)
    psd=plt.semilogy(f, sqrt(Pxx_den), 'k')
    plt.xlim([0, 100])
    x=[0, 100]
    plt.xticks(arange(min(x), max(x), 10.0), size=10)
    ##plt.ticklabel_format(x, fontsize=1000)
    ##plt.font_manager.FontProerties()
    plt.ylim([1e-1, 1e2])
    plt.yticks(size=10)
    #plt.legend(handles=[psd1, psd2], loc=0)
    #for label in ax.get_xticklabels():
    #   label.set_color('r')
    plt.xlabel('Frequency [Hz]', fontsize=40)
    plt.ylabel('PSD [V**2/Hz]', fontsize=40)
    plt.show()
    
    return

def psd_2chan (sub_data1, sub_data2, windowtype, samplingrate) :  # Calculates PSD, plots it.
    


    window=scipy.signal.get_window(windowtype, samplingrate)
    f, Pxx_den = signal.periodogram(sub_data1, samplingrate, window, samplingrate)
    psd=plt.semilogy(f, sqrt(Pxx_den), 'b')
    
    window=scipy.signal.get_window(windowtype, samplingrate)
    f, Pxx_den = signal.periodogram(sub_data2, samplingrate, window, samplingrate)
    psd=plt.semilogy(f, sqrt(Pxx_den), 'k')
    
    
    
    
    
    plt.xlim([0, 100])
    x=[0, 100]
    plt.xticks(arange(min(x), max(x), 5.0), size=10)
    ##plt.ticklabel_format(x, fontsize=1000)
    ##plt.font_manager.FontProerties()
    plt.ylim([1e-1, 1e2])
    plt.yticks(size=10)
    #plt.legend(handles=[psd1, psd2], loc=0)
    #for label in ax.get_xticklabels():
    #   label.set_color('r')
    plt.xlabel('Frequency [Hz]', fontsize=40)
    plt.ylabel('PSD [V**2/Hz]', fontsize=40)
    plt.show()
    
    return