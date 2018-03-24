#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:44:17 2017

@author: bettyallison
"""

import numpy as np #allows math functions
import matplotlib.pyplot as plt #allows graphs to be created
from mpl_toolkits.basemap import Basemap

input1=np.genfromtxt('spectrabrown.txt', delimiter=',', names=True, dtype=None)
input2=np.genfromtxt('spectrared.txt', delimiter=',', names=True, dtype=None)
input3=np.genfromtxt('purplespect.txt', delimiter=',', names=True, dtype=None)
input4=np.genfromtxt('spectblue.txt', delimiter=',', names=True, dtype=None)


x=np.linspace(5,30,num=1000)

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

y1=[]
y=[]
for i in range(len(x)):
    y.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))
    
    y1.append(10**(-0.4*((y[i])-2.78)))

xplanet=[30,28.9,28.7,28.5,28.3,28.1,26.9,26.7,26.5,26.3,26.1,25.2,25.4,25.6,25.8,27.2,27.4,27.6,27.8,29.2,29.4,29.6,29.8]

y2=[]
yplanet=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet.append(10**(-0.4*((y2[i])-2.78)))


normalisation=np.sum(yplanet)
xpoints=np.linspace(1,23,num=23)
plt.scatter(xpoints,yplanet/normalisation)
plt.ylabel('Normalized Flux from M[3.6]')
plt.xlabel('Slice Number')
plt.show()

combined=[]
comb=[]
Nextra=11
for i in range(len(xpoints)):
    summation=0
    for j in range(Nextra):
        if i+j<len(xpoints):
            summation+=yplanet[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation+=yplanet[difference]
            #print i,j,difference
    combined.append(summation/normalisation)
    comb.append(summation)
    
long=[0,30,60,90,120,150,180,210,240,270,300,330,360]

plt.scatter(xpoints,combined)
plt.xlabel('Longitude')
plt.ylabel('Combined Flux in M[4.5]')
plt.show()
############Created a Planet###################################
xmax2=3600#arr2.shape[1] #Automatically determines x and y values from the array
ymax2=1800#arr2.shape[0]
segments2=len(yplanet) #This is your number of slices
colours=['r','y','b','g','m','c','k']
xlength2=xmax2*1.0/segments2 #Length of each slice

generatedarray=np.zeros(shape=(ymax2,xmax2))

fluxaverage=0
sliceaverage2=[] #This array saves all the averages if you need them later
ylower=0 #These are your Y upper and lower bounds. Change to 0 and ymax if you want the full image.
yupper=1800
counter=0

for i in range(int(segments2)): #number of segments
    for x in range(int(xlength2*i),int(xlength2*(i+1))):
        for y in range(ylower,yupper):
            #if counter != 10:
            #    counter+=1
            #else:
            #    counter=0
            try: generatedarray[y,x]=yplanet[i]
            except Exception: print x,y,i

#plt.imshow(generatedarray) ################################################LOOK AT THIS HERE
#plt.axis('off')
#plt.savefig("planettemp.png", bbox_inches='tight')
#plt.show()

print "Done"

#############################################################################
'''
bmap = Basemap(projection='ortho', lat_0 = 0, lon_0 = 0,
              resolution = 'l', area_thresh = 1000.)
# plot surface
bmap.warpimage(image='planet1copy.jpeg')
# draw the edge of the map projection region (the projection limb)
bmap.drawmapboundary()
# draw lat/lon grid lines every 30 degrees.
bmap.drawmeridians(np.arange(0, 360, 30))
bmap.drawparallels(np.arange(-90, 90, 30))
plt.show()
'''
#Need to fix this init
##############################################################################
#ALL AGAIN DIFFERENT MAGNITUDE

c0= 9.73946
c1= -4.39968e-01
c2= 7.65343e-02
c3= -3.63435e-03
c4= 5.82107e-05
xplanet=[30,28.9,28.7,28.5,28.3,28.1,26.9,26.7,26.5,26.3,26.1,25.2,25.4,25.6,25.8,27.2,27.4,27.6,27.8,29.2,29.4,29.6,29.8]
y1=[]
y=[]
for i in range(len(xplanet)):
    y.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    y1.append(10**(-0.4*((y[i])-3.26)))
    
print 'done'
yS=[]
yS.append(10**(-0.4*((y[i])-3.26))) #flux of the sun

xplanet=[30,28.9,28.7,28.5,28.3,28.1,26.9,26.7,26.5,26.3,26.1,25.2,25.4,25.6,25.8,27.2,27.4,27.6,27.8,29.2,29.4,29.6,29.8]
y2=[]
yplanet2=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet2.append(10**(-0.4*((y2[i])-3.26)))

print 'done'

normalisation=np.sum(yplanet2)
xpoints=np.linspace(1,23,num=23)
plt.scatter(xpoints,yplanet2/normalisation)
plt.ylabel('Normalized Flux from M[4.5]')
plt.xlabel('Slice Number')
plt.show()

combined2=[]
comb2=[]
Nextra=11
for i in range(len(xpoints)):
    summation2=0
    for j in range(Nextra):
        if i+j<len(xpoints):
            summation2+=yplanet2[i+j]
        else:
            difference=(i+j)-len(xpoints)
            summation2+=yplanet2[difference]
            #print i,j,difference
    combined2.append(summation2/normalisation)
    comb2.append(summation2)
    
long=[0,30,60,90,120,150,180,210,240,270,300,330,360]

plt.scatter(xpoints,combined2)
plt.xlabel('Longitude')
plt.ylabel('Combined Flux in M[4.5]')
plt.show()

#########################################################################

#Lets go back to magnitudes#

M36=[]
M45=[]
diff=[]

for i in range(len(comb2)):
    M36.append(-2.5*np.log10(comb[i]/2.78))
    M45.append(-2.5*np.log10(comb2[i]/3.26))
    diff.append(M36[i]-M45[i])

plt.scatter(xpoints,M36)
plt.xlabel('Longitude')
plt.ylabel('Combined Magnitude in M[3.6]')
plt.gca().invert_yaxis()
plt.show()

print diff
plt.scatter(diff,M36)
plt.title('Colour Magnitude Diagram')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[3.6]')
plt.ylim((8,20))
plt.xlim((0,3))
plt.gca().invert_yaxis()
plt.show() 

plt.scatter(diff,M45)
plt.title('Colour Magnitude Diagram')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[4.5]')
plt.ylim((8,20))
plt.xlim((0,3))
plt.gca().invert_yaxis()
plt.show() 
'''
plt.scatter(diff,M45)
plt.title('Colour Magnitude Diagram')
plt.xlabel('[3.6]-[4.5]')
plt.ylabel('M[4.5]')
#plt.ylim((10.5,13.75))
#plt.xlim((-0.2,2))
plt.gca().invert_yaxis()
plt.show()     
'''   
##########################################

print M36

print 'done'

print M45