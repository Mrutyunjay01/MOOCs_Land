import numpy as np
import matplotlib.pyplot as plt
import math

t = np.arange(1, 10, 0.01)
x = np.sin(2  * math.pi * t)

plt.plot(t, x)