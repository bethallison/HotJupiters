#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:36:50 2017

@author: bettyallison
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np #allows math functions
from mpl_toolkits.basemap import Basemap


plt.figure(figsize=(3, 3))
ax = plt.axes(projection=ccrs.NorthPolarStereo())
ax.coastlines(resolution='110m')
ax.gridlines()

plt.figure(figsize=(3, 3))
ax = plt.axes(projection=ccrs.NearsidePerspective(satellite_height=10000000.0, central_longitude=-3.53, central_latitude=50.72))
ax.coastlines(resolution='110m')
ax.gridlines()


#Planet###################################
x=np.linspace(5,30,num=1000)

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

xplanet=[30,29,28,27,26,25,24,23,22,23,24,25,26,27,28,29,30]

y1=[]
y=[]
for i in range(len(x)):
    y.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))
    
    y1.append(10**(-0.4*((y[i])-2.78)))

y2=[]
yplanet=[]

for i in range(len(xplanet)):
    y2.append((c0*xplanet[i]**0)+(c1*xplanet[i]**1)+(c2*xplanet[i]**2)+(c3*xplanet[i]**3)+(c4*xplanet[i]**4))
    
    yplanet.append(10**(-0.4*((y2[i])-2.78)))


xmax2=3600#arr2.shape[1] #Automatically determines x and y values from the array
ymax2=1800#arr2.shape[0]
segments2=len(xplanet) #This is your number of slices
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

plt.imshow(generatedarray) ################################################LOOK AT THIS HERE
plt.axis('off')
plt.savefig("planettemp.png", bbox_inches='tight')
plt.show()

print "Done"

#############################################################################

bmap = Basemap(projection='ortho', lat_0 = 90, lon_0 = 0,
              resolution = 'l', area_thresh = 1000.)
# plot surface
bmap.warpimage(image='planet1copy.jpeg')
# draw the edge of the map projection region (the projection limb)
bmap.drawmapboundary()
# draw lat/lon grid lines every 30 degrees.
bmap.drawmeridians(np.arange(0, 360, 30))
bmap.drawparallels(np.arange(-90, 90, 30))
plt.show()