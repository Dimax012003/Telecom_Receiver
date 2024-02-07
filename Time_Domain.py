import matplotlib.pyplot as plt
import numpy as np
from scipy import fft
from math import sqrt
class TimeDomain():
    def __init__(self,tstart,tstop,step,receiver):
        self.tstart=tstart
        self.tstop=tstop
        self.step=step
        self.t=np.arange(tstart,tstop,step)
        self.receiver=receiver
    def plot_time(self,receive):

        plt.plot(self.t,fft.ifft(receive.Spectrum()))
        plt.grid(True)
        plt.ylabel('x(t)')
        plt.xlabel('t')
        plt.show()
    def plot_spectrum(self,RF,Oscillator,IF,LPF):
        f=fft.fftfreq(10000000,d=5/10000000)

        rf=RF.get_Spectrum().real**2
        sig=(abs(self.receiver.Spectrum().real*rf))

        new_sig=fft.ifft(sig)*fft.ifft(Oscillator.getSignal().real)
        new_sig1=fft.fft(new_sig).real

        If=IF.get_Spectrum().real**2
        new_sig2=abs(If*new_sig1).real/100000000000

        time_sig1=fft.ifft(new_sig2)*fft.ifft(Oscillator.getSignal().real)
        new_sig3=fft.fft(time_sig1).real
        new_sig4=new_sig3*(LPF.get_Spectrum().real**2)

        fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
        ax[0][0].plot(f, self.receiver.Spectrum())
        ax[0][1].plot(f, sig)
        ax[0][2].plot(f, new_sig1)
        ax[1][0].plot(f, new_sig2)
        ax[1][1].plot(f, new_sig3)
        ax[1][2].plot(f, new_sig4)

        for i in range(0,2):
            for j in range(0,3):
                ax[i][j].grid(True)

        plt.grid(True)
        plt.ylabel('X(f)')
        plt.xlabel('f(MHz)')
        plt.show()