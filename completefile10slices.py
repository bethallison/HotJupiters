#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 19:13:41 2018

@author: bettyallison
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:35:47 2018

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

#square root 2 chi ^2/N
#best 2 bands,then best 3 bands etc....
#chi squared vs number of bands 
#find some lit
#heng and showman atmospheric dynamics of hot exoplanets
#thermal structure of an exoplanet  kevin steevenson 
#temperTURE vs pressure ratios


input45=np.genfromtxt('HeatherCh2.txt', names=True, dtype=None, delimiter=' ')

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05






xplanet36=[12,12,12,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]

xplanet36=[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,26,26,26]
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
fraction=18

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

c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05

#xplanet45=[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,15,15,15,15,15,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
#xplanet45=[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,10,10,10,10,10,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12] #chi 1

#xplanet45=[26,26,26,26,26,26,26,26,26,26,16,16,16,8,8,8,16,16,16,16]

#xplanet45=[22,22,22,22,22,22,22,22,15,15,12,12,12,12,12,12,12,12,12,12,22,22,22,22,22,22,22,22,15,15,12,12,12,12,12,12,12,12,12,12]

xplanet45=[16,16,16,18,18,18,18,18,18,18,18,18,18,18,16,16,16,14,14,14,14,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,14,14,14,14] #chi 0.675

xplanet45=[16,16,16,18,18,18,18,19,19,19,19,18,18,18,16,16,16,14,14,14,14,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,14,14,14,14] #0.65

xplanet45=[16,16,16,18,18,18,18,19,19,19,19,18,18,18,16,16,16,14,14,14,14,12,12,12,12,12,12,10,10,10,12,12,12,12,12,12,14,14,14,14] #bright spot 1.07
xplanet45=[15,15,16,16,17,17,17,18,18,18,18,18,18,18,17,17,16,16,15,15,14,14,14,14,13,13,13,13,12,12,12,12,13,13,13,13,14,14,14,14] #1.48 
         
xplanet45=[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]

xplanet45=[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,26,26,26]
y45=[]
yplanet45=[]

for i in range(len(xplanet45)):
    y45.append((c0*xplanet45[i]**0)+(c1*xplanet45[i]**1)+(c2*xplanet45[i]**2)+(c3*xplanet45[i]**3)+(c4*xplanet45[i]**4))
    
    yplanet45.append(10**(-0.4*((y45[i])-3.921)))

normalisation45=np.sum(yplanet45)

xpoints45=np.linspace(1,len(xplanet45),num=len(xplanet45))


combined45=[]
comb45=[]
Nextra=((len(xplanet45)/2))
enable_darkening=True
fraction=18
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
            summation=yplanet45[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation=yplanet45[difference]
        if separation != 0 and enable_darkening==True: summation2+=summation*(np.abs(fraction-separation)/fraction)
        else: summation2+=summation
    combined45.append((summation2/normalisation45))
    comb45.append(summation2/(len(xplanet45)/2))

long=[0,30,60,90,120,150,180,210,240,270,300,330,360]
new45x=[]
a=360/len(xpoints)
for i in range(len(xpoints)):
    
    new45x.append((xpoints[i]*a)-a)
    
M45=[]
diff=[]

for i in range(len(comb45)):
    M45.append(3.892-(2.5*np.log10(comb45[i])))

colmag=[]

for i in range(len(M36)):
    colmag.append(M36[i]-M45[i])
    

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



#M45
xmax2=300#arr2.shape[1] #Automatically determines x and y values from the array
ymax2=180#arr2.shape[0]
segments2=len(xplanet45) #This is your number of slices
colours=['r','y','b','g','m','c','k']
xlength2=xmax2*1.0/segments2 #Length of each slice

generatedarray2=np.zeros(shape=(ymax2,xmax2))

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
            try: generatedarray2[y,x]=-xplanet45[i]
            except Exception: print x,y,i

###########################################
#Heathers Data            

input36=np.genfromtxt('HeatherCh1.txt', names=True, dtype=None, delimiter=' ')

input45=np.genfromtxt('HeatherCh2.txt', names=True, dtype=None, delimiter=' ')

Nbins=200


bin_size=(np.max(input45['Phase'])-np.min(input45['Phase']))/Nbins
phase_values45=[]
flux_values45=np.linspace(0,0,num=Nbins)
for i in range(Nbins):
    phase_values45.append(bin_size*i)
    
counter=0.
for i in range(0,Nbins-1):
    #print i
    if i == Nbins: break
    for j in range(len(input45['Flux'])):
        if phase_values45[i] <= input45['Phase'][j] < phase_values45[i+1]:
            flux_values45[i]+=input45['Flux'][j]
            counter+=1
    if counter != 0: flux_values45[i]=flux_values45[i]/counter
    elif counter == 0: flux_values45[i]=-99
    counter=0.
xdegrees=[]
for i in range(len(phase_values45)):
    xdegrees.append((phase_values45[i]*180.0)/360)


    
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
    

new6x=[]
for i in range(len(new45x)):
    new6x.append(new45x[i]/360)
    
remove_positions=[]
counter=0
for i in phase_values5:
    if flux_values45[counter]==-99: remove_positions.append(counter)
    elif 0.4<i<0.6:
        if flux_values45[counter] < 0.0009:
            remove_positions.append(counter)
    counter+=1
            
phase_values45_removed=np.delete(phase_values5,remove_positions)
flux_values45_removed=np.delete(flux_values45,remove_positions)
    


#################################################################


from scipy.interpolate import interp1d


interpolation36=interp1d(phase_values36_removed,flux_values36_removed)
interpolation45=interp1d(phase_values45_removed,flux_values45_removed)

chi36=[]
#error36=0.333/(len(input2['BJD']/40))**0.5
error36=0.00333/(len(input36['Phase']/len(xplanet36)))**0.5

chi45=[]
#error45=0.466/(len(input1['BJD']/40))**0.5
error45=0.00466/(len(input45['Phase']/len(xplanet45)))**0.5

res36=[]
res3=[]
for i in range(len(comb36)):

    distance=np.abs(comb36[i]-interpolation36(new5x[i]))**2
    chi36.append(distance/error36**2)
    res3.append(distance*0.5)

distance236=[]
res236=[]
for i in range(len(res3)):
    distance36=(comb36[i]-interpolation36(new5x[i]))**2
    res36.append(distance36**0.5)
    distance236.append(comb36[i]-interpolation36(new5x[i]))
    res236.append(distance236[i])

reserr36=[]
for i in range(len(res36)):
    reserr36.append(((chi36[i])**0.5)/Nbins)
    
    

res45=[]
res4=[]  
distance245=[]
res245=[] 
for i in range(len(comb45)):

    distance=np.abs(comb45[i]-interpolation45(new6x[i]))**2    
    chi45.append(distance/error45**2)
    res4.append(distance**0.5)
for i in range(len(res4)):
    res45.append(res4[i])
    distance245.append(comb45[i]-interpolation45(new5x[i]))
    res245.append(distance245[i])

reserr45=[]
for i in range(len(chi45)):
    reserr45.append(((chi45[i])**0.5)/Nbins) 


x7=np.linspace(0,1,len(res36))
x8=np.linspace(0,1,len(res45))


#############################################################################
colmag=[]

for i in range(len(M36)):
    colmag.append(M36[i]-M45[i])
    


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




####M36
plt.imshow(generatedarray,cmap='viridis') ################################################LOOK AT THIS HERE
plt.title('M36')
plt.axis('off')
plt.savefig("M36Model.pdf", bbox_inches='tight')
plt.show()

f, axarr = plt.subplots(2, sharex=True,gridspec_kw = {'height_ratios':[3, 1]})
axarr[0].plot(new5x, comb36,label='Model 3.6')
axarr[0].scatter(phase_values36_removed,flux_values36_removed,c='#ff8f66',s=2, label='Knutson Data')
axarr[0].set_title('M36')
axarr[0].set_ylabel('Combined Flux in 3.6')
axarr[1].scatter(x7, res236,c='#c71585')
axarr[1].errorbar(x7,res236,yerr=error36,ls='none')
axarr[1].set_title('Residulals')
axarr[1].set_ylim(min(res236),max(res236))
axarr[1].set_xlabel('Longitude')
plt.show()

inputRed=np.genfromtxt('ReducedPoints.txt', names=True, dtype=None, delimiter=' ')

print len(inputRed['Col'])
print len(inputRed['M36'])
print len(inputRed['M45'])

y36R=[]
y45R=[]
xcolR=[]
for i in range(len(inputRed['M36'])):
    y36R.append(inputRed['M36'][i])
    y45R.append(inputRed['M45'][i])
    xcolR.append(inputRed['Col'][i])
#plt.scatter(inputRed['Col'][i], inputRed['M36'][i], label='Reduced Knutson')
#plt.show()
plt.scatter(colour,y,label='Polynomial',s=0.2,c='r')
plt.scatter(xcolR,y36R,s=20,c='m',label='Knutson Reduced')
plt.scatter(colmag,M36,s=40,c=color36,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 3.6 microns')
plt.ylim(8,20)
plt.xlim(-1,3)
plt.gca().invert_yaxis()
plt.legend()
plt.savefig('planetHR1HOPE.pdf')
plt.show()

print "3.6 Chi-Squared: ", np.sum(chi36)/len(comb36), "+/-", np.sum(reserr36)


#######M45
plt.imshow(generatedarray2,cmap='viridis') ################################################LOOK AT THIS HERE
plt.title('M45')
plt.axis('off')
plt.savefig("M45Model.pdf", bbox_inches='tight')
plt.show()

f, axarr = plt.subplots(2, sharex=True,gridspec_kw = {'height_ratios':[3, 1]})
axarr[0].plot(new5x, comb45,label='Model 4.5')
axarr[0].scatter(phase_values45_removed,flux_values45_removed,c='#ff8f66',s=2, label='Knutson Data')
axarr[0].set_title('M45')
axarr[0].set_ylabel('Combined Flux in 4.5')
axarr[1].scatter(x7, res245,c='#c71585')
axarr[1].errorbar(x7,res245,yerr=error45,ls='none')
axarr[1].set_title('Residulals')
axarr[1].set_ylim(min(res245),max(res245))
axarr[1].set_xlabel('Longitude')
plt.show()



plt.scatter(colour,y1,label='Polynomial',s=0.2,c='r')
plt.scatter(xcolR,y45R,s=20,c='m',label='Knutson Reduced')
plt.scatter(colmag,M45,s=40,c=color45,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 4.5 microns')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.legend()
plt.savefig('planetHR2HOPE.pdf')
plt.show()

print "4.5 Chi-Squared: ", np.sum(chi45)/len(comb45), "+/-", np.sum(reserr45)

