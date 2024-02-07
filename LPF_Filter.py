from numpy import pi
import numpy as np
from numpy import fft
class LPF():
    def __init__(self,W):
        self.W=2*W+2
    def create_filter(self):
        f = fft.fftfreq(10000000, d=5 / 10000000)
        t=np.linspace(0,5,10000000)
        self.Hf=fft.fft(0.1*np.sinc(self.W*t))
    def get_Spectrum(self):
        return self.Hf