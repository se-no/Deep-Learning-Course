import tensorflow as tf
import numpy as np
x = np.array([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = np.array([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
x = tf.constant(x)
y = tf.constant(y)
w = (len(x)*tf.reduce_sum(x * y) - tf.reduce_sum(x)*tf.reduce_sum(y))/ (len(x)*tf.reduce_sum(tf.pow(x,2))-tf.reduce_sum(x)**2)
b = (tf.reduce_mean(y) - w * tf.reduce_mean(x))/ len(x)
print("w={}\nb={}".format(w,b))