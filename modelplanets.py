#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:49:57 2017

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created


c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05


xplanet=[30,30,30,30,30,30,28,28,28,28,27,27,22,22,20,20]

y2=[]
yplanet=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet.append(10**(-0.4*((y2[i])-2.778683)))


normalisation=np.sum(yplanet)
xpoints=np.linspace(1,len(xplanet),num=len(xplanet))
plt.scatter(xpoints,yplanet/normalisation)
plt.ylabel('Normalized Flux from M[3.6]')
plt.xlabel('Slice Number')
plt.show()

combined=[]
comb=[]
Nextra=(len(xplanet)/2)
for i in range(len(xpoints)):
    summation=0
    for j in range(Nextra):
        if i+j<len(xpoints):
            summation+=yplanet[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation+=yplanet[difference]
            #print i,j,difference
    combined.append((summation/normalisation))
    comb.append(summation/(len(xplanet)/2))
    
long=[0,30,60,90,120,150,180,210,240,270,300,330,360]
print 'comb= ',comb
plt.scatter(xpoints,comb)
plt.xlabel('Longitude')
plt.ylabel('Combined Flux in M[4.5]')
plt.show()



#############################################################################

#ALL AGAIN DIFFERENT MAGNITUDE



c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05

yS=[]
#yS.append(10**(-0.4*((y[i])-3.26))) #flux of the sun


y2=[]
yplanet2=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet2.append(10**(-0.4*((y2[i])-3.26)))

print 'done'

normalisation=np.sum(yplanet2)
xpoints=np.linspace(1,len(xplanet),num=len(xplanet))
plt.scatter(xpoints,yplanet2/normalisation)
plt.ylabel('Normalized Flux from M[4.5]')
plt.xlabel('Slice Number')
plt.show()

combined2=[]
comb2=[]
Nextra=(len(xplanet)/2)
for i in range(len(xpoints)):
    summation=0
    for j in range(Nextra):
        if i+j<len(xpoints):
            summation+=yplanet[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation+=yplanet[difference]
            #print i,j,difference
    combined.append((summation/normalisation))
    comb2.append(summation/(len(xplanet)/2))
print 'comb2 ',comb2   
long=[0,30,60,90,120,150,180,210,240,270,300,330,360]

plt.scatter(xpoints,comb2)
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

print diff
plt.scatter(xpoints,M36)
plt.xlabel('Longitude')
plt.ylabel('Combined Magnitude in M[3.6]')
plt.gca().invert_yaxis()
plt.show()

print diff
plt.scatter(diff,M36)
plt.scatter(0.244,11.006,c='r')
plt.scatter(1.55,13.06,c='m')
plt.title('Colour Magnitude Diagram')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[3.6]')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.legend()
plt.gca().invert_yaxis()
plt.show() 

plt.scatter(diff,M45)
plt.scatter(0.244,10.762,c='r')
plt.scatter(1.55,11.51,c='m')
plt.title('Colour Magnitude Diagram')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[4.5]')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.legend()
plt.gca().invert_yaxis()
plt.show() 
'''
#plt.scatter(diff,M45)
#plt.title('Colour Magnitude Diagram')
#plt.xlabel('[3.6]-[4.5]')
#plt.ylabel('M[4.5]')
##plt.ylim((10.5,13.75))
##plt.xlim((-0.2,2))
#plt.gca().invert_yaxis()
#plt.show()     
'''   
##########################################

print 'M36 ',M36

print 'done'

print 'M45 ',M45

############################################



c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

x_value=17 ## Change this ONLY
y_value=(c0*x_value**0)+(c1*x_value**1)+(c2*x_value**2)+(c3*x_value**3)+(c4*x_value**4)
print y_value

print diff
 
