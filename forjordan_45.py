'''
inputs that i want. 
Spectral class range to be investigated in 26-10. 
each x planet has 40 slices, so i need 20 for each type.

xplanet36=[26 x20, 25 x20]
xplanet45 = [26 x 20, 25 x20]

you can mix these all up.
I want it to go through each combination but the combinations for xplanet36 and xplanet45 are not the same. 
ie 
xplanet 36= [18, 12]
xplanet 45 = [26,18]

KEY POINT:THE FIRST SLICE (THE FIRST 20 POINTS) NEED TO BE GREATER THAN THE OTHER 20 POINTS. 
IE X=[20,18] NOT [18,20]
Only xplanet36 requires an offset. 
ONLY AN OFFSST OF 10
[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]
[15,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,20]
[15,15,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,20,20]
[15,15,15,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,20,20,20]
[15,15,15,15,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,20,20,20,20]
......
[15,15,15,15,15,15,15,15,15,15,20,20,20,20,20,20,20,20,20,20,15,15,15,15,15,15,15,15,15,15,20,20,20,20,20,20,20,20,20,20]
THIS IS THE FINAL OFFSET
[]





'''

###############################################################################

import numpy as np #allows math functions

input36=np.genfromtxt('HeatherCh1.txt', names=True, dtype=None, delimiter=' ')
#heathers data in 3.6

input45=np.genfromtxt('HeatherCh2.txt', names=True, dtype=None, delimiter=' ')
#heathers data in 4.5
'''
c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05
#these are used to find magnitudes in 3.6


xplanet36=[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12] 
#this is my one input for 3.6. It's 40 long. 20 of each spectral class. Currently does not have an offset but should have one. 

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


xplanet45=[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12] 


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
fraction=10
################DO NOT REMOTE THESE LINES:
Nextra_halved=Nextra/2.
if fraction<Nextra_halved:
    raise TypeError("Fraction is smaller than half of Nextra. This is physically impossible.")
################
for i in range(len(xpoints45)):
    summation2=0
    for j in range(Nextra):
        separation=np.abs(j-Nextra_halved)
        if i+j<len(xpoints45):
            summation=yplanet45[i+j]
        else:
            difference=(i+j)-len(xpoints45)
            summation=yplanet45[difference]
        if separation != 0 and enable_darkening==True: summation2+=summation*(np.abs(fraction-separation)/fraction)
        else: summation2+=summation
    combined45.append((summation2/normalisation45))
    comb45.append(summation2/(len(xplanet45)/2))

long=[0,30,60,90,120,150,180,210,240,270,300,330,360]
new45x=[]
a=360/len(xpoints45)
for i in range(len(xpoints45)):
    
    new45x.append((xpoints45[i]*a)-a)
    
M45=[]
diff=[]

for i in range(len(comb45)):
    M45.append(3.892-(2.5*np.log10(comb45[i])))


###########################################
#Heathers Data            

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
'''

bin_size2=(np.max(input36['Phase'])-np.min(input36['Phase']))/Nbins
phase_values4=[]
flux_values36=np.linspace(0,0,num=Nbins)
for i in range(Nbins):
    phase_values4.append((bin_size2*i))

    
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
'''   


#####################################################
'''
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
    
'''
new6x=[]
for i in range(len(new45x)):
    new6x.append(new45x[i]/360)
    
remove_positions=[]
counter=0
for i in phase_values45:
    if flux_values45[counter]==-99: remove_positions.append(counter)
    elif 0.4<i<0.6:
        if flux_values45[counter] < 0.0009:
            remove_positions.append(counter)
    counter+=1
            
phase_values45_removed=np.delete(phase_values45,remove_positions)
flux_values45_removed=np.delete(flux_values45,remove_positions)



#################################################################


from scipy.interpolate import interp1d


#interpolation36=interp1d(phase_values36_removed,flux_values36_removed)
interpolation45=interp1d(phase_values45_removed,flux_values45_removed)
'''
chi36=[]
error36=0.00333/(len(input36['Phase']/len(xplanet36)))**0.5

'''
chi45=[]
error45=0.00466/(200)**0.5
'''
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
    
    
'''
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
    distance245.append(comb45[i]-interpolation45(new6x[i]))
    res245.append(distance245[i])

reserr45=[]
for i in range(len(chi45)):
    reserr45.append(((chi45[i])**0.5)/Nbins) 


#print "3.6 Chi-Squared: ", np.sum(chi36), "+/-", np.sum(reserr36)

print "4.5 Chi-Squared: ", np.sum(chi45), "+/-", np.sum(reserr45)

