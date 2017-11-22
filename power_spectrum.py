# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:09:44 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
from matplotlib.pyplot import *
from numpy import *
import scipy.fftpack
from scipy import signal

prm.


window=scipy.signal.get_window('hamming', samplingrate)

f, Pxx_den = signal.periodogram(chan, samplingrate, window)