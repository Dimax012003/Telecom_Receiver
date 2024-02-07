from numpy import pi
import numpy as np
from numpy import fft
import cmath
class Iffilter():
    def __init__(self,fif,W):
        self.fif=fif
        self.W=W
    def create_filter(self):
        f = fft.fftfreq(10000000, d=5 / 10000000)
        t=np.linspace(0,5,10000000)
        self.Hf=fft.fft(2*self.W*np.sinc(self.W*t)*np.cos(2*pi*self.fif*t))
    def get_Spectrum(self):
        return self.Hf