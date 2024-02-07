import matplotlib.pyplot as plt
from sympy import sympify, sin, cos, sinc
from math import cos
from sympy import Symbol,diff,lambdify
from numpy import pi
import numpy as np
from numpy import fft
import cmath
class Rffilter():
    def __init__(self,flow,fhigh):
        self.flow=flow
        self.fhigh=fhigh
        self.fcenter=(fhigh+flow)/2
    def create_filter(self):
        f = fft.fftfreq(10000000, d=5 / 10000000)
        t=np.linspace(0,5,10000000)
        W=self.fhigh-self.flow
        self.Hf=fft.fft(2*0.1*np.sinc(W*t)*np.cos(2*pi*self.fcenter*t))
    def get_Spectrum(self):
        return self.Hf