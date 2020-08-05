# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:26:19 2020

@author: MRUTYUNJAY BISWAL
"""

import tensorflow as tf

dataset = tf.data.Dataset.range(10)
dataset = dataset.window(5, shift=1, drop_remainder=True) #drop_reaminder truncates the window less than window size

for window_dataset in dataset:
    for val in window_dataset:
        print(val.numpy(), end=" ")
    print()
    """
0 1 2 3 4 
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 
5 6 7 8 9 
"""
    
# convert to numpy data format
dataset = dataset.flat_map(lambda window : window.batch(5))
print(dataset)
for win in dataset:
    print(win.numpy())
"""
[0 1 2 3 4]
[1 2 3 4 5]
[2 3 4 5 6]
[3 4 5 6 7]
[4 5 6 7 8]
[5 6 7 8 9]
"""
# split into feature and label
    
dataset = dataset.map(lambda win : (win[:-1], win[-1:])) # last value is label and the rest is feature
for x, y in dataset:
    print(x.numpy(), y.numpy())

"""
[0 1 2 3] [4]
[1 2 3 4] [5]
[2 3 4 5] [6]
[3 4 5 6] [7]
[4 5 6 7] [8]
[5 6 7 8] [9]
"""

# shuffle the dataset before training
dataset = dataset.shuffle(buffer_size=10) # size of 10 ( dataset)
for x, y in dataset:
    print(x.numpy(), y.numpy())
    
# batching the data
dataset = dataset.batch(2).prefetch(1)
for x, y in dataset:
    print("x: ", x.numpy())
    print("y: ", y.numpy())
    