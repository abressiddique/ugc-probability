# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:05:57 2020

@author: sandhya addetla
"""
import numpy as np
B1 = np.array([[0,0,1],[0,1,0],[1,0,0]])
B2 = np.array([[0,0,0,0,1,1],
              [0,0,0,0,1,1],
              [0,0,1,1,0,0],
              [0,0,1,1,0,0],
              [1,1,0,0,0,0],
              [1,1,0,0,0,0]])
B3 = np.array([[0,0,0,0,0,0,1,1,1],
              [0,0,0,0,0,0,1,1,1],
              [0,0,0,0,0,0,1,1,1],
              [0,0,0,1,1,1,0,0,0],
              [0,0,0,1,1,1,0,0,0],
              [0,0,0,1,1,1,0,0,0],
              [1,1,1,0,0,0,0,0,0],
              [1,1,1,0,0,0,0,0,0],
              [1,1,1,0,0,0,0,0,0]])

print("Rank of matrix") 
print(" {} is : {}".format(B1, np.linalg.matrix_rank(B1)))
print("Rank of matrix") 
print(" {} is : {}".format(B2, np.linalg.matrix_rank(B2)))
print("Rank of matrix") 
print(" {} is : {}".format(B3, np.linalg.matrix_rank(B3)))
