import matplotlib.pyplot as plt
from scipy.fft import fft
import numpy as np
import wave
import sys


# spf = wave.open("e4.wav", "r")

# spf = wave.open("piano.wav", "r")
wavs = ['e4', 'c4']
# wavs = ['12-M1']

combined = []
plt.figure(1, figsize=(14,8))

# Number of sample points
N = 600

for wavFile in wavs:
	spf = wave.open(wavFile + '.wav', 'r')	
	signal = spf.readframes(-1)
	signal = np.frombuffer(signal, dtype="int16")
	fs = spf.getframerate()

	num_channels = spf.getnchannels()

	channels = [signal[channel::num_channels] for channel in range(num_channels)]
	# if wavFile == 'e4':
	# 	channels = [channel[:2000]/2 for channel in channels]
	# elif wavFile == 'c4':
	# 	channels = [channel[:2000] for channel in channels]
	# else:
	# 	channels = [channel[70000:120000] for channel in channels]
	channels = [channel[:N] for channel in channels]

	for channel in channels:
		Time=np.linspace(0, len(channel)/fs, num=len(channel))
		combined.append(channel)
		# plt.plot(Time, channel)
combined = np.sum(combined, axis = 0)//len(combined)


# sample spacing
T = 1.0 / 800.0
yf = fft(combined)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

plt.title("Signal Wave...")
# plt.plot(Time, combined)
plt.show()
print(len(yf))
