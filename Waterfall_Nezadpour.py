#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import glob
from datetime import datetime
from scipy import signal
from scipy.optimize import curve_fit
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter


# In[2]:


### Set These Parameters:

Dir = r"C:\Users\sarin\OneDrive\Desktop\2025_02_19"

start_time = datetime(2025, 2, 19, 9, 25, 0)
end_time = datetime(2025, 2, 19, 16, 58, 0)
Number_of_files_in_single_time_slot = 2

Central_freq = 1420 #MHz


# In[3]:


def power_function(iq_array):

    #print("Reading file ...")

    signal_voltage = np.sqrt( iq_array[:,0]**2 + iq_array[:,1]**2)


    return signal_voltage


# In[4]:


start_time = datetime(2024, 11, 18, 10, 20, 0)
end_time = datetime(2024, 11, 18, 18, 17, 0)
Number_of_files_in_single_time_slot = 1


# In[5]:


Waterfall_Size = 0
j = 0

for name in sorted(glob.glob(Dir+'/*.*')):
    time = datetime.strptime("2025_02_19_" + name.split("/")[-1].split(".")[0].split("_")[0], "%Y-%m-%d_%H-%M-%S")

    if (time >= start_time) & (time <= end_time):
        j = j + 1
        if j == Number_of_files_in_single_time_slot :
            Waterfall_Size = Waterfall_Size + 1
            j = 0


# In[7]:


power_2D = np.zeros((257, Waterfall_Size), float)
time_array = np.array([])

i = -1
j = 0

for name in sorted(glob.glob(Dir+'/*.*')):
    # Extract just the filename without path
    filename = name.split("\\")[-1]  # Use backslash for Windows
    # Remove extension and split by underscores
    time_part = filename.split(".")[0].split("_")[0]
    time = datetime.strptime("2025_02_19_" + time_part, "%Y-%m-%d_%H-%M-%S")


    if (time >= start_time) & (time <= end_time):
        fs, data = wavfile.read(name)
        signal_voltage = power_function(data)
        signal_voltage = np.append(signal_voltage, power_function(data))
        j = j + 1
        if j == Number_of_files_in_single_time_slot :
            i = i + 1
            freq, spectrum = signal.welch(signal_voltage, fs, nperseg=512)
            power_2D[:, i] = abs(spectrum) / 254400 * 1e12   #fW
            time_array = np.append(time_array, time)
            signal_voltage = np.array([])
            j = 0


# In[8]:


plt.figure(figsize=(13,8))

extent = [mdates.date2num(time_array[0]), mdates.date2num(time_array[-1]), freq[0]/1e6 + Central_freq, freq[-1]/1e6 + Central_freq]
plt.imshow(power_2D, origin='lower', extent=extent, interpolation='nearest', cmap='jet', vmin = 0, vmax = 12, aspect = 'auto')

#plt.title("Sun Observation (SABA Collaboration)", fontsize = 30)
#plt.imshow(H, extent=extent, interpolation='nearest', origin='lower',cmap=my_cmap, aspect=0.5)
plt.subplots_adjust(bottom=0.1, left=0.15, right=1., top=0.94, wspace = 0.01)

plt.ylabel("Frequency (MHz)", fontsize = 20)
plt.xlabel("Time (HH:MM)", fontsize = 20)
cbar = plt.colorbar(shrink=0.8)
cbar.ax.tick_params(labelsize=20)
cbar.set_label(label='Power (fW/Hz)' ,fontsize = 20)
plt.tick_params(labelsize=20)
#plt.axis.xaxis_date()
#plt.xlim(mdates.date2num(datetime(2024, 11, 18, 10, 50, 0)), mdates.date2num(datetime(2024, 11, 18, 15, 40, 0)))
plt.gca().xaxis.set_major_formatter( DateFormatter('%H:%M') )
plt.savefig("Waterfall_sun.png")
plt.show()
