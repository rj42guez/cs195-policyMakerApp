import tkinter as tk
import json
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import scrolledtext 
from tkinter.filedialog import asksaveasfile 
from tkinter.filedialog import askopenfilename

from pathlib import Path

root = Tk()
root.title("UPD Policy Maker 1.0")
root.geometry("1300x700")

main = tk.PanedWindow(root, background="#468585")

main.pack(side="top", fill="both", expand=True)

left_pane = tk.Frame(main, background="#DEF9C4", width=200)
right_pane = tk.PanedWindow(main, background="#9CDBA6", width=200)
main.add(left_pane)
main.add(right_pane)


introLabel = Label(main, background="#9CDBA6", foreground="purple", text = "Welcome to the UPD Policy Maker App")
aboutLabel1 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, justify="left", text = "The UPD Policy Maker App is exclusive to all students, faculty, and staff of the UP Diliman community. Here, users start by creating an analysis on a policy and defining the problematic situation and their undesirable effects. It also lets them do the following:")
aboutLabel2 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, justify="left", text = "1. Enumerate the efforts/measures that are currently being done to tackle the problem ")
aboutLabel3 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, justify="left", text = "2. List down the accomplishments and the assessments on each effort/measure")
aboutLabel4 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, justify="left", text = "3. Define the root cause of the problem")
aboutLabel5 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, justify="left", text = "4. Assess the existing policies ")

currentlyOpenLabel = Label(root, text = "Recently Opened Projects ")
ProjectTitleLabel = Label(root, text = "Project Title:  ")

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)
main.columnconfigure(3, weight=1)
main.columnconfigure(4, weight=1)
main.columnconfigure(5, weight=1)

introLabel.place(x=600, y=23)

aboutLabel1.place(x=240, y=63)
aboutLabel2.place(x=240, y=123)
aboutLabel3.place(x=240, y=153)
aboutLabel4.place(x=240, y=183)
aboutLabel5.place(x=240, y=213)

projectTitle = Label(main, background="#9CDBA6", foreground="purple",  text = "")
polAnaTitle = Label(main, background="#9CDBA6", foreground="purple",  text = "")
probSit = Label(main, background="#9CDBA6", foreground="purple",  text = "")
undeEff = Label(main, background="#9CDBA6", foreground="purple",  text = "")
# currEffo
# effoMeas
# acco
# asse

def saveFile():
        files = [('All Files', '*.*'),  
                ('Python Files', '*.py'), 
                ('Text Document', '*.txt')] 
        file = asksaveasfile(filetypes = files, defaultextension = files) 
        print(file)

def openFile():
    filename = askopenfilename(parent=root, title="Select a POL File")
    f = open(filename)
    
    content = f
    data = json.load(content)

    root.title("UPD Policy Maker - "+data[0])

    projectTitle.config(text = "")
    polAnaTitle.config(text = "")
    probSit.config(text = "")
    undeEff.config(text = "")
    # currEffo
    # effoMeas
    # acco
    # asse

    projectTitle.config(text = data[0])
    polAnaTitle.config(text = data[1])
    probSit.config(text = data[2])
    undeEff.config(text = data[3])
    # currEffo
    # effoMeas
    # acco
    # asse

    projectTitleLabel = Label(main, background="#9CDBA6", foreground="purple", text = "Project Title: ")
    polAnaTitleLabel = Label(main, background="#9CDBA6", foreground="purple",  text = "Policy Analysis Title: ")
    probSitLabel = Label(main, background="#9CDBA6", foreground="purple",  text = "Problematic Situation: ")
    undeEffLabel = Label(main, background="#9CDBA6", foreground="purple",  text = "Undesirable Effects: ")
    
    currEffoLabel = Label(main, background="#9CDBA6", foreground="purple",  text = "Current Efforts: ")
    effoMeasLabel = Label(main, background="#9CDBA6", foreground="purple",  text = "Effort/Measure")
    accoLabel = Label(main, text = "Accomplishments")
    asseLabel = Label(main, text = "Assessments")

                
    projectTitleLabel.place(x=240, y=273)
    projectTitle.place(x=400, y=273)
    polAnaTitleLabel.place(x=240, y=303)
    polAnaTitle.place(x=400, y=303)
    probSitLabel.place(x=240, y=333)
    probSit.place(x=400, y=333) 
    undeEffLabel.place(x=240, y=363)
    undeEff.place(x=400, y=363)
    currEffoLabel.grid(x=240, y=393)


def createNewProject():
    newProject = Toplevel(root)
    newProject.title("UPD Policy Maker - Create New Project")
    newProject.geometry("1080x500")

    scrollbar = ttk.Scrollbar(newProject)

    blank1 = Label(newProject, text = "  ")
    blank2 = Label(newProject, text = "  ")
    blank3 = Label(newProject, text = "  ")
    blank4 = Label(newProject, text = "  ")
    blank5 = Label(newProject, text = "  ")
    blank6 = Label(newProject, text = "  ")

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

    def option_selected(event):
        probSit.configure(font = (fontsList.get(), fontSize.get())) 
        undeEff.configure(font = (fontsList.get(), fontSize.get())) 
    
    fontSize = Entry(newProject, width=10)
    indentation = Entry(newProject, width=10)

    analystLabel1 = Label(newProject, text = "Analyst")
    analystLabel2 = Label(newProject, text = "Enter name of analyst: ")
    analyst = Entry(newProject, width=50)

    levelsLabel1 = Label(newProject, text = "Levels of Analysis ")
    levelNLabel = Label(newProject, text = "National ")
    levelLLabel = Label(newProject, text = "Local ")
    levelOLabel = Label(newProject, text = "Organizational ")

    nLevel = Entry(newProject, width=50)
    lLevel = Entry(newProject, width=50)
    oLevel = Entry(newProject, width=50)

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
    
    projectTitleLabel1.grid(row=2, column=0, sticky = W, padx=7)
    projectTitleLabel2.grid(row=3, column=0, sticky = W, padx=7)
    projectTitle.grid(row=3, column=1, sticky = W, padx=7)
    blank1.grid(row=4, column=0, padx=7)
    analystLabel1.grid(row=5, column=0, sticky = W, padx=7)
    analystLabel2.grid(row=6, column=0, sticky = W, padx=7)
    analyst.grid(row=6, column=1, sticky = W, padx=7)
    blank2.grid(row=7, column=0)
    settingsLabel.grid(row=8, column=0, sticky = W, padx=7)
    fontStyleLabel.grid(row=9, column=0, sticky = W, padx=7)
    fontsList.grid(row=9, column=1, sticky = W, padx=7)
    fontSizeLabel.grid(row=10, column=0, sticky = W, padx=7)
    fontSize.grid(row=10, column=1, sticky = W, padx=7)
    indentationLabel.grid(row=11, column=0, sticky = W, padx=7)
    indentation.grid(row=11, column=1, sticky = W, padx=7)
    blank3.grid(row=12, column=0)
    polAnaTitleLabel1.grid(row=5, column=2, sticky = W, padx=7)
    polAnaTitleLabel2.grid(row=6, column=2, sticky = W, padx=7)
    polAnaTitle.grid(row=6, column=3, sticky = W, padx=7)
    levelsLabel1.grid(row=8, column=2, sticky = W, padx=7)
    levelNLabel.grid(row=9, column=2, sticky = W, padx=7)
    levelLLabel.grid(row=10, column=2, sticky = W, padx=7)
    levelOLabel.grid(row=11, column=2, sticky = W, padx=7)
    nLevel.grid(row=9, column=3, sticky = W, padx=7)
    lLevel.grid(row=10, column=3, sticky = W, padx=7)
    oLevel.grid(row=11, column=3, sticky = W, padx=7)
    blank5.grid(row=4, column=0)
    probSitLabel1.grid(row=13, column=0, sticky = W, padx=7)
    probSitLabel2.grid(row=14, column=0, sticky = W, padx=7)
    probSit.grid(row=14, column=1, sticky = W, padx=7)
    blank6.grid(row=15, column=0)
    undeEffLabel1.grid(row=13, column=2, sticky = W, padx=7)
    undeEffLabel2.grid(row=14, column=2, sticky = W, padx=7)
    undeEff.grid(row=14, column=3, sticky = W, padx=7)
    
    def saveFile():
        projectTitle.config(bg="white")
        fontSize.config(bg="white")
        polAnaTitle.config(bg="white")
        probSit.config(bg="white")
        undeEff.config(bg="white")


        projecttitle = projectTitle.get()
        if not projecttitle.strip():
             projectTitle.config(bg="#ffd0d0")
             return
        
        fontstyle = fontsList.get()
        
        fontsize = fontSize.get()
        if fontsize.isnumeric() == False:
             fontSize.config(bg="#ffd0d0")
             return
        
        policyanalysis = polAnaTitle.get()
        if not policyanalysis.strip():
             polAnaTitle.config(bg="#ffd0d0")
             return
        
        problematicsituation = probSit.get("1.0", tk.END)
        if not problematicsituation.strip():
             probSit.config(bg="#ffd0d0")
             return
        
        undesirableeffects = undeEff.get("1.0", tk.END)
        if not undesirableeffects.strip():
             undeEff.config(bg="#ffd0d0")
             return
 
        data = [projecttitle, policyanalysis, problematicsituation, undesirableeffects, fontstyle, fontsize]

        filename = projecttitle
        fileobject = open(filename + '.pol', 'w')
        json.dump(data, fileobject)
        fileobject.close()

        newProject.destroy()
        newProject.update()
    
    def clearCreate():
        projectTitle.config(bg="white")
        fontSize.config(bg="white")
        polAnaTitle.config(bg="white")
        probSit.config(bg="white")
        undeEff.config(bg="white")
        
        projectTitle.delete(0, END)
        polAnaTitle.delete(0, END)
        fontSize.delete(0, END)
        indentation.delete(0, END)
        probSit.delete("1.0", tk.END)
        undeEff.delete("1.0", tk.END)

    btnCreate = Button(newProject, text = "Create a Project", command = lambda: saveFile())
    btnClear = Button(newProject, text = "Clear", command = lambda: clearCreate())
    btnCreate.grid(row=18, column=1, pady=10)
    btnClear.grid(row=18, column=0, pady=10)

menubar = Menu(root) 

file1 = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file1) 
file1.add_command(label ='Create New', command = createNewProject) 
file1.add_command(label ='Open', command = openFile) 
file1.add_command(label ='Save', command = saveFile) 
file1.add_separator() 
file1.add_command(label ='Exit', command = root.destroy)

file2 = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Settings', menu = file2) 
file2.add_command(label ='Change Font Size') 
file2.add_command(label ='Change Font Style') 
file2.add_command(label ='Change Indentation') 

root.config(menu=menubar)

root.mainloop()