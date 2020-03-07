import matplotlib.pyplot as plt
import numpy as np
import wave

file = 'piano.wav'

with wave.open(file,'r') as wav_file:
    #Extract Raw Audio from Wav File
    signal = wav_file.readframes(-1)
    signal = np.fromstring(signal, 'Int16')

    #Split the data into channels 
    channels = [[] for channel in range(wav_file.getnchannels())]
    for index, datum in enumerate(signal):
        channels[index%len(channels)].append(datum)

    #Get time from indices
    fs = wav_file.getframerate()
    Time=np.linspace(0, len(signal)/len(channels)/fs, num=len(signal)/len(channels))

    #Plot
    plt.figure(1)
    plt.title('Signal Wave...')
    for channel in channels:
        plt.plot(Time,channel)
    plt.show()