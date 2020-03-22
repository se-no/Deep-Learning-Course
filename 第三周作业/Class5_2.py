import os
import numpy as np
x= np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

xa=x.sum()/x.size
ya=y.sum()/y.size
flag=1
wue=wst=0
while flag<x.size:
    wue+=(x[flag]-xa)*(y[flag]-ya)
    wst+=(x[flag]-xa)**2
    flag+=1
w=wue/wst
b=ya-w*xa
print("W = %f,b = %f"%(w,b))
os.system("pause")