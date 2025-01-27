import tkinter as tk 
from tkinter import *

def changeFontSize(fontsize):
    popup = Tk()
    popup.geometry("200x200")
    popup.title("UPD Policy Maker 1.0 - Change Font Size")

    label = Label(popup, text = "Change font size: ")
    fontSize = Entry(popup, width=10)

    def change():
        fontsize = int(fontSize.get())
        print(fontsize)
        popup.destroy
        popup.update

    label.place(x=10, y=10)
    fontSize.place(x=70, y=10)

    button = Button(popup, text = "Change", command = change)
    button.place(x=10, y=30)


def changeFontStyle():
    popup = Tk()
    popup.geometry("300x200")
    popup.title("UPD Policy Maker 1.0 - Change Font Style")

def changeIndentation():
    popup = Tk()
    popup.geometry("300x200")
    popup.title("UPD Policy Maker 1.0 - Change Indentation")
    
    