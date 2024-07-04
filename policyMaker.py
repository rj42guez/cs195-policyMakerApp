import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import scrolledtext 
from tkinter.filedialog import asksaveasfile 
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry("500x400")

def save():
        files = [('All Files', '*.*'),  
                ('Python Files', '*.py'), 
                ('Text Document', '*.txt')] 
        file = asksaveasfile(filetypes = files, defaultextension = files) 

def open():
    filename = askopenfilename(parent=root)
    f = open(filename)
    f.read()

def createNewProject():
    newProject = Toplevel(root)
    newProject.title("Create New Project")
    newProject.geometry("600x700")

    scrollbar = ttk.Scrollbar(newProject)

    blank1 = Label(newProject, text = "  ")
    blank2 = Label(newProject, text = "  ")
    blank3 = Label(newProject, text = "  ")
    blank4 = Label(newProject, text = "  ")
    blank5 = Label(newProject, text = "  ")

    projectTitleLabel1 = Label(newProject, text = "Project Title")
    projectTitleLabel2 = Label(newProject, text = "Enter project title: ")
    projectTitle = Entry(newProject, width=50)

    settingsLabel = Label(newProject, text = "Settings")
    fontStyleLabel = Label(newProject, text = "Choose font style: ")
    fontSizeLabel = Label(newProject, text = "Choose font size: ")
    indentationLabel = Label(newProject, text = "Choose indentation: ")
    
    font.families()
    fonts = list(font.families())
    fonts.sort()
    
    selectedFont = tk.StringVar()

    fontsList = ttk.Combobox(newProject, width=30, values=fonts)
    print("font is ", fontsList.current())

    def option_selected(event):
        probSit.configure(font = (fontsList.get(), fontSize.get())) 
        undeEff.configure(font = (fontsList.get(), fontSize.get())) 
    
    fontSize = Entry(newProject, width=10)
    indentation = Entry(newProject, width=10)

    polAnaTitleLabel1 = Label(newProject, text = "Policy Analysis Title ")
    polAnaTitleLabel2 = Label(newProject, text = "Enter policy analysis title: ")
    polAnaTitle = Entry(newProject, width=50)

    probSitLabel1 = Label(newProject, text = "Problematic Situation")
    probSitLabel2 = Label(newProject, text = "Enter problematic situation: ")
    probSit = scrolledtext.ScrolledText(newProject, height = 5, width=30, font=(fontsList.get(), 14))
    
    undeEffLabel1 = Label(newProject, text = "Undesirable Effects")
    undeEffLabel2 = Label(newProject, text = "Enter undesirable effects: ")
    undeEff = scrolledtext.ScrolledText(newProject, height = 5, width=30, font=(fontsList.get(), 14))

    fontsList.bind("<<ComboboxSelected>>", option_selected)
    fontSize.bind("<Return>", option_selected)
    
    blank5.grid(row=1, column=0)
    projectTitleLabel1.grid(row=2, column=0, sticky = W, pady = 1)
    projectTitleLabel2.grid(row=3, column=0, sticky = W, pady = 1)
    projectTitle.grid(row=3, column=1, sticky = W, pady = 1)
    blank1.grid(row=4, column=0)
    settingsLabel.grid(row=5, column=0, sticky = W, pady = 1)
    fontStyleLabel.grid(row=6, column=0, sticky = W, pady = 1)
    fontsList.grid(row=6, column=1, sticky = W, pady = 1)
    fontSizeLabel.grid(row=7, column=0, sticky = W, pady = 1)
    fontSize.grid(row=7, column=1, sticky = W, pady = 1)
    indentationLabel.grid(row=8, column=0, sticky = W, pady = 1)
    indentation.grid(row=8, column=1, sticky = W, pady = 1)
    blank2.grid(row=9, column=0)
    polAnaTitleLabel1.grid(row=10, column=0, sticky = W, pady = 1)
    polAnaTitleLabel2.grid(row=11, column=0, sticky = W, pady = 1)
    polAnaTitle.grid(row=11, column=1, sticky = W, pady = 1)
    blank3.grid(row=12, column=0)
    probSitLabel1.grid(row=13, column=0, sticky = W, pady = 1)
    probSitLabel2.grid(row=14, column=0, sticky = W, pady = 1)
    probSit.grid(row=14, column=1, sticky = W, pady = 1)
    blank4.grid(row=15, column=0)
    undeEffLabel1.grid(row=16, column=0, sticky = W, pady = 1)
    undeEffLabel2.grid(row=17, column=0, sticky = W, pady = 1)
    undeEff.grid(row=17, column=1, sticky = W, pady = 1)

    btn = Button(newProject, text = "Save", command = lambda: save())
    btn.grid(row=20, column=1, pady = 4)

menubar = Menu(root) 

file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='Create New', command = createNewProject) 
file.add_command(label ='Open', command = open) 
file.add_command(label ='Save', command = save) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy)

root.config(menu=menubar)

introLabel = Label(root, text = "Welcome to UPD Policy Maker App")
introLabel.pack(pady = 2)

btn = Button(root, text ="Create a New Project", command = createNewProject)
btn.pack(pady = 10)

root.mainloop()