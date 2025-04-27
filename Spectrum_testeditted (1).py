import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import signal
import os

# Directory where WAV files are stored
data_dir = r"C:\Users\sarin\OneDrive\Desktop\2025_02_19"

Central_freq = 1420  # MHz

def power_function(iq_array):
    """Calculate signal voltage from IQ data or mono WAV files."""
    if len(iq_array.shape) == 1:  # If mono
        signal_voltage = np.abs(iq_array)
    else:  # If stereo or IQ data
        signal_voltage = np.sqrt(iq_array[:, 0]**2 + iq_array[:, 1]**2)
    return signal_voltage


file_name1="09-31-16_1420000000Hz.wav"
file_path1 = os.path.join(data_dir, file_name1)  # Correct path joining
fs1, data1 = wavfile.read(file_path1)    
signal_voltage1 = power_function(data1)
freq1, spectrum1 = signal.welch(signal_voltage1, fs1, nperseg=1024)
Df = freq1[20] - freq1[19]  # Smallest frequency step

file_name2="09-53-27_1420000000Hz.wav"
file_path2 = os.path.join(data_dir, file_name2)  # Correct path joining
fs2, data2 = wavfile.read(file_path2)    
signal_voltage2 = power_function(data2)
freq2, spectrum2 = signal.welch(signal_voltage2, fs2, nperseg=1024)
Df = freq2[20] - freq2[19]  # Smallest frequency step

file_name3="10-18-26_1420000000Hz.wav"
file_path3 = os.path.join(data_dir, file_name3)  # Correct path joining
fs3, data3 = wavfile.read(file_path3)    
signal_voltage3 = power_function(data3)
freq3, spectrum3 = signal.welch(signal_voltage3, fs3, nperseg=1024)
Df = freq3[20] - freq3[19]  # Smallest frequency step

file_name4="10-40-54_1420000000Hz.wav"
file_path4 = os.path.join(data_dir, file_name4)  # Correct path joining
fs4, data4 = wavfile.read(file_path4)    
signal_voltage4= power_function(data4)
freq4, spectrum4 = signal.welch(signal_voltage4, fs4, nperseg=1024)
Df = freq4[20] - freq4[19]  # Smallest frequency step

file_name5="11-12-36_1420000000Hz.wav"
file_path5 = os.path.join(data_dir, file_name5)  # Correct path joining
fs5, data5 = wavfile.read(file_path5)    
signal_voltage5= power_function(data5)
freq5, spectrum5 = signal.welch(signal_voltage5, fs5, nperseg=1024)
Df = freq5[20] - freq5[19]  # Smallest frequency step

file_name6="11-45-08_1420000000Hz.wav"
file_path6 = os.path.join(data_dir, file_name6)  # Correct path joining
fs6, data6 = wavfile.read(file_path6)    
signal_voltage6= power_function(data6)
freq6, spectrum6 = signal.welch(signal_voltage6, fs6, nperseg=1024)
Df = freq6[20] - freq6[19]  # Smallest frequency step

file_name7="12-10-05_1420000000Hz.wav"
file_path7 = os.path.join(data_dir, file_name6)  # Correct path joining
fs7, data7 = wavfile.read(file_path7)    
signal_voltage7= power_function(data7)
freq7, spectrum7 = signal.welch(signal_voltage7, fs7, nperseg=1024)
Df = freq7[20] - freq7[19]  # Smallest frequency step

file_name8="12-52-23_1420000000Hz.wav"
file_path8 = os.path.join(data_dir, file_name8)  # Correct path joining
fs8, data8 = wavfile.read(file_path8)    
signal_voltage8= power_function(data8)
freq8, spectrum8 = signal.welch(signal_voltage8, fs8, nperseg=1024)
Df = freq8[20] - freq8[19]  # Smallest frequency step

file_name9="13-14-58_1420000000Hz.wav"
file_path9 = os.path.join(data_dir, file_name6)  # Correct path joining
fs9, data9 = wavfile.read(file_path9)    
signal_voltage9= power_function(data9)
freq9, spectrum9 = signal.welch(signal_voltage9, fs9, nperseg=1024)
Df = freq9[20] - freq9[19]  # Smallest frequency step

file_name10="13-57-14_1420000000Hz.wav"
file_path10 = os.path.join(data_dir, file_name10)  # Correct path joining
fs10, data10 = wavfile.read(file_path10)    
signal_voltage10= power_function(data10)
freq10, spectrum10 = signal.welch(signal_voltage10, fs10, nperseg=1024)
Df = freq10[20] - freq10[19]  # Smallest frequency step

file_name11="14-34-57_1420000000Hz.wav"
file_path11 = os.path.join(data_dir, file_name11)  # Correct path joining
fs11, data11 = wavfile.read(file_path11)    
signal_voltage11= power_function(data11)
freq11, spectrum11 = signal.welch(signal_voltage11, fs11, nperseg=1024)
Df = freq11[20] - freq11[19]  # Smallest frequency step

file_name12="15-02-22_1420000000Hz.wav"
file_path12 = os.path.join(data_dir, file_name12)  # Correct path joining
fs12, data12 = wavfile.read(file_path12)    
signal_voltage12= power_function(data12)
freq12, spectrum12 = signal.welch(signal_voltage12, fs12, nperseg=1024)
Df = freq12[20] - freq12[19]  # Smallest frequency step

file_name13="15-29-55_1420000000Hz.wav"
file_path13 = os.path.join(data_dir, file_name13)  # Correct path joining
fs13, data13 = wavfile.read(file_path13)    
signal_voltage13= power_function(data13)
freq13, spectrum13 = signal.welch(signal_voltage13, fs13, nperseg=1024)
Df = freq13[20] - freq13[19]  # Smallest frequency step

file_name14="16-07-06_1420000000Hz.wav"
file_path14 = os.path.join(data_dir, file_name10)  # Correct path joining
fs14, data14 = wavfile.read(file_path14)    
signal_voltage14= power_function(data14)
freq14, spectrum14 = signal.welch(signal_voltage14, fs14, nperseg=1024)
Df = freq14[20] - freq14[19]  # Smallest frequency step


file_name15="16-44-10_1420000000Hz.wav"
file_path15 = os.path.join(data_dir, file_name15)  # Correct path joining
fs15, data15 = wavfile.read(file_path15)    
signal_voltage15= power_function(data15)
freq15, spectrum15 = signal.welch(signal_voltage15, fs15, nperseg=1024)
Df = freq15[20] - freq15[19]  # Smallest frequency step
    # Plot
plt.figure(figsize=(13, 8))
plt.plot(freq1/ 1e6 + Central_freq, abs(spectrum1) * Df / 254400 * 1e6, linewidth=2,label=file_name1)
plt.plot(freq2/ 1e6 + Central_freq, abs(spectrum2) * Df / 254400 * 1e6, linewidth=2 ,label=file_name2)
plt.plot(freq3/ 1e6 + Central_freq, abs(spectrum3) * Df / 254400 * 1e6, linewidth=2 ,label=file_name3)
plt.plot(freq4/ 1e6 + Central_freq, abs(spectrum4) * Df / 254400 * 1e6, linewidth=2 ,label=file_name4)
plt.plot(freq5/ 1e6 + Central_freq, abs(spectrum5) * Df / 254400 * 1e6, linewidth=2 ,label=file_name5)
plt.plot(freq6/ 1e6 + Central_freq, abs(spectrum6) * Df / 254400 * 1e6, linewidth=2 ,label=file_name6)
plt.plot(freq7/ 1e6 + Central_freq, abs(spectrum7) * Df / 254400 * 1e6, linewidth=2 ,label=file_name7)
plt.plot(freq8/ 1e6 + Central_freq, abs(spectrum8) * Df / 254400 * 1e6, linewidth=2 ,label=file_name8)
plt.plot(freq9/ 1e6 + Central_freq, abs(spectrum9) * Df / 254400 * 1e6, linewidth=2 ,label=file_name9)
plt.plot(freq10/ 1e6 + Central_freq, abs(spectrum10) * Df / 254400 * 1e6, linewidth=2 ,label=file_name10)
plt.plot(freq11/ 1e6 + Central_freq, abs(spectrum11) * Df / 254400 * 1e6, linewidth=2 ,label=file_name11)
plt.plot(freq12/ 1e6 + Central_freq, abs(spectrum12) * Df / 254400 * 1e6, linewidth=2 ,label=file_name12)
plt.plot(freq13/ 1e6 + Central_freq, abs(spectrum13) * Df / 254400 * 1e6, linewidth=2 ,label=file_name13)
plt.plot(freq14/ 1e6 + Central_freq, abs(spectrum14) * Df / 254400 * 1e6, linewidth=2 ,label=file_name14)

plt.ylabel("Power (nW)", fontsize=20)
plt.xlabel("Frequency (MHz)", fontsize=20)
plt.legend(loc='lower right', fontsize=15, fancybox=True, shadow=True)
plt.grid(True)
plt.tick_params(labelsize=20)

    # Save the plot
#save_path = os.path.join(data_dir, f"{file_name1}_spectrum.png")
#plt.savefig(save_path)
#print(f"  Saved plot: {save_path}")

    # Show plot
plt.show()

