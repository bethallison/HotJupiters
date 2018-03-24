#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:21:19 2017

@author: bettyallison
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:28:46 2017

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05


xplanet1=[30,30,30,30,30,30,28,28,28,28,27,27,22,22,20,20]

y21=[]
yplanet1=[]

for i in range(len(xplanet1)):
    y21.append((c0*xplanet1[i]**0)+(c1*xplanet1[i]**1)+(c2*xplanet1[i]**2)+(c3*xplanet1[i]**3)+(c4*xplanet1[i]**4))
    
    yplanet1.append(10**(-0.4*((y21[i])-3.921)))
 
    
xplanet2=[16,16,15,15,14,14,13,13,12]
y22=[]
yplanet2=[]

for i in range(len(xplanet2)):
    y22.append((c0*xplanet2[i]**0)+(c1*xplanet2[i]**1)+(c2*xplanet2[i]**2)+(c3*xplanet2[i]**3)+(c4*xplanet2[i]**4))
    
    yplanet2.append(10**(-0.4*((y22[i])-3.921)))


xplanet3=[12,13,13,13,14,14,15,15,16,16]
y23=[]
yplanet3=[]

for i in range(len(xplanet3)):
    y23.append((c0*xplanet3[i]**0)+(c1*xplanet3[i]**1)+(c2*xplanet3[i]**2)+(c3*xplanet3[i]**3)+(c4*xplanet3[i]**4))
    
    yplanet3.append(10**(-0.4*((y23[i])-3.921)))
    

xplanet4=[20,20,22,22,27,27,28,28,28,28,30,30,30,30,30]
y24=[]
yplanet4=[]

for i in range(len(xplanet4)):
    y24.append((c0*xplanet4[i]**0)+(c1*xplanet4[i]**1)+(c2*xplanet4[i]**2)+(c3*xplanet4[i]**3)+(c4*xplanet4[i]**4))
    
    yplanet4.append(10**(-0.4*((y24[i])-3.921-2)))

yplanet=yplanet1+yplanet2+yplanet3+yplanet4
xplanet=xplanet1+xplanet2+xplanet3+xplanet4
print xplanet

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


###############################################################################

c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05


#xplanet1=[28,28,28,28,27,27,22,22,20,20]

y21=[]
yplanet1=[]

for i in range(len(xplanet1)):
    y21.append((c0*xplanet1[i]**0)+(c1*xplanet1[i]**1)+(c2*xplanet1[i]**2)+(c3*xplanet1[i]**3)+(c4*xplanet1[i]**4))
    
    yplanet1.append(10**(-0.4*((y21[i])-3.921)))
 
    
#xplanet2=[16,16,15,15,14,14]
y22=[]
yplanet2=[]

for i in range(len(xplanet2)):
    y22.append((c0*xplanet2[i]**0)+(c1*xplanet2[i]**1)+(c2*xplanet2[i]**2)+(c3*xplanet2[i]**3)+(c4*xplanet2[i]**4))
    
    yplanet2.append(10**(-0.4*((y22[i])-3.921)))


#xplanet3=[14,14,15,15,16,16]
y23=[]
yplanet3=[]

for i in range(len(xplanet3)):
    y23.append((c0*xplanet3[i]**0)+(c1*xplanet3[i]**1)+(c2*xplanet3[i]**2)+(c3*xplanet3[i]**3)+(c4*xplanet3[i]**4))
    
    yplanet3.append(10**(-0.4*((y23[i])-3.921)))
    

#xplanet4=[20,20,22,22,27,27,28,28,28,28]
y24=[]
yplanet4=[]

for i in range(len(xplanet4)):
    y24.append((c0*xplanet4[i]**0)+(c1*xplanet4[i]**1)+(c2*xplanet4[i]**2)+(c3*xplanet4[i]**3)+(c4*xplanet4[i]**4))
    
    yplanet4.append(10**(-0.4*((y24[i])-3.921-2)))

yplanet8=yplanet1+yplanet2+yplanet3+yplanet4
xplanet=xplanet1+xplanet2+xplanet3+xplanet4
print xplanet


normalisation4=np.sum(yplanet8)
print normalisation4
xpoints4=np.linspace(1,len(xplanet),num=len(xplanet))
plt.scatter(xpoints4,yplanet8)
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
            summation4+=yplanet8[i+j]
        else:
            difference4=(i+j)-len(xpoints4)
            summation4+=yplanet8[difference4]
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
    
#plt.scatter(colmag,M36,s=2)
#plt.xlabel('Colour Index')
#plt.ylabel('ABSOLUTE MAG 3.6')
#plt.ylim((8,20))
#plt.xlim((0,3))
#plt.gca().invert_yaxis()
#plt.show()
#
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


plt.scatter(colmag,M36,s=3,label='Model Planet')   

plt.scatter(colour,y,label='Polynomial',s=0.2,c='y')


plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 3.6 microns')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.legend()
plt.savefig('planetHR1HOPE.pdf')
plt.show()

plt.scatter(colour,y1,label='Polynomial',s=0.2,c='y')
plt.scatter(colmag,M45,s=3,label='Model Planet')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 4.5 microns')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.legend()
plt.savefig('planetHR2HOPE.pdf')
plt.show()

print M36
print M45
print colmag


