import numpy as np
import matplotlib.pyplot as plt

Dir = "/Volumes/MORLOX/Radio-telescope-data/11-18-24/sun/IQ/2024_11_18/"

Central_freq = 1420 #MHz

def power_function(iq_array):

    print("Reading file ...")

    signal_voltage = np.sqrt( iq_array[:,0]**2 + iq_array[:,1]**2)


    return signal_voltage

#Reading the file

file_name_1 = "10-25-00_1420000000Hz.wav"

fs, data_1 = wavfile.read(Dir + file_name_1)

signal_voltage_1 = power_function(data_1)

#Evaluating the spectrum
freq_1, spectrum_1 = signal.welch(signal_voltage_1, fs, nperseg=1024)

Df = freq_1[20]-freq_1[19]

#Plotting

plt.figure(figsize=(13,8))

plt.plot(freq_1/1e6 + Central_freq, abs(spectrum_1) * Df / 254400 * 1e6, linewidth = 2, label = '10:25')

plt.ylabel("Power (nW)", fontsize = 20)
plt.xlabel("Frequency (MHz)", fontsize = 20)
plt.legend(loc='lower right',fontsize=15,fancybox=True, shadow=True)
plt.grid(True)
plt.tick_params(labelsize=20)
#plt.yscale('log')
#plt.xlim(1420.25,1420.3)
#plt.ylim(0.125, 0.2)
plt.savefig("test.png")
plt.show()
