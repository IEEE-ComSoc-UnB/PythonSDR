# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:41:22 2017

@author: Calil
"""

from pygame import mixer
from time import sleep

from scanner import Scanner

# Itialize music mixer
mixer.init()
mixer.music.load('../audio/car_alarm_short.mp3')

# RTL Parameters
sample_rate = 2.048e6
gain = 49.6

scn = Scanner(sample_rate,gain)

# Scanner parameters
center_freq = 433.9e6
#center_freq = 96.1e6
thresh = 10

# Start monitoring
scn.start_monitor_energy_until(center_freq,thresh)

mixer.music.play()
sleep(1)

print("END")