#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 18:56:57 2017

@author: bettyallison
"""
from colour import Color
import numpy as np
import matplotlib.pyplot as plt
#, hue=0.2
X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
Y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

Z = [x for _,x in sorted(zip(Y,X))]
print(Z) 