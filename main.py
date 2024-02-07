import numpy as np
from tkinter import *
from Receive import Receive
from Time_Domain import TimeDomain
from RF_Filter import Rffilter
from Oscillator import Oscillator
from IF_Filter import Iffilter
from LPF_Filter import LPF
global time
def close_window():
    print("Τερματισμος")
    root.destroy()
# Δημιουργία βασικού παραθύρου
root = Tk()
root.title("Hyperheterodyne Receiver")
label = Label(root, text="High Side Injection")
label.pack()

t=np.arange(0,100,0.00001)
time=TimeDomain(0,0,0.1,0)
def signal():
    root7=Tk()
    text=Entry(root7,font=("Arial black",8))
    text.grid(padx=5,pady=5)
    text.grid(row=0,column=2)
    a=Entry(root7,font=("Arial black",8))
    a.grid(padx=5,pady=5)
    a.grid(row=2,column=2)

    def sss():
        f=text.get()
        A=a.get()
        try:
            f=float(f)
            A=float(A)
        except:
            print("error")
        global receive
        receive=Receive(True, t, f,A)
    label1= Label(root7,text="f(Hz)=")
    label1.grid(row=0,column=1)
    label2=Label(root7,text="Amplitude(Volts)")
    label2.grid(row=2,column=1)
    button = Button(root7, text="εκτελεση", command=sss)
    button.grid(row=2,column=3,columnspan=10)
def adjust_signal():
    root1=Tk()
    text=Entry(root1,font=("Arial black",8))
    text.grid(padx=5,pady=10)
    text.grid(row=0,column=2)
    a=Entry(root1,font=("Arial black",8))
    a.grid(padx=5,pady=5)
    a.grid(row=2,column=2)
    label1= Label(root1,text="f(Hz)=")
    label1.grid(row=0,column=1)
    label2=Label(root1,text="Amplitude(Volts)")
    label2.grid(row=2,column=1)
    def sss():
        f=text.get()
        A=a.get()
        try:
            f=float(f)
            A=float(A)
        except:
            print("error")

        new_receive = Receive(True, t, f,A)
        receive.add_signal(new_receive)
        print(receive.Spectrum())
        print(receive.get_function())
    button = Button(root1, text="εκτελεση", command=sss)
    button.grid(row=2,column=3,columnspan=10)
def plot_time():
    time = TimeDomain(0, 10 / (receive.frequency()), 1 / (receive.frequency() * 1000000), receive)
    time.plot_time(receive)
def plot_spectrum():
    time = TimeDomain(0, 10 / (receive.frequency()), 1 / (receive.frequency() * 10000), receive)

    IF = Iffilter(abs(osci.getfl() - receive.frequencies()["center"]), receive.frequencies()["max"]-receive.frequencies()["min"]+2000)
    IF.create_filter()
    lpf = LPF(receive.frequencies()["max"])
    lpf.create_filter()
    time.plot_spectrum(RF,osci,IF,lpf)
def RF_Filter():
    root1=Tk()
    floor=Entry(root1,font=("Arial black",8))
    floor.grid(padx=5,pady=5)
    floor.grid(row=0,column=2)
    top=Entry(root1,font=("Arial black",8))
    top.grid(padx=5,pady=5)
    top.grid(row=2,column=2)
    def sss():
        fl=floor.get()
        fh=top.get()
        try:
            fl=float(fl)
            fh=float(fh)
        except:
            print("error")
        global RF
        RF = Rffilter(fl, fh)
        RF.create_filter()
    label1= Label(root1,text="Low Frequency")
    label1.grid(row=0,column=1)
    label2=Label(root1,text="High Frequency")
    label2.grid(row=2,column=1)
    button = Button(root1, text="εκτελεση", command=sss)
    button.grid(row=2,column=3,columnspan=10)
def oscillator():
    root7=Tk()
    text=Entry(root7,font=("Arial black",8))
    text.grid(padx=5,pady=5)
    text.grid(row=0,column=2)
    a=Entry(root7,font=("Arial black",8))
    a.grid(padx=5,pady=5)
    a.grid(row=2,column=2)

    def sss():
        f=text.get()
        A=a.get()
        try:
            f=float(f)
            A=float(A)
        except:
            print("error")
        global osci
        osci=Oscillator(f,A)
    label1= Label(root7,text="f(Hz)=")
    label1.grid(row=0,column=1)
    label2=Label(root7,text="Amplitude(Volts)")
    label2.grid(row=2,column=1)
    button = Button(root7, text="εκτελεση", command=sss)
    button.grid(row=2,column=3,columnspan=10)

buttons=[]
buttons.append(Button(root,text="Oscillator",command=oscillator))
buttons.append(Button(root,text="RF Filter",command=RF_Filter))
buttons.append(Button(root,text="Time Domain",command=plot_time))
buttons.append(Button(root,text="Spectrum",command=plot_spectrum))
buttons.append(Button(root, text="Insert one signal", command=signal))
buttons.append(Button(root, text="Adjust signal",command=adjust_signal))
buttons.append(Button(root, text="End programm",command=close_window))
for butt in buttons:
    butt.pack()
# Ξεκίνηση της κύριας βρόχου εκτέλεσης του παραθύρου
root.mainloop()