from tkinter import *
from time import time
import pandas as pd

start_time = end_time = 0
key_timing_array = []

master = Tk()
e = Entry(master)
e.pack()
e.focus_set()

def record_key(event):
    if event.char == '\r':
        e.unbind("<Key>")
        print(key_timing_array)
        return

    print("Pressed", repr(event.char))
    end_time = time()
    print ("Measured time: ", end_time-start_time)
    key_timing = end_time-start_time
    key_timing_array.append(key_timing)

def write_to_csv():
    return

e.bind("<Key>", record_key)

start_time = time()
mainloop()

