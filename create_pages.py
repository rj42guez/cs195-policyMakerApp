import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
from policyAnalytics import mainProject

def page_1():
    blank = Label(mainProject, text = "  ")

    projectTitleLabel1 = Label(mainProject, text = "Project Title")
    projectTitle = Entry(mainProject, width=30)

    settingsLabel = Label(mainProject, text = "Settings")
    fontStyleLabel = Label(mainProject, text = "Choose font style: ")
    fontSizeLabel = Label(mainProject, text = "Choose font size: ")
    indentationLabel = Label(mainProject, text = "Choose indentation: ")
    
    font.families()
    fonts = list(font.families())
    fonts.sort()

    fontsList = ttk.Combobox(mainProject, width=30, values=fonts)
    fontSize = Entry(mainProject, width=10)
    indentation = Entry(mainProject, width=10)

    analystNameLabel1 = Label(mainProject, text = "Analyst")
    analystName = Entry(mainProject, width=30)

    levelsLabel1 = Label(mainProject, text = "Levels of Analysis ")

    varNat = tk.IntVar()
    varLoc = tk.IntVar()
    varOrg = tk.IntVar()

    national = tk.Checkbutton(mainProject, text='National',variable=varNat, onvalue=1, offvalue=0)
    local = tk.Checkbutton(mainProject, text='Local',variable=varLoc, onvalue=1, offvalue=0)
    organizational = tk.Checkbutton(mainProject, text='Organizational',variable=varOrg, onvalue=1, offvalue=0)

    polAnaTitleLabel1 = Label(mainProject, text = "Policy Analysis Title ")
    polAnaTitle = Entry(mainProject, width=30)

    status = ttk.Label(mainProject, text="")

    projectTitleLabel1.grid(row=2, column=0, padx=7)
    projectTitle.grid(row=3, column=0, padx=7)
    analystNameLabel1.grid(row=2, column=1, padx=7)
    analystName.grid(row=3, column=1, padx=7)
    polAnaTitleLabel1.grid(row=2, column=2, padx=7)
    polAnaTitle.grid(row=3, column=2, padx=7)
    blank.grid(row=4, column=0)
    settingsLabel.grid(row=5, column=0)
    fontStyleLabel.grid(row=6, column=0, sticky = W, padx=7)
    fontsList.grid(row=6, column=1, sticky = W, padx=7)
    fontSizeLabel.grid(row=7, column=0, sticky = W, padx=7)
    fontSize.grid(row=7, column=1, sticky = W, padx=7)
    indentationLabel.grid(row=8, column=0, sticky = W, padx=7)
    indentation.grid(row=8, column=1, sticky = W, padx=7)
    levelsLabel1.grid(row=5, column=2, padx=7)
    national.grid(row=6, column=2, sticky = W, padx=56)
    local.grid(row=7, column=2, sticky = W, padx=56)
    organizational.grid(row=8, column=2, sticky = W, padx=56)

    def page_1_validate():
        projecttitle = projectTitle.get()
        if not projecttitle.strip():
            status.config(
                text="Enter project title",
                foreground="red",
            )
            return
        
        fontstyle = fontsList.get()

        fontsize = fontSize.get()
        if fontsize.isnumeric() == False:
            status.config(
                text="Enter font size",
                foreground="red",
            )
            return
                
        analyst = analystName.get()
        if not analyst.strip():
            status.config(
                text="Enter analyst name",
                foreground="red",
            )
            return
                
        policyanalysis = polAnaTitle.get()
        if not policyanalysis.strip():
            status.config(
                text="Enter policy analysis title",
                foreground="red",
            )
            return
        
        filename = projecttitle
        fileobject = open(filename + '.pol', 'w')
        fileobject.write(projecttitle+"\n"+analyst+"\n"+policyanalysis+"\n"+fontstyle+"\n"+fontsize+"\n")

        frame1.destroy() 
        btnCreate.destroy() 
        btnClear.destroy() 

def page_2():
    blank = Label(mainProject, text = "  ")

    projectTitleLabel1 = Label(mainProject, text = "Project Title")
    projectTitle = Entry(mainProject, width=30)

    settingsLabel = Label(mainProject, text = "Settings")
    fontStyleLabel = Label(mainProject, text = "Choose font style: ")
    fontSizeLabel = Label(mainProject, text = "Choose font size: ")
    indentationLabel = Label(mainProject, text = "Choose indentation: ")
    
    font.families()
    fonts = list(font.families())
    fonts.sort()

    fontsList = ttk.Combobox(mainProject, width=30, values=fonts)
    fontSize = Entry(mainProject, width=10)
    indentation = Entry(mainProject, width=10)

    analystNameLabel1 = Label(mainProject, text = "Analyst")
    analystName = Entry(mainProject, width=30)

    levelsLabel1 = Label(mainProject, text = "Levels of Analysis ")

    varNat = tk.IntVar()
    varLoc = tk.IntVar()
    varOrg = tk.IntVar()

    national = tk.Checkbutton(mainProject, text='National',variable=varNat, onvalue=1, offvalue=0)
    local = tk.Checkbutton(mainProject, text='Local',variable=varLoc, onvalue=1, offvalue=0)
    organizational = tk.Checkbutton(mainProject, text='Organizational',variable=varOrg, onvalue=1, offvalue=0)

    polAnaTitleLabel1 = Label(mainProject, text = "Policy Analysis Title ")
    polAnaTitle = Entry(mainProject, width=30)

    status = ttk.Label(mainProject, text="")

    varRoot1 = tk.IntVar()
    varRoot2 = tk.IntVar()
    varRoot3 = tk.IntVar()
    varRoot4 = tk.IntVar()
    varRoot5 = tk.IntVar()
    varRoot6 = tk.IntVar()
    varRoot7 = tk.IntVar()

    projectTitleLabel1.grid(row=2, column=0, padx=7)
    projectTitle.grid(row=3, column=0, padx=7)
    analystNameLabel1.grid(row=2, column=1, padx=7)
    analystName.grid(row=3, column=1, padx=7)
    polAnaTitleLabel1.grid(row=2, column=2, padx=7)
    polAnaTitle.grid(row=3, column=2, padx=7)
    blank.grid(row=4, column=0)
    settingsLabel.grid(row=5, column=0)
    fontStyleLabel.grid(row=6, column=0, sticky = W, padx=7)
    fontsList.grid(row=6, column=1, sticky = W, padx=7)
    fontSizeLabel.grid(row=7, column=0, sticky = W, padx=7)
    fontSize.grid(row=7, column=1, sticky = W, padx=7)
    indentationLabel.grid(row=8, column=0, sticky = W, padx=7)
    indentation.grid(row=8, column=1, sticky = W, padx=7)
    levelsLabel1.grid(row=5, column=2, padx=7)
    national.grid(row=6, column=2, sticky = W, padx=56)
    local.grid(row=7, column=2, sticky = W, padx=56)
    organizational.grid(row=8, column=2, sticky = W, padx=56)