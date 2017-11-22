# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:29:46 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk

This class has the setters and getters for the parameters. The parameters need to be set in main
and they can be called by calling the getter functions.
For example to set and get filepath:
prm.set_filepath('D:\\ERUK\\Wireless_Opto\\171120_VGATCRE_150_Day_3')
prm.get_filepath()
"""

class Parameters:
    
    
    filepath = ''
    filename = ''
    sampling_rate = 512
    window =''
    
    def get_window(self):
        return Parameters.window
    
    def set_window(self, wd):
        
        Parameters.window = wd
        
    def get_filepath(self):
        return Parameters.filepath

    def set_filepath(self, fp):
        Parameters.filepath = fp
    
    def get_filename(self):
        return self.filename

    def set_filename(self, fn):
        Parameters.filename = fn
                
    def set_sampling_rate(self, sr):
        
        Parameters.sampling_rate = sr
    

        
    
