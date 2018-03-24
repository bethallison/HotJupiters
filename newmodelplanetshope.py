#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:32:21 2018

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

#xplanet=[28,28,28,28,28,28,28,24.5,24.5,24.5,24.5,24.5,24.5,24.5,19.5,19.5,13,13,13,13,13,19.5,19.5]

#xplanet=[30,30,30,30,30,30,30,30,30,30,26,26,26,26,26,26,26,26,26,26,18,18,18,18,14,14,14,14,14,14,14,14,18,18,18]

#xplanet.reverse()
#xplanet=[30,30,30,30,30,26,26,26,26,26,26,18,18,14,14,14,14,14,18,18,18]

#xplanet=[28.4,28.4,28.4,28.4,28.4,24.8,24.8,24.8,24.8,24.8,17.6,17.6,14,14,14,14,14,17.6,17.6,17.6]

#xplanet=[34.5931407427,25.8368491427,30.0241739903,28.1349879366,21.3644141725,18.6126196243,23.8523887641,36.7007703007,16.7673653217,30.6138991248,22.470661447,33.3874718386,17.1484595857,43.3307976053,17.1909593081,53.8451713862,29.7847674399,43.3687483237,16.3996937136,40.0900713692,11.3555363105,24.4279427843,23.1275422961,30.1584816121,5.52509474009,-4.35570690375,34.8973028814,26.8733079591,9.26095178772,19.8997985727,-5.81599112691,15.6255039895,31.3838739055,21.1331242305,29.4025558597]

#xplanet=[23.1263883698,22.5159843308,22.7893802563,23.028460096,23.1559827572,22.0609209613,22.5723705806,23.339411259,22.9781587339,23.1647261327,22.5299020218,23.0715279302,23.2718326845,22.857249479,23.3086910694,22.565466398,19.2273093549,17.2140879322,17.315658475,17.1796871336,18.3658734178,18.8057207674,17.5577795206,16.2856941196,16.6410266835,17.4182382368,18.0619412638,18.537567353,17.2083141008,17.9482085013,18.4553592178,18.3143426623,17.6368002657,17.0903383945,22.1418117285]        
        
        
#xplanet=[17.8567499072,16.4263207229,17.420103141,18.9006732521,17.8727390494,17.5767283152,17.6909077794,17.7289373726,17.2033394091,17.7120493849,18.4449325034,17.4484944931,17.6482253122,17.1032131331,17.5624125744,18.5785524257,18.5690362979,16.9399169438,16.7608920365,18.6708253268,18.2087175124,17.9075429892,18.9091461873,18.7483275367,18.2250124321,18.1811269512,18.5099944253,18.018400464,17.9710359739,17.660063385,17.2865681139,17.3029307859,18.8413401555,17.7822924156,17.5869494112]
   
xplanet=[29,29,28,28,27,27,26,26,24,18,16,15,14,14,13,12,14,14,18,20,21,22,22,24,24,24]

   
print len(xplanet)




y2=[]
yplanet=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet.append(10**(-0.4*((y2[i])-3.921)))
 
    


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

y1=[]
yplanet1=[]
xplanet1=[29,28,27,27,26,24,24,23,22,21,20,19,19,17,17,16,16,15,15,14,14,13,15,16,16,18]
print len(xplanet1)
for i in range(len(xplanet1)):
    y1.append((c0*xplanet1[i]**0)+(c1*xplanet1[i]**1)+(c2*xplanet1[i]**2)+(c3*xplanet1[i]**3)+(c4*xplanet1[i]**4))
    
    yplanet1.append(10**(-0.4*((y1[i])-3.921)))
 
    



normalisation4=np.sum(yplanet1)
print normalisation4
xpoints4=np.linspace(1,len(xplanet),num=len(xplanet))
plt.scatter(xpoints4,yplanet1)
plt.ylim(0,0.005)
plt.ylabel('Normalized Flux from M[4.5]')
plt.xlabel('Slice Number')
plt.show()

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