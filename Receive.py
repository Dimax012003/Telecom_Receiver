import matplotlib.pyplot as plt
from sympy import sympify, sin, cos, sinc
from math import cos
from sympy import Symbol,diff,lambdify
from numpy import pi
import numpy as np
from numpy import fft
from tkinter import *
class Receive():
    def __init__(self,display,t,frequency,amplitude):
        self.frequencies_list=[]
        self.display = display
        self.f = frequency
        self.A=amplitude
        self.t=t
        self.fun=[]
        self.function1 = lambda t:self.A*cos(2*pi*self.f*t)
        self.expr = self.A*np.cos(self.f*t*2*pi)
        t1 = np.linspace(0, 5, 10000000)
        self.frequencies_list.append(self.f)
        self.signal = np.fft.fft(self.A *5/10000000* np.cos(t1 * self.f * pi * 2)+5/10000000*np.random.normal(0,1,10000000))
    def get_function(self):
        return self.function1
    def set_plot(self):
        self.display = True
    def get_status(self):
        return self.display
    def frequency(self):
        return self.f
    def Spectrum(self):
        return self.signal
    def get_samples(self,t):
        for i in range(0,len(t)):
            self.fun.append(self.function1(t[i]))
        return self.fun
    def frequencies(self):
        sum=0
        for freqs in self.frequencies_list:
            sum+=freqs
        freq={
            "min":int(min(self.frequencies_list)),
            "center":0,
            "max":int(max(self.frequencies_list)),
        }
        if len(self.frequencies_list)==1:
            freq["center"]=self.f
        else :freq["center"]=int(sum/len(self.frequencies_list))
        return freq
    def add_signal(self,receive):
        self.frequencies_list.append(receive.frequency())
        self.signal=receive.Spectrum()+self.signal
        return self.signal
