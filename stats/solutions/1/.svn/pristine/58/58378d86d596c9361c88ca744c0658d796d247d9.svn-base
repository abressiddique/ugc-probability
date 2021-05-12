import numpy as np 
import matplotlib.pyplot as plt



#generating arrays:
x = np.linspace(0, 10)
y= np.linspace(-10, 0)


plt.grid(color='grey', ls='--')

#plot for the pdf
plt.plot(x, np.exp(-x), color='cyan')
plt.plot(y, 0*y, color='cyan')

#plot for the cdf
plt.plot(x, 1-np.exp(-x), color='red')
plt.plot(y, 0*y, color='red')

#some points and reference lines:
plt.plot(0,0, 'go')
plt.plot(0,1,'go')
plt.vlines(x=0, ymin=0, ymax=1, ls='--')

#labels:
plt.xlabel('$z$')
plt.ylabel('$f_{Z_n}(z)$')
plt.ylabel('$F_{Z_n}(z)$')

plt.show() 