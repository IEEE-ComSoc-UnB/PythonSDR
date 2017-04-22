# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:41:22 2017

@author: Calil
"""

from scanner import Scanner

sample_rate = 2.048e6
gain = 4

scn = Scanner(sample_rate,gain)

center_freq = 96.2e6
samp_scale = 64

scn.plot_psd(center_freq,samp_scale)