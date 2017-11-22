# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:26:07 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
import glob
import os
import parameters

prm = parameters.Parameters()


def init_params():
    prm.set_filepath('D:\\ERUK\\Wireless_Opto\\171120_VGATCRE_150_Day_3')
    prm.set_sampling_rate(512)
    prm.set_filename('vgatcre_150_day3.txt')
    prm.set_window('hamming')
    x=prm.get_filename()
    
    
init_params()