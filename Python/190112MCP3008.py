from tkinter import *;
from gpiozero import MCP3008;
from threading import Timer;

class App:
    def __init__(self, window):
        self.gpioInit();
        mainFrame = Frame(window, borderwidth=2, relief=GROOVE);
        
    def gpioInit(self):
        self.vrChannel = MCP3008(channel=7);
        Timer(1, gpioAutoUpdate).start();
        
    def gpioAutoUpdate(self):
        print("pot={}".format(self.vrChannel));
        Timer(1, gpioAutoUpdate).start();
    

if __name__ == "__name__":
    window = Tk();
    window.title("MCP3008");
    root = App(window);
    window.mainloop();   