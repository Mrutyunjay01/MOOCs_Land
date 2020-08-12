# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-1.5, 1.5, 0.0003)  # time axis
fun = 0 * t
T = 1/2
T1 = 1/4
Tp = 100
t2 = np.arange(-6 * T1, 6 * T1, 0.01)
y2 = []
for i in t2:
    if (i < -T1 and i > -3 * T1) or (i < 3 * T1 and i > T1) or i < -5 * T1 or i > 5 * T1:
        check = 0
    else:
        check = 1
        
    y2.append(check)


harmonics = [1, 2, 3, 5, 10, 50]

# iterate through harmonics
for h in harmonics:
    print(h)
    fun = 0 * t
    Ck = 0
    fk = 0
    Carr = []
     
    for k in np.arange(-h, h, 1):
         
        if k ==0:
            continue
        Ck = 1/2 * np.sinc(k/2)
        fk = Ck * np.exp(2 * np.pi * k * t * 1j)
        fun += fk
        
        Carr.append(Ck)
    
    fun += 1/2
    print(Carr)
    plt.figure()
    plt.plot(t, fun)