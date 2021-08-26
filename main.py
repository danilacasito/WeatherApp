import os
import requests
from configparser import ConfigParser
from tkinter import *


class window:
    def search(self):
        pass
    def addWidgets(self):
        self.city_text = StringVar()
        self.city_entry = Entry(self.window, textvariable=self.city_text)
        self.city_entry.place(width=150,x=70,y=20,height=20)
        self.city_text_f = Label(self.window, text="City:")
        self.city_text_f.place(y=20,x=20)
        self.search_btn = Button(self.window, text="Search", command=self.search)
        self.search_btn.place(x=230, y=20,height=20)
        self.temperature_label = Label(self.window, text="TEST 20", font={"bold",100})
        self.temperature_label.place(x=300/2,y=300/2,anchor=CENTER)
    def __init__(self):
        self.window = Tk()
        self.window.geometry("300x300")
        self.addWidgets()
        self.window.mainloop()

if __name__ == "__main__":
    window()