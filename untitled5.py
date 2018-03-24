#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:57:47 2017

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

x1=np.linspace(16,50,num=100)
x2=np.linspace(50,16,num=100)
xplanet=[]
xplanet=np.concatenate((x1, x2), axis=0)
y2=[]
yplanet=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet.append(10**(-0.4*((y2[i])-2.78)))


normalisation=np.sum(yplanet)

xpoints=np.linspace(1,68,num=200)
plt.scatter(xpoints,yplanet/normalisation)
plt.ylabel('Normalized Flux from M[3.6]')
plt.xlabel('Slice Number')
plt.show()

combined=[]
comb=[]
Nextra=100
for i in range(len(xpoints)):
    summation=0
    for j in range(Nextra):
        if i+j<len(xpoints):
            summation+=yplanet[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation+=yplanet[difference]
            #print i,j,difference
    combined.append(summation/normalisation)
    comb.append(summation)
    
long=[0,30,60,90,120,150,180,210,240,270,300,330,360]

plt.scatter(xpoints,combined)
plt.xlabel('Longitude')
plt.ylabel('Combined Flux in M[4.5]')
plt.show()
#######################################################################
c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05
x1=np.linspace(16,50,num=100)
x2=np.linspace(50,16,num=100)
xplanet=[]
xplanet=np.concatenate((x1, x2), axis=0)
y1=[]
y=[]
for i in range(len(xplanet)):
    y.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    y1.append(10**(-0.4*((y[i])-3.26)))
    
print 'done'


x1=np.linspace(16,50,num=100)
x2=np.linspace(50,16,num=100)
xplanet=[]
xplanet=np.concatenate((x1, x2), axis=0)
y2=[]
yplanet2=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet2.append(10**(-0.4*((y2[i])-3.26)))

print 'done'

normalisation=np.sum(yplanet2)
xpoints=np.linspace(1,68,num=200)
plt.scatter(xpoints,yplanet2/normalisation)
plt.ylabel('Normalized Flux from M[4.5]')
plt.xlabel('Slice Number')
plt.show()

combined2=[]
comb2=[]
Nextra=100
for i in range(len(xpoints)):
    summation2=0
    for j in range(Nextra):
        if i+j<len(xpoints):
            summation2+=yplanet2[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation2+=yplanet2[difference]
            #print i,j,difference
    combined2.append(summation2/normalisation)
    comb2.append(summation2)
    
long=[0,30,60,90,120,150,180,210,240,270,300,330,360]

plt.scatter(xpoints,combined2)
plt.xlabel('Longitude')
plt.ylabel('Combined Flux in M[4.5]')
plt.show()

#########################################################################

#Lets go back to magnitudes#

M36=[]
M45=[]
diff=[]

for i in range(len(comb2)):
    M36.append(-2.5*np.log10(comb[i]/2.78))
    M45.append(-2.5*np.log10(comb2[i]/3.26))
    diff.append(M36[i]-M45[i])



plt.scatter(diff,M45)
plt.title('Colour Magnitude Diagram')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[4.5]')
#plt.ylim((8,20))
#plt.xlim((0,4))
plt.gca().invert_yaxis()
plt.show() 

plt.scatter(diff,M45)
plt.title('Colour Magnitude Diagram')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[4.5]')
#plt.ylim((10.5,13.75))
#plt.xlim((-0.2,2))
plt.gca().invert_yaxis()
plt.show()       
##########################################