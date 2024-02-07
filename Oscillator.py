import matplotlib.pyplot as plt
from sympy import sympify, sin, cos, sinc
from math import cos
from sympy import Symbol,diff,lambdify
from numpy import pi
import numpy as np
from numpy import fft
class Oscillator():
    def __init__(self,fl,amplitude):
        self.fl=fl
        self.a=amplitude
        t = np.linspace(0, 5, 10000000)
        self.signal=self.a*np.cos(2*pi*fl*t)
    def getSignal(self):
        return fft.fft(self.signal)
    def getfl(self):
        return self.fl
