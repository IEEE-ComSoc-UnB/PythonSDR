# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:41:22 2017

@author: Calil
"""

import matplotlib.pyplot as plt
import numpy as np

from scanner import Scanner

sample_rate = 2.048e6
gain = 4

scn = Scanner(sample_rate,gain)

center_freq = 96.1e6
smp_scale = 128

scn.plot_psd(center_freq,smp_scale)

f, pow_db = scn.calc_psd(center_freq,smp_scale)

print(np.max(pow_db))

plt.plot(f,pow_db)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [dB]')
plt.grid(True)
plt.show()

scn.start_monitor(center_freq,smp_scale,50)