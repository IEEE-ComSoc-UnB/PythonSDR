# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:19:28 2017

@author: Calil
"""

import matplotlib.pyplot as plt

from src.scanner import Scanner

sample_rate = 2.048e6
gain = 49.6

scn = Scanner(sample_rate,gain)

center_freq = 312e6

scn.plot_psd(center_freq)

f, pow_db = scn.calc_psd(center_freq)

plt.plot(f,pow_db)
plt.xlabel('Frequency [Hz]')
plt.ylabel('PSD [dB]')
plt.grid(True)
plt.show()

thresh = 5.4

#scn.start_monitor_psd(center_freq,count_max=200,monit="MEAN")
scn.start_monitor_psd_until(center_freq,thresh,count_max=200,monit="MEAN")
print("END")
