#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:39:55 2017

@author: bettyallison
"""
#This code creates an HR diagram with Dupuy and Liu data 

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

input1=np.genfromtxt('LDWARFS.txt', delimiter=',', names=True, dtype=None)
input2=np.genfromtxt('MDWARFS.txt', delimiter=',', names=True, dtype=None)
input3=np.genfromtxt('TDWARFS.txt', delimiter=',', names=True, dtype=None)
input4=np.genfromtxt('YDWARFS.txt', delimiter=',', names=True, dtype=None)

C1=[]

for i in range(len(input1['MCH1'])):
    C1.append((input1['MCH1'])[i]-(input1['MCH2'])[i])

C2=[]

for i in range(len(input2['MCH1'])):
    C2.append((input2['MCH1'])[i]-(input2['MCH2'])[i])

C3=[]


for i in range(len(input3['MCH1'])):
    C3.append((input3['MCH1'])[i]-(input3['MCH2'])[i])
   
C4=[]

for i in range(len(input4['MCH1'])):
    C4.append((input4['MCH1'])[i]-(input4['MCH2'])[i])


x=np.linspace(5,30,num=1000)

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

y=[]
for i in range(len(x)):
    y.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))


c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05

y1=[]
for i in range(len(x)):
    y1.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))

col=[]
for i in range(len(y1)):
    col.append(y[i]-y1[i])

plt.scatter(C1,input1['MCH1'],c='g',label='L Dwarfs')
plt.scatter(C2,input2['MCH1'],color='r',label='M Dwarfs')
plt.scatter(C3,input3['MCH1'],color='b',label='T Dwarfs')
plt.scatter(C4,input4['MCH1'],color='y',label='Y Dwarfs')
plt.title('Colour Magnitude Diagram Using Dupuy and Liu Data')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[3.6]')
plt.ylim((6,20))
plt.xlim((-0.5,3))
#plt.ylim((10.5,13.75))
#plt.xlim((-0.2,2))
plt.gca().invert_yaxis()
plt.legend()
plt.show()   



   

plt.scatter(col,y1,c='g',label='Polynomial Fit',s=2)
plt.scatter(C1,input1['MCH2'],c='g',label='L Dwarfs')
plt.scatter(C2,input2['MCH2'],color='r',label='M Dwarfs')
plt.scatter(C3,input3['MCH2'],color='b',label='T Dwarfs')
plt.scatter(C4,input4['MCH2'],color='y',label='Y Dwarfs')
plt.title('Colour Magnitude Diagram Using Dupuy and Liu Data')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[4.5]')
plt.ylim((6,20))
plt.xlim((-0.5,3))
#plt.ylim((10.5,13.75))
#plt.xlim((-0.2,2))
plt.gca().invert_yaxis()
plt.legend()
plt.show()   
