#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:00:52 2018

@author: bettyallison
"""

import numpy as np #allows math functions

input36=np.genfromtxt('results36.txt', names=True, dtype=None, delimiter=';')


for i in range(len(input36['chi2'])):
    a=np.sort(input36['chi2'])
    
print a

input45=np.genfromtxt('results45.txt', names=True, dtype=None, delimiter=';')


for i in range(len(input45['chi2'])):
    b=np.min(input45['chi2'])
    
print b