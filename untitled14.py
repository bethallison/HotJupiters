#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 11:50:01 2017

@author: bettyallison
"""

import numpy as np
import matplotlib.pyplot as plt

input1=np.genfromtxt('newdupuydata.txt', delimiter=',', names=True, dtype=None)

x=np.linspace(5,30,num=1000)

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

y=[]
for i in range(len(x)):
    y.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))
   
Y=[]
for i in range(len(input1['Spec'])):
    Y.append((input1['M36'][i])-(input1['distmod'][i]))
    
    
error_y1=input1['eM36']

#
#plt.scatter(input1['Spec'],Y,c='k',label='M6-L2')
#plt.errorbar(input1['Spec'],Y,yerr=error_y1,ls='none')
#plt.scatter(x,y,c='g',label='Polynomial Fit',s=2)
#plt.xlabel('Spectral Class')
#plt.ylabel('Absolute Magnitude M[3.6]')
#plt.legend()
#plt.xlim(5,30)
##plt.ylim(5,30)
#plt.gca().invert_yaxis()
#
#plt.show()


######################################################

x=np.linspace(5,30,num=1000)

c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05

y1=[]
for i in range(len(x)):
    y1.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))

Y1=[]
for i in range(len(input1['Spec'])):
    Y1.append((input1['M45'][i])-(input1['distmod'][i]))  

error_y1=input1['eM45']


#plt.scatter(input1['Spec'],Y1,c='k',label='M6-L2')
#plt.errorbar(input1['Spec'],Y1,yerr=error_y1,ls='none')
#plt.scatter(x,y,c='g',label='Polynomial Fit',s=2)
#plt.xlabel('Spectral Class')
#plt.ylabel('Absolute Magnitude M[4.5]')
#plt.legend()
#plt.xlim(5,30)
##plt.ylim(5,30)
#plt.gca().invert_yaxis()
#
#plt.show()

############################################################
colour1=[]
for i in range(len(input1['Spec'])):
    colour1.append(Y[i]-Y1[i])

colour=[]
for i in range(len(x)):
    colour.append(y[i]-y1[i])

#JUST T DWARFS#
M1TA=[13.72,16.28,15.38,14.82,15.71,16.84,14.06,15.59,13.9,14.67,14.1,12.67,14.28,14.41,14.47,14.76,13.1,13.76,16.28,14.39,14.71,14.01,12.86,14.19,14.39,12.63,15.95,16.93,14.53,14.69,13.8,15.44,12.63,14.3,15.25,14.43,14.95,16.62,13.72,16.44,14.69,14.48]

M2TA=[13.07,14.49,13.62,13.57,13.66,14.65,13.91,14.98,12.95,12.68,12.29,11.93,12.19,13.01,12.95,14.6,11.64,11.66,14.35,12.95,13.88,12.23,12.73,13.23,12.93,12.39,13.91,16.08,13.6,12.76,12.12,14.01,11.32,13.08,13.86,12.39,14.46,14.6,13.39,14.43,13.69,13.38]

xTA=[]
y1TA=[]
y2TA=[]
for i in range(len(M1TA)):
    y1TA.append(M1TA[i]-1.5)
    y2TA.append(M2TA[i]-1.5)
    
    xTA.append(y1TA[i]-y2TA[i])

#L DWARFS#    
M1L=[12.54,10.19,13.39,10.29,8.87,10.26,11.77,12.77,11.49,11.75,11.7,11.66,11.49,11.17,11.76,12.72,10.99,10.27,12.91,12.7,13.25,12.76,11.53,10.38,13.08,11.05,12.35]
M2L=[12.48,10.24,13.24,10.2,8.79,9.95,11.52,12.64,11.6,11.62,11.59,11.47,11.5,11.22,11.77,12.64,10.98,10.4,12.61,12.65,13.13,12.64,11.4,10.24,12.89,11.14,12.11]
xL=[]

for i in range(len(M1L)):
    xL.append(M1L[i]-M2L[i])


plt.scatter(xTA,y1TA,color='b')
plt.scatter(xL,M1L,color='g')
plt.scatter(colour,y,label='Polynomial',s=2)
plt.title('Contrained Colour Magnitude Diagram')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[3.6]')
plt.ylim((6,20))
plt.xlim((-0.5,3))
#plt.ylim((10.5,13.75))
#plt.xlim((-0.2,2))
plt.gca().invert_yaxis()
plt.show()

plt.scatter(xTA,y2TA,color='b')
plt.scatter(xL,M2L,color='g')
plt.scatter(colour,y1,label='Polynomial',s=2)
plt.title('Constrained Colour Magnitude Diagram')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[4.5]')
plt.ylim((6,20))
plt.xlim((-0.5,3))
#plt.ylim((10,12))
#plt.xlim((-0.2,2))
plt.gca().invert_yaxis()
plt.show()

#MAking the dwarfs brighter seems to be good and has a good impact 



