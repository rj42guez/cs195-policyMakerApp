from tkinter import *

root = Tk()
root.geometry("750x250")

introLabel = Label(root, text = "Welcome to UPD Policy Maker App")

projectTitleLabel = Label(root, text = "Enter project title: ")
projectTitle = Entry(root, width=50)

introLabel.grid(sticky = "nsew", pady = 2)
projectTitleLabel.grid(row=1, column=0, sticky = W, pady = 2)
projectTitle.grid(row=1, column=2, sticky = W, pady = 2)

polAnaTitleLabel = Label(root, text = "Enter project analysis title: ")
polAnaTitle = Entry(root, width=50)

introLabel.grid(sticky = "nsew", pady = 2)
projectTitleLabel.grid(row=1, column=0, sticky = W, pady = 2)
projectTitle.grid(row=1, column=2, sticky = W, pady = 2)
polAnaTitleLabel.grid(row=3, column=0, sticky = W, pady = 2)
polAnaTitle.grid(row=3, column=2, sticky = W, pady = 2)



root.mainloop()