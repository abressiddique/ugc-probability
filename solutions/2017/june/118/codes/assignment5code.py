import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import bernoulli
def plot(alpha,mu):
  x=np.arange(0,5,0.1)
  y=alpha*np.power((x-mu),(alpha-1))
  for i in range(len(x)):
    if x[i]<=mu:
      y[i]=0

  plt.plot(x,y)
  plt.xlabel("y (alpha = "+ str(alpha) + " ; mu = " + str(mu)+")")
  plt.ylabel("Hazard Function H(y)")
  plt.show()

plot(0.5, -2)
plot(3,2)
