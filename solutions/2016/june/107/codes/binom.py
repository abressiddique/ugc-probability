from scipy.stats import binom
import matplotlib.pyplot as plt

sim_len = 1000000

X = binom.rvs(n = 100, p = 0.5, size = sim_len)
Y = binom.rvs(n = 100, p = 0.5, size = sim_len)

Z = X+Y

plt.hist(Z, bins = 200)
plt.show()
