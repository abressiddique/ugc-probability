import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sample_size=10000
k=[0]*sample_size
X=[0]*sample_size
count=0
exp=0
expx=0
expy=0
Y=np.random.normal(size=sample_size)
for i in range(sample_size):
    k[i]=np.random.choice([-1,1],p=[0.5,0.5])
    X[i]=k[i]*Y[i]
    exp+=X[i]*Y[i]
    expx+=X[i]
    expy+=Y[i]
    if X[i]<0 and Y[i]<0:
        count+=1
print("P(X<0,y<0)=%f"%(count/sample_size))
print("cov(X,Y)=%f"%(exp/sample_size**2-(expx*expy/sample_size**2)))


sns.distplot(Y,label='Y' ,hist=False)
sns.distplot(X,label='X', hist=False)
plt.legend()
plt.show()