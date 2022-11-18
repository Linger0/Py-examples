import math
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-poster')

# iterative cooley tukey fft for dyadics
def fft(v):
    n, h  = len(v), len(v) >> 1
    old, new = v[:], [0] * n
    sublen, stride = 1, n

    while sublen < n:
        stride >>= 1
        for k in range(0, n, 2*stride):
            for i in range(stride):
                omega = math.exp(math.pi * k / n)
                new[i+(k>>1)]   = old[i+k] + omega * old[i+k+stride]
                new[i+(k>>1)+h] = old[i+k] - omega * old[i+k+stride]
        old, new = new, old
        sublen <<= 1

    return old

# sampling rate
sr = 128
# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)

freq = 1.
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7
x += 0.5* np.sin(2*np.pi*freq*t)

plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')

plt.show()

X=fft(x)

# calculate the frequency
X = np.array(X)
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T

plt.figure(figsize = (12, 6))
plt.subplot(121)
plt.stem(freq, abs(X), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

# normalize the amplitude
X_oneside =X[:n_oneside]/n_oneside

plt.subplot(122)
plt.stem(f_oneside, abs(X_oneside), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('Normalized FFT Amplitude |X(freq)|')
plt.tight_layout()
plt.show()