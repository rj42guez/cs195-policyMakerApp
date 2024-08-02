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
from pathlib import Path
import csv
import seaborn as sns
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt 
from sklearn import linear_model
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from mpl_toolkits.mplot3d import axes3d
from licensing.models import *
from licensing.methods import Key, Helpers


global size
size = 10

root = Tk()
root.title("Policy Analytics")
root.geometry("1300x700")

main = tk.PanedWindow(root, background="#ffffff")

main.pack(side="top", fill="both", expand=True)

# activeKey = "password12345"

# enterActiveKey = input("Please enter the activation key down below:\n")
# if activeKey == enterActiveKey:
#     print("Activation key is successful.")
# while activeKey != enterActiveKey:
#     print("Activation key is incorrect. Please re-run the program")
#     break

left_pane = tk.Frame(main, background="#76090c", width=200)
right_pane = tk.PanedWindow(main, background="#ffffff", width=200)
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

introLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin Gothic Heavy", 14), text = "Welcome to Policy Analytics")
aboutLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Policy Analytics is a tool for learning policy analysis. This software can be used in training programs and classroom learning. It provides a step-by-step procedure that allows users to input and process basic essential data for problem structuring, forecasting and assessment of policy alternatives, recommending or prescribing the best/optimal policy alternative, designing an implementation plan, and building a monitoring and evaluation plan. Its outputs can be used in writing a complete policy issue paper. It is based on the “Elements of the Policy Issue Paper” in Annex 1 of Public Policy Analysis: An Integrated Approach by William N. Dunn (2018) with modifications based on the teaching and training experiences of its creator, Dr. Ebinezer R. Florano, Professor of Public Policy at the University of the Philippines, National College of Public Administration and Governance and Convenor of the UPCIDS Data Science for Public Policy Program (DSPPP).")
arrLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "All rights reserved@2024 – UPCIDS-DSPPP")
creatorLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Creator: Dr. Ebinezer R. Florano")
programmerLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Programmers: Raphael Justin Portuguez and Emmerson Isip")
reveiwerLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Reviewers: --------------")
adminLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Administrative Assistance: Lilian J. Marfil and Zhelly Ann Langsangan")

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


    
def createNewProject():

    newProject = Toplevel(root)
    newProject.title("UPD Policy Maker - Create New Project")
    newProject.geometry("660x210")

    blank = Label(newProject, text = "  ")
    
    frame1 = tk.LabelFrame(newProject)

    projectTitleLabel1 = Label(frame1, text = "Project Title")
    projectTitle = Entry(frame1, width=30)

    settingsLabel = Label(frame1, text = "Settings")
    fontStyleLabel = Label(frame1, text = "Choose font style: ")
    fontSizeLabel = Label(frame1, text = "Choose font size: ")
    indentationLabel = Label(frame1, text = "Choose indentation: ")
    
    font.families()
    fonts = list(font.families())
    fonts.sort()

    fontsList = ttk.Combobox(frame1, width=30, values=fonts)
    fontSize = Entry(frame1, width=10)
    indentation = Entry(frame1, width=10)

    analystNameLabel1 = Label(frame1, text = "Analyst")
    analystName = Entry(frame1, width=30)

    levelsLabel1 = Label(frame1, text = "Levels of Analysis ")

    varNat = tk.IntVar()
    varLoc = tk.IntVar()
    varOrg = tk.IntVar()

    national = tk.Checkbutton(frame1, text='National',variable=varNat, onvalue=1, offvalue=0)
    local = tk.Checkbutton(frame1, text='Local',variable=varLoc, onvalue=1, offvalue=0)
    organizational = tk.Checkbutton(frame1, text='Organizational',variable=varOrg, onvalue=1, offvalue=0)

    polAnaTitleLabel1 = Label(frame1, text = "Policy Analysis Title ")
    polAnaTitle = Entry(frame1, width=30)

    varRoot1 = tk.IntVar()
    varRoot2 = tk.IntVar()
    varRoot3 = tk.IntVar()
    varRoot4 = tk.IntVar()
    varRoot5 = tk.IntVar()
    varRoot6 = tk.IntVar()
    varRoot7 = tk.IntVar()

    frame1.place(x=10, y=10)
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
    
    def clearCreate():
        projectTitle.config(bg="white")
        fontSize.config(bg="white")
        polAnaTitle.config(bg="white")
        # probSit.config(bg="white")
        # undeEff.config(bg="white")
        
        projectTitle.delete(0, END)
        polAnaTitle.delete(0, END)
        fontSize.delete(0, END)
        indentation.delete(0, END)
        # probSit.delete("1.0", tk.END)
        # undeEff.delete("1.0", tk.END)

    def saveNewProject():
        projecttitle = projectTitle.get()
        if not projecttitle.strip():
                projectTitle.config(bg="#ffd0d0")
                return
        
        fontstyle = fontsList.get()
            
        fontsize = fontSize.get()
        if fontsize.isnumeric() == False:
            fontSize.config(bg="#ffd0d0")
            return

        analyst = analystName.get()
        if not analyst.strip():
            analystName.config(bg="#ffd0d0")
            return
            
        policyanalysis = polAnaTitle.get()
        if not policyanalysis.strip():
            polAnaTitle.config(bg="#ffd0d0")
            return
            
        # problematicsituation = probSit.get("1.0", tk.END)
        # if not problematicsituation.strip():
        #     probSit.config(bg="#ffd0d0")
        #     return
                
        # undesirableeffects = undeEff.get("1.0", tk.END)
        # if not undesirableeffects.strip():
        #     undeEff.config(bg="#ffd0d0")
        #     return
        # save the project
        filename = projecttitle
        fileobject = open(filename + '.pol', 'w')
        fileobject.close()

        frame1.destroy() 
        btnCreate.destroy() 
        btnClear.destroy() 

        # write problematic situation and undesirable effects

        frame2 = tk.LabelFrame(newProject)

        probSitLabel = Label(frame2, text = "Problematic Situation")
        probSit = scrolledtext.ScrolledText(frame2, height = 8, width=30)
        
        undeEffLabel = Label(frame2, text = "Undesirable Effects")
        undeEff = scrolledtext.ScrolledText(frame2, height = 8, width=30)
        
        frame2.place(x=40, y=10)
        probSitLabel.grid(row=1, column=0, sticky = W, padx=7)
        probSit.grid(row=2, column=0, sticky = W, padx=7)
        undeEffLabel.grid(row=1, column=1, sticky = W, padx=7)
        undeEff.grid(row=2, column=1, sticky = W, padx=7)

        def next1():
            frame2.destroy() 
            btnNext1.destroy() 

            newProject.geometry("640x500")
            
            frame3 = tk.LabelFrame(newProject)

            # enumerate current efforts

            currEffLabel = Label(frame3, text = "Current Efforts/Measures of the Government to Solve the Situational Problem")
            effortsTable=ttk.Treeview(frame3)
            effortsTable["columns"]=("1","2","3")
            effortsTable['show']='headings'
            effortsTable.column("1",width=200,anchor='c')
            effortsTable.column("2",width=200,anchor='c')
            effortsTable.column("3",width=200,anchor='c')
            effortsTable.heading("1",text="Effort/Measure")
            effortsTable.heading("2",text="Accomplishments")
            effortsTable.heading("3",text="Assessment")

            effoLabel = Label(newProject, text = "Effort")
            accoLabel = Label(newProject, text = "Accomplishment")
            asseLabel = Label(newProject, text = "Assessment")

            effort = tk.Entry(newProject, width=20)
            accomplishment = tk.Entry(newProject, width=20) 
            assessment = tk.Entry(newProject, width=20) 

            addButton = tk.Button(newProject, text='Add', width=10, command=lambda: add_data())  
            editButton = tk.Button(newProject, text="Edit", width=10, command=lambda: edit_data())

            def show_data(a):
                effort.delete(0,END)
                accomplishment.delete(0,END)
                assessment.delete(0,END)

                selectedItem = effortsTable.selection()[0]
                effort.insert(0, effortsTable.item(selectedItem)['values'][0])
                accomplishment.insert(0, effortsTable.item(selectedItem)['values'][1])
                assessment.insert(0, effortsTable.item(selectedItem)['values'][2])

            effortsTable.bind("<<TreeviewSelect>>", show_data)

            def edit_data():
                effortText = effort.get()                          # read effort
                accomplishmentText = accomplishment.get()          # read accomplishment
                assessmentText = assessment.get()                  # read assessment

                selected_item = effortsTable.selection()[0]
                effortsTable.item(selected_item, text="blub", values=(effortText, accomplishmentText, assessmentText))

            def add_data():
                effortText = effort.get()                          # read effort
                accomplishmentText = accomplishment.get()          # read accomplishment
                assessmentText = assessment.get()                  # read assessment

                effortsTable.insert("",'end', values=(effortText, accomplishmentText, assessmentText))
                effortText.delete('1.0',END)  # reset the text entry box
                accomplishmentText.delete('1.0',END)  # reset the text entry box
                assessmentText.delete('1.0',END)
                effort.focus() 

            frame3.place(x=10, y=10)
            currEffLabel.grid(row=0, column=1)
            effortsTable.grid(row=1, column=1)
            effoLabel.place(x=90, y=270)
            effort.place(x=45, y=300)
            accoLabel.place(x=275, y=270)
            accomplishment.place(x=261, y=300)
            asseLabel.place(x=510, y=270)
            assessment.place(x=480, y=300)
            addButton.place(x=190, y=330)
            editButton.place(x=380, y=330)

            def next2():
                frame3.destroy() 
                btnNext2.destroy() 

                newProject.geometry("660x210")

                frame4 = tk.LabelFrame(newProject)

                var = IntVar()
                
                StatisticalMethod = Label(frame4, text = "Statistical Method")
                Qualita = Label(frame4, text = "Qualitative")
                Quantita = Label(frame4, text = "Quantitative")
                R1 = Radiobutton(frame4, text="Linear Regression", variable=var, value=1)
                R2 = Radiobutton(frame4, text="Multiple Regression", variable=var, value=2)
                R3 = Radiobutton(frame4, text="Logistic Regression", variable=var, value=3)
                R4 = Radiobutton(frame4, text="Problem Tree Analysis", variable=var, value=4)
                R5 = Radiobutton(frame4, text="Delphi Technique", variable=var, value=5)

                StatisticalMethod.place(x = 275, y=10)
                frame4.place(x=190, y=50)
                Quantita.grid(row=1, column=0)
                Qualita.grid(row=1, column=1)
                R1.grid(row=2, column=0)
                R2.grid(row=3, column=0)
                R3.grid(row=4, column=0)
                R4.grid(row=2, column=1)
                R5.grid(row=3, column=1)

                def next3():                    
                    if (int(var.get()) == 1):
                        analysis = Toplevel(main)
                        analysis.title("UPD Policy Maker - Analysis")
                        analysis.geometry("830x480")

                        filename = askopenfilename(filetypes=[("CSV Files", "*.csv")])
                        df = pd.read_csv(filename, usecols=[0,1])
                        data_x = df.iloc[:, [0]]
                        data_y = df.iloc[:, [1]]

                        column_names = list(df.columns)

                        model = sm.OLS(data_y, data_x).fit()


                        lb1 = Label(analysis,text=model.summary(), font="Consolas", justify="left")
                        lb1.pack()

                        ax = sns.lmplot(x=column_names[0], y=column_names[1], data=df, aspect=1.5, scatter_kws={'alpha':0.2})
                        plt.show() 
                        
                    elif(int(var.get()) == 2):
                        analysis = Toplevel(main)
                        analysis.title("UPD Policy Maker - Analysis")
                        analysis.geometry("830x480")
                        
                        filename = askopenfilename(filetypes=[("CSV Files", "*.csv")])
                        df = pd.read_csv(filename)

                        # data_x = df.iloc[:, [0]]
                        # data_y = df.iloc[:, [1]]
                        # Define the independent variables
                        df.head()

                        x = df['RM']
                        y = df['CRIM']
                        z = df['MEDV']

                        
                        fig = plt.figure()
                        ax = fig.add_subplot(111, projection='3d')

                        # Define the independent variables
                        # Add the data points
                        ax.scatter(x, y, z)

                        # # Fit a plane using np.linalg.lstsq
                        # A = np.vstack([x, y, np.ones_like(x)]).T
                        # plane_coef, _, _, _ = np.linalg.lstsq(A, z, rcond=None)

                        # # Create a meshgrid for the plane
                        # x_plane, y_plane = np.meshgrid(x, y)
                        # z_plane = plane_coef[0] * x_plane + plane_coef[1] * y_plane + plane_coef[2]

                        # # Add the regression plane
                        # ax.plot_surface(x_plane, y_plane, z_plane, alpha=0.5)

                        # Add labels and title
                        ax.set_xlabel('Number of Rooms')
                        ax.set_ylabel('Crime Rate')
                        ax.set_zlabel('Median Value of Homes ($1000s)')
                        plt.title('Multiple Linear Regression')

                        # Show the plot
                        plt.show()

                    elif(int(var.get()) == 3):
                        analysis = Toplevel(main)
                        analysis.title("UPD Policy Maker - Analysis")
                        analysis.geometry("830x480")

                        filename = askopenfilename(filetypes=[("CSV Files", "*.csv")])
                        df = pd.read_csv(filename)
                        data_x = df.iloc[:, [0]]
                        data_y = df.iloc[:, [1]]

                        column_names = list(df.columns)

                        logit_model = sm.Logit(data_y, data_x).fit()

                        lb1 = Label(analysis,text=logit_model.summary(), font="Consolas", justify="left")
                        lb1.pack()

                        ax = sns.regplot(x=column_names[0], y=column_names[1], data=df, logistic=True, scatter_kws={'color': 'black'}, line_kws={'color': 'red'})
                        plt.show() 
                    
                    elif(int(var.get()) == 4):
                        analysis = Toplevel(main)
                        analysis.title("UPD Policy Maker - Analysis")
                        analysis.geometry("830x480")

                        class ShapeEditorApp:

                            def __init__(self, root):
                                global textValue
                                textValue = StringVar()

                                self.root = root
                                self.root.title("UPD Policy Maker - Analysis")

                                # Create Canvas widget
                                self.canvas = tk.Canvas(analysis, bg="white")
                                self.canvas.pack(fill=tk.BOTH, expand=True)

                                # Initialize shape variables
                                self.current_shape = None
                                self.start_x = None
                                self.start_y = None
                                self.current_shape_item = None

                                # Create buttons
                                self.color_button = tk.Button(root, text="Color", command=self.choose_color)
                                self.pen_button = Button(root, text='Pen', command=self.use_pen)
                                self.rect_button = tk.Button(root, text="Rectangle", command=self.create_rectangle)
                                self.circle_button = tk.Button(root, text="Arrow", command=self.create_arrow)
                                self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
                                self.text_frame = Frame(root, height=100, width=200, relief=SUNKEN, borderwidth=3)
                                self.text_entry = Entry(self.text_frame, textvariable=textValue, bg="white" , width=20)
                                self.pen_button.pack(side=tk.LEFT)
                                self.clear_button.pack(side=tk.LEFT)
                                self.color_button.pack(side=tk.LEFT)
                                self.rect_button.pack(side=tk.LEFT)
                                self.circle_button.pack(side=tk.LEFT)
                                self.text_frame.pack(side=tk.LEFT)                         
                                self.text_entry.pack(side=tk.LEFT)

                                # Bind mouse events
                                self.canvas.bind("<Button-1>", self.start_draw)
                                self.canvas.bind("<B1-Motion>", self.draw_shape)
                                self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
                                self.canvas.bind("<Button-2>", self.add_text)
                                self.canvas.bind("<Button-3>", self.add_text)

                            def add_text(self, event):
                                self.canvas.create_text(event.x, event.y, text=textValue.get())
                            
                            def use_pen(self):
                                self.activate_button(self.pen_button)

                            def choose_color(self):
                                global color 
                                color = colorchooser.askcolor(title="Choose color")

                            def create_rectangle(self):
                                self.current_shape = "rectangle"

                            def create_arrow(self):
                                self.current_shape = "arrow"

                            def start_draw(self, event):
                                self.start_x = event.x
                                self.start_y = event.y
                                if self.current_shape == "rectangle":
                                    self.current_shape_item = self.canvas.create_rectangle(
                                        self.start_x, self.start_y, self.start_x, self.start_y, outline=color[1]
                                    )
                                elif self.current_shape == "arrow":
                                    self.current_shape_item = self.canvas.create_line(
                                        self.start_x, self.start_y, self.start_x, self.start_y, fill=color[1], arrow="last", width=5
                                    )

                            def draw_shape(self, event):
                                if self.current_shape_item:
                                    x, y = event.x, event.y
                                    self.canvas.coords(self.current_shape_item, self.start_x, self.start_y, x, y)

                            def stop_draw(self, event):
                                self.current_shape_item = None

                            def clear_canvas(self):
                                self.canvas.delete("all")

                        app = ShapeEditorApp(analysis)
                        
                    frame4.destroy() 
                    btnNext3.destroy() 

                    newProject.geometry("830x480")

                    frame5 = tk.LabelFrame(newProject)

                    assessExistLabel = Label(frame5, text = "Assessment of Existing Policies that Address the Root Cause")
                    assessmentTable=ttk.Treeview(frame5)
                    assessmentTable["columns"]=("1","2","3","4")
                    assessmentTable['show']='headings'
                    assessmentTable.column("1",width=200,anchor='c')
                    assessmentTable.column("2",width=200,anchor='c')
                    assessmentTable.column("3",width=200,anchor='c')
                    assessmentTable.column("4",width=200,anchor='c')
                    assessmentTable.heading("1",text="Existing Policy")
                    assessmentTable.heading("2",text="Relevant Provision(s)")
                    assessmentTable.heading("3",text="Accomplishments")
                    assessmentTable.heading("4",text="Assessment")

                    existLabel = Label(newProject, text = "Existing Policy")
                    releLabel = Label(newProject, text = "Relevant Provision")
                    accompLabel2 = Label(newProject, text = "Accomplishment")
                    assessLabel2 = Label(newProject, text = "Assessment")

                    existingPolicy = tk.Entry(newProject, width=30)
                    relevantProvision = tk.Entry(newProject, width=30) 
                    accomplishment2 = tk.Entry(newProject, width=30) 
                    assessment2 = tk.Entry(newProject, width=30) 

                    addButton2 = tk.Button(newProject, text='Add', width=10, command=lambda: add_data2())  
                    editButton2 = tk.Button(newProject, text="Edit", width=10, command=lambda: edit_data2())

                    def show_data2(a):
                        existingPolicy.delete(0,END)
                        relevantProvision.delete(0,END)
                        accomplishment2.delete(0,END)
                        assessment2.delete(0,END)

                        selectedItem = assessmentTable.selection()[0]
                        existingPolicy.insert(0, assessmentTable.item(selectedItem)['values'][0])
                        relevantProvision.insert(0, assessmentTable.item(selectedItem)['values'][1])
                        accomplishment2.insert(0, assessmentTable.item(selectedItem)['values'][2])
                        assessment2.insert(0, assessmentTable.item(selectedItem)['values'][3])

                    assessmentTable.bind("<<TreeviewSelect>>", show_data2)

                    def edit_data2():
                        existingPolicyText = existingPolicy.get()               # read existing policy
                        relevantProvisionText = relevantProvision.get()         # read relevant provision
                        accomplishment2Text = accomplishment2.get()             # read accomplishment 
                        assessment2Text = assessment2.get()                     # read assessment                 
                                                
                        selected_item = assessmentTable.selection()[0]
                        assessmentTable.item(selected_item, text="blub", values=(existingPolicyText, relevantProvisionText, accomplishment2Text, assessment2Text))

                    def add_data2():
                        existingPolicyText = existingPolicy.get()               # read existing policy
                        relevantProvisionText = relevantProvision.get()         # read relevant provision
                        accomplishment2Text = accomplishment2.get()             # read accomplishment 
                        assessment2Text = assessment2.get()                     # read assessment      

                        global assessmentTuple
                        assessmentTuple = [existingPolicyText, relevantProvisionText, accomplishment2Text, assessment2Text]

                        # effortList.append(efforttuple)

                        assessmentTable.insert("",'end', values=(existingPolicyText, relevantProvisionText, accomplishment2Text, assessment2Text))
                        existingPolicyText.delete('1.0',END)                    # reset the text entry box
                        relevantProvisionText.delete('1.0',END)                 # reset the text entry box
                        accomplishment2Text.delete('1.0',END)                   # reset the text entry box
                        assessment2Text.delete('1.0',END)                       # reset the text entry box
                        existingPolicyText.focus() 

                    frame5.place(x=10, y=10)
                    effoLabel.destroy()
                    effort.destroy()
                    accoLabel.destroy()
                    accomplishment.destroy()
                    asseLabel.destroy()
                    assessment.destroy()
                    addButton.destroy()
                    editButton.destroy()
                    assessExistLabel.grid(row=0, column=1)
                    assessmentTable.grid(row=1, column=1)
                    existLabel.place(x=40, y=270)
                    existingPolicy.place(x=200, y=270)
                    releLabel.place(x=40, y=330)
                    relevantProvision.place(x=200, y=330)
                    accompLabel2.place(x=40, y=390)
                    accomplishment2.place(x=200, y=390)
                    assessLabel2.place(x=40, y=450)
                    assessment2.place(x=200, y=450)
                    addButton2.place(x=450, y=330)
                    editButton2.place(x=450, y=390)

                    def next4():
                        frame5.destroy() 
                        btnNext4.destroy() 

                        existLabel.destroy()
                        existingPolicy.destroy()
                        releLabel.destroy()
                        relevantProvision.destroy()
                        accoLabel.destroy()
                        accompLabel2.destroy()
                        assessLabel2.destroy()
                        assessment2.destroy()
    
                        newProject.geometry("660x210")

                        # write problematic situation and undesirable effects

                        frame6 = tk.LabelFrame(newProject)

                        rootCauseLabel = Label(frame6, text = "Root Cause of the Problem")
                        rootCause = scrolledtext.ScrolledText(frame6, height = 8, width=30)
                        
                        policyProbLabel = Label(frame6, text = "Policy Problem")
                        policyProb = scrolledtext.ScrolledText(frame6, height = 8, width=30)
                        
                        frame6.place(x=40, y=10)
                        rootCauseLabel.grid(row=1, column=0, sticky = W, padx=7)
                        rootCause.grid(row=2, column=0, sticky = W, padx=7)
                        policyProbLabel.grid(row=1, column=1, sticky = W, padx=7)
                        policyProb.grid(row=2, column=1, sticky = W, padx=7)

                        def finish():
                            return

                        btnFinish = Button(newProject, text = "Finish", width=10, command = lambda: finish())
                        btnFinish.place(x=270, y=170)

                    btnNext4 = Button(newProject, text = "Next", width=10, command = lambda: next4())
                    btnNext4.place(x=600, y=390)
                    
                btnNext3 = Button(newProject, text = "Next", width=10, command = lambda: next3())
                btnNext3.place(x=280, y=170)
            
            btnNext2 = Button(newProject, text = "Next", width=10, command = lambda: next2())
            btnNext2.place(x=285, y=400)
            
        btnNext1 = Button(newProject, text = "Next", width=10, command = lambda: next1())
        btnNext1.place(x=270, y=170)

        projectTitle.config(bg="white")
        fontSize.config(bg="white")
        polAnaTitle.config(bg="white")
        probSit.config(bg="white")
        undeEff.config(bg="white")

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

        data = [projecttitle, policyanalysis, fontstyle, fontsize, n, l, o]

        filename = projecttitle
        fileobject = open(filename + '.pol', 'w')
        json.dump(data, fileobject)
        fileobject.close()

        newProject.destroy()
        newProject.update()

    btnCreate = Button(newProject, text = "Create", width=10, command = lambda: saveNewProject())
    btnClear = Button(newProject, text = "Clear", width=10, command = lambda: clearCreate())
    btnCreate.place(x=380, y=170)
    btnClear.place(x=190, y=170)

menubar = Menu(root) 

file1 = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file1) 
file1.add_command(label ='Create New', command = createNewProject)
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