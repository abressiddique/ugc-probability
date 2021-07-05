import numpy as np
import matplotlib.pyplot as plt
import math
# evenly sampled time at 200ms intervals
t = np.arange(0., 100., 0.2)
alpha1=4 # for alpha>1
alpha2=0.5 # for alpha<1
alpha3=1  #for alpha=1
mu = 1
# red dashes, blue squares and green triangles
plt.plot(t, alpha1*pow(t-mu, alpha1-1), 'r--', t, alpha3*pow(t-mu, alpha3-1), 'g--')
plt.show()
plt.plot( t, alpha2*pow(t-mu, alpha2-1), 'b--', t, alpha3*pow(t-mu, alpha3-1), 'g--')
plt.show()
