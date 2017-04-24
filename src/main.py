# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:41:22 2017

@author: Calil
"""

from pygame import mixer
from time import sleep

from scanner import Scanner

mixer.init()
mixer.music.load('C:/Users/Calil/Documents/RPi & SDR/SDR/PythonSDR/audio/car_alarm_short.mp3')

sample_rate = 2.048e6
gain = 49.6

scn = Scanner(sample_rate,gain)

center_freq = 433.9e6
thresh = 7.0

scn.start_monitor_psd_until(center_freq,thresh,monit="MEAN")

mixer.music.play()
sleep(1)

print("END")