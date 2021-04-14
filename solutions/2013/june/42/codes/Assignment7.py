from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt
  
sim_size=10000
#number of simulations

x_rvs = expon.rvs(loc=0,scale=1,size=sim_size)
#Random variable X

y_rvs = expon.rvs(loc=0,scale=1,size=sim_size)
#Random variable Y

sum=0

z_rvs = list(range(sim_size))

for i in range(sim_size):
  z_rvs[i] = max(x_rvs[i],y_rvs[i])
  sum=sum+z_rvs[i]

print(sum/sim_size)
