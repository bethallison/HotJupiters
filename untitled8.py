#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:49:57 2017

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

x=np.linspace(5,30,num=1000)

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

y=[]
for i in range(len(x)):
    y.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))
   
x_value=15 ## Change this ONLY
y_value=(c0*x_value**0)+(c1*x_value**1)+(c2*x_value**2)+(c3*x_value**3)+(c4*x_value**4)
print y_value

x_value=24.5 ## Change this ONLY
y_value=(c0*x_value**0)+(c1*x_value**1)+(c2*x_value**2)+(c3*x_value**3)+(c4*x_value**4)
print y_value
    


c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05



#xplanet=[15,17,19,21,23,25,24,22,20,18,16,14]

#xplanet=[32,30,28,26,24,22,23,25,27,29,31,33] #good spread but too bright!

#xplanet=[38,36,34,32,30,28,29,31,33,35,37,39] far too dim!

#xplanet=[32,31.5,30.5,30,28,27.5,26.5,26,27,29,31,33] #almost there!

#xplanet=[31,30.5,30.2,30,29.5,29,28.5,28,28.5,29.4,30.4,31.4]

#xplanet=[31,29,28.8,28.6,28.4,28.2,28,28,28.2,28.6,29,31]

#xplanet=[15,15,18,18,22,22,25,25,28,28,31,31,33,33,32,32,30,30,27,27,25,25,23,23,21,21,19,19,17,17]
#xplanet=[30,29,28,20,19,18,10,9,8,18,19,20,28,29,30]
#xplanet=[8,9,8,4,6,4]

#xplanet=[21.5,20,22,25.5,28,25,23] This is the perfect model

xplanet=[27,25,23,21,19,17,15,13,14,16,18,20,22,24,26,28]

#xplanet=[25,24,21,20,19,18,15,14,14,15,17,18,19,20,25,24]
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
Nextra=3
for i in range(len(xpoints)):
    summation=0
    for j in range(Nextra):
        if i+j<len(xpoints):
            summation+=yplanet[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation+=yplanet[difference]
            #print i,j,difference
    combined.append(summation/len(xplanet))
    comb.append(summation)
    
long=[0,30,60,90,120,150,180,210,240,270,300,330,360]
print 'comb= ',comb
plt.scatter(xpoints,combined)
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
Nextra=3
for i in range(len(xpoints)):
    summation2=0
    for j in range(Nextra):
        if i+j<len(xpoints):
            summation2+=yplanet2[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation2+=yplanet2[difference]
            #print i,j,difference
    combined2.append(summation2/len(xplanet))
    comb2.append(summation2)
print 'comb2 ',comb2   
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
    M36.append(-2.5*np.log10(combined[i]/2.78))
    M45.append(-2.5*np.log10(combined2[i]/3.26))
    diff.append(M36[i]-M45[i])

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
plt.xlim((0,3))
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
plt.xlim((0,3))
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
