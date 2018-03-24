#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:26:19 2018

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created
from colour import Color

#input1=np.genfromtxt('final_unbinned_ch1_phot.txt', names=True, dtype=None)#, delimiter=' ')
#input2=np.genfromtxt('final_unbinned_ch2_phot.txt', names=True, dtype=None)

#print min(input1['RelativeFlux'])
#print min(input2['RelativeFlux'])

P=2*np.pi
#2455558.156373
#2455559.568294
#t=[]
#for i in range(len(input1['BJD'])):
#    t.append(input1['BJD'][i]-2455560.665100)

t=np.linspace(0,2*np.pi,20)
    

#use period and T from her paper
c1=-0.000479
c2=-0.000389
c3=0.000035
c4=-0.00002
#t=np.linspace(0,2*np.pi,40)

y=[]
for i in range(len(t)):
    y.append((c1*np.cos(((2*np.pi*t[i])/P))+(c2*np.sin((2*np.pi*t[i])/P))+(c3*np.cos((2*np.pi*t[i])/P))+(c4*np.sin((2*np.pi*t[i])/P))-0.0006+0.1242))

t4=[]
for i in range(len(t)):
    t4.append((t[i]/(2*np.pi)))
plt.scatter(t4,y,label='M3.6')
plt.legend()
plt.ylim(min(y),max(y))
plt.show()

#input2=np.genfromtxt('final_unbinned_ch2_phot.txt', names=True, dtype=None)
##2455187.689833
##2455189.056386
#P=2.759461

t2=np.linspace(0,2*np.pi,20)
#for i in range(len(input2['BJD'])):
#    t2.append(input2['BJD'][i]-2455190.161580)
    
c1=-0.000448
c2=-0.000122
c3=-0.00002
c4=0.000982

y1=[]
for i in range(len(t2)):
    y1.append((c1*np.cos((2*np.pi*t2[i])/P))+(c2*np.sin((2*np.pi*t2[i])/P))+(c3*np.cos((2*np.pi*t2[i])/P))+(c4*np.sin((2*t2[i]*np.pi)/P))-0.00085+0.0982)

t3=[]
for i in range(len(t2)):
    t3.append((t2[i]/(2*np.pi)))
    
plt.scatter(t3,y1,label='M4.5')
plt.legend()
plt.ylim(min(y1),max(y1))
plt.show()

#normalisation=np.sum(y)
##print normalisation
#xpoints=np.linspace(1,len(t),num=len(t))
##plt.scatter(xpoints,yplanet)
##plt.ylim(0,0.005)
##plt.ylabel('Normalized Flux from M[3.6]')
##plt.xlabel('Slice Number')
##plt.show()
#
#combined=[]
#comb=[]
#Nextra=((len(t)/2))
#enable_darkening=True
#fraction=(len(t)/4)
#################DO NOT REMOTE THESE LINES:
#Nextra_halved=Nextra/2.
#if fraction<Nextra_halved:
#    raise TypeError("Fraction is smaller than half of Nextra. This is physically impossible.")
#################
#for i in range(len(xpoints)):
#    summation2=0
#    for j in range(Nextra):
#        separation=np.abs(j-Nextra_halved)
#        if i+j<len(xpoints):
#            summation=y[i+j]
#        else:
#            difference=(i+j)-len(xpoints)
#            summation=y[difference]
#        if separation != 0 and enable_darkening==True: summation2+=summation*(np.abs(fraction-separation)/fraction)
#        else: summation2+=summation
#    combined.append((summation2/normalisation))
#    comb.append(summation2/(len(t)/2))
#    
#
#newx=[]
#a=360./len(xpoints)
#for i in range(len(xpoints)):
#    
#    newx.append((xpoints[i]*a)-a)
#    
#plt.scatter(newx,comb)
#plt.ylim(min(comb),max(comb))
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux in M[3.6]')
#plt.show()

M36=[]
M45=[]
diff=[]

for i in range(len(y)):
    M36.append(3.921-(2.5*np.log10(y[i])))
    
    
#normalisation4=np.sum(y1)
##print normalisation4
#xpoints4=np.linspace(1,len(t2),num=len(t2))
##plt.scatter(xpoints4,yplanet1)
##plt.ylim(0,0.005)
##plt.ylabel('Normalized Flux from M[4.5]')
##plt.xlabel('Slice Number')
##plt.show()
#
#combined4=[]
#comb4=[]
#Nextra=((len(t2)/2))
#enable_darkening=True
#fraction=(len(t2)/4)
#################DO NOT REMOTE THESE LINES:
#Nextra_halved=Nextra/2.
#if fraction<Nextra_halved:
#    raise TypeError("Fraction is smaller than half of Nextra. This is physically impossible.")
#################
#for i in range(len(xpoints)):
#    summation2=0
#    for j in range(Nextra):
#        separation=np.abs(j-Nextra_halved)
#        if i+j<len(xpoints):
#            summation=y1[i+j]
#        else:
#            difference=(i+j)-len(xpoints)
#            summation=y1[difference]
#        if separation != 0 and enable_darkening==True: summation2+=summation*(np.abs(fraction-separation)/fraction)
#        else: summation2+=summation
#    combined4.append((summation2/normalisation4))
#    comb4.append(summation2/(len(t2)/2))
#
#long=[0,30,60,90,120,150,180,210,240,270,300,330,360]
#new4x=[]
#a=360/len(xpoints)
#for i in range(len(xpoints)):
#    
#    new4x.append((xpoints[i]*a)-a)
#    
#plt.scatter(new4x,comb4)
#plt.ylim(min(comb4),max(comb4))
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux in M[4.5]')
#plt.show()

#plt.scatter(newx,comb,label='M36')
#plt.scatter(new4x,comb4,label='M45')
#plt.ylim(0,0.0015)
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux')
#plt.legend()
#plt.show()


M45=[]
diff=[]

for i in range(len(y1)):
    M45.append(3.892-(2.5*np.log10(y1[i])))

colmag=[]

for i in range(len(M36)):
    colmag.append(M36[i]-M45[i])
    

color36= [(str(item/max(M36))) for item in M36]
color45= [(str(item/max(M45))) for item in M45]


#plt.scatter(colour,y,label='Polynomial',s=0.2,c='r')
plt.scatter(colmag,M36,s=40,c=color36,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 3.6 microns')
#plt.ylim((8,20))
#plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.legend()
#plt.savefig('planetHR1HOPE.pdf')
plt.show()

#plt.scatter(colour,y1,label='Polynomial',s=0.2,c='r')
plt.scatter(colmag,M45,s=40,c=color45,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 4.5 microns')
#plt.ylim((8,20))
#plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.legend()
#plt.savefig('planetHR2HOPE.pdf')
plt.show()