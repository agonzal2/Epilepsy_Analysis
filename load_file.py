# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:17:18 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
from numpy import *

def load_file(x):
    file=prm.get_filename()
    print(file)
    data=loadtext(file)
    return data
    
    
    
    
