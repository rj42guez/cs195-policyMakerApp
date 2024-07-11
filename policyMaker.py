import tkinter as tk
# from settings import *
import json
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import scrolledtext 
from tkinter.filedialog import asksaveasfile 
from tkinter.filedialog import askopenfilename

from pathlib import Path

global size
size = 10

root = Tk()
root.title("UPD Policy Maker 1.0")
root.geometry("1300x700")

main = tk.PanedWindow(root, background="#468585")

main.pack(side="top", fill="both", expand=True)

left_pane = tk.Frame(main, background="#DEF9C4", width=200)
right_pane = tk.PanedWindow(main, background="#9CDBA6", width=200)
main.add(left_pane)
main.add(right_pane)

def changeFontSize():
    popup = Toplevel(root)
    popup.geometry("200x200")
    popup.title("UPD Policy Maker 1.0 - Change Font Size")

    label = Label(popup, text = "Change font size: ")
    fontSize = Entry(popup, width=10)

    def change():
        size = int(fontSize.get())
        print(size)
        popup.update()
        popup.destroy()

    label.place(x=10, y=10)
    fontSize.place(x=70, y=10)

    button = Button(popup, text = "Change", command = change)
    button.place(x=10, y=30)

introLabel = Label(main, background="#9CDBA6", foreground="purple", font=("Franklin Gothic Heavy", 14), text = "Welcome to the UPD Policy Analytics App")
aboutLabel1 = Label(main, background="#9CDBA6", foreground="purple", font=("Franklin ", 10), wraplength=1000, justify="left", text = "The UPD Policy Maker App is exclusive to all students, faculty, and staff of the UP Diliman community. Here, users start by creating an analysis on a policy and defining the problematic situation and their undesirable effects. It also lets them do the following:")
aboutLabel2 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, font=("Franklin ", 10), justify="left", text = "1. Enumerate the efforts/measures that are currently being done to tackle the problem ")
aboutLabel3 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, font=("Franklin ", 10), justify="left", text = "2. List down the accomplishments and the assessments on each effort/measure")
aboutLabel4 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, font=("Franklin ", 10), justify="left", text = "3. Define the root cause of the problem")
aboutLabel5 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, font=("Franklin ", 10), justify="left", text = "4. Assess the existing policies ")

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

effortList = []

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

    projectTitle.config(text = data[0])
    polAnaTitle.config(text = data[1])
    probSit.config(text = data[2])
    undeEff.config(text = data[3])

    projectTitleLabel = Label(root, background="#9CDBA6", foreground="purple", text = "Project Title: ")
    polAnaTitleLabel = Label(root, background="#9CDBA6", foreground="purple",  text = "Policy Analysis Title: ")
    probSitLabel = Label(root, background="#9CDBA6", foreground="purple",  text = "Problematic Situation: ")
    undeEffLabel = Label(root, background="#9CDBA6", foreground="purple",  text = "Undesirable Effects: ")
    
    effortsTable=ttk.Treeview(root,selectmode='browse')
    effortsTable["columns"]=("1","2","3","4")
    effortsTable['show']='headings'
    effortsTable.column("1",width=30,anchor='c')
    effortsTable.column("2",width=200,anchor='c')
    effortsTable.column("3",width=200,anchor='c')
    effortsTable.column("4",width=200,anchor='c')
    effortsTable.heading("1",text="id")
    effortsTable.heading("2",text="Efforts/Measures")
    effortsTable.heading("3",text="Accomplishments")
    effortsTable.heading("4",text="Assessments")

    global i
    i = 0

    currEffoLabel = Label(root, background="#9CDBA6", foreground="purple",  text = "Current Efforts: ")
    accoLabel = Label(root, background="#9CDBA6", foreground="purple",  text = "Enter accomplishment: ")
    asseLabel = Label(root, background="#9CDBA6", foreground="purple",  text = "Enter assessment: ")
    effoLabel = Label(root, background="#9CDBA6", foreground="purple",  text = "Enter effort/: ")

    effort = tk.Text(root,  height=1, width=70,bg='white') 
    accomplishment = tk.Text(root,  height=1, width=70,bg='white') 
    assessment = tk.Text(root,  height=1, width=70,bg='white') 

    b1 = tk.Button(root,  text='Add Effort', width=10, command=lambda: add_data())  

    def add_data():

        effortText = effort.get("1.0",END)                    # read effort
        accomplishmentText = accomplishment.get("1.0",END)    # read accomplishment
        assessmentText = assessment.get("1.0",END)                # read assessment

        global i
        i = i + 1

        global efforttuple
        efforttuple = [effortText, accomplishmentText, assessmentText]

        effortList.append(efforttuple)

        effortsTable.insert("",'end', values=(i, effortText, accomplishmentText, assessmentText))
        effortText.delete('1.0',END)  # reset the text entry box
        accomplishmentText.delete('1.0',END)  # reset the text entry box
        assessmentText.delete('1.0',END)
        effort.focus()  
                
    projectTitleLabel.place(x=240, y=273)
    projectTitle.place(x=400, y=273)
    polAnaTitleLabel.place(x=240, y=303)
    polAnaTitle.place(x=400, y=303)
    probSitLabel.place(x=240, y=333)
    probSit.place(x=400, y=333) 
    undeEffLabel.place(x=240, y=363)
    undeEff.place(x=400, y=363)
    currEffoLabel.place(x=240, y=393)
    effortsTable.place(x=240, y=423)

    effoLabel.place(x=500, y=273)
    accoLabel.place(x=500, y=303)
    asseLabel.place(x=500, y=333)
    effort.place(x=700, y=273)
    accomplishment.place(x=700, y=303)
    assessment.place(x=700, y=333)

    b1.place(x=500, y=363)
      

def createNewProject():
    newProject = Toplevel(root)
    newProject.title("UPD Policy Maker - Create New Project")
    newProject.geometry("1080x700")

    scrollbar = ttk.Scrollbar(newProject)

    blank1 = Label(newProject, text = "  ")
    blank2 = Label(newProject, text = "  ")
    blank3 = Label(newProject, text = "  ")
    blank4 = Label(newProject, text = "  ")
    blank5 = Label(newProject, text = "  ")
    blank6 = Label(newProject, text = "  ")

    projectTitleLabel1 = Label(newProject, text = "Project Title")
    projectTitleLabel2 = Label(newProject, text = "Enter project title: ")
    projectTitle = Entry(newProject, width=30)

    settingsLabel = Label(newProject, text = "Settings")
    fontStyleLabel = Label(newProject, text = "Choose font style: ")
    fontSizeLabel = Label(newProject, text = "Choose font size: ")
    indentationLabel = Label(newProject, text = "Choose indentation: ")
    
    font.families()
    fonts = list(font.families())
    fonts.sort()
    
    selectedFont = tk.StringVar()

    fontsList = ttk.Combobox(newProject, width=30, values=fonts)
    
    fontSize = Entry(newProject, width=10)
    indentation = Entry(newProject, width=10)

    analystLabel1 = Label(newProject, text = "Analyst")
    analystLabel2 = Label(newProject, text = "Enter name of analyst: ")
    analyst = Entry(newProject, width=30)

    levelsLabel1 = Label(newProject, text = "Levels of Analysis ")
    levelsLabel2 = Label(newProject, text = "Check levels of analysis: ")

    varNat = tk.IntVar()
    varLoc = tk.IntVar()
    varOrg = tk.IntVar()

    national = tk.Checkbutton(newProject, text='National',variable=varNat, onvalue=1, offvalue=0)
    local = tk.Checkbutton(newProject, text='Local',variable=varLoc, onvalue=1, offvalue=0)
    organizational = tk.Checkbutton(newProject, text='Organizational',variable=varOrg, onvalue=1, offvalue=0)

    polAnaTitleLabel1 = Label(newProject, text = "Policy Analysis Title ")
    polAnaTitleLabel2 = Label(newProject, text = "Enter policy analysis title: ")
    polAnaTitle = Entry(newProject, width=30)

    probSitLabel1 = Label(newProject, text = "Problematic Situation")
    probSitLabel2 = Label(newProject, text = "Enter problematic situation: ")
    probSit = scrolledtext.ScrolledText(newProject, height = 5, width=30)
    
    undeEffLabel1 = Label(newProject, text = "Undesirable Effects")
    undeEffLabel2 = Label(newProject, text = "Enter undesirable effects: ")
    undeEff = scrolledtext.ScrolledText(newProject, height = 5, width=30)

    rootCLabel1 = Label(newProject, text = "Root Cause of the Problem")

    varRoot1 = tk.IntVar()
    varRoot2 = tk.IntVar()
    varRoot3 = tk.IntVar()
    varRoot4 = tk.IntVar()
    varRoot5 = tk.IntVar()
    varRoot6 = tk.IntVar()
    varRoot7 = tk.IntVar()

    quantitative = tk.Checkbutton(newProject, text='Quantitative',variable=varRoot1, onvalue=1, offvalue=0)
    regLin = tk.Checkbutton(newProject, text='Linear Regression',variable=varRoot2, onvalue=1, offvalue=0)
    regMul = tk.Checkbutton(newProject, text='Multiple Regression',variable=varRoot3, onvalue=1, offvalue=0)
    regLog = tk.Checkbutton(newProject, text='Logistic Regression',variable=varRoot4, onvalue=1, offvalue=0)
    qualitative = tk.Checkbutton(newProject, text='Qualitative',variable=varRoot5, onvalue=1, offvalue=0)
    probTreeAnalysis = tk.Checkbutton(newProject, text='Problem Tree Analysis',variable=varRoot6, onvalue=1, offvalue=0)
    delphiTechnique = tk.Checkbutton(newProject, text='Delphi Technique',variable=varRoot7, onvalue=1, offvalue=0)
    undeEff = scrolledtext.ScrolledText(newProject, height = 5, width=30)

    polProbLabel1 = Label(newProject, text = "Policy Problem")
    polProbLabel2 = Label(newProject, text = "Enter policy problem: ")
    polProb = scrolledtext.ScrolledText(newProject, height = 5, width=30)

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
    levelsLabel2.grid(row=9, column=2, sticky = W, padx=7)
    national.grid(row=9, column=3, sticky = W, padx=7)
    local.grid(row=10, column=3, sticky = W, padx=7)
    organizational.grid(row=11, column=3, sticky = W, padx=7)
    blank5.grid(row=4, column=0)
    probSitLabel1.grid(row=13, column=0, sticky = W, padx=7)
    probSitLabel2.grid(row=14, column=0, sticky = W, padx=7)
    probSit.grid(row=14, column=1, sticky = W, padx=7)
    undeEffLabel1.grid(row=13, column=2, sticky = W, padx=7)
    undeEffLabel2.grid(row=14, column=2, sticky = W, padx=7)
    undeEff.grid(row=14, column=3, sticky = W, padx=7)
    blank6.grid(row=15, column=0)
    rootCLabel1.grid(row=16, column=0, sticky = W, padx=7)
    quantitative.grid(row=17, column=0, sticky = W, padx=7)
    regLin.grid(row=18, column=0, sticky = W, padx=14)
    regLog.grid(row=19, column=0, sticky = W, padx=14)
    regMul.grid(row=20, column=0, sticky = W, padx=14)
    qualitative.grid(row=17, column=1, sticky = W, padx=7)
    probTreeAnalysis.grid(row=18, column=1, sticky = W, padx=14)
    delphiTechnique.grid(row=19, column=1, sticky = W, padx=14)
    polProbLabel1.grid(row=16, column=2, sticky = W, padx=7)
    polProbLabel2.grid(row=17, column=2, sticky = W, padx=7)
    polProb.grid(row=17, column=3, sticky = W, padx=7)
    
    def saveNewlyCreatedFile():
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

        n = varNat.get()
        l = varLoc.get()
        o = varOrg.get()

        quan = varRoot1.get()
        regLi = varRoot2.get()
        regMu = varRoot3.get()
        regLo = varRoot4.get()
        qual = varRoot5.get()
        prob = varRoot6.get()
        delp = varRoot7.get()

        data = [projecttitle, policyanalysis, problematicsituation, undesirableeffects, fontstyle, fontsize, n, l, o, quan, regLi, regMu, regLo, qual, prob, delp]

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

    btnCreate = Button(newProject, text = "Create a Project", command = lambda: saveNewlyCreatedFile())
    btnClear = Button(newProject, text = "Clear", command = lambda: clearCreate())
    btnCreate.grid(row=21, column=1, pady=10)
    btnClear.grid(row=21, column=0, pady=10)

menubar = Menu(root) 

file1 = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file1) 
file1.add_command(label ='Create New', command = createNewProject) 
file1.add_command(label ='Open', command = openFile) 
file1.add_command(label ='Save') 
file1.add_separator() 
file1.add_command(label ='Exit', command = root.destroy)

file2 = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Settings', menu = file2) 
file2.add_command(label ='Change Font Size', command = lambda: changeFontSize()) 
file2.add_command(label ='Change Font Style') 
file2.add_command(label ='Change Indentation') 

root.config(menu=menubar)

root.mainloop()