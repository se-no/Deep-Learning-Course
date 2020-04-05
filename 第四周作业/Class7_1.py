import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.ticker import  MultipleLocator
title = ["R-缩放","G-镜像+旋转","B-裁剪","RGB"]
plt.rcParams["font.sans-serif"] = "SimHei"
plt.tight_layout(rect=[0,0,1,0.8])
path = "C:/Users/Administrator/Desktop/lena/"
img =Image.open(path+"lena512color.tiff")
img_r,img_g,img_b = img.split()
img_rgb = Image.merge("RGB",[img_r,img_g,img_b])
imgs = [img_r,img_g,img_b,img_rgb]
imgs[0] = imgs[0].resize((50,50))    #R
imgs[1] = imgs[1].transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)  #G
imgs[2] = imgs[2].crop((0,0,300,300))   #B
plt.tight_layout(rect=[0,0,1,0.8])
for i in range(4):

    plt.subplot(2,2,i+1)
    plt.title(title[i],fontsize = 14)
    plt.tight_layout(rect=[0,0,1,0.9])
    if i != 1:
        plt.axis("off")
    else:
        plt.axis("on")
        ax=plt.subplot(2,2,i+1)
        xmajorLocator = MultipleLocator(200)
        ymajorLocator = MultipleLocator(100)
        ax.xaxis.set_major_locator(xmajorLocator)
        ax.yaxis.set_major_locator(ymajorLocator)
    plt.imshow(imgs[i], cmap='gray') 
plt.suptitle("图像基本操作",fontsize=20,color="B")
plt.show()
imgs[3].save(path+"test.png")
os.system("pause")