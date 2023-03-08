import tkinter
import tkinter.simpledialog
from tkinter import *
import tkintermapview
import webbrowser


window = Tk()


def home_clicked():
    window.title("Main")
    window.geometry("1920x1080")
    window.columnconfigure(10)
    window.rowconfigure(10)
    Hello = tkinter.Label(text="Welcome").grid(row=1, column=1)
    placeholder = tkinter.Button().grid(row=2, column=1)
    browse = tkinter.Button(text="click to open browser", command=lambda: browse_clicked()).grid(row=3, column=3, padx= 10, pady=10)
    map = tkinter.Button(text="click for map", command=lambda:  map_clicked()).grid(row=3, column=2, padx= 10, pady= 10)
    profile = tkinter.Button(text="click for profile", command=lambda: profile_clicked()).grid(row=3, column=1, padx= 10, pady= 10)
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

