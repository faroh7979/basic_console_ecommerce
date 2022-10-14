from tkinter import Tk


def open_window():
    window = Tk()

    window.geometry('700x600')
    window.title('Welcome to Liverpool FC Fan Shop')

    return window


window_opener = open_window()
