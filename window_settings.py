from tkinter import *


def open_window():
    window = Tk()

    window.geometry('700x600')
    window.title('Welcome to Liverpool FC Fan Shop')

    return window


def create_frame():
    frame_func = Canvas(window_opener, width=700, height=600)
    frame_func.grid(row=0, column=0)

    return frame_func


window_opener = open_window()
frame = create_frame()
