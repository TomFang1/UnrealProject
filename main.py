import tkinter
import tkinter.simpledialog
from tkinter import *
import tkintermapview
import webbrowser


window = Tk()


def home_clicked():
    window.title("Main")
    window.geometry("1920x1080")
    browse = tkinter.Button(text="click to open browser", command=lambda: browse_clicked())
    browse.place(x=350, y=100)
    map = tkinter.Button(text="click for map", command=lambda:  map_clicked())
    map.place(x=50, y=100)
    profile = tkinter.Button(text="click for profile")
    profile.configure(command=lambda: profile_clicked())
    profile.place(x=200, y=100)

    window.mainloop()


def map_clicked():
    window.title("Map")
    back = tkinter.Button(text="Back to home", command=lambda: map_widget.destroy() & back.destroy() & home_clicked())
    back.place(x=10, y=10)
    map_widget = tkintermapview.TkinterMapView(window, width=1800, height=1080, corner_radius=0)
    map_widget.place(x=0, y=50)


def profile_clicked():
    window.title("Profile")
    back = tkinter.Button(text="Back to home", command=lambda: back.destroy() & home_clicked())
    back.place(x=10, y=10)


def browse_clicked():
    e1 = tkinter.Entry(window)
    e1.place(x=10, y=10)
    search = tkinter.Button(text="search", command=lambda: webbrowser.open("https://www.google.de/search?q=" + Entry.get(e1)))
    search.place(x=15, y=35)



home_clicked()

