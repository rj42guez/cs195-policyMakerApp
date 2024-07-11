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

class Project:
    title: str
    lvlAnalysis: int
    problem: str
    effects: str
    efforts: list
    method: str
    root_cause: str
    policy_problem: str
    #more to come


def createNewStep3(lvlAnalysis): #steps 1 and 2 are already done in the root
    step3Window = Toplevel(root)
    step3Window.title("Policy Analytics - Create New Project (Problem and Effects)")
    step3Window.geometry("1000x700")

    introLabel = Label(step3Window, font=("Franklin Gothic Heavy", 12), text="Create New Project (Problem and Effects)")
    titleLabel = Label(step3Window, font=("Franklin ", 10), text="Enter Project Title: ")
    problemLabel = Label(step3Window, font=("Franklin ", 10), text="Enter Problematic Situation: ")
    effectsLabel = Label(step3Window, font=("Franklin ", 10), text="Enter Undesirable Effects: ")

    title = Entry(step3Window, width=100)
    problem = scrolledtext.ScrolledText(step3Window, height=10, width=75)
    effects = scrolledtext.ScrolledText(step3Window, height=10, width=74)

    introLabel.grid(row=0, column=0, sticky=W, padx=7, pady=20)
    titleLabel.grid(row=2, column=0, sticky=W, padx=7, pady=10)
    problemLabel.grid(row=3, column=0, sticky=W, padx=7, pady=10)
    effectsLabel.grid(row=4, column=0, sticky=W, padx=7, pady=10)
    title.grid(row=2, column=1, sticky=W, padx=7, pady=10)
    problem.grid(row=3, column=1, sticky=W, padx=7, pady=10)
    effects.grid(row=4, column=1, sticky=W, padx=7, pady=10)
    
    NextButton = tk.Button(step3Window, text="Next", background= "#ADD8E6", padx=20, pady=10, font=("Franklin Gothic Heavy", 10), command=lambda: tryNext())
    NextButton.grid(row=5, column=1, sticky=W, padx=7, pady=10)

    def tryNext():
        title.config(background="white")
        problem.config(background="white")
        effects.config(background="white")

        titleText = title.get()
        problemText = problem.get("1.0",'end-1c')
        effectsText = effects.get("1.0",'end-1c')

        if not titleText.strip():
            title.config(background="#ffd0d0")
            return
        if not problemText.strip():
            problem.config(background="#ffd0d0")
            return
        if not effectsText.strip():
            effects.config(background="#ffd0d0")
            return
        
        newProject = Project()
        newProject.title = titleText
        newProject.lvlAnalysis = lvlAnalysis
        newProject.problem = problemText
        newProject.effects = effectsText

        step3Window.destroy()
        createNewStep4(newProject)



def createNewStep4(newProject):
    step4Window = Tk()
    step4Window.title("Policy Analytics - Create New Project (Current Efforts)")
    step4Window.geometry("1000x700")

    introLabel = Label(step4Window, font=("Franklin Gothic Heavy", 12), text="Create New Project (Current Efforts)")
    instructionLabel = Label(step4Window, font=("Franklin ", 10), text="List down current efforts/measures of the government to solve the situational problem")

    introLabel.grid(row=0, column=0, columnspan=6, sticky=W, padx=7, pady=20) 
    instructionLabel.grid(row=2, column=0, columnspan=6, sticky=W, padx=7, pady=10)

    effortsLabel = Label(step4Window, font=("Franklin Gothic Heavy", 10), text="Efforts/Measures", width=30)
    accomplishmentsLabel = Label(step4Window, font=("Franklin Gothic Heavy", 10), text="Accomplishments", width=30)
    assessmentsLabel = Label(step4Window, font=("Franklin Gothic Heavy", 10), text="Assessments", width=30)

    effortsLabel.grid(row=3, column=0, columnspan=2, sticky=W, padx=7, pady=10)
    accomplishmentsLabel.grid(row=3, column=2, columnspan=2, sticky=W, padx=7, pady=10)
    assessmentsLabel.grid(row=3, column=4, sticky=W, columnspan=2, padx=7, pady=10)

    lastRow = 4
    effortCount = 0
    effortsList = []

    AddButton = tk.Button(step4Window, text="Add more", background= "#ffffe0", font=("Franklin", 10), command=lambda: addEffort(lastRow))
    AddButton.grid(row=lastRow, column = 0, sticky=W, padx=7, pady=10)

    NextButton = tk.Button(step4Window, text="Next", background= "#ADD8E6", padx=20, pady=10, font=("Franklin Gothic Heavy", 10), command=lambda: tryNext(), state=tk.DISABLED)
    NextButton.grid(row=lastRow+2, column=0, sticky=W, padx=7, pady=10)

    def addEffort(i):
        newEffort = Entry(step4Window, width=30)
        newAccomplishments = Entry(step4Window, width=30)
        newAssessments = Entry(step4Window, width=30)

        newEffort.grid(row=i, column=0, columnspan=2, sticky=W, padx=7, pady=10)
        newAccomplishments.grid(row=i, column=2, columnspan=2, sticky=W, padx=7, pady=10)
        newAssessments.grid(row=i, column=4, columnspan=2, sticky=W, padx=7, pady=10)

        nonlocal lastRow, AddButton, effortCount, effortsList, NextButton
        lastRow += 1
        effortCount += 1
        
        NextButton.grid(row=lastRow+2, column=0, sticky=W, padx=7, pady=10)
        NextButton.config(state=tk.NORMAL)

        AddButton.grid(row=lastRow, column = 0, sticky=W, padx=7, pady=10)
        if effortCount == 10:
            AddButton.config(state=tk.DISABLED)

        effortsList.append([newEffort, newAccomplishments, newAssessments])

    def tryNext():
        effortsListText = []

        for effort in effortsList:
            entryText = []
            for item in effort:
                entryText.append(item.get())
            effortsListText.append(entryText)

        newProject.efforts = effortsListText

        step4Window.destroy()
        createNewStep5(newProject)



def createNewStep5(newProject):
    step5Window = Tk()
    step5Window.title("Policy Analytics - Create New Project (Method)")
    step5Window.geometry("1000x700")

    introLabel = Label(step5Window, font=("Franklin Gothic Heavy", 12), text="Create New Project (Method)")
    instructionLabel = Label(step5Window, font=("Franklin ", 10), text="Pick a method to use")
    introLabel.grid(row=0, column=0, columnspan=2, sticky=W, padx=7, pady=20) 
    instructionLabel.grid(row=2, column=0, columnspan=2, sticky=W, padx=7, pady=10)

    quantiLabel = Label(step5Window, font=("Franklin Gothic Heavy", 10), text="Quantitative")
    qualiLabel = Label(step5Window, font=("Franklin Gothic Heavy", 10), text="Qualitative")
    quantiLabel.grid(row=3, column=0, sticky=W, padx=7, pady=10)
    qualiLabel.grid(row=3, column=1, sticky=W, padx=7, pady=10)

    method = tk.StringVar(value="")
    linearReg = tk.Radiobutton(step5Window, text='Linear regression', font=("Franklin ", 10), variable=method, value="linear regression", command=lambda: NextButton.config(state=tk.NORMAL))
    multipleReg = tk.Radiobutton(step5Window, text='Multiple regression', font=("Franklin ", 10), variable=method, value="multiple regression", command=lambda: NextButton.config(state=tk.NORMAL))
    logisticReg = tk.Radiobutton(step5Window, text='Logistic regression', font=("Franklin ", 10), variable=method, value="logistic regression", command=lambda: NextButton.config(state=tk.NORMAL))
    problemTree = tk.Radiobutton(step5Window, text='Problem Tree Analysis', font=("Franklin ", 10), variable=method, value="problem tree analysis", command=lambda: NextButton.config(state=tk.NORMAL))
    delphiTech = tk.Radiobutton(step5Window, text='Delphi Technique', font=("Franklin ", 10), variable=method, value="delphi technique", command=lambda: NextButton.config(state=tk.NORMAL))

    linearReg.grid(row=4, column=0, sticky=W, padx=7, pady=10)
    multipleReg.grid(row=5, column=0, sticky=W, padx=7, pady=10)
    logisticReg.grid(row=6, column=0, sticky=W, padx=7, pady=10)
    problemTree.grid(row=4, column=1, sticky=W, padx=7, pady=10)
    delphiTech.grid(row=5, column=1, sticky=W, padx=7, pady=10)

    NextButton = tk.Button(step5Window, text="Next", background= "#ADD8E6", padx=20, pady=10, font=("Franklin Gothic Heavy", 10), command=lambda: tryNext(newProject), state=tk.DISABLED)
    NextButton.grid(row=7, column=0, sticky=W, padx=7, pady=10)

    def tryNext(newProject):
        newProject.method = method

        step5Window.destroy()
        createNewStep6(newProject)



def createNewStep6(newProject):
    step6Window = Tk()
    step6Window.title("Policy Analytics - Create New Project (Method Process)")
    step6Window.geometry("1000x700")

    introLabel = Label(step6Window, font=("Franklin Gothic Heavy", 12), text="Create New Project (Method Process)")
    instructionLabel = Label(step6Window, font=("Franklin ", 10), text="idk kung ano gagawin dito lol")
    introLabel.grid(row=0, column=0, sticky=W, padx=7, pady=20) 
    instructionLabel.grid(row=2, column=0, sticky=W, padx=7, pady=10)

    NextButton = tk.Button(step6Window, text="Next", background= "#ADD8E6", padx=20, pady=10, font=("Franklin Gothic Heavy", 10), command=lambda: tryNext(newProject))
    NextButton.grid(row=4, column=0, sticky=W, padx=7, pady=10)

    def tryNext(newProject):
        step6Window.destroy()
        createNewStep8(newProject)



def createNewStep8(newProject): #step 7 already done in step 6
    step8Window = Tk()
    step8Window.title("Policy Analytics - Create New Project (Policy Assessments)")
    step8Window.geometry("1000x700")

    introLabel = Label(step8Window, font=("Franklin Gothic Heavy", 12), text="Create New Project (Policy Assessments)")
    instructionLabel = Label(step8Window, font=("Franklin ", 10), text="Assessments of existing policies that address the root cause. [UNFINISHED]")
    introLabel.grid(row=0, column=0, sticky=W, padx=7, pady=20) 
    instructionLabel.grid(row=2, column=0, sticky=W, padx=7, pady=10)

    NextButton = tk.Button(step8Window, text="Next", background= "#ADD8E6", padx=20, pady=10, font=("Franklin Gothic Heavy", 10), command=lambda: tryNext(newProject))
    NextButton.grid(row=4, column=0, sticky=W, padx=7, pady=10)

    def tryNext(newProject):
        step8Window.destroy()
        createNewStep9(newProject)



def createNewStep9(newProject):
    step9Window = Toplevel(root)
    step9Window.title("Policy Analytics - Create New Project (Root cause and policy problem)")
    step9Window.geometry("1000x700")

    introLabel = Label(step9Window, font=("Franklin Gothic Heavy", 12), text="Create New Project (Root cause and policy problem)")
    causeLabel = Label(step9Window, font=("Franklin ", 10), text="Enter Root Cause: ")
    policyLabel = Label(step9Window, font=("Franklin ", 10), text="Enter Policy Problem: ")

    title = Entry(step9Window, width=100)
    cause = scrolledtext.ScrolledText(step9Window, height=10, width=75)
    policy = scrolledtext.ScrolledText(step9Window, height=10, width=74)

    introLabel.grid(row=0, column=0, sticky=W, padx=7, pady=20)
    causeLabel.grid(row=3, column=0, sticky=W, padx=7, pady=10)
    policyLabel.grid(row=4, column=0, sticky=W, padx=7, pady=10)
    title.grid(row=2, column=1, sticky=W, padx=7, pady=10)
    cause.grid(row=3, column=1, sticky=W, padx=7, pady=10)
    policy.grid(row=4, column=1, sticky=W, padx=7, pady=10)
    
    NextButton = tk.Button(step9Window, text="Next", background= "#ADD8E6", padx=20, pady=10, font=("Franklin Gothic Heavy", 10), command=lambda: tryNext(newProject))
    NextButton.grid(row=5, column=1, sticky=W, padx=7, pady=10)

    def tryNext(newProject):
        cause.config(background="white")
        policy.config(background="white")

        causeText = cause.get("1.0",'end-1c')
        policyText = policy.get("1.0",'end-1c')

        if not causeText.strip():
            cause.config(background="#ffd0d0")
            return
        if not policyText.strip():
            policy.config(background="#ffd0d0")
            return
        
        newProject.lvlAnalysis = lvlAnalysis
        newProject.root_cause = causeText
        newProject.policy_problem = policyText

        step9Window.destroy()
        createNewStep10(newProject)



def createNewStep10(newProject):
    step10Window = Tk()
    step10Window.title("Policy Analytics - Create New Project (Policy Formmulation)")
    step10Window.geometry("1000x700")

    introLabel = Label(step10Window, font=("Franklin Gothic Heavy", 12), text="Create New Project (Policy Formulation)")
    instructionLabel = Label(step10Window, font=("Franklin ", 10), text="idk")
    introLabel.grid(row=0, column=0, sticky=W, padx=7, pady=20) 
    instructionLabel.grid(row=2, column=0, sticky=W, padx=7, pady=10)

    title = Label(step10Window, font=("Franklin ", 10), text="Title: "+newProject.title)
    lvlAnalysis = Label(step10Window, font=("Franklin ", 10), text="Level of analysis: "+str(newProject.lvlAnalysis.get()))
    problem = Label(step10Window, font=("Franklin ", 10), text="Problem: "+newProject.problem)
    effects = Label(step10Window, font=("Franklin ", 10), text="Effects: "+newProject.effects)
    efforts = Label(step10Window, font=("Franklin ", 10), text="Efforts: "+str(newProject.efforts))
    method = Label(step10Window, font=("Franklin ", 10), text="Method: "+str(newProject.method.get()))
    root_cause = Label(step10Window, font=("Franklin ", 10), text="Root cause: "+newProject.root_cause)
    policy_problem = Label(step10Window, font=("Franklin ", 10), text="Policy problem: "+newProject.policy_problem)

    title.grid(row=3, column=0, sticky=W, padx=7, pady=10)
    lvlAnalysis.grid(row=4, column=0, sticky=W, padx=7, pady=10)
    problem.grid(row=5, column=0, sticky=W, padx=7, pady=10)
    effects.grid(row=6, column=0, sticky=W, padx=7, pady=10)
    efforts.grid(row=7, column=0, sticky=W, padx=7, pady=10)
    method.grid(row=8, column=0, sticky=W, padx=7, pady=10)
    root_cause.grid(row=9, column=0, sticky=W, padx=7, pady=10)
    policy_problem.grid(row=10, column=0, sticky=W, padx=7, pady=10)

    NextButton = tk.Button(step10Window, text="Done", background= "#ADD8E6", padx=20, pady=10, font=("Franklin Gothic Heavy", 10), command=lambda: tryNext(newProject))
    NextButton.grid(row=12, column=0, sticky=W, padx=7, pady=10)

    def tryNext(newProject): #temporary function
        step10Window.destroy()



#ROOT WINDOW
root = Tk()
root.title("Policy Analytics")
root.geometry("1300x700")

main = tk.PanedWindow(root, background="#468585")
main.pack(side="top", fill="both", expand=True)

left_pane = tk.Frame(main, background="#DEF9C4", width=200)
right_pane = tk.PanedWindow(main, background="#9CDBA6", width=200)
main.add(left_pane)
main.add(right_pane)

introLabel = Label(main, background="#9CDBA6", foreground="purple", font=("Franklin Gothic Heavy", 14), text = "Policy Analytics")
aboutLabel1 = Label(main, background="#9CDBA6", foreground="purple", font=("Franklin ", 10), wraplength=1000, justify="left", text = "Policy Analytics is exclusive to all students, faculty, and staff of the UP Diliman community. Here, users start by creating an analysis on a policy and defining the problematic situation and their undesirable effects. It also lets them do the following:")
aboutLabel2 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, font=("Franklin ", 10), justify="left", text = "1. Enumerate the efforts/measures that are currently being done to tackle the problem ")
aboutLabel3 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, font=("Franklin ", 10), justify="left", text = "2. List down the accomplishments and the assessments on each effort/measure")
aboutLabel4 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, font=("Franklin ", 10), justify="left", text = "3. Define the root cause of the problem")
aboutLabel5 = Label(main, background="#9CDBA6", foreground="purple", wraplength=1000, font=("Franklin ", 10), justify="left", text = "4. Assess the existing policies ")

introLabel.place(x=600, y=23)
aboutLabel1.place(x=240, y=63)
aboutLabel2.place(x=240, y=123)
aboutLabel3.place(x=240, y=153)
aboutLabel4.place(x=240, y=183)
aboutLabel5.place(x=240, y=213)

lvlAnalysis = tk.IntVar(value=0)

lvlAnalysisLabel = Label(main, background="#9CDBA6", foreground="purple", font=("Franklin ", 10), wraplength=1000, justify="left", text = "Choose level of analysis:")
national = tk.Radiobutton(root, text='National', background="#9CDBA6", foreground="purple", activebackground="#9CDBA6", font=("Franklin ", 10), variable=lvlAnalysis, value=3, command=lambda: createButton.config(state=tk.NORMAL))
local = tk.Radiobutton(root, text='Local', background="#9CDBA6", foreground="purple", activebackground="#9CDBA6", font=("Franklin ", 10), variable=lvlAnalysis, value=2, command=lambda: createButton.config(state=tk.NORMAL))
organizational = tk.Radiobutton(root, text='Organizational', background="#9CDBA6", foreground="purple", activebackground="#9CDBA6", font=("Franklin ", 10), variable=lvlAnalysis, value=1, command=lambda: createButton.config(state=tk.NORMAL))
createButton = tk.Button(root, text="Create New", background="purple", foreground="#FFFFE0", padx=20, pady=10, font=("Franklin Gothic Heavy", 10), command=lambda: createNewStep3(lvlAnalysis), state=tk.DISABLED)

lvlAnalysisLabel.place(x=240, y=273)
national.place(x=240, y=303)
local.place(x=240, y=333)
organizational.place(x=240, y=363)
createButton.place(x=240, y=393)



root.mainloop()