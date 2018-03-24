#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:22:43 2017

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created
from colour import Color

input1=np.genfromtxt('final_unbinned_ch2_phot.txt', names=True, dtype=None)

#list1=input1['RelativeFlux']
#    
#print np.min(list1)
#
##2455189.056386 this is the centre point
#
input2=np.genfromtxt('final_unbinned_ch1_phot.txt', names=True, dtype=None)

periodCh1=[]
for i in range(len(input2['BJD'])):
    periodCh1.append((input2['BJD'][i]-2455559.568294))

fluxCh1=[]
for i in range(len(input2['BJD'])):
    fluxCh1.append((0.000932*periodCh1[i])+((-1*0.000573)*(periodCh1[i]**2)))

#plt.scatter(period2,flux2)
#plt.show()

#plt.scatter(period2,input2['RelativeFlux'],s=0.5)
#
#plt.ylabel('Absolute Normalised Flux in 3.6')
#plt.show()

fluxyCh1=[]
for i in range(len(periodCh1)):
    fluxyCh1.append(((input2['RelativeFlux'])[i])-fluxCh1[i])

#plt.scatter(periodCh1,fluxyCh1)
#plt.ylim(0.96,1.015)
#plt.show()



###############################################################################
Nextra=1000
binvaluesyCh1=[]
valuesyCh1=[]

summation=0
for i in range(len(fluxyCh1)):
    valuesyCh1.append(fluxyCh1[i])
    summation+=valuesyCh1[i]
    if i%Nextra == 0:
        binvaluesyCh1.append(summation/Nextra)
        summation=0
        
Nextra=1000
binvaluesxCh1=[]
valuesxCh1=[]

summation=0
for i in range(len(fluxyCh1)):
    valuesxCh1.append(periodCh1[i])
    summation+=valuesxCh1[i]
    if i%Nextra == 0:
        binvaluesxCh1.append(summation/Nextra)
        summation=0
        

plt.scatter(binvaluesxCh1,binvaluesyCh1,s=0.5)
#plt.plot(x1,y=1,c='g')
#plt.xlim(0,12500)
plt.ylim(0.975,1.0015)
plt.ylabel('Relative Flux in 3.6')
plt.xlabel('Orbital Period')
plt.savefig('Heatherultered.pdf')
plt.show()

newyCh1=[]
newxCh1=[]
for i in range(len(binvaluesxCh1)):
    newyCh1.append((binvaluesyCh1[i]-0.99905-0.0005))
    newxCh1.append(((binvaluesxCh1[i]-(10/180)-0.1)))
plt.scatter(newxCh1,newyCh1,s=0.2)
plt.ylim(0,0.007)
plt.xlim(0,(360/180))


newxxCh1=[]
for i in range(len(newxCh1)):
    newxxCh1.append(newxCh1[i]+(400/180)+0.225)
    
#plt.scatter(newx,newy)
#plt.ylim(0,0.007)
#plt.xlim(-250,0)
#plt.show() 

plt.scatter(newxxCh1,newyCh1,s=0.2)
plt.ylim(0,0.007)
plt.xlim(0,360/180)
plt.show()   


print len(newyCh1)
output = open('HeatherCh1.txt', 'w')
output.write('Phase'+' '+'Flux'+'\n')

#save titles for text file
for i in range(len(newxxCh1)):
    if (0 <= newxxCh1[i] <= 2) and (0 <= newyCh1[i] <= 0.007):
        output.write(str(newxxCh1[i])+' '+ str(newyCh1[i])+ '\n')

for i in range(len(newxCh1)):
    if (0 <= newxCh1[i] <= 2) and (0 <= newyCh1[i] <= 0.007):
        output.write(str(newxCh1[i])+' '+ str(newyCh1[i])+ '\n')

    
output.close()
print 'Hello'
print len(newxCh1)
'''
input4=np.genfromtxt('HeatherCh1.txt', names=True, dtype=None, delimiter=' ')




input3=np.genfromtxt('HeatherCh2.txt', names=True, dtype=None, delimiter=' ')

print len(input3['Flux'])

print len(input4['Flux'])


Nbins=100


bin_size=(np.max(input3['Phase'])-np.min(input3['Phase']))/Nbins
phase_values3=[]
flux_values3=np.linspace(0,0,num=Nbins)
for i in range(Nbins):
    phase_values3.append(bin_size*i)
    
counter=0.
for i in range(0,Nbins-1):
    #print i
    if i == Nbins: break
    for j in range(len(input3['Flux'])):
        if phase_values3[i] <= input3['Phase'][j] < phase_values3[i+1]:
            flux_values3[i]+=input3['Flux'][j]
            counter+=1
    if counter != 0: flux_values3[i]=flux_values3[i]/counter
    elif counter == 0: flux_values3[i]=-99
    counter=0.
xdegrees=[]
for i in range(len(phase_values3)):
    xdegrees.append((phase_values3[i]*180.0)/360)

plt.scatter(xdegrees,flux_values3,s=2)
plt.ylim(0,0.0015)
plt.ylabel('Ratio of Flux Planet/Flux Star in 4.5 microns')
plt.xlabel('Orbital Phase')
plt.savefig('minitransit.pdf')
plt.show()
    
phase_values4=[]
flux_values4=np.linspace(0,0,num=Nbins)
for i in range(Nbins):
    phase_values4.append(bin_size*i)
    
counter=0.
for i in range(0,Nbins-1):
    #print i
    if i == Nbins: break
    for j in range(len(input4['Flux'])):
        if phase_values4[i] <= input4['Phase'][j] < phase_values4[i+1]:
            flux_values4[i]+=input4['Flux'][j]
            counter+=1
    if counter != 0: flux_values4[i]=flux_values4[i]/counter
    elif counter == 0: flux_values4[i]=-99
    counter=0.
    
plt.scatter(phase_values4,flux_values4,s=2)
plt.ylim(0,0.0015)
plt.ylabel('Flux of Planet in 3.6 microns')
plt.xlabel('Period in 2*Pi Radians')
plt.show()

phase_values5=[]
for i in range(len(phase_values4)):
    phase_values5.append(phase_values4[i]/2)
    
plt.scatter(phase_values5,flux_values4,s=2)
plt.scatter(xdegrees,flux_values3,s=2)
plt.ylim(0,0.0015)
plt.show()
#print 'F36 ',flux_values4
#print 'F45 ',flux_values3
 

    
colourflux=[]
fluxY3=[]
M36=[]
col1=[]

for i in range(len(flux_values3)):
    if flux_values3[i]==-99 or flux_values4[i]==-99: pass
    else:
        colourflux.append(flux_values4[i]-flux_values3[i])
        fluxY3.append(flux_values3[i])
        col1.append(phase_values3[i])


       
colourflux2=[]
fluxY4=[]
col=[]
M45=[]

fluxval4 = [x for _,x in sorted(zip(phase_values4,flux_values4))]
fluxval3 = [x for _,x in sorted(zip(phase_values3,flux_values3))]

for i in range(len(flux_values3)):
    if fluxval3[i]==-99 or fluxval4[i]==-99: pass
    else:
        colourflux2.append(fluxval4[i]-fluxval3[i])
        fluxY4.append(fluxval4[i])
        col.append(phase_values3[i])
        

      
for i in range(len(fluxY3)):
    M36.append(3.921-(2.5*np.log10(fluxY4[i])))
    M45.append(3.892-(2.5*np.log10(fluxY3[i])))
for i in range(len(flux_values3)):
    for j in range(len(input4['Flux'])):
        if input4['Phase'][j]==input3['Phase'][i]:
            colourflux.append(input4['Flux'][j]-input3['Flux'][i])
            #fluxY.append(input4['Flux'][j])
#
#plt.scatter(colourflux,fluxY3=col,cmap='gray')
#plt.xlim(np.min(colourflux),np.max(colourflux))
#plt.ylim(np.min(fluxY3),np.max(fluxY3)+0.001)
#plt.show()  
#
#plt.scatter(colourflux2,fluxY4,c=col1,cmap='gray')
###plt.gray()
#plt.xlim(np.min(colourflux2),np.max(colourflux2))
#plt.ylim(np.min(fluxY4),np.max(fluxY4)+0.001)
##
#plt.show() 

colmag=[]
for i in range(len(M45)):
    colmag.append(M36[i]-M45[i])
t=[]
ds=1./len(M36)
for i in range(len(M36)):
    t.append(phase_values4)
    s=str(Color("blue", saturation=ds*i).hex)
    if len(s)==4:
        s="#000"+s[1]+s[2]+s[3]
    plt.scatter(colmag[i],M36[i],c=s,s=2)

#plt.scatter(colmag,M36)
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 3.6 micorns')
plt.gca().invert_yaxis()
plt.ylim(19,7)
plt.xlim(-1,3)
plt.show()

           
plt.scatter(colmag,M45,s=2)
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 4.5 microns')
plt.gca().invert_yaxis()
plt.ylim(19,7)
plt.xlim(-1,3)
plt.savefig('HR45.pdf')
plt.show()

plt.scatter(colmag,M36,s=2)
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 3.6 microns')
plt.gca().invert_yaxis()
plt.ylim(19,7)
plt.xlim(-1,3)
plt.savefig('HR36.pdf')
plt.show()


#############################################
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

#
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




plt.scatter(colmag,M36,s=2,label='Knutson et al. HD 189733b')
plt.scatter(colour,y,s=2,label='Dupuy and Liu Polynomial')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 3.6 microns')
plt.gca().invert_yaxis()
plt.legend()
plt.ylim(19,7)
plt.xlim(-1,3)
plt.savefig('HRplus36.pdf')
plt.show()

plt.scatter(colmag,M45,s=2,label='Knutson et al. HD 189733b')
plt.scatter(colour,y1,s=2,label='Dupuy and Liu Polynomial')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 4.5 microns')
plt.gca().invert_yaxis()
plt.legend()
plt.ylim(19,7)
plt.xlim(-1,3)
plt.savefig('HRplus45.pdf')
plt.show()


print 'M45', M45
print 'M36', M36
print 'colmag', colmag

print min(M45)
print max(M45)
print max(M36)
print min(M36)

print len(M45)
print len(M36)

output = open('ReducedPoints.txt', 'w')
output.write('M36'+' '+'M45'+' '+'Col'+'\n')


for i in range(len(M36)):
    output.write(str(M36[i])+' '+ str(M45[i])+' '+str((M36[i]-M45[i]))+' '+'\n')

output.close()
'''
