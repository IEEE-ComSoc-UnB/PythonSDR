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
    
    def plot_psd(self,fc,samp_scale=256):
        # Update center frequency
        if self.sdr.center_freq != fc:
            self.sdr.center_freq = fc

        # Read samples
        samples = self.sdr.read_samples(samp_scale*1024)

        # use matplotlib to estimate and plot the PSD
        psd(samples, NFFT=1024, Fs=self.sdr.sample_rate/1e6, \
            Fc=self.sdr.center_freq/1e6)
        xlabel('Frequency (MHz)')
        ylabel('Relative power (dB)')

        show()
        
        # 
        
    def calc_psd(self,fc,samp_scale=256):
        if self.sdr.center_freq != fc:
            self.sdr.center_freq = fc

        smpls = self.sdr.read_samples(samp_scale*1024)

        # use matplotlib to estimate the PSD
        f, pow_sd = sig.welch(smpls,fs=self.sdr.sample_rate,nfft=1024,\
                              nperseg = 1024,return_onesided = False)
        
        f = f + fc
        
        pow_db = 10*np.log10(pow_sd)
        pow_db = pow_db - np.min(pow_db)
        
        return f, pow_db
    
    
    async def monitor_energy(self,fc,samp_scale,count_max):
        if self.sdr.center_freq != fc:
            self.sdr.center_freq = fc
        count = 0
        
        async for smpls in self.sdr.stream(num_samples_or_bytes=1024):
            count = count + 1
            pow_sd = np.sum(np.absolute(smpls)**2)
            
            pow_db = 10*np.log10(pow_sd)
            
            print(pow_db)
                
            if count > count_max:
                self.sdr.stop()
                
        self.sdr.close()
        
    async def monitor_energy_until(self,fc,thresh,samp_scale):
        if self.sdr.center_freq != fc:
            self.sdr.center_freq = fc
        
        async for smpls in self.sdr.stream(num_samples_or_bytes=1024):
            pow_sd = np.sum(np.absolute(smpls)**2)
            
            pow_db = 10*np.log10(pow_sd)
            
            print(pow_db)
                
            if pow_db > thresh:
                self.sdr.stop()
                
        self.sdr.close()
        print("Threshold reached!")
        
    def start_monitor_energy(self,fc,samp_scale = 256,count_max=50):
        asy.get_event_loop().run_until_complete(self.monitor_energy(fc,\
                          samp_scale,count_max))
        
    def start_monitor_energy_until(self,fc,thresh,samp_scale = 256):
        asy.get_event_loop().run_until_complete(self.monitor_energy_until(fc,\
                          thresh,samp_scale))