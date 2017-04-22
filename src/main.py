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
samp_scale = 128

scn.plot_psd(center_freq,samp_scale)

f, pow_sd = scn.calc_psd(center_freq,samp_scale)

plt.plot(f,np.sqrt(pow_sd))
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V RMS]')
plt.show()