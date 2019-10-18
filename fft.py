from scipy import signal
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np

N = 256                     # number of samples
T = 0.01                    # time between samples
t = np.linspace(0, N*T, N)  # time array

squ3Hz  = signal.square(2 * np.pi * 3 * t)
sin3Hz  = np.sin(2 * np.pi * 3 *t)
sin9Hz  = np.sin(2 * np.pi * 9 *t)
# N//4 performs int division by 4

# now calculate the fft for these signals
sinf = fft(sin3Hz)
squf = fft(squ3Hz)
freq = np.linspace(0, 1/(2*T), N//2)
plt.plot(freq, 2/N*np.abs(sinf[0:N//2]), freq, 2/N*np.abs(squf[0:N//2]))
plt.grid(True)
plt.xlabel("freq - Hz")
plt.savefig("fft.png")

plt.clf()
plt.plot(t[:N//4], 1.1*sin3Hz[:N//4], 
         t[:N//4], squ3Hz[:N//4], 
         t[:N//4], 1.1*sin3Hz[:N//4] + 0.4*sin9Hz[:N//4])
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xlabel("time - sec")
plt.savefig("timeSignals.png")
