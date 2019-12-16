import datetime
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import time, threading
WAIT_SECONDS = 1#每隔多久(秒)更新一次

class mclass:
    def __init__(self,  window):
        super().__init__()
        self.window = window
        self.box = Entry(window)
        self.button = Button (window, text="開始遊戲", command=self.foo)
        self.box.pack ()
        self.button.pack()
        self.tx = StringVar()
        self.tx.set("current time")
        self.label = Label(window, textvariable=self.tx).pack()#add text
        self.game_stab = Label(window, text="遊戲進行時間(秒)").pack()#add text
        self.game_time = StringVar()
        self.game_time.set("0")
        self.l_game_time = Label(window, textvariable=self.game_time).pack()#add text

    def word(self,time):#更新畫面
        self.tx.set(time)
        self.game_time.set(str(int(self.game_time.get())+1))
        
    def foo(self):#每秒做一次的區域
        self.word(time.ctime())
        threading.Timer(WAIT_SECONDS, self.foo).start()
        
window= Tk()
start= mclass (window)
window.mainloop()
