#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:15:05 2017

@author: bettyallison
"""

#This code is about creating Dupuy and Liu Polynomials

#Initially let's plot a spectral class vs magnitude graph 

#M,L,T,Y

#brown M6-L2 (M6=6 and T9=29)

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

input1=np.genfromtxt('spectrabrown.txt', delimiter=',', names=True, dtype=None)
input2=np.genfromtxt('spectrared.txt', delimiter=',', names=True, dtype=None)
input3=np.genfromtxt('purplespect.txt', delimiter=',', names=True, dtype=None)
input4=np.genfromtxt('spectblue.txt', delimiter=',', names=True, dtype=None)


x=np.linspace(5,30,num=1000)

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

y=[]
for i in range(len(x)):
    y.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))
   
x_value=20 ## Change this ONLY
y_value=(c0*x_value**0)+(c1*x_value**1)+(c2*x_value**2)+(c3*x_value**3)+(c4*x_value**4)
print y_value

error_y1=input1['eCH1']
error_y2=input2['eCH1']
error_y3=input3['eCH1']
error_y4=input4['eCH1']
    
plt.scatter(x,y,c='g',label='Polynomial Fit',s=2)
plt.scatter(input1['spect'],input1['MCH1'],c='k',label='M6-L2')
plt.errorbar(input1['spect'],input1['MCH1'],yerr=error_y1,ls='none')
plt.scatter(input2['spect'],input2['MCH1'],c='r',label='L2.5-L9')
plt.errorbar(input2['spect'],input2['MCH1'],yerr=error_y2,ls='none')
plt.scatter(input3['spect'],input3['MCH1'],c='m',label='L9.5-T4')
plt.errorbar(input3['spect'],input3['MCH1'],yerr=error_y3,ls='none')
plt.scatter(input4['spect'],input4['MCH1'],c='c',label='T4.5-Y0')
plt.errorbar(input4['spect'],input4['MCH1'],yerr=error_y4,ls='none')
plt.xlabel('Spectral Class')
plt.ylabel('Absolute Magnitude M[3.6]')
plt.legend()
plt.gca().invert_yaxis()
plt.show()



#################################

x=np.linspace(5,30,num=1000)

c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05

y=[]
for i in range(len(x)):
    y.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))
   
x_value=20 ## Change this ONLY
y_value=(c0*x_value**0)+(c1*x_value**1)+(c2*x_value**2)+(c3*x_value**3)+(c4*x_value**4)
print y_value

plt.scatter(x,y,c='g',label='Polynomial Fit',s=2)
plt.scatter(input1['spect'],input1['MCH2'],c='k',label='M6-L2')
plt.scatter(input2['spect'],input2['MCH2'],c='r',label='L2.5-L9')
plt.scatter(input3['spect'],input3['MCH2'],c='m',label='L9.5-T4')
plt.scatter(input4['spect'],input4['MCH2'],c='c',label='T4.5-Y0')
plt.xlabel('Spectral Class')
plt.ylabel('Absolute Magnitude M[4.5]')
plt.legend()
plt.ylim(6,18)
plt.gca().invert_yaxis()
plt.show()

#########################################

#TURNING THIS IS INTO FLUXES 
#M[3.6]
F1=[]
for i in range(len(input1['MCH1'])):
    F1.append(10**(-0.4*((input1['MCH1'][i])-2.78)))
F2=[]
for i in range(len(input2['MCH1'])):
    F2.append(10**(-0.4*((input2['MCH1'][i])-2.78)))
F3=[]
for i in range(len(input3['MCH1'])):
    F3.append(10**(-0.4*((input3['MCH1'][i])-2.78)))
F4=[]
for i in range(len(input4['MCH1'])):
    F4.append(10**(-0.4*((input4['MCH1'][i])-2.78)))


x=np.linspace(5,30,num=1000)

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

y1=[]
y=[]
for i in range(len(x)):
    y.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))
    
    y1.append(10**(-0.4*((y[i])-2.78)))

error_y5=input1['eCH2']
error_y6=input2['eCH2']
error_y7=input3['eCH2']
error_y8=input4['eCH2']


plt.scatter(x,y1,c='g',label='Polynomial Fit',s=2)
plt.scatter(input1['spect'],F1,c='k',label='M6-L2')
#plt.errorbar(input1['spect'],input1['MCH2'],yerr=error_y5,ls='none')
plt.scatter(input2['spect'],F2,c='r',label='L2.5-L9')
#plt.errorbar(input2['spect'],input2['MCH2'],yerr=error_y6,ls='none')
plt.scatter(input3['spect'],F3,c='m',label='L9.5-T4')
#plt.errorbar(input3['spect'],input3['MCH2'],yerr=error_y7,ls='none')
plt.scatter(input4['spect'],F4,c='c',label='T4.5-Y0')
#plt.errorbar(input4['spect'],input4['MCH2'],yerr=error_y8,ls='none')
plt.xlabel('Spectral Class')
plt.ylabel('Absolute Flux in M[3.6]')
plt.legend()

plt.show()

#########################################

#TURNING THIS IS INTO FLUXES 
#M[4.5]
F1=[]
for i in range(len(input1['MCH1'])):
    F1.append(10**(-0.4*((input1['MCH1'][i])-3.26)))
F2=[]
for i in range(len(input2['MCH1'])):
    F2.append(10**(-0.4*((input2['MCH1'][i])-3.26)))
F3=[]
for i in range(len(input3['MCH1'])):
    F3.append(10**(-0.4*((input3['MCH1'][i])-3.26)))
F4=[]
for i in range(len(input4['MCH1'])):
    F4.append(10**(-0.4*((input4['MCH1'][i])-3.26)))


x=np.linspace(5,30,num=1000)

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

y1=[]
y=[]
for i in range(len(x)):
    y.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))
    
    y1.append(10**(-0.4*((y[i])-3.26)))

x_value=20 ## Change this ONLY
y1_value=(c0*x_value**0)+(c1*x_value**1)+(c2*x_value**2)+(c3*x_value**3)+(c4*x_value**4)
y_value=(10**(-0.4*((y1_value)-3.26)))
print y_value


plt.scatter(x,y1,c='g',label='Polynomial Fit',s=2)
plt.scatter(input1['spect'],F1,c='k',label='M6-L2')
plt.scatter(input2['spect'],F2,c='r',label='L2.5-L9')
plt.scatter(input3['spect'],F3,c='m',label='L9.5-T4')
plt.scatter(input4['spect'],F4,c='c',label='T4.5-Y0')
plt.xlim(6,30)
plt.ylim(0,0.01)
plt.xlabel('Spectral Class')
plt.ylabel('Absolute Flux in M[4.5]')
plt.legend()

plt.show()