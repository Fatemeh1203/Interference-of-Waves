import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)
x = np.arange(0, 10, 0.01)
a1, f1, phi1 = 1, 10, 0
a2, f2, phi2 = 5, 10, 0
landa1 = 0.1
landa2 = 0.1
k1 = 2*np.pi*landa1
k2 = 2*np.pi*landa2
y1 = a1 * np.sin((k1*x) - (2 * np.pi * f1 * t) + phi1)
y2 = a2 * np.sin((k2*x) + (2 * np.pi * f2 * t) + phi2)
yt = y1 + y2

fig, (ax0, ax1, ax2) = plt.subplots(3, sharex=True, figsize=(10,5))

ax0.plot(t, yt, 'c')
ax0.set_ylabel("sum")

ax1.plot(t, y1, 'b')
ax1.set_ylabel("signal 1")

ax2.plot(t, y2, 'r')
ax2.set_ylabel("signal 2")
ax2.set_xlabel("time in s")

plt.show()
