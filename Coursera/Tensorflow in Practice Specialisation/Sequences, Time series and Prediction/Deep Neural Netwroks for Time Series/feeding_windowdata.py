# -*- coding: utf-8 -*-

"""
Created on Fri Jul 10 20:26:19 2020

@author: MRUTYUNJAY BISWAL
"""

import tensorflow as tf
import numpy as np

def window_dataset(series, window_size, batch_sized, shuffle_buffer):
    
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size +1, shift=1, drop_remainder=True)
    dataset = dataset.flat_map(lambda win : win.batch(window_size + 1))
    dataset = dataset.shuffle(shuffle_buffer).map(lambda win : (win[:-1], win[-1:]))
    dataset = dataset.batch(batch_sized).prefetch(1)
    
    return dataset
    pass

# preparing the data
def trend(time, slope=0):
    return slope * time

def seasonal_pattern(season_time):
    """Just an arbitrary pattern, you can change it if you wish"""
    return np.where(season_time < 0.4,
                    np.cos(season_time * 2 * np.pi),
                    1 / np.exp(3 * season_time))

def seasonality(time, period, amplitude=1, phase=0):
    """Repeats the same pattern at each period"""
    season_time = ((time + phase) % period) / period
    return amplitude * seasonal_pattern(season_time)

def noise(time, noise_level=1, seed=None):
    rnd = np.random.RandomState(seed)
    return rnd.randn(len(time)) * noise_level

time = np.arange(4 * 365 + 1, dtype="float32")
baseline = 10
series = trend(time, 0.1)  
baseline = 10
amplitude = 40
slope = 0.05
noise_level = 5

# Create the series
series = baseline + trend(time, slope) + seasonality(time, period=365, amplitude=amplitude)
# Update with noise
series += noise(time, noise_level, seed=42)

split_time = 1000
time_train = time[:split_time]
x_train = series[:split_time]
time_valid = time[split_time:]
x_valid = series[split_time:]

# define the parameters for the dataset
WINDOW_SIZE = 20
BATCH_SIZE = 32
SHUFFLE_BUFFER_SIZE = 1000

dataset = window_dataset(series, window_size=WINDOW_SIZE, batch_sized=BATCH_SIZE,
                         shuffle_buffer=SHUFFLE_BUFFER_SIZE)
# make a simple linear reg Model
l0 = tf.keras.layers.Dense(1, input_shape=[WINDOW_SIZE])
model = tf.keras.models.Sequential([l0])

model.compile(loss='mse',
              optimizer=tf.keras.optimizers.SGD(lr=1e-6, momentum=0.9))
model.fit(dataset, epochs=100, verbose=1)
print('Layer Weights {}'.format(l0.get_weights()))

forecast = []
for time in range(len(series) - WINDOW_SIZE):
    forecast.append(model.predict(series[time : time + WINDOW_SIZE][np.newaxis]))
    
forecast = forecast[split_time - WINDOW_SIZE : ]
results = np.array(forecast)[:, 0, 0]
print(results)
print('Mean absolute Error: {}'.format(tf.keras.metrics.mean_absolute_error(x_valid, results).numpy()))