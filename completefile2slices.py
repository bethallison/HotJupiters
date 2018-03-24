#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:40:12 2018

@author: bettyallison
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:30:52 2018

@author: bettyallison
"""
import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created

input36=np.genfromtxt('HeatherCh1.txt', names=True, dtype=None, delimiter=' ')


c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05





xplanet36=[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,13,13,13,13,13,13,13,13,13,10,10,10,13,13,13,13,13,13,13,13,26,26,26]

xplanet36=[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,13,13,13,13,13,13,13,13,13,8,10,10,13,13,13,13,13,13,13,13,26,26,26]

xplanet36=[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,16,16,16,16,16,15,14,13,12,11,11,11,11,11,11,11,12,13,14,15,16,26,26,26,26] #model 2
xplanet36=[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,13,13,13,13,13,13,13,13,13,10,10,10,13,13,13,13,13,13,13,13,26,26,26]
#xplanet36=[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,16,16,16,16,16,15,14,13,12,11,11,11,11,11,11,11,12,13,14,15,16,24,24,24,24]
xplanet36=[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,26,26,26] 
 #model 2

xplanet36=[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,13,13,13,13,13,13,13,13,13,13,10,10,10,13,13,13,13,13,13,13,13,26,26,26]
xplanet36=[13,13,13,13,13,13,13,13,13,13,13,10,10,10,13,13,13,13,13,13,13,13,13,13,26,26,26,26,26,26,26,26,26,26,26,26,26,13,13,13] #swap around the midpoint
xplanet36=[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,13,13,13,
13,13,13,13,13,13,10,10,10,13,13,13,13,13,13,13,13,26,26,26]
y36=[]
yplanet36=[]

for i in range(len(xplanet36)):
    y36.append((c0*xplanet36[i]**0)+(c1*xplanet36[i]**1)+(c2*xplanet36[i]**2)+(c3*xplanet36[i]**3)+(c4*xplanet36[i]**4))
    
    yplanet36.append(10**(-0.4*((y36[i])-3.921)))
   
normalisation=np.sum(yplanet36)
xpoints=np.linspace(1,len(xplanet36),num=len(xplanet36))

combined36=[]
comb36=[]
Nextra=((len(xplanet36)/2))
enable_darkening=True
fraction=10

Nextra_halved=Nextra/2.
if fraction<Nextra_halved:
    raise TypeError("Fraction is smaller than half of Nextra. This is physically impossible.")
################
for i in range(len(xpoints)):
    summation2=0
    for j in range(Nextra):
        separation=np.abs(j-Nextra_halved)
        if i+j<len(xpoints):
            summation=yplanet36[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation=yplanet36[difference]
        if separation != 0 and enable_darkening==True: summation2+=summation*(np.abs(fraction-separation)/fraction)
        else: summation2+=summation
    combined36.append((summation2/normalisation))
    comb36.append(summation2/(len(xplanet36)/2))
    

newx=[]
a=360./len(xpoints)
for i in range(len(xpoints)):
    
    newx.append((xpoints[i]*a)-a)
    

M36=[]
M45=[]
diff=[]

for i in range(len(comb36)):
    M36.append(3.921-(2.5*np.log10(comb36[i])))


###############################################################################
'''
c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05
'''

xplanet45=[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12] #chi 0.44

    

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



############################################################
colour1=[]
for i in range(len(input1['Spec'])):
    colour1.append(Y[i]-Y1[i])

colour=[]
for i in range(len(x)):
    colour.append(y[i]-y1[i])


###########################################

color36= [(str(item/max(M36))) for item in M36]
color45= [(str(item/max(M45))) for item in M45]


###########################################


#M36
xmax2=300#arr2.shape[1] #Automatically determines x and y values from the array
ymax2=180#arr2.shape[0]
segments2=len(xplanet36) #This is your number of slices
colours=['r','y','b','g','m','c','k']
xlength2=xmax2*1.0/segments2 #Length of each slice

generatedarray=np.zeros(shape=(ymax2,xmax2))

fluxaverage=0
sliceaverage2=[] #This array saves all the averages if you need them later
ylower=0 #These are your Y upper and lower bounds. Change to 0 and ymax if you want the full image.
yupper=180
counter=0

for i in range(int(segments2)): #number of segments
    for x in range(int(xlength2*i),int(xlength2*(i+1))):
        for y in range(ylower,yupper):
            #if counter != 10:
            #    counter+=1
            #else:
            #    counter=0
            try: generatedarray[y,x]=-xplanet36[i]
            except Exception: print x,y,i


###########################################
#Heathers Data            

input36=np.genfromtxt('HeatherCh1.txt', names=True, dtype=None, delimiter=' ')

#input45=np.genfromtxt('HeatherCh2.txt', names=True, dtype=None, delimiter=' ')

Nbins=200


bin_size=(np.max(input36['Phase'])-np.min(input36['Phase']))/Nbins  
phase_values4=[]
flux_values36=np.linspace(0,0,num=Nbins)
for i in range(Nbins):
    phase_values4.append((bin_size*i))

    
counter=0.
for i in range(0,Nbins-1):
    #print i
    if i == Nbins: break
    for j in range(len(input36['Flux'])):
        if phase_values4[i] <= input36['Phase'][j] < phase_values4[i+1]:
            flux_values36[i]+=input36['Flux'][j]
            counter+=1
    if counter != 0: flux_values36[i]=flux_values36[i]/counter
    elif counter == 0: flux_values36[i]=-99
    counter=0.

phase_values5=[]
for i in range(len(phase_values4)):
    phase_values5.append(phase_values4[i]/2)
    


#####################################################

new5x=[]
for i in range(len(newx)):
    new5x.append(newx[i]/360)
    
remove_positions=[]
counter=0
for i in phase_values5:
    if flux_values36[counter]==-99: remove_positions.append(counter)
    elif 0.4<i<0.6:
        if flux_values36[counter] < 0.0008:
            remove_positions.append(counter)
    counter+=1
            
phase_values36_removed=np.delete(phase_values5,remove_positions)
flux_values36_removed=np.delete(flux_values36,remove_positions)

plt.scatter(phase_values36_removed,flux_values36_removed,s=2)
plt.scatter(new5x,comb36,s=2,c='r')
plt.ylim(0,0.002)
plt.show()

#################################################################


from scipy.interpolate import interp1d


interpolation36=interp1d(phase_values36_removed,flux_values36_removed)
print interpolation36
#interpolation45=interp1d(phase_values45_removed,flux_values45_removed)

chi36=[]

#error36=(0.00333/len((input36['Phase']))**0.5)/((len(input36['Phase'])/200))**0.5
error36=0.00333/(985890/40)**0.5


#input36['Phase']

res36=[]
res3=[]
for i in range(len(comb36)):

    distance=np.abs(comb36[i]-interpolation36(new5x[i]))**2
    chi36.append(distance/(error36)**2)


distance236=[]
res236=[]
for i in range(len(chi36)):
    distance36=(comb36[i]-interpolation36(new5x[i]))**2
    res36.append(distance36**0.5)
    distance236.append(comb36[i]-interpolation36(new5x[i]))
    res236.append(distance236[i])

print sum(chi36)
reserr36=[]
for i in range(len(res36)):
    reserr36.append(((2*chi36[i])**0.5)/40)
    
    





x7=np.linspace(0,1,len(res36))


f, axarr = plt.subplots(2, sharex=True,gridspec_kw = {'height_ratios':[3, 1]})
axarr[0].plot(new5x, comb36,label='Model 3.6')
axarr[0].scatter(phase_values36_removed,flux_values36_removed,c='#ff8f66',s=2, label='Knutson Data')
axarr[0].set_title('3.6')
axarr[0].set_ylabel('Combined Flux in 3.6')
axarr[1].scatter(x7, res236,c='#c71585')
axarr[1].axhline(0)
axarr[1].errorbar(x7,res236,yerr=error36,ls='none')
axarr[1].set_title('Residulals')
axarr[1].set_ylim(-0.00005,0.00005)
axarr[1].set_xlabel('Longitude')
plt.savefig('modelextra.pdf')
plt.show()

print "3.6 Chi-Squared: ", np.sum(chi36)/len(comb36), "+/-", np.sum(reserr36)


