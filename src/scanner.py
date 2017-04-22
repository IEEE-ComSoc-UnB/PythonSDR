# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:06:19 2017

Code adapted from: https://pypi.python.org/pypi/pyrtlsdr

@author: Calil
"""

from pylab import psd, xlabel, ylabel, show
from rtlsdr import RtlSdr

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