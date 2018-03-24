#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:41:08 2018

@author: bettyallison
"""

c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05


xplanet=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]

y1=[]
yplanet1=[]

for i in range(len(xplanet)):
    y1.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet1.append(10**(-0.4*((y1[i])-3.921)))
    
print yplanet1