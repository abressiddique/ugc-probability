import numpy as np
import math
import matplotlib.pyplot as plt

simlen = int(1e6)

theta = 4.5

n1 = 30     
n2= 20      
n3 = 10     #three values of n

#n1
sum_arr = np.zeros(1000)
count_arr = np.zeros(1000)
res_arr = np.zeros(1000)
s = np.random.exponential(theta, (simlen, n1))
for i in range(simlen):
    x1 = min(s[i])
    t = sum(s[i])
    sum_arr[math.ceil(t)]+= x1
    count_arr[math.ceil(t)]+=1

for i in range(200):
    res_arr[i] = (sum_arr[i])/(count_arr[i])

def func(x):
    return x/(n1*n1)

vec_func = np.vectorize(func)
x = np.arange(1, 100, 1)

plt.plot(x, vec_func(x))
plt.plot(x, res_arr[x])


#n2
sum_arr = np.zeros(500)
count_arr = np.zeros(500)
res_arr = np.zeros(500)
s = np.random.exponential(theta, (simlen, n2))
for i in range(simlen):
    x1 = min(s[i])
    t = sum(s[i])
    sum_arr[math.ceil(t)]+= x1
    count_arr[math.ceil(t)]+=1

for i in range(150):
    res_arr[i] = (sum_arr[i])/(count_arr[i])

def func(x):
    return x/(n2*n2)

vec_func = np.vectorize(func)
x = np.arange(1, 100, 1)

plt.plot(x, vec_func(x))
plt.plot(x, res_arr[x])

#n3
sum_arr = np.zeros(500)
count_arr = np.zeros(500)
res_arr = np.zeros(500)
s = np.random.exponential(theta, (simlen, n3))
for i in range(simlen):
    x1 = min(s[i])
    t = sum(s[i])
    sum_arr[math.ceil(t)]+= x1
    count_arr[math.ceil(t)]+=1

for i in range(100):
    res_arr[i] = (sum_arr[i])/(count_arr[i])

def func(x):
    return x/(n3*n3)

vec_func = np.vectorize(func)
x = np.arange(1, 100, 1)

plt.plot(x, vec_func(x))
plt.plot(x, res_arr[x])
plt.xlabel("$t$")
plt.ylabel("$E(X_{(1)}|T=t)$")
plt.legend(["Theoretical plot for n = 30", "Simulated plot for n = 30", "Theoretical plot for n = 20", "Simulated plot for n = 20", "Theoretical plot for n = 10", "Simulated plot for n = 10"])
plt.grid()
plt.show()