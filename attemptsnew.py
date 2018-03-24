#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 00:58:15 2018

@author: bettyallison
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:46:30 2018

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


xplanet36=[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,12,12,12,12,12,12,12,10,10,10,10,10,10,12,12,12,12,12,12,12]

xplanet36=[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
#xplanet36=[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
xplanet36=[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,25,25,25]
y36=[]
yplanet36=[]

for i in range(len(xplanet36)):
    y36.append((c0*xplanet36[i]**0)+(c1*xplanet36[i]**1)+(c2*xplanet36[i]**2)+(c3*xplanet36[i]**3)+(c4*xplanet36[i]**4))
    
    yplanet36.append(10**(-0.4*((y36[i])-3.921)))
   
normalisation=np.sum(yplanet36)
#print normalisation
xpoints=np.linspace(1,len(xplanet36),num=len(xplanet36))
#plt.scatter(xpoints,yplanet)
#plt.ylim(0,0.005)
#plt.ylabel('Normalized Flux from M[3.6]')
#plt.xlabel('Slice Number')
#plt.show()

combined36=[]
comb36=[]
Nextra=((len(xplanet36)/2))
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
    
#plt.scatter(newx,comb)
#plt.ylim(min(comb),0.005)
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux in M[3.6]')
#plt.show()

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

xplanet45=[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
xplanet45=[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
xplanet45=[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
#xplanet45=[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
y45=[]
yplanet45=[]

for i in range(len(xplanet45)):
    y45.append((c0*xplanet45[i]**0)+(c1*xplanet45[i]**1)+(c2*xplanet45[i]**2)+(c3*xplanet45[i]**3)+(c4*xplanet45[i]**4))
    
    yplanet45.append(10**(-0.4*((y45[i])-3.921)))

normalisation45=np.sum(yplanet45)
#print normalisation4
xpoints45=np.linspace(1,len(xplanet45),num=len(xplanet45))
#plt.scatter(xpoints4,yplanet1)
#plt.ylim(0,0.005)
#plt.ylabel('Normalized Flux from M[4.5]')
#plt.xlabel('Slice Number')
#plt.show()

combined45=[]
comb45=[]
Nextra=((len(xplanet45)/2))
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
    
#plt.scatter(new4x,comb4)
#plt.ylim(0,0.005)
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux in M[4.5]')
#plt.show()

#plt.scatter(newx,comb,label='M36')
#plt.scatter(new4x,comb4,label='M45')
#plt.ylim(0,0.0015)
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux')
#plt.legend()
#plt.show()


M45=[]
diff=[]

for i in range(len(comb45)):
    M45.append(3.892-(2.5*np.log10(comb45[i])))



#plt.scatter(new4x,M45)
#plt.xlabel('Longitude')
#plt.ylabel('Combined Magnitude in M[4.5]')
#plt.gca().invert_yaxis()
#plt.show()

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


#plt.scatter(colour,y,label='Polynomial',s=0.2,c='r')
#plt.scatter(colmag,M36,s=40,c=color36,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
#plt.xlabel('[3.6]-[4.5]')
#plt.ylabel('Absolute Magnitude in 3.6 microns')
#plt.ylim((8,20))
#plt.xlim((-1,3))
#plt.gca().invert_yaxis()
#plt.legend()
#plt.savefig('planetHR1HOPE.pdf')
#plt.show()
#
#plt.scatter(colour,y1,label='Polynomial',s=0.2,c='r')
#plt.scatter(colmag,M45,s=40,c=color45,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
#plt.xlabel('[3.6]-[4.5]')
#plt.ylabel('Absolute Magnitude in 4.5 microns')
#plt.ylim((8,20))
#plt.xlim((-1,3))
#plt.gca().invert_yaxis()
#plt.legend()
#plt.savefig('planetHR2HOPE.pdf')
#plt.show()
#
#print 'M45', M45
#print 'M36', M36
#print colmag
#
#print min(M45)
#print max(M45)
#print max(M36)
#print min(M36)




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

#plt.imshow(generatedarray,cmap='viridis') ################################################LOOK AT THIS HERE
#plt.title('M36')
#plt.axis('off')
#plt.savefig("M36Model.pdf", bbox_inches='tight')
#plt.show()

#print "Done"

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

#plt.imshow(generatedarray2,cmap='viridis') ################################################LOOK AT THIS HERE
#plt.title('M45')
#plt.axis('off')
#plt.savefig("M45Model.pdf", bbox_inches='tight')
#plt.show()
#
#print "Done"

###########################################################
#plt.scatter(newx,comb36)
#plt.ylim(min(comb36),0.005)
#plt.title('Planet Orbital Flux 3.6')
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux in M[3.6]')
#plt.show()
##This is for M36
#
#plt.scatter(new45x,comb45)
#plt.ylim(0,0.005)
#plt.title('Planet Orbital Flux 4.5')
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux in M[4.5]')
#plt.show()
#This is the flux for M4.5

########################################################
#input1=np.genfromtxt('final_unbinned_ch2_phot.txt', names=True, dtype=None)
#
##list1=input1['RelativeFlux']
##    
##print np.min(list1)
##
###2455189.056386 this is the centre point
##
#input2=np.genfromtxt('final_unbinned_ch1_phot.txt', names=True, dtype=None)
#
#periodCh1=[]
#for i in range(len(input2['BJD'])):
#    periodCh1.append((input2['BJD'][i]-2455559.568294))
#
#fluxCh1=[]
#for i in range(len(input2['BJD'])):
#    fluxCh1.append((0.000932*periodCh1[i])+((-1*0.000573)*(periodCh1[i]**2)))
#
##print len(input2['BJD'])
##print len(input1['BJD'])
##plt.scatter(period2,flux2)
##plt.show()
#
##plt.scatter(period2,input2['RelativeFlux'],s=0.5)
##
##plt.ylabel('Absolute Normalised Flux in 3.6')
##plt.show()
#
#fluxyCh1=[]
#for i in range(len(periodCh1)):
#    fluxyCh1.append(((input2['RelativeFlux'])[i])-fluxCh1[i])
#
##plt.scatter(periodCh1,fluxyCh1)
##plt.show()
#
#
#
################################################################################
#Nextra=1000
#binvaluesyCh1=[]
#valuesyCh1=[]
#
#summation=0
#for i in range(len(fluxyCh1)):
#    valuesyCh1.append(fluxyCh1[i])
#    summation+=valuesyCh1[i]
#    if i%Nextra == 0:
#        binvaluesyCh1.append(summation/Nextra)
#        summation=0
#        
#Nextra=1000
#binvaluesxCh1=[]
#valuesxCh1=[]
#
#summation=0
#for i in range(len(fluxyCh1)):
#    valuesxCh1.append(periodCh1[i])
#    summation+=valuesxCh1[i]
#    if i%Nextra == 0:
#        binvaluesxCh1.append(summation/Nextra)
#        summation=0
#        
#
##plt.scatter(binvaluesx2,binvaluesy2,s=0.5)
###plt.plot(x1,y=1,c='g')
###plt.xlim(0,12500)
##plt.ylim(0.975,1.001)
##plt.ylabel('Absolute Normalised Flux in 3.6')
##plt.show()
#
#newyCh1=[]
#newxCh1=[]
#for i in range(len(binvaluesxCh1)):
#    newyCh1.append((binvaluesyCh1[i]-0.99905-0.0005))
#    newxCh1.append(((binvaluesxCh1[i]-(10/180)-0.1)))
##plt.scatter(newxCh1,newyCh1,s=0.2)
##plt.ylim(0,0.007)
##plt.xlim(0,(360/180))
#
#
#newxxCh1=[]
#for i in range(len(newxCh1)):
#    newxxCh1.append(newxCh1[i]+(400/180)+0.225)
#    
##plt.scatter(newx,newy)
##plt.ylim(0,0.007)
##plt.xlim(-250,0)
##plt.show() 
#
##plt.scatter(newxxCh1,newyCh1,s=0.2)
##plt.ylim(0,0.007)
##plt.xlim(0,360/180)
##plt.show()   
#
#
#output = open('HeatherCh1.txt', 'w')
#output.write('Phase'+' '+'Flux'+'\n')
#
##save titles for text file
#for i in range(len(newxxCh1)):
#    if (0 <= newxxCh1[i] <= 2) and (0 <= newyCh1[i] <= 0.007):
#        output.write(str(newxxCh1[i])+' '+ str(newyCh1[i])+ '\n')
#
#for i in range(len(newxCh1)):
#    if (0 <= newxCh1[i] <= 2) and (0 <= newyCh1[i] <= 0.007):
#        output.write(str(newxCh1[i])+' '+ str(newyCh1[i])+ '\n')
#
#    
#output.close()
##print 'Hello'

input36=np.genfromtxt('HeatherCh1.txt', names=True, dtype=None, delimiter=' ')




input45=np.genfromtxt('HeatherCh2.txt', names=True, dtype=None, delimiter=' ')

#print len(input45['Flux'])
#
#print len(input36['Flux'])


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

#plt.scatter(xdegrees,flux_values3,s=2)
#plt.ylim(0,0.0015)
#plt.ylabel('Ratio of Flux Planet/Flux Star in 4.5 microns')
#plt.xlabel('Orbital Phase')
#plt.savefig('minitransit.pdf')
#plt.show()
    
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
    
#plt.scatter(phase_values5,flux_values4,s=2)
#plt.ylim(0,0.0015)
#plt.ylabel('Flux of Planet in 3.6 microns')
#plt.xlabel('Period in 2*Pi Radians')
#plt.show()


    
#plt.scatter(phase_values5,flux_values4,s=2)
#plt.scatter(xdegrees,flux_values3,s=2)
#plt.ylim(0,0.0015)
#plt.show()
#print 'F36 ',flux_values4
#print 'F45 ',flux_values3

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
    
#plt.scatter(new5x,comb36,label='Model M36')
#plt.scatter(phase_values36_removed,flux_values36_removed,s=2,label='Knutson Data')
#
#plt.ylim(min(comb36),0.0015)
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux in M[3.6]')
#plt.legend()
#plt.show()
#print len(flux_values36)
#This is for M36
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
    
#plt.scatter(new6x,comb45,label='Model M45')
#plt.scatter(phase_values45_removed,flux_values45_removed,s=2,label='Knutson Data')
#plt.ylim(0,0.0015)
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux in M[4.5]')
#plt.show()
#print len(flux_values45)
#This is the flux for M4.5

#################################################################
#I WANT TO GET RID OF THE STRAY POINTS 
#new5x,phase_values5

#comb[i],flux_values4[i]
#plt.clf()
#plt.scatter(new5x,comb36,c='r')
#plt.scatter(phase_values5,flux_values36,c='c')
#plt.ylim(-0.5,1.5)
#plt.show()

from scipy.interpolate import interp1d

#interpolation36=interp1d(phase_values5,flux_values36)
#interpolation45=interp1d(phase_values5,flux_values45)

interpolation36=interp1d(phase_values36_removed,flux_values36_removed)
interpolation45=interp1d(phase_values45_removed,flux_values45_removed)

chi36=[]
#error36=0.333/(len(input2['BJD']/40))**0.5
error36=0.00333/(len(input36['Phase']/len(xplanet36)))**0.5

chi45=[]
#error45=0.466/(len(input1['BJD']/40))**0.5
error45=0.00466/(len(input45['Phase']/len(xplanet45)))**0.5
'''
for i in range(len(comb)):
    chi36.append(((comb[i]-flux_values4[i])**2)/flux_values4[i])
    
for i in range(len(comb4)):
    chi45.append(((comb4[i]-flux_values3[i])**2)/flux_values3[i])
'''
#square root 2 chi ^2/N
res36=[]
res3=[]
for i in range(len(comb36)):
    #distance=np.abs(comb[i]-flux_values4[i])**2
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
    
    
#print "3.6 Chi-Squared: ", np.sum(chi36)/len(comb36)
res45=[]
res4=[]  
distance245=[]
res245=[] 
for i in range(len(comb45)):
    #distance=np.abs(comb4[i]-flux_values3[i])**2
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
#print "4.5 Chi-Squared: ", np.sum(chi45)/len(comb45)

#res36=[]
#res45=[]
#
#for i in range(len(comb36)):
#    res36.append(comb36[i]-flux_values36[i])
#for i in range(len(comb45)):
#    res45.append(comb45[i]-flux_values45[i])

x7=np.linspace(0,1,len(res36))
x8=np.linspace(0,1,len(res45))

#plt.scatter(x7,res36)
#plt.title('Residuals M36')
#plt.ylim(min(res36),max(res36))
#plt.show()   
#
#plt.scatter(x8,res45)
#plt.title('Residuals M45')
#plt.ylim(min(res45),max(res45))
#plt.show() 
#print 'chi36', chi36
#print 'chi45', chi45
#f, axarr = plt.subplots(2, sharex=True,gridspec_kw = {'height_ratios':[3, 1]})
#axarr[0].plot(new5x, comb36,label='Model 3.6')
#axarr[0].scatter(phase_values36_removed,flux_values36_removed,c='#ff8f66',s=2, label='Knutson Data')
#axarr[0].set_title('M36')
#axarr[0].set_ylabel('Combined Flux in 3.6')
#axarr[1].plot(x7, res36,c='#c71585')
#axarr[1].set_title('Residulals')
#axarr[1].set_ylim(min(res36),max(res36))
#axarr[1].set_xlabel('Longitude')
#plt.show()
#
#f, axarr = plt.subplots(2, sharex=True,gridspec_kw = {'height_ratios':[3, 1]})
#axarr[0].plot(new5x, comb45,label='Model 4.5')
#axarr[0].scatter(phase_values45_removed,flux_values45_removed,c='#ff8f66',s=2, label='Knutson Data')
#axarr[0].set_title('M45')
#axarr[0].set_ylabel('Combined Flux in 4.5')
#axarr[1].plot(x7, res45,c='#c71585')
#axarr[1].set_title('Residulals')
#axarr[1].set_ylim(min(res45),max(res45))
#axarr[1].set_xlabel('Longitude')
#plt.show()


#plt.imshow(generatedarray,cmap='viridis') ################################################LOOK AT THIS HERE
#plt.title('M45')
#plt.axis('off')
#plt.savefig("M45Model.pdf", bbox_inches='tight')
#plt.show()

#plt.scatter(phase_values45_removed,flux_values45_removed,s=2,label='Knutson Data')
#plt.ylim(0,0.0015)
#plt.xlabel('Longitude')
#plt.ylabel('Combined Flux in M[4.5]')
#plt.show()

#############################################################################
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


#plt.scatter(colour,y,label='Polynomial',s=0.2,c='r')
#plt.scatter(colmag,M36,s=40,c=color36,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
#plt.xlabel('[3.6]-[4.5]')
#plt.ylabel('Absolute Magnitude in 3.6 microns')
#plt.ylim((8,20))
#plt.xlim((-1,3))
#plt.gca().invert_yaxis()
#plt.legend()
#plt.savefig('planetHR1HOPE.pdf')
#plt.show()
#
#plt.scatter(colour,y1,label='Polynomial',s=0.2,c='r')
#plt.scatter(colmag,M45,s=40,c=color45,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
#plt.xlabel('[3.6]-[4.5]')
#plt.ylabel('Absolute Magnitude in 4.5 microns')
#plt.ylim((8,20))
#plt.xlim((-1,3))
#plt.gca().invert_yaxis()
#plt.legend()
#plt.savefig('planetHR2HOPE.pdf')
#plt.show()

#f, axarr = plt.subplots(2, sharex=False,gridspec_kw = {'height_ratios':[1,2]})
#axarr[0].imshow(generatedarray,cmap='viridis') ################################################LOOK AT THIS HERE
#axarr[0].set_title('M45')
#axarr[0].axis('off')
#axarr[1].scatter(colour,y1,label='Polynomial',s=0.2,c='r')
#axarr[1].scatter(colmag,M45,s=40,c=color45,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
#axarr[1].set_xlabel('[3.6]-[4.5]')
#axarr[1].set_ylabel('Absolute Magnitude in 4.5 microns')
#axarr[1].set_ylim((8,20))
#axarr[1].set_xlim((-1,3))
#axarr[1].invert_yaxis()
#axarr[1].legend()
#plt.show()


#f, ((ax1), (ax2), (ax3), (ax4)) = plt.subplots(4, 1, sharex=False, sharey=False)
#ax1.imshow(generatedarray,cmap='viridis') 
#ax1.set_title('M45')
#ax1.axis('off')
#ax2.plot(new5x, comb45,label='Model 4.5')
#ax2.scatter(phase_values45_removed,flux_values45_removed,c='#ff8f66',s=2, label='Knutson Data')
#ax2.set_title('M45')
#ax2.set_ylabel('Combined Flux in 4.5')
#ax2.legend()
#ax3.plot(x7, res45,c='#c71585')
#ax3.set_title('Residulals')
#ax3.set_ylim(min(res45),max(res45))
#ax3.set_xlabel('Longitude')
#ax3.scatter(colour,y1,label='Polynomial',s=0.2,c='r')
#ax3.scatter(colmag,M45,s=40,c=color45,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
#ax4.set_xlabel('[3.6]-[4.5]')
#ax4.set_ylabel('Absolute Magnitude in 4.5 microns')
#ax4.set_ylim((8,20))
#ax4.set_xlim((-1,3))
#ax4.invert_yaxis()
#ax4.legend()
#plt.show()

####M36
#plt.imshow(generatedarray,cmap='viridis') ################################################LOOK AT THIS HERE
#plt.title('M36')
#plt.axis('off')
#plt.savefig("M36Model.pdf", bbox_inches='tight')
#plt.show()
#
#f, axarr = plt.subplots(2, sharex=True,gridspec_kw = {'height_ratios':[3, 1]})
#axarr[0].plot(new5x, comb36,label='Model 3.6')
#axarr[0].scatter(phase_values36_removed,flux_values36_removed,c='#ff8f66',s=2, label='Knutson Data')
#axarr[0].set_title('3.6 Microns')
#axarr[0].set_ylabel('Combined Flux in 3.6')
#axarr[1].scatter(x7, res236,c='#c71585')
#axarr[1].errorbar(x7,res236,yerr=reserr36,ls='none')
#axarr[1].set_title('Longitude')
#axarr[1].set_ylim(-0.01,0.01)
#axarr[1].set_xlabel('Longitude')
##plt.savefig('model1.pdf')
#plt.show(new5x, comb36,label='Model 3.6')

plt.scatter(new5x, comb36,label='Model 3.6')
plt.title('3.6 Microns')
plt.ylabel('Combined Flux in 3.6 microns')
plt.xlabel('Orbital Phase')
plt.ylim(0,0.0005)
plt.show()

plt.scatter(colour,y,label='Polynomial',s=0.2,c='r')
plt.scatter(colmag,M36,s=40,c=color36,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 3.6 microns')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.legend()
#plt.savefig('finalplanet36.pdf')
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
axarr[0].set_title('4.5 Microns')
axarr[0].set_ylabel('Combined Flux in 4.5')
axarr[1].scatter(x7, res245,c='#c71585')
axarr[1].errorbar(x7,res245,yerr=reserr45,ls='none')
axarr[1].set_title('Longitude')
axarr[1].set_ylim(-0.01,0.01)
axarr[1].set_xlabel('Longitude')
#plt.savefig('model2.pdf')
plt.show()



plt.scatter(colour,y1,label='Polynomial',s=0.2,c='r')
plt.scatter(colmag,M45,s=40,c=color45,cmap=plt.cm.get_cmap('viridis_r'),label='Model Planet')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('Absolute Magnitude in 4.5 microns')
plt.ylim((8,20))
plt.xlim((-1,3))
plt.gca().invert_yaxis()
plt.legend()
#plt.savefig('finalplanet45.pdf')
plt.show()

print "4.5 Chi-Squared: ", np.sum(chi45)/len(comb45), "+/-", np.sum(reserr45)