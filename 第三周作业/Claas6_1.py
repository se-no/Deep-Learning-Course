import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

#���ز�ʿ�ٷ�������
boston_housing = tf.keras.datasets.boston_housing
(x, y), (_, _) = boston_housing.load_data(test_split=0)

#��ʼ����
plt.rcParams['font.sans-serif'] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False

titles = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "TAX", "PTRATIO", "B-1000", "LSTAT", "MEDV"]

#------------------------------------------------------------1
#��ʾ���������뷿�۹�ϵ
plt.figure(figsize=(12, 12))

for i in range(13):
    plt.subplot(4, 4, (i+1))
    plt.scatter(x[:, i], y)
    plt.xlabel(titles[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i+1) + "." + titles[i] + " - Price")

plt.tight_layout(rect = [0, 0, 1, 0.9])

# plt.tight_layout()

plt.suptitle("���������뷿�۵Ĺ�ϵ", x=0.5, fontsize=20)
plt.show()


#---------------------------------------------------------------2
for i in range(13):
    print(i+1, "-", titles[i])

inr = int(input("��ѡ�����ԣ�"))

#��ʾָ�������뷿�۹�ϵ
plt.figure(num = titles[inr-1])
plt.subplot(111)
plt.scatter(x[:, inr-1], y)
plt.xlabel(titles[inr-1])
plt.ylabel("Price($1000's)")
plt.title(str(inr) + "." + titles[inr-1] + " - Price")
plt.show()