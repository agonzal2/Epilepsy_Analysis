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
    windowtype =''
    filelength = 500
    starttime=0
    endtime=90
    
    def get_starttime(self):
        
        return Parameters.starttime
    
    def set_starttime(self, start):
        
        Parameters.starttime=start
    
    def get_endtime(self):
        
        return Parameters.endtime
    
    def set_endtime(self, end):
        
        Parameters.endtime=end
    
    
    def get_filelength(self):
        
        return Parameters.filelength
    
    def set_filelength(self, leng):
        Parameters.filelength=leng
    
    def get_windowtype(self):
        return Parameters.windowtype
    
    def set_windowtype(self, wt):
        
        Parameters.windowtype = wt
        
    def get_filepath(self):
        return Parameters.filepath

    def set_filepath(self, fp):
        Parameters.filepath = fp
    
    def get_filename(self):
        return self.filename

    def set_filename(self, fn):
        Parameters.filename = fn
        
    def get_sampling_rate(self):
        return Parameters.sampling_rate
                
    def set_sampling_rate(self, sr):
        
        Parameters.sampling_rate = sr
    

        
    
