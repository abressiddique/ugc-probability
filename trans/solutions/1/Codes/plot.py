import numpy as np
import matplotlib.pyplot as plt
import math
import random

def F(x):
  return math.sin(x)
X = np.linspace(0,math.pi,10000)
y = random.random()
Y = [F(x) for x in X]
Y1= [y for x in X]
Y2= np.linspace(0,y,10000)
X2= [math.asin(y) for i in Y2]
X3= [math.pi-math.asin(y) for i in Y2]
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(X,Y,label='Y=$\sinx$')
plt.plot(X,Y1,label="Y=y")
plt.plot(X2,Y2,label='X=$\sin^{-1}y$')
plt.plot(X3,Y2,label='X=$\pi-\sin^{-1}y$')
plt.legend()
plt.grid()
plt .show()