#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:34:55 2017

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

input1=np.genfromtxt('final_unbinned_ch2_phot.txt', names=True, dtype=None)

input2=np.genfromtxt('final_unbinned_ch1_phot.txt', names=True, dtype=None)


x=np.linspace(1,len(input1['RelativeFlux']),num=len(input1['RelativeFlux']))

y=[]
for i in range(len(input1['RelativeFlux'])):
    #if input1['RelativeFlux'][i] >= 1:
    y.append((input1['RelativeFlux'])[i])



#plt.scatter(x,y,s=0.5)
#plt.xlim(750000,850000)
#plt.show()


combined=[]
comb=[]
Nextra=50
for i in range(len(x)):
    summation=0
    for j in range(Nextra):
        if i+j<len(x):
            summation+=y[i+j]
        else:
            difference=(i+j)-len(x)
            summation+=y[difference]
            #print i,j,difference
    combined.append(summation/Nextra)
    comb.append(summation)
    
x1=np.linspace(1,len(combined),num=len(combined))

plt.scatter(x1,combined,s=0.5)
plt.xlim(750000,850000)
plt.show()
'''
x1=np.linspace(1,len(y),num=len(y))
#plt.scatter(x1,y)
#plt.show()

F45=10**(-0.4*(3.921-3.26))

print F45

#in absolute flux F45=1.05e-10

fp=[]
M=[]
for i in range(len(y)):
    fp.append(y[i]*1.05e-10)
    M.append((-2.5*np.log(fp[i]))+3.26)
    
########################################################################
    
x2=np.linspace(1,len(input2['RelativeFlux']),num=len(input2['RelativeFlux']))

y1=[]
for i in range(len(input2['RelativeFlux'])):
    if input2['RelativeFlux'][i] >= 1:
        y1.append((input2['RelativeFlux'])[i]-1)
        
x3=np.linspace(1,len(y1),num=len(y1))

fp=[]
M2=[]
for i in range(len(y1)):
    fp.append(y1[i]*1.05e-10)
    M2.append((-2.5*np.log(fp[i]))+2.78)
    
print len(M2)
print len(M)
'''