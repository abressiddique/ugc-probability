import matplotlib.pyplot as plt
import numpy as np
import math

n=int(10000)
def F(x):
    if(x<=0):
        return 0
    elif(x>0 and x<n):
        return 1-np.exp(-x)
    elif(x>=n):
        return 1
    
X = np.linspace(-20,50,1000)#though n tends to infnity in solution, exp(-x) converges to 0  very fastly!
Y = [F(x) for x in X]

plt.plot(X,Y)
plt.xlabel('$x$')
plt.ylabel('$F_{n(1-T_{n})}(x)$')
plt.title('Cumulative Distribution Function')
plt.grid()
plt.show()