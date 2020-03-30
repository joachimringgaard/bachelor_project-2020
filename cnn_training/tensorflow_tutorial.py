#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
layers = tf.keras.layers
print(tf.__version__)

mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape,"\n",len(train_labels))


numpy_matrix = np.ndarray((1000,1)).reshape((10,10,10))

print(numpy_matrix.ndim, numpy_matrix.shape, numpy_matrix.dtype)

digit = train_images[4]

plt.imshow(digit, cmap=plt.cm.binary)
plt.show()