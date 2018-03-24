
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:52:19 2017

@author: bettyallison
"""
import numpy as np
x=np.linspace(5,30,num=1000)

c0=9.34220
c1=-3.35222e-01
c2=6.91081e-02
c3=-3.60108e-03
c4=6.50191e-05

y=[]
for i in range(len(x)):
    y.append((c0*x[i]**0)+(c1*x[i]**1)+(c2*x[i]**2)+(c3*x[i]**3)+(c4*x[i]**4))
   
x_value=20

 ## Change this ONLY
y_value=(c0*x_value**0)+(c1*x_value**1)+(c2*x_value**2)+(c3*x_value**3)+(c4*x_value**4)
print y_value

flux=(10**(-0.4*(y_value-2.778683)))

print 1000000*flux


