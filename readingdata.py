#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:50:02 2018

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

input1=np.genfromtxt('results364.txt', names=True, dtype=None, delimiter=';')

input2=np.genfromtxt('results445.txt', names=True, dtype=None, delimiter=';')
    
   
x=np.sort(input1['chi2'])
x1=[]
for i in range(len(x)):
    x1.append(x[i])
    

#26;23;10;16;14.6423884059;0.0913961293316;0
#20;19;10;13;41.6941961227;0.156871025947;0