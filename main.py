import tkinter as tk
import json
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import scrolledtext 
from tkinter import colorchooser
from tkinter.filedialog import asksaveasfile 
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

from flow import createNewProject

global size
size = 10

root = Tk()
root.title("Policy Analytics")
root.geometry("1300x700")

main = tk.PanedWindow(root, background="#ffffff")

main.pack(side="top", fill="both", expand=True)

left_pane = tk.Frame(main, background="#76090c", width=200)
right_pane = tk.PanedWindow(main, background="#ffffff", width=200)
main.add(left_pane)
main.add(right_pane)

introLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin Gothic Heavy", 14), text = "Welcome to Policy Analytics")
aboutLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Policy Analytics is a tool for learning policy analysis. This software can be used in training programs and classroom learning. It provides a step-by-step procedure that allows users to input and process basic essential data for problem structuring, forecasting and assessment of policy alternatives, recommending or prescribing the best/optimal policy alternative, designing an implementation plan, and building a monitoring and evaluation plan. Its outputs can be used in writing a complete policy issue paper. It is based on the “Elements of the Policy Issue Paper” in Annex 1 of Public Policy Analysis: An Integrated Approach by William N. Dunn (2018) with modifications based on the teaching and training experiences of its creator, Dr. Ebinezer R. Florano, Professor of Public Policy at the University of the Philippines, National College of Public Administration and Governance and Convenor of the UPCIDS Data Science for Public Policy Program (DSPPP).")
arrLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "All rights reserved@2024 – UPCIDS-DSPPP")
creatorLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Creator: Dr. Ebinezer R. Florano")
programmerLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Programmers: Raphael Justin Portuguez and Emmerson Isip")
reveiwerLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Reviewers: Colin Rosales, Danne Nicole Pinpin, and Jean Phoebe Yao")
adminLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Administrative Assistance: Lilian J. Marfil and Zhelly Ann Linsangan")

dspppLogo = (Image.open("logo_DSPPP.png"))
cidsLogo = (Image.open("logo_UP_CIDS.png"))
upLogo = (Image.open("logo_UP.png"))

up = upLogo.resize((100, 100))
dsppp = dspppLogo.resize((100, 100))

up = ImageTk.PhotoImage(up)
dsppp = ImageTk.PhotoImage(dsppp)
cids = ImageTk.PhotoImage(cidsLogo)

currentlyOpenLabel = Label(main, text = "Recently Opened Projects ")
ProjectTitleLabel = Label(main, text = "Project Title:  ")

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)
main.columnconfigure(3, weight=1)
main.columnconfigure(4, weight=1)
main.columnconfigure(5, weight=1)

introLabel.place(x=600, y=23)
aboutLabel.place(x=240, y=63)
arrLabel.place(x=595, y=200)

upLabel=Label(main, image=up)
upLabel.place(x=380, y=250)
dspppLabel=Label(main, image=dsppp)
dspppLabel.place(x=630, y=250)
cidsLabel=Label(main, image=cids)
cidsLabel.place(x=880, y=250)

creatorLabel.place(x=380, y=400)
programmerLabel.place(x=380, y=430)
reveiwerLabel.place(x=380, y=460)
adminLabel.place(x=380, y=490)

menubar = Menu(root) 

file1 = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file1) 
file1.add_command(label ='Create New', command = createNewProject)
file1.add_command(label ='Save') 
file1.add_separator() 
file1.add_command(label ='Exit', command = root.destroy)

file2 = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Settings', menu = file2) 
file2.add_command(label ='Change Font Size') 
file2.add_command(label ='Change Font Style') 
file2.add_command(label ='Change Indentation') 

root.config(menu=menubar)

root.mainloop()