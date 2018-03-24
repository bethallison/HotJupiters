#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:48:42 2017

@author: bettyallison
"""
import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05
#Units for M3.6

#xplanet=[30,29,28,27,24,23,23,24,27,28,29,30]
#xplanet=[29,29,29,28,28,27.5,27.5,27,27,25,25,24,24,24,23,18,20,23,23,26,26,27,27,28,28,28.5,28.5,29,29,29]

#xplanet=[30,30,30,29,29,28,28,27,27,26,26,25,25,20,20,20,24,24,24,26,26,27,27,28,28,29,29,30,30]
#xplanet=[30,29,28,27,26,25,24,23,22,23,24,25,26,27,28,29,30] #keep this one

#xplanet=[29,28,25,24,23,23,24,25,28,29]

#basic basic planet xplanet=[20,20,20,26,26,26]

#xp2=[14,16,18,20,22,24,26,27,28,28,29,30,30,30,28,28,27,26,25,22,20,18,16,14] perfect

xplanet=[24,24,24,24,24,24,24,24]

#xplanet=[28,28,28,28,28,27,26,26,26,25,25,25,24,18,18,18,18,15,15,15,15,15,13,13,13,13,13,15,15,15,15,15,18,18,18,18,18,24,25,25,25,25,26,26,26,27,28,28,28,28,28]

#xplanet=[]
#for i in range(len(xp1)):
#    xplanet.append(((xp1[i]*3)+(xp2[i]*9))/12)
#
#print xplanet


#Spectral Class 
y2=[]
yplanet=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet.append(10**(-0.4*((y2[i])-3.921)))

print y2
print yplanet

normalisation=np.sum(yplanet)
print normalisation
xpoints=np.linspace(1,len(xplanet),num=len(xplanet))
plt.scatter(xpoints,yplanet)
plt.ylim(0,0.005)
plt.ylabel('Normalized Flux from M[3.6]')
plt.xlabel('Slice Number')
plt.show()

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
    
long=[0,30,60,90,120,150,180,210,240,270,300,330,360]
newx=[]
a=360/len(xpoints)
for i in range(len(xpoints)):
    
    newx.append((xpoints[i]*a)-a)
    
plt.scatter(newx,comb)
plt.ylim(min(comb),0.005)
plt.xlabel('Longitude')
plt.ylabel('Combined Flux in M[3.6]')
plt.show()

M36=[]
M45=[]
diff=[]

for i in range(len(comb)):
    M36.append(3.921-(2.5*np.log10(comb[i])))


plt.scatter(newx,M36)
plt.xlabel('Longitude')
plt.ylabel('Combined Magnitude in M[3.6]')
plt.gca().invert_yaxis()
plt.show()

print 'M36', M36
#############################################################################

c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05


#Spectral Class 
y4=[]
yplanet4=[]

for i in range(len(xplanet)):
    y4.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet4.append(10**(-0.4*((y4[i])-3.892)))

print y4
print yplanet4

normalisation4=np.sum(yplanet4)
print normalisation4
xpoints4=np.linspace(1,len(xplanet),num=len(xplanet))
plt.scatter(xpoints4,yplanet4)
plt.ylim(0,0.005)
plt.ylabel('Normalized Flux from M[4.5]')
plt.xlabel('Slice Number')
plt.show()

combined4=[]
comb4=[]
Nextra=((len(xplanet)/2))
for i in range(len(xpoints4)):
    summation4=0
    for j in range(Nextra):
        if i+j<len(xpoints4):
            summation4+=yplanet4[i+j]
        else:
            difference4=(i+j)-len(xpoints4)
            summation4+=yplanet[difference4]
            #print i,j,difference
    combined4.append((summation4/normalisation4))
    comb4.append(summation4/((len(xpoints))/2))
    
long=[0,30,60,90,120,150,180,210,240,270,300,330,360]
new4x=[]
a=360/len(xpoints4)
for i in range(len(xpoints4)):
    
    new4x.append((xpoints4[i]*a)-a)
    
plt.scatter(new4x,comb4)
plt.ylim(0,0.005)
plt.xlabel('Longitude')
plt.ylabel('Combined Flux in M[4.5]')
plt.show()


M45=[]
diff=[]

for i in range(len(comb4)):
    M45.append(3.892-(2.5*np.log10(comb4[i])))



plt.scatter(new4x,M45)
plt.xlabel('Longitude')
plt.ylabel('Combined Magnitude in M[4.5]')
plt.gca().invert_yaxis()
plt.show()

colmag=[]

for i in range(len(M36)):
    colmag.append(M36[i]-M45[i])
    
plt.scatter(colmag,M36,s=2)
plt.xlabel('Colour Index')
plt.ylabel('ABSOLUTE MAG 3.6')
plt.ylim((8,20))
plt.xlim((0,3))
plt.gca().invert_yaxis()
plt.show()

#plt.scatter(colmag,M45,s=2)
#plt.xlabel('Colour Index')
#plt.ylabel('ABSOLUTE MAG 4.5')
#plt.ylim((8,20))
#plt.xlim((0,3))
#plt.gca().invert_yaxis()
#plt.show()
#
#print 'M36', M36
#print 'M45', M45

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


#plt.scatter(colour,y,label='Polynomial')
#plt.scatter(colour1,Y,label='Data')
#plt.xlabel('colour')
#plt.ylabel('Absolute Magnitude M3.6')
#plt.legend()
#plt.gca().invert_yaxis()
#plt.show()
#
#plt.scatter(colour,y1,label='Data')
#plt.scatter(colour1,Y1,label='Polynomial')
#plt.xlabel('colour')
#plt.ylabel('Absolute Magnitude M4.5')
#plt.legend()
#plt.gca().invert_yaxis()
#plt.show()

###########################################

plt.scatter(colmag,M36)
plt.scatter(colour,y,label='Polynomial',s=2)
plt.xlabel('Colour Index')
plt.ylabel('ABSOLUTE MAG 3.6')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.show()

plt.scatter(colmag,M45)
plt.scatter(colour,y1,label='Polynomial',s=2)
plt.xlabel('Colour Index')
plt.ylabel('ABSOLUTE MAG 4.5')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.show()

#####################################
brightM36=[]
for i in range(len(M36)):
    brightM36.append(M36[i]-1.5)
    
brightM45=[]
for i in range(len(M45)):
    brightM45.append(M45[i]-1.5)
    
    
plt.scatter(colmag,brightM36)
plt.scatter(colour,y,label='Polynomial',s=2)
plt.xlabel('Colour Index')
plt.ylabel('ABSOLUTE MAG 3.6')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.show()

plt.scatter(colmag,brightM45)
plt.scatter(colour,y1,label='Polynomial',s=2)
plt.xlabel('Colour Index')
plt.ylabel('ABSOLUTE MAG 4.5')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.show()