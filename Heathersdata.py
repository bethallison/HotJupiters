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


#combined=[]
#comb=[]
Nextra=500
binvalues=[]

summation=0
for i in range(len(input1['RelativeFlux'])):
    summation+=input1['RelativeFlux'][i]
    if i%Nextra == 0:
        binvalues.append(summation/Nextra)
        summation=0
        
#for i in range(len(x)):
#    summation=0
#    for j in range(Nextra):
#        if i+j<len(x):
#            summation+=y[i+j]
#        else:
#            difference=(i+j)-len(x)
#            summation+=y[difference]
#            #print i,j,difference
#    combined.append(summation/Nextra)
#    comb.append(summation)
    
x1=np.linspace(0,len(binvalues),num=len(binvalues))

plt.scatter(x1,binvalues,s=0.5)
#plt.plot(x1,y=1,c='g')
#plt.xlim(0,12500)
plt.ylim(0.97,1.003)
plt.ylabel('Relative Flux to Star')
plt.show()

plt.scatter(x1,binvalues,s=0.5)
#plt.plot(x1,y=1,c='g')
#plt.xlim(0,12500)
plt.ylim(0.997,1.003)
plt.ylabel('Relative Flux to Star')
plt.show()

plt.scatter(x1,binvalues,s=0.5)
plt.title('first occulatation')
#plt.plot(x1,y=1,c='g')
#plt.xlim(0,12500)
plt.ylim(0.97,1.003)
plt.ylabel('Relative Flux to Star')
plt.xlim(200,500)
plt.show()

plt.scatter(x1,binvalues,s=0.5)
plt.title('transit')
#plt.plot(x1,y=1,c='g')
#plt.xlim(0,12500)
plt.ylim(0.97,1.003)
plt.ylabel('Relative Flux to Star')
plt.xlim(1450,1750)
plt.show()

plt.scatter(x1,binvalues,s=0.5)
plt.title('second occulatation')
#plt.plot(x1,y=1,c='g')
#plt.xlim(0,12500)
plt.ylim(0.997,1.003)
plt.ylabel('Relative Flux to Star')
plt.xlim(2750,3100)
plt.show()


F45=10**(-0.4*(3.921-3.26))
print F45

abflux=[]
for i in range(len(binvalues)):
    abflux.append((binvalues[i]*F45)-F45)
    
plt.scatter(x1,abflux,s=0.5)
#plt.plot(x1,y=1,c='g')
#plt.xlim(0,12500)
plt.ylabel('Absolute FLux')
plt.ylim(-0.02,0.005)
plt.show()


fp=[]
M=[]
for i in range(len(abflux)):
    M.append((-2.5*np.log(abflux[i]))+3.26)
    
########################################################################

plt.scatter(x1,M,s=0.5)
#plt.ylim(4.77,4.85)
plt.show()
