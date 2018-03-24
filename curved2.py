#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:42:10 2018

@author: bettyallison
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:59:00 2018

@author: bettyallison
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:56:44 2018

@author: bettyallison
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:32:21 2018

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

input4=np.genfromtxt('HeatherCh1.txt', names=True, dtype=None, delimiter=' ')




input3=np.genfromtxt('HeatherCh2.txt', names=True, dtype=None, delimiter=' ')

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05


#xplanet=[29,29,29,29,29,29,29,29,29,29,16,16,16,16,16,16,16,16,14,14,14,14,11,11,11,8,8,8,11,11,16,16,18,18,18,18,18,18,18,18]

#xplanet=[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,18,18,18,18,18,18,18,18,18,18,14,14,13,13,10,10,13,13,16,16,18,18,18,18,18,18,19,19,19,19,19,19,29,29,29,29,29,29,29,29] #legit keep this
#xplanet=[27,27,27,27,27,27,27,27,27,27,27,27,27,16,16,16,16,16,16,16,12,10,9,9,11,13,13,13,14,14,14,14,14,24,24,24,24,24,24,24]
#xplanet=[9,9,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29]
#xplanet=[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,24,24,24,24] #NEEW FAV

#xplanet=[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,24,24,24,24] #

#xplanet=[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,24,24,24,24,24]

xplanet=[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,24,24,24,24]
print len(xplanet)




y2=[]
yplanet=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet.append(10**(-0.4*((y2[i])-3.921)))
 
print yplanet    
'''
#yplanet=[0.00002,0.00003,0.00008,0.00012,0.00018,0.00026,0.00035,0.00044,0.00055,0.00066,0.00077,0.0009,0.00106,0.00125,0.00147,0.00175,0.0021,0.00257,0.00315,0.0039]
yplanet=[0.0000,0.00005,0.00005,0.0001,0.00015,0.0002,0.0002,0.0003,0.0004,0.0005,0.0007,0.0009,0.001,0.0015,0.002,0.0025,0.0025,0.0025,0.0015,0.001,0.001,0.001,0.0008,0.0008,0.0006]
#0.0008,0.0006,0.0004,0.0002,0
#the ideal 3.6 model
print len(yplanet)
xplanet=np.linspace(1,len(yplanet),len(yplanet))
'''
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
enable_darkening=True
fraction=10
################DO NOT REMOTE THESE LINES:
Nextra_halved=Nextra/2.
if fraction<Nextra_halved:
    raise TypeError("Fraction is smaller than half of Nextra. This is physically impossible.")
################
for i in range(len(xpoints)):
    summation2=0
    for j in range(Nextra):
        separation=np.abs(j-Nextra_halved)
        if i+j<len(xpoints):
            summation=yplanet[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation=yplanet[difference]
        if separation != 0 and enable_darkening==True: summation2+=summation*(np.abs(fraction-separation)/fraction)
        else: summation2+=summation
    combined.append((summation2/normalisation))
    comb.append(summation2/(len(xplanet)/2))
    

newx=[]
a=360./len(xpoints)
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




#xplanet1=[28,28,28,28,27,27,27,27,26,26,26,26,24,24,24,24,23,23,23,23,21,21,21,21,20,20,20,20,20,20,18,18,18,18,18,18,17,17,17,17,15,15,15,14,14,14,14,14,14,15,15,15,15,15,15,15,17,17,17,17] #Legit keep this

#xplanet1=[28,28,27,27,26,26,24,24,23,23,21,21,20,20,20,20,18,18,18,17,17,15,14,14,14,15,15,15,17,17]
#xplanet1=[23,23,22,22,21,21,19,19,18,18,16,16,15,15,15,13,13,13,12,12,10,10,9,9,9,10,10,10,12,12]

#xplanet1=[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]#NEW FAV

xplanet1=[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,15,15,15,15,15,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
#xplanet1=[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5,11.5]

print len(xplanet1)

#xplanet1=[9,9,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29]

y1=[]
yplanet1=[]

for i in range(len(xplanet1)):
    y1.append((c0*xplanet1[i]**0)+(c1*xplanet1[i]**1)+(c2*xplanet1[i]**2)+(c3*xplanet1[i]**3)+(c4*xplanet1[i]**4))
    
    yplanet1.append(10**(-0.4*((y1[i])-3.921)))
 
    


'''
yplanet1=[0,0.0001,0.0002,0.0002,0.0003,0.0004,0.0004,0.0005,0.0006,0.0006,0.0007,0.0007,0.0008,0.0008,0.0008,0.0015,0.0015,0.002,0.002,0.0020,0.0025,0.002,0.002,0.0015,0.00015]
print len(yplanet1)

xplanet=np.linspace(1,len(yplanet),len(yplanet))
'''
normalisation4=np.sum(yplanet1)
print normalisation4
xpoints4=np.linspace(1,len(xplanet),num=len(xplanet))
plt.scatter(xpoints4,yplanet1)
plt.ylim(0,0.005)
plt.ylabel('Normalized Flux from M[4.5]')
plt.xlabel('Slice Number')
plt.show()

'''
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

'''
combined4=[]
comb4=[]
Nextra=((len(xplanet)/2))
enable_darkening=True
fraction=10
################DO NOT REMOTE THESE LINES:
Nextra_halved=Nextra/2.
if fraction<Nextra_halved:
    raise TypeError("Fraction is smaller than half of Nextra. This is physically impossible.")
################
for i in range(len(xpoints)):
    summation2=0
    for j in range(Nextra):
        separation=np.abs(j-Nextra_halved)
        if i+j<len(xpoints):
            summation=yplanet1[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation=yplanet1[difference]
        if separation != 0 and enable_darkening==True: summation2+=summation*(np.abs(fraction-separation)/fraction)
        else: summation2+=summation
    combined4.append((summation2/normalisation4))
    comb4.append(summation2/(len(xplanet)/2))

long=[0,30,60,90,120,150,180,210,240,270,300,330,360]
new4x=[]
a=360/len(xpoints)
for i in range(len(xpoints)):
    
    new4x.append((xpoints[i]*a)-a)
    
plt.scatter(new4x,comb4)
plt.ylim(0,0.005)
plt.xlabel('Longitude')
plt.ylabel('Combined Flux in M[4.5]')
plt.show()

plt.scatter(newx,comb,label='M36')
plt.scatter(new4x,comb4,label='M45')
plt.ylim(0,0.0015)
plt.xlabel('Longitude')
plt.ylabel('Combined Flux')
plt.legend()
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

color36= [(str(item/max(M36))) for item in M36]
color45= [(str(item/max(M45))) for item in M45]


plt.scatter(colour,y,label='Polynomial',s=0.2,c='r')
plt.scatter(colmag,M36,s=40,c=color36,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 3.6 microns')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.legend()
plt.savefig('planetHR1HOPE.pdf')
plt.show()

plt.scatter(colour,y1,label='Polynomial',s=0.2,c='r')
plt.scatter(colmag,M45,s=40,c=color45,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 4.5 microns')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.legend()
plt.savefig('planetHR2HOPE.pdf')
plt.show()

print 'M45', M45
print 'M36', M36
print colmag

print min(M45)
print max(M45)
print max(M36)
print min(M36)

xplanetf=[]
for i in range(len(xplanet)):
    xplanetf.append(xplanet[i]-xplanet1[i])
print xplanetf
    