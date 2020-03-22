import os
import numpy as np
np.random.seed(612)
a = np.random.randn(1000)
x = int(input("请输入一个1-100之间的整数:"))
print("序号\t索引值\t随机数")
i=1
y=x
while x <= 1000:
    print("%d\t%d\t%f" %(i,x,a[x-1]))
    i+=1
    x+=y
os.system("pause")
