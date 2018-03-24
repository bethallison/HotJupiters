#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:09:54 2017

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
values=[]

summation=0
for i in range(len(input1['RelativeFlux'])):
    values.append(((input1['RelativeFlux'])[i]))
    summation+=values[i]
    if i%Nextra == 0:
        binvalues.append(summation/Nextra)
        summation=0
        

    
x1=np.linspace(0,len(binvalues),num=len(binvalues))

x11=[]
for i in range(len(x1)):
    x11.append(x1[i]/len(x1))
    

plt.scatter(x11,binvalues,s=0.5)
#plt.plot(x1,y=1,c='g')
#plt.xlim(0,12500)
#plt.ylim(0.0,-0.005)
plt.ylabel('Relative Flux to the Star in 4.5 microns')
plt.ylim(0.975,1.003)
plt.xlabel('Arbitury Period Units')
plt.show()



############################################################################3

x3=np.linspace(1,len(input2['RelativeFlux']),num=len(input2['RelativeFlux']))

y3=[]
for i in range(len(input2['RelativeFlux'])):
    #if input1['RelativeFlux'][i] >= 1:
    y3.append((input2['RelativeFlux'])[i])



#plt.scatter(x,y,s=0.5)
#plt.xlim(750000,850000)
#plt.show()


#combined=[]
#comb=[]
Nextra2=500
binvalues2=[]
values2=[]

summation2=0
for i in range(len(input2['RelativeFlux'])):
    values2.append(((input2['RelativeFlux'])[i]))
    summation2+=values2[i]
    if i%Nextra2 == 0:
        binvalues2.append(summation2/Nextra2)
        summation2=0
        

    
x4=np.linspace(0,len(binvalues2),num=len(binvalues2))

x44=[]
for i in range(len(x4)):
    x44.append(x4[i]/len(x4))
    
    

plt.scatter(x44,binvalues2,s=0.5)
#plt.plot(x1,y=1,c='g')
#plt.xlim(0,12500)
#plt.ylim(0.0,-0.005)
plt.ylabel('Relative Flux to the Star in 3.6 microns')
plt.ylim(0.975,1.003)
plt.xlabel('Arbitury Period Units')
plt.show()

#2455559.568294
unbinnedx=[]
for i in range(len(input2['BJD'])):
    unbinnedx.append(input2['BJD'][i]-2455559.568294)

binnedx=[]
Nextra2x=500
binvalues2x=[]
values2x=[]

summation2x=0
for i in range(len(unbinnedx)):
    values2x.append(unbinnedx[i])
    summation2x+=values2x[i]
    if i%Nextra2x == 0:
        binvalues2x.append((summation2x/Nextra2x)*180)
        summation2x=0

fancyx=[]
for i in range(len(binvalues2x)):
    fancyx.append(binvalues2x[i]/360)
    
plt.scatter(fancyx,binvalues2,s=0.5)
plt.ylabel('Relative Flux to the Star in 3.6 microns')
plt.ylim(0.965,1.003)
plt.xlabel('Orbital Phase')
plt.savefig('Transit36.pdf')
plt.show()
#thing=[]
#for i in range(len(binvalues)):
#    if binvalues[i] > 0:
#        thing.append(binvalues[i])
#        
#x2=np.linspace(0,len(thing),num=len(thing))
#
#plt.scatter(x2,thing,label='M4.5')
#plt.ylim(0,0.0025)
##plt.xlim(1500,1750)
#
#
#thing2=[]
#for i in range(len(binvalues2)):
#    if binvalues2[i] > 0:
#        thing2.append(binvalues2[i])
#        
#x5=np.linspace(0,len(thing2),num=len(thing2))
#
#plt.scatter(x5,thing2,label='M3.6')
#plt.ylim(0,0.0025)
##plt.xlim(1500,1750)
#plt.legend()
#plt.show()

#########################################
#mag1=[]
#for i in range(len(thing)):
#    mag1.append((-2.5*np.log(thing[i]))-3.26)
#print mag1
#
#mag2=[]
#for i in range(len(thing2)):
#    mag2.append((-2.5*np.log(thing2[i]))-2.73)
#    
#plt.scatter(x2,mag1)
#plt.scatter(x5,mag2)
#plt.xlabel('Number')
#plt.ylabel('Flux')
#plt.show()
#
#
################################################
#
#
#thing=[]
#for i in range(len(binvalues)):
#    if binvalues[i] < 0:
#        thing.append(binvalues[i])
#        
#x2=np.linspace(0,len(thing),num=len(thing))
#
#plt.scatter(x2,thing,label='M4.5')
##plt.ylim(0,0.0025)
##plt.xlim(1500,1750)
#
#
#thing2=[]
#for i in range(len(binvalues2)):
#    if binvalues2[i] < 0:
#        thing2.append(binvalues2[i])
#        
#x5=np.linspace(0,len(thing2),num=len(thing2))
#
#plt.scatter(x5,thing2,label='M3.6')
#plt.ylim(0,0.0025)
##plt.xlim(1500,1750)
#plt.legend()
#plt.show()



    
    