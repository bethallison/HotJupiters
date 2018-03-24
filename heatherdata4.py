#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:20:36 2017

@author: bettyallison
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:22:43 2017

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

input1=np.genfromtxt('final_unbinned_ch2_phot.txt', names=True, dtype=None)

#list1=input1['RelativeFlux']
#    
#print np.min(list1)
#
##2455189.056386 this is the centre point
#
#input2=np.genfromtxt('final_unbinned_ch1_phot.txt', names=True, dtype=None)

period1=[]
for i in range(len(input1['BJD'])):
    period1.append((input1['BJD'][i]-2455189.056386))

flux1=[]
for i in range(len(input1['BJD'])):
    flux1.append((-1*0.000731)*(period1[i]))

#plt.scatter(period1,flux1)
#plt.show()
#
#plt.scatter(period1,input1['RelativeFlux'],s=0.5)
#
#plt.ylabel('Absolute Normalised Flux in 3.6')
#plt.show()

fluxy1=[]
for i in range(len(period1)):
    fluxy1.append((((input1['RelativeFlux'])[i])-flux1[i]))

#plt.scatter(period1,fluxy1)
#plt.show()



###############################################################################
Nextra=1000
binvaluesy1=[]
valuesy1=[]

summation=0
for i in range(len(fluxy1)):
    valuesy1.append(fluxy1[i])
    summation+=valuesy1[i]
    if i%Nextra == 0:
        binvaluesy1.append(summation/Nextra)
        summation=0
        
Nextra=1000
binvaluesx1=[]
valuesx1=[]

summation=0
for i in range(len(fluxy1)):
    valuesx1.append(period1[i])
    summation+=valuesx1[i]
    if i%Nextra == 0:
        binvaluesx1.append(summation/Nextra)
        summation=0
        

plt.scatter(binvaluesx1,binvaluesy1,s=0.5)
#plt.plot(x1,y=1,c='g')
#plt.xlim(0,12500)
plt.ylim(0.975,1.001)
plt.ylabel('Absolute Normalised Flux in 4.5')
plt.xlabel('Arbitrary Orbital Phase')
plt.show()

#ynew=[]
#xnew=[]
#
#for i in range(len(binvaluesx1)):
#    if binvaluesy1[i] < 0.0002:
#        ynew.append(binvaluesy1[i])
#        #xnew.append(binvaluesx1[i])
#xnew=np.linspace(0,len(ynew),num=len(ynew))
#plt.scatter(xnew,ynew)
'''
newy=[]   
newx=[]     
for i in range(len(binvaluesy1)):
    newy.append((binvaluesy1[i]-0.999-0.0002))
    newx.append(((binvaluesx1[i]-(10/180)-0.1)))

plt.scatter(newx,newy,s=0.2)
plt.ylim(0,0.007)
plt.xlim(0,360/180)


newxx=[]
for i in range(len(newx)):
    newxx.append(newx[i]+(400/180)+0.225)
    
#plt.scatter(newx,newy)
#plt.ylim(0,0.007)
#plt.xlim(-250,0)
#plt.show() 

plt.scatter(newxx,newy,s=0.2)
plt.ylim(0,0.007)
plt.xlim(0,360/180)
plt.show()

output = open('HeatherCh2.txt', 'w')
output.write('Phase'+' '+'Flux'+'\n')

#save titles for text file
for i in range(len(newxx)):
    if (0 <= newxx[i] <= 2) and (0 <= newy[i] <= 0.007):
        output.write(str(newxx[i])+' '+ str(newy[i])+ '\n')

for i in range(len(newx)):
    if (0 <= newx[i] <= 2) and (0 <= newy[i] <= 0.007):
        output.write(str(newx[i])+' '+ str(newy[i])+ '\n')


    
output.close()
print 'Hello'

input3=np.genfromtxt('HeatherCh2.txt', names=True, dtype=None, delimiter=' ')

df=[]
f=[]
B=[]
M=[]
for i in range(len(input3['Flux'])):
    f.append((input3['Flux'][i]))
    M.append((3.892+(2.5*np.log(f[i]))))

plt.scatter(input3['Phase'],M)
plt.show()
#period=[]
#F=[]
#c1=-0.0479
#c2=-0.0389
#c3=0.0025
#c4=-0.0020
#x=np.linspace(0,2,num=1000)
#for i in range(len(x)):
#    F.append((c1*np.cos(((2*np.pi*x[i])/2)+(0.25/np.pi)))+(c2*np.sin(((2*np.pi*x[i])/2)+(0.25/np.pi)))+(c3*np.cos(((4*np.pi*x[i])/2)+(0.25/np.pi)))+(c4*np.sin((((4*np.pi*x[i]))/2)+(0.25/np.pi))))
#    
#
#plt.scatter(x,F)
#
#print len(x)
#print len(F)
##plt.scatter(x,F)
#plt.show()
'''