#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:26:47 2018

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

A36=[]
A45=[]
chi36=[]
chi45=[]



x=[]
for i in range(1000000):
    x.append(np.random.normal(0,1))
    A36.append(1+(x[i]*0.00333))
    A45.append(1+(x[i]*0.00466))
    '''
    chi36.append((np.sum(((1-A36[i]))**2/(0.00333*A36[i])**2)))
    chi45.append((np.sum(((1-A45[i]))**2/(0.00466*A45[i])**2)))
    
x1=np.linspace(0,len(x),len(x))

plt.axhline(1)
plt.scatter(x1,A36,c='m')
plt.scatter(x1,A45,c='c')
plt.show()

print np.sum(chi36)
print np.sum(chi45)
#calculating chi squared
'''

#now try binned data 


#
#bins = np.linspace(0, 1, 5000)
#digitized = np.digitize(A36, bins)
#bin_means = [A36[digitized == i].mean() for i in range(1, len(bins))]


bins = 20
slices = np.linspace(0, len(A36), bins+1, True).astype(np.int)
counts = np.diff(slices)

mean36 = np.add.reduceat(A36, slices[:-1]) / counts

bins = 20
slices = np.linspace(0, len(A45), bins+1, True).astype(np.int)
counts = np.diff(slices)

mean45 = np.add.reduceat(A45, slices[:-1]) / counts

error36=0.00333/(50000**0.5)
error45=0.00466/(50000**0.5)

redchi36=[]
for i in range(len(mean36)):
    redchi36.append((np.sum(((1-mean36[i]))**2/(error36**2))))
    
print np.sum(redchi36)
    
