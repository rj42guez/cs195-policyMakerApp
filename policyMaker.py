from tkinter import *

root = Tk()
root.geometry("1000x750")

def createNewProject():
    newProject = Toplevel(root)
    newProject.title("Create New Project")
    newProject.geometry("750x250")

    introLabel = Label(newProject, text = "Welcome to UPD Policy Maker App")

    projectTitleLabel = Label(newProject, text = "Enter project title: ")
    projectTitle = Entry(newProject, width=50)

    introLabel.grid(sticky = "nsew", pady = 2)
    projectTitleLabel.grid(row=1, column=0, sticky = W, pady = 2)
    projectTitle.grid(row=1, column=2, sticky = W, pady = 2)

    polAnaTitleLabel = Label(newProject, text = "Enter project analysis title: ")
    polAnaTitle = Entry(newProject, width=50)

    introLabel.grid(sticky = "n", pady = 2)

    projectTitleLabel.grid(row=1, column=0, sticky = W, pady = 2)
    projectTitle.grid(row=1, column=2, sticky = W, pady = 2)

    polAnaTitleLabel.grid(row=3, column=0, sticky = W, pady = 2)
    polAnaTitle.grid(row=3, column=2, sticky = W, pady = 2)

btn = Button(root, 
             text ="Create a New Project", 
             command = createNewProject)
btn.pack(pady = 10)

root.mainloop()