#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:03:40 2018

@author: bettyallison
"""

import numpy as np #allows math functions



xplanet=[30,30,30,30,30,30,30,30,30,30,26,26,26,26,26,26,26,26,26,26,18,18,18,18,14,14,14,14,14,14,14,14,18,18,18]

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

y2=[]
yplanet=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet.append(10**(-0.4*((y2[i])-3.921)))
 
    


normalisation=np.sum(yplanet)
xpoints=np.linspace(1,len(xplanet),num=len(xplanet))


combined=[]
comb=[]
Nextra=((len(xplanet)/2))
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
    

    

M36=[]
M45=[]
diff=[]

for i in range(len(comb)):
    M36.append(3.921-(2.5*np.log10(comb[i])))




###############################################################################

c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05


y1=[]
yplanet1=[]

for i in range(len(xplanet)):
    y1.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet1.append(10**(-0.4*((y1[i])-3.921)))
 
    
normalisation4=np.sum(yplanet1)
xpoints4=np.linspace(1,len(xplanet),num=len(xplanet))


combined4=[]
comb4=[]
Nextra=((len(xplanet)/2))
for i in range(len(xpoints)):
    summation4=0
    for j in range(Nextra):
        if i+j<len(xpoints):
            summation4+=yplanet1[i+j]
        else:
            difference4=(i+j)-len(xpoints)
            summation4+=yplanet1[difference4]
            #print i,j,difference
    combined4.append((summation4/normalisation4))
    comb4.append(summation4/((len(xpoints))/2))
    

new4x=[]
a=360/len(xpoints)
for i in range(len(xpoints)):
    
    new4x.append((xpoints[i]*a)-a)

M45=[]
diff=[]

for i in range(len(comb4)):
    M45.append(3.892-(2.5*np.log10(comb4[i])))


colmag=[]

for i in range(len(M36)):
    colmag.append(M36[i]-M45[i])
    

    