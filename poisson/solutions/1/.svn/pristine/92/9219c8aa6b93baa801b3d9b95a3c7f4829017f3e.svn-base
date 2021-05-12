#Assignment-4
import collections
import numpy as np
import random
import matplotlib.pyplot as plt
import scipy

def CountFrequency(arr):
    return collections.Counter(arr)  
simlen = 10000
x = np.linspace(0,150,100)
#Taking lambda = 5
s = np.random.poisson(5, simlen)
#count, bins, ignored = plt.hist(s, 14, density=True)
#plt.show()
freq = CountFrequency(s)
# iterate dictionary named as freq to print
# count of each element
freqArrayX = np.zeros(25)
freqArrayY = np.zeros(100)
for (key, value) in freq.items():
    print (key, " -> ", value)
    freqArrayX[key] = value
    if (key*key) + 3 < 100:
      freqArrayY[(key*key) + 3] = value
y = np.random.poisson(5,simlen)
freqArrayYExpFunc = CountFrequency(y)
freqArrayYExp = np.zeros(100)
for (key,value) in freqArrayYExpFunc.items():
    if (key*key) + 3 < 100:
      freqArrayYExp[(key*key) + 3] = value

plt.stem(freqArrayY, markerfmt='o', use_line_collection=True, label = 'Simulated')
plt.stem(freqArrayYExp, markerfmt='o', use_line_collection=True, label = 'Theoretical')
plt.legend()
plt.grid()
plt.show()
plt.stem(freqArrayX, markerfmt='o', use_line_collection=True, label = 'X')
plt.legend()
plt.grid()