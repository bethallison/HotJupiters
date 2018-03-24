#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:31:51 2017

@author: bettyallison
"""
import numpy as np
import matplotlib.pyplot as plt
#newdupuydata
#distance modulus = m-M

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


plt.scatter(input1['Spec'],Y,c='k',label='M6-L2')
plt.errorbar(input1['Spec'],Y,yerr=error_y1,ls='none')
plt.scatter(x,y,c='g',label='Polynomial Fit',s=2)
plt.xlabel('Spectral Class')
plt.ylabel('Absolute Magnitude M[3.6]')
plt.legend()
plt.xlim(5,30)
#plt.ylim(5,30)
plt.gca().invert_yaxis()
plt.savefig('dwarfs1.pdf')
plt.show()


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


plt.scatter(input1['Spec'],Y1,c='k',label='M6-L2')
plt.errorbar(input1['Spec'],Y1,yerr=error_y1,ls='none')
plt.scatter(x,y,c='g',label='Polynomial Fit',s=2)
plt.xlabel('Spectral Class')
plt.ylabel('Absolute Magnitude M[4.5]')
plt.legend()
plt.xlim(5,30)
#plt.ylim(5,30)
plt.gca().invert_yaxis()

plt.show()

############################################################
colour1=[]
for i in range(len(input1['Spec'])):
    colour1.append(Y[i]-Y1[i])

colour=[]
for i in range(len(x)):
    colour.append(y[i]-y1[i])


plt.scatter(colour,y,label='Polynomial')
plt.scatter(colour1,Y,label='Data')
plt.xlabel('colour')
plt.ylabel('Absolute Magnitude M3.6')
plt.legend()
plt.gca().invert_yaxis()
plt.savefig('dwarfs2.pdf')
plt.show()

plt.scatter(colour,y1,label='Data')
plt.scatter(colour1,Y1,label='Polynomial')
plt.xlabel('colour')
plt.ylabel('Absolute Magnitude M4.5')
plt.legend()
plt.gca().invert_yaxis()
plt.show()
