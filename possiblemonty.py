#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:30:08 2018

@author: bettyallison
"""
import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created
import random as random

KM45=[12.444732956429712, 12.214759814316036, 12.200203755651437, 12.233776632874324, 12.011170259333095, 11.945160481209395, 11.682955627773834, 11.540517694017211, 11.667242633261749, 11.405836029262789, 11.402774149108549, 11.249318312622005, 11.25334517266783, 11.077982824966837, 11.127645258079092, 11.148395711552983, 11.153649245490643, 11.605783078026629, 11.20706648712318, 11.198547895046959, 11.168552237295142, 11.334258115371483, 11.482975258717543, 11.270363340142252, 11.257541286898597, 11.56023312090438, 11.579051025757925, 11.619803597509138, 11.783809535643332, 11.743360963705365, 11.606023627293947, 12.113835052216276, 12.260931800761815, 12.283665416937346, 12.41451522794538]
KM36=[12.929918535055258, 12.869741243111614, 12.707082907864702, 12.373724155377618, 12.091591397879775, 12.057232840632452, 11.921020645551645, 11.712833900718039, 11.482485000286323, 11.518170000150526, 11.331896293417021, 11.192705936207238, 11.12843724097436, 11.055330906368338, 11.07143517416878, 11.14254398755131, 11.292343839078768, 12.858613962005776, 11.491912964805911, 11.303996019385977, 11.452125490596625, 11.515602478961151, 11.635351560924166, 11.971820410752194, 12.132329383113701, 12.434507942466061, 12.783809213312034, 12.657520926303135, 13.272075461416675, 13.717087539604261, 13.442947410399988, 14.094862035056888, 14.976494728047545, 14.367900949262577, 13.621214073833734]

Kcolmag=[0.48518557862554523, 0.65498142879557797, 0.50687915221326563, 0.13994752250329334, 0.080421138546679316, 0.11207235942305616, 0.23806501777781008, 0.17231620670082748, -0.18475763297542613, 0.11233397088773778, -0.070877855691527714, -0.05661237641476724, -0.12490793169346937, -0.022651918598498355, -0.056210083910311681, -0.0058517240016726646, 0.13869459358812541, 1.2528308839791471, 0.28484647768273064, 0.10544812433901818, 0.28357325330148342, 0.18134436358966788, 0.15237630220662268, 0.70145707060994233, 0.87478809621510401, 0.87427482156168068, 1.2047581875541091, 1.0377173287939971, 1.4882659257733426, 1.9737265758988958, 1.836923783106041, 1.9810269828406124, 2.7155629272857293, 2.0842355323252306, 1.2066988458883543]


M45=[13.4080109586275, 13.318060560680593, 13.234995519265192, 13.157836277111299, 12.914242737418542, 12.715411506223878, 12.547417740909765, 12.401968017383384, 12.164518198978971, 11.969793848018398, 11.804739026837716, 11.680432732618124, 11.568907515453507, 11.467778414746094, 11.375271424290382, 11.290031133784829, 11.255049022804865, 11.221158932392289, 11.188294743147074, 11.200503468809876, 11.212851040093021, 11.259363592022357, 11.307958254625492, 11.358830208406269, 11.41220343410008, 11.524478319366949, 11.649716875663771, 11.791308346616994, 11.954173845607817, 12.116918977064513, 12.308434388674087, 12.541123876282686, 12.837680504837245, 12.996655208743361, 13.182967069247542]
M36=[14.644850054299175, 14.516707823375686, 14.402105402268608, 14.298452968991542, 13.689168852827708, 13.301239090080132, 13.016017495333069, 12.790348972410092, 12.454148823190938, 12.197809364689912, 11.99058017208805, 11.82673524346489, 11.684404428256117, 11.558587973885647, 11.445848960942122, 11.34372298279313, 11.297464558679224, 11.25309672621581, 11.210470996557746, 11.216238317116067, 11.222036436770507, 11.271193745978199, 11.322682661551369, 11.376735428207228, 11.433620817631496, 11.552886406657196, 11.686888444645092, 11.839788868546822, 12.017807275870057, 12.216226877036394, 12.459202014640699, 12.772716702108605, 13.215284316907345, 13.51896833282381, 13.942075467670815]


print len(M45)
print len(KM45)
print len(M36)
print len(KM36)

chiM36=[]
for i in range(len(M36)):
    chiM36.append(np.sum((M36[i]-KM36[i])**2))


chiM45=[]
for i in range(len(M45)):
    chiM45.append(np.sum((M45[i]-KM45[i])**2))

###############################################################################

#N=len(input1['DATA'])

#this code is the same as the code above but is over velocity and sigma. 
#def function(vel,sig):
#    if (9695 > vel > 9705) or (0 > sig > 3): return 0
#    else: return ((1./(sig*(2*np.pi)**0.5))**N)*(np.exp(-0.5*(np.sum((vel-input1['DATA'])**2))/sig**2))

def function(xplanet):
    
    for i in range(len(xplanet)):
        if xplanet[i]>30 or xplanet[i]<6: return 0

    N=len(xplanet)
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
    enable_darkening=True
    fraction=15
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
                if separation != 0 and enable_darkening==True:      summation2+=summation*(np.abs(fraction-separation)/fraction)
                else: summation2+=summation
                combined.append((summation2/normalisation))
                comb.append(summation2/(len(xplanet)/2))
        
    
        
    
    M36=[]
    M45=[]
    
    
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
    xpoints=np.linspace(1,len(xplanet),num=len(xplanet))
    
    
    combined4=[]
    comb4=[]
    Nextra=((len(xplanet)/2))
    enable_darkening=True
    fraction=15
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
                if separation != 0 and enable_darkening==True:          summation2+=summation*(np.abs(fraction-separation)/fraction)
                else: summation2+=summation
                combined4.append((summation2/normalisation4))
                comb4.append(summation2/(len(xplanet)/2))
    
    M45=[]
    
    
    for i in range(len(comb4)):
        M45.append(3.892-(2.5*np.log10(comb4[i])))
    
    
    colmag=[]
    
    for i in range(len(M36)):
        colmag.append(M36[i]-M45[i])
    
    chiM36=[]
    for i in range(len(M36)):
        chiM36.append(np.sum((M36[i]-KM36[i])**2))


    chiM45=[]
    for i in range(len(M45)):
        chiM45.append(np.sum((M45[i]-KM45[i])**2))
    
    chicolmag=[]
    for i in range(len(M45)):
        chicolmag.append(np.sum((colmag[i]-Kcolmag[i])**2))        
    
    return (((1/(2*np.pi)**0.5))**N)*((np.exp(-0.5*(np.sum((chiM45[i])**2)))))

Tburn=int(1e5)
T= int(1e5)
xplanet_old=[28,28,28,28,28,28,28,28,28,28,28,26,26,26,26,26,26,26,26,26,18,18,18,18,14,14,14,14,14,14,14,14,18,18,18]
correct=0.0
dx=0.5
probability=function(xplanet_old)

for i in range(Tburn):
    xplanet=[]
    for j in range(len(xplanet_old)):
        xplanet.append(xplanet_old[j]+(random.uniform(-1,1)*dx))
    
    probability_maybe = function(xplanet)
    if probability_maybe > probability:
        probability = probability_maybe
        xplanet_old = xplanet
        correct=correct+1
    elif probability_maybe < probability:
        value1=probability_maybe/probability
        value2=random.uniform(0,1)
        if value2 < value1:
            probability = probability_maybe
            xplanet_old = xplanet
            correct=correct+1
            
    if i%50==0:
        correct2=correct/50
        if correct2 > 0.25:
            dx=dx + 0.02
        elif correct2 < 0.25:
            dx=dx - 0.02
            
        correct=0.0
            
print dx, correct2 
###

#samplesV=[]
#samplesS=[]
x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
x7=[]
x8=[]
x9=[]
x10=[]
x11=[]
x12=[]
x13=[]
x14=[]
x15=[]
x16=[]
x17=[]
x18=[]
x19=[]
x20=[]
x21=[]
x22=[]
x23=[]
x24=[]
x25=[]
x26=[]
x27=[]
x28=[]
x29=[]
x30=[]
x31=[]
x32=[]
x33=[]
x34=[]
x35=[]

for i in range(T):
    xplanet=[]
    for j in range(len(xplanet_old)):
        xplanet.append(xplanet_old[j]+(random.uniform(-1,1)*dx))
    
    probability_maybe = function(xplanet)
    if probability_maybe > probability:
        probability = probability_maybe
        xplanet_old = xplanet
        correct=correct+1
    elif probability_maybe < probability:
        value1=probability_maybe/probability
        value2=random.uniform(0,1)
        if value2 < value1:
            probability = probability_maybe
            xplanet_old = xplanet
            correct=correct+1
    x1.append(xplanet_old[0])
    x2.append(xplanet_old[1])
    x3.append(xplanet_old[2])
    x4.append(xplanet_old[3])
    x5.append(xplanet_old[4])
    x6.append(xplanet_old[5])
    x7.append(xplanet_old[6])
    x8.append(xplanet_old[7])
    x9.append(xplanet_old[8])
    x10.append(xplanet_old[9])
    x11.append(xplanet_old[10])
    x12.append(xplanet_old[11])
    x13.append(xplanet_old[12])
    x14.append(xplanet_old[13])
    x15.append(xplanet_old[14])
    x16.append(xplanet_old[15])
    x17.append(xplanet_old[16])
    x18.append(xplanet_old[17])
    x19.append(xplanet_old[18])
    x20.append(xplanet_old[19])
    x21.append(xplanet_old[20])
    x22.append(xplanet_old[21])
    x23.append(xplanet_old[22])
    x24.append(xplanet_old[23])
    x25.append(xplanet_old[24])
    x26.append(xplanet_old[25])
    x27.append(xplanet_old[26])
    x28.append(xplanet_old[27])
    x29.append(xplanet_old[28])
    x30.append(xplanet_old[29])
    x31.append(xplanet_old[30])
    x32.append(xplanet_old[31])
    x33.append(xplanet_old[32])
    x34.append(xplanet_old[33])
    x35.append(xplanet_old[34])
    
'''            
for i in range(T):
    vel=vel_old+(random.uniform(-1,1)*dvel)
    sig=sig_old+(random.uniform(-1,1)*dsig)
    probability_maybe = function(vel,sig)
    if probability_maybe > probability:
        probability = probability_maybe
        vel_old = vel
        sig_old = sig
    elif probability_maybe < probability:
        value1=probability_maybe/probability
        value2=random.uniform(0,1)
        if value2 < value1:
            probability = probability_maybe
            vel_old = vel
            sig_old = sig
    samplesV.append(vel_old)
    samplesS.append(sig_old)
''' 

plt.hist(x1,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x1.pdf')
plt.clf()
plt.hist(x2,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x2.pdf')
plt.clf()
plt.hist(x3,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x3.pdf')
plt.clf()
plt.hist(x4,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x4.pdf')
plt.clf()
plt.hist(x5,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x5.pdf')
plt.clf()
plt.hist(x6,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x6.pdf')
plt.clf()
plt.hist(x7,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x7.pdf')
plt.clf()
plt.hist(x8,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x8.pdf')
plt.clf()
plt.hist(x9,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x9.pdf')
plt.clf()
plt.hist(x10,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x10.pdf')
plt.clf()
plt.hist(x11,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x11.pdf')
plt.clf()
plt.hist(x12,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x12.pdf')
plt.clf()
plt.hist(x13,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x13.pdf')
plt.clf()
plt.hist(x14,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x14.pdf')
plt.clf()
plt.hist(x15,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x15.pdf')
plt.clf()
plt.hist(x16,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x16.pdf')
plt.clf()
plt.hist(x17,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x17.pdf')
plt.clf()
plt.hist(x18,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x18.pdf')
plt.clf()
plt.hist(x19,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x19.pdf')
plt.clf()
plt.hist(x20,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x20.pdf')
plt.clf()
plt.hist(x21,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x21.pdf')
plt.clf()
plt.hist(x22,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x22.pdf')
plt.clf()
plt.hist(x23,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x23.pdf')
plt.clf()
plt.hist(x24,bins=50,normed=1)
plt.xlabel('x24')
plt.ylabel('PDF')
plt.savefig('x24.pdf')
plt.clf()
plt.hist(x25,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x25.pdf')
plt.clf()
plt.hist(x26,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x26.pdf')
plt.clf()
plt.hist(x27,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x27.pdf')
plt.clf()
plt.hist(x28,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x28.pdf')
plt.clf()
plt.hist(x29,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x29.pdf')
plt.clf()
plt.hist(x30,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x30.pdf')
plt.clf()
plt.hist(x31,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x31.pdf')
plt.clf()
plt.hist(x32,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x32.pdf')
plt.clf()
plt.hist(x33,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x33.pdf')
plt.clf()
plt.hist(x34,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x34.pdf')
plt.clf()
plt.hist(x35,bins=50,normed=1)
plt.xlabel('x1')
plt.ylabel('PDF')
plt.savefig('x35.pdf')
plt.clf()

#plotting a histogram over velocity 
'''
plt.hist(samplesS,bins=50,normed=1)
plt.xlabel('Sigma m/s')
plt.ylabel('Posterior Probability Density Function')
plt.show()
#plotting a histogram over sigma.
'''
print np.mean(x1)
print np.mean(x2)
print np.mean(x3)
print np.mean(x4)
print np.mean(x5)
print np.mean(x6)
print np.mean(x7)
print np.mean(x8)
print np.mean(x9)
print np.mean(x10)
print np.mean(x11)
print np.mean(x12)
print np.mean(x13)
print np.mean(x14)
print np.mean(x15)
print np.mean(x16)
print np.mean(x17)
print np.mean(x18)
print np.mean(x19)
print np.mean(x20)
print np.mean(x21)
print np.mean(x22)
print np.mean(x23)
print np.mean(x24)
print np.mean(x25)
print np.mean(x26)
print np.mean(x27)
print np.mean(x28)
print np.mean(x29)
print np.mean(x30)
print np.mean(x31)
print np.mean(x32)
print np.mean(x33)
print np.mean(x34)
print np.mean(x35)
