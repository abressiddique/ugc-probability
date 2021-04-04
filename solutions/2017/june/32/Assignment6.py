# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:29:24 2020

@author: Rishab
"""
import numpy as np
from numpy import linalg as LA

A = np.array([[1,1,2],[1,-2,-5],[2,5,-3]])  #Symmetric matrix
B = LA.eigvalsh(A)  #Method for computing eigen values of a real symmetric matrix
print(B)