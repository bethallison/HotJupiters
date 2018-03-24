#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 13:22:02 2017

@author: bettyallison
"""

import random
import matplotlib.pyplot as plt
x=[x/1000 for x in random.sample(range(100000),100)]
xbins=range(0,len(x))
plt.hist(x, bins=xbins, color='blue')
plt.show()