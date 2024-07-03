from tkinter import *
from tkinter import font
from tkinter import ttk

root = Tk()
root.geometry("1000x750")

def createNewProject():
    newProject = Toplevel(root)
    newProject.title("Create New Project")
    newProject.geometry("750x250")

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
    fontsList = ttk.Combobox(newProject, width=30, values=fonts)
    fontSize = Entry(newProject, width=10)
    indentation = Entry(newProject, width=10)

    polAnaTitleLabel1 = Label(newProject, text = "Policy Analysis Title: ")
    polAnaTitleLabel2 = Label(newProject, text = "Enter policy analysis title: ")
    polAnaTitle = Entry(newProject, width=50)

    projectTitleLabel1.grid(row=1, column=0, sticky = W, pady = 1)
    projectTitleLabel2.grid(row=2, column=0, sticky = W, pady = 1)
    projectTitle.grid(row=2, column=1, sticky = W, pady = 1)
    settingsLabel.grid(row=4, column=0, sticky = W, pady = 1)
    fontStyleLabel.grid(row=5, column=0, sticky = W, pady = 1)
    fontsList.grid(row=5, column=1, sticky = W, pady = 1)
    fontSizeLabel.grid(row=6, column=0, sticky = W, pady = 1)
    fontSize.grid(row=6, column=1, sticky = W, pady = 1)
    indentationLabel.grid(row=7, column=0, sticky = W, pady = 1)
    indentation.grid(row=7, column=1, sticky = W, pady = 1)
    polAnaTitleLabel1.grid(row=9, column=0, sticky = W, pady = 1)
    polAnaTitleLabel2.grid(row=10, column=0, sticky = W, pady = 1)
    polAnaTitle.grid(row=10, column=1, sticky = N, pady = 1)


introLabel = Label(root, text = "Welcome to UPD Policy Maker App")
introLabel.pack(pady = 2)

btn = Button(root, 
             text ="Create a New Project", 
             command = createNewProject)
btn.pack(pady = 10)

root.mainloop()