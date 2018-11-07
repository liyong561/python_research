from keras.datasets import mnist
import matplotlib.pyplot as plt
(train_images,train_labels),(test_images,test_labels)=mnist.load_data() 
# 看源码，就没有one hot 参数，要自实现。
print(train_images.shape,train_labels)
digit=train_images[4] # the 4th picture
print(train_labels[1])