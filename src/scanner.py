# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:06:19 2017

Code adapted from: https://pypi.python.org/pypi/pyrtlsdr

@author: Calil
"""

from pylab import psd, xlabel, ylabel, show
import scipy.signal as sig
from rtlsdr import RtlSdr
import numpy as np
import asyncio as asy

class Scanner(object):
    
    def __init__(self,sample_rate,gain):
        self.sdr = RtlSdr()

        # configure device
        self.sdr.sample_rate = sample_rate
        self.sdr.gain = gain
    
    def plot_psd(self,fc,samp_scale):
        self.sdr.center_freq = fc

        samples = self.sdr.read_samples(samp_scale*1024)

        # use matplotlib to estimate and plot the PSD
        psd(samples, NFFT=1024, Fs=self.sdr.sample_rate/1e6, \
            Fc=self.sdr.center_freq/1e6)
        xlabel('Frequency (MHz)')
        ylabel('Relative power (dB)')

        show()
        
    def calc_psd(self,fc,samp_scale):
        self.sdr.center_freq = fc

        smpls = self.sdr.read_samples(samp_scale*1024)

        # use matplotlib to estimate and plot the PSD
        f, pow_sd = sig.welch(smpls,fs=self.sdr.sample_rate,nfft=1024,\
                              nperseg = 1024,return_onesided = False)
        
        return f,10*np.log10(pow_sd)
    
    
    async def monitor_psd(self,fc,samp_scale,count_max):
        self.sdr.center_freq = fc
        count = 0
        
        async for smpls in self.sdr.stream():
            count = count + 1
            f, pow_sd = sig.welch(smpls,fs=self.sdr.sample_rate,nfft=1024,\
                              nperseg = 1024,return_onesided = False)
            print(np.max(10*np.log10(pow_sd)))
            
            if count > count_max:
                self.sdr.stop()
                
        self.sdr.close()
        
    def start_monitor(self,fc,samp_scale,count_max=10):
        asy.get_event_loop().run_until_complete(self.monitor_psd(fc,\
                          samp_scale,count_max))