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
import seaborn as sns
import pandas as pd
import numpy as np
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
root.title("Policy Analytics 3.0")
root.geometry("1300x700")

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'blue',
                                       'fieldbackground': 'red',
                                       'background': 'green'
                                       }}}
                         )

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

introLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin Gothic Heavy", 14), text = "Welcome to Policy Analytics 3.0")
aboutLabel = Label(main, background="#ffffff", foreground="#76090c", font=("Franklin ", 10), wraplength=1000, justify="center", text = "Policy Analytics 3.0 is a tool for learning policy analysis. This software can be used in training programs and classroom learning. It provides a step-by-step procedure that allows users to input and process basic essential data for problem structuring, forecasting and assessment of policy alternatives, recommending or prescribing the best/optimal policy alternative, designing an implementation plan, and building a monitoring and evaluation plan. Its outputs can be used in writing a complete policy issue paper. It is based on the “Elements of the Policy Issue Paper” in Annex 1 of Public Policy Analysis: An Integrated Approach by William N. Dunn (2018) with modifications based on the teaching and training experiences of its creator, Dr. Ebinezer R. Florano, Professor of Public Policy at the University of the Philippines, National College of Public Administration and Governance and Convenor of the UPCIDS Data Science for Public Policy Program (DSPPP).")
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
    
def createNewProject():
    global filename, fileobject

    mainProject = Toplevel(root)
    
    varRoot1 = tk.IntVar()
    varRoot2 = tk.IntVar()
    varRoot3 = tk.IntVar()
    varRoot4 = tk.IntVar()
    varRoot5 = tk.IntVar()
    varRoot6 = tk.IntVar()
    varRoot7 = tk.IntVar()

    status = ttk.Label(mainProject, text="")

    def page_1():
        mainProject.title("Policy Analytics 3.0 - Create New Project")
        mainProject.geometry("660x210")

        blank = Label(mainProject, text = "  ")
        
        frame1 = tk.LabelFrame(mainProject)

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

        polAnaTitleLabel1 = Label(frame1, text = "Policy Analysis Title")
        polAnaTitle = Entry(frame1, width=30)

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
    
        def clear_page_1():
            projectTitle.config(bg="white")
            fontSize.config(bg="white")
            analystName.config(bg="white")
            polAnaTitle.config(bg="white")
            fontsList.set('')
            # probSit.config(bg="white")
            # undeEff.config(bg="white")
            
            projectTitle.delete(0, END)
            polAnaTitle.delete(0, END)
            analystName.delete(0, END)
            fontSize.delete(0, END)
            indentation.delete(0, END)
            # probSit.delete("1.0", tk.END)
            # undeEff.delete("1.0", tk.END)

        def create_project():
            global projecttitle
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
            
            # save the project
            global filename, fileobject
            filename = projecttitle
            fileobject = open(filename + '.pol', 'w')
            fileobject.write(projecttitle+"\n"+analyst+"\n"+policyanalysis+"\n"+fontstyle+"\n"+fontsize+"\n")

            frame1.destroy()
            btnCreate.destroy() 
            btnClear1.destroy()  
            page_2()

        btnCreate = Button(mainProject, text = "Create", width=10, command = lambda: create_project())
        btnClear1 = Button(mainProject, text = "Clear", width=10, command = lambda: clear_page_1())
        btnCreate.place(x=380, y=170)
        btnClear1.place(x=190, y=170)
        status.place(x=10, y=170)

    page_1()

    def page_2():                                                               # write problematic situation and undesirable effects
        mainProject.geometry("660x210")
        frame2 = tk.LabelFrame(mainProject)

        status.config(text="")

        probSitLabel = Label(frame2, text = "Problematic Situation")
        probSit = scrolledtext.ScrolledText(frame2, height = 8, width=30)
        
        undeEffLabel = Label(frame2, text = "Undesirable Effects")
        undeEff = scrolledtext.ScrolledText(frame2, height = 8, width=30)
        
        frame2.place(x=40, y=10)
        probSitLabel.grid(row=1, column=0, sticky = W, padx=7)
        probSit.grid(row=2, column=0, sticky = W, padx=7)
        undeEffLabel.grid(row=1, column=1, sticky = W, padx=7)
        undeEff.grid(row=2, column=1, sticky = W, padx=7)
        
        def back_1():
            frame2.destroy() 
            btnBack1.destroy()
            btnNext1.destroy() 
            page_1()
        
        def next_1():
            problematicsituation = probSit.get("1.0", tk.END)
            if not problematicsituation.strip():
                status.config(
                text="Enter problematic\nsituation",
                foreground="red",
            )
                return
                    
            undesirableeffects = undeEff.get("1.0", tk.END)
            if not undesirableeffects.strip():
                status.config(
                text="Enter undesirable\neffects",
                foreground="red",
            )
                return
        
            fileobject.writelines(problematicsituation+"\n"+undesirableeffects+"\n")

            frame2.destroy() 
            btnBack1.destroy()
            btnNext1.destroy() 
            page_3()

        btnBack1 = Button(mainProject, text = "Back", width=10, command = lambda: back_1())
        btnNext1 = Button(mainProject, text = "Next", width=10, command = lambda: next_1())
        btnBack1.place(x=140, y=170)
        btnNext1.place(x=400, y=170)
    
    def page_3():
        mainProject.geometry("640x500")

        status.config(text="")
            
        frame3 = tk.LabelFrame(mainProject)

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

        effoLabel = Label(mainProject, text = "Effort")
        accoLabel = Label(mainProject, text = "Accomplishment")
        asseLabel = Label(mainProject, text = "Assessment")

        effort = tk.Entry(mainProject, width=20)
        accomplishment = tk.Entry(mainProject, width=20) 
        assessment = tk.Entry(mainProject, width=20) 

        addButton = tk.Button(mainProject, text='Add', width=10, command=lambda: add_data())  
        editButton = tk.Button(mainProject, text="Edit", width=10, command=lambda: edit_data())

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

        def back_2():
            frame3.destroy() 
            effoLabel.destroy()
            effort.destroy()
            accoLabel.destroy()
            accomplishment.destroy()
            asseLabel.destroy()
            assessment.destroy()
            addButton.destroy()
            editButton.destroy()
            btnBack2.destroy()
            btnNext2.destroy() 
            page_2()
        
        def next_2():
            frame3.destroy() 
            effoLabel.destroy()
            effort.destroy()
            accoLabel.destroy()
            accomplishment.destroy()
            asseLabel.destroy()
            assessment.destroy()
            addButton.destroy()
            editButton.destroy()
            btnBack2.destroy()
            btnNext2.destroy() 
            page_4()

        btnBack2 = Button(mainProject, text = "Back", width=10, command = lambda: back_2())
        btnNext2 = Button(mainProject, text = "Next", width=10, command = lambda: next_2())
        btnBack2.place(x=190, y=400)
        btnNext2.place(x=380, y=400)

    def page_4():
        mainProject.geometry("660x210")

        frame4 = tk.LabelFrame(mainProject)

        global var
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

        def analyses():                    
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
        
        def back_3():
            frame4.destroy() 
            btnBack3.destroy()
            btnNext3.destroy() 
            page_3()
        
        def next_3():
            frame4.destroy()
            btnBack3.destroy()
            btnNext3.destroy() 
            analyses()
            page_5()

        btnBack3 = Button(mainProject, text = "Back", width=10, command = lambda: back_3())
        btnNext3 = Button(mainProject, text = "Next", width=10, command = lambda: next_3())
        btnBack3.place(x=190, y=170)
        btnNext3.place(x=380, y=170)

    def page_5(): 
        mainProject.geometry("830x600")

        frame5 = tk.LabelFrame(mainProject)
        
        rootCauseLabel = Label(frame5, text = "Root Cause of the Problem")
        rootCause = Entry(frame5, width=100)

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

        existLabel = Label(mainProject, text = "Existing Policy")
        releLabel = Label(mainProject, text = "Relevant Provision")
        accompLabel2 = Label(mainProject, text = "Accomplishment")
        assessLabel2 = Label(mainProject, text = "Assessment")

        existingPolicy = tk.Entry(mainProject, width=30)
        relevantProvision = tk.Entry(mainProject, width=30) 
        accomplishment2 = tk.Entry(mainProject, width=30) 
        assessment2 = tk.Entry(mainProject, width=30) 

        addButton2 = tk.Button(mainProject, text='Add', width=10, command=lambda: add_data2())  
        editButton2 = tk.Button(mainProject, text="Edit", width=10, command=lambda: edit_data2())

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
        rootCauseLabel.grid(row=0, column=1)
        rootCause.grid(row=1, column=1)
        assessExistLabel.grid(row=2, column=1)
        assessmentTable.grid(row=3, column=1)
        existLabel.place(x=40, y=330)
        existingPolicy.place(x=200, y=330)
        releLabel.place(x=40, y=390)
        relevantProvision.place(x=200, y=390)
        accompLabel2.place(x=40, y=450)
        accomplishment2.place(x=200, y=450)
        assessLabel2.place(x=40, y=510)
        assessment2.place(x=200, y=510)
        addButton2.place(x=450, y=390)
        editButton2.place(x=450, y=450)

        def back_4():
            frame5.destroy() 
            existLabel.destroy()
            existingPolicy.destroy()
            releLabel.destroy()
            relevantProvision.destroy()
            accomplishment2.destroy()
            accompLabel2.destroy()
            assessLabel2.destroy()
            assessment2.destroy()
            btnBack4.destroy()
            btnNext4.destroy() 
            addButton2.destroy()
            editButton2.destroy()
            page_4()
        
        def next_4():
            frame5.destroy() 
            existLabel.destroy()
            existingPolicy.destroy()
            releLabel.destroy()
            relevantProvision.destroy()
            accomplishment2.destroy()
            accompLabel2.destroy()
            assessLabel2.destroy()
            assessment2.destroy()
            btnBack4.destroy()
            btnNext4.destroy() 
            addButton2.destroy()
            editButton2.destroy()
            page_6()

        btnBack4 = Button(mainProject, text = "Back", width=10, command = lambda: back_4())
        btnNext4 = Button(mainProject, text = "Next", width=10, command = lambda: next_4())
        btnBack4.place(x=600, y=390)
        btnNext4.place(x=600, y=450)

    def page_6():                                                   # write problematic situation and undesirable effects
        mainProject.geometry("660x210")

        frame6 = tk.LabelFrame(mainProject)

        policyProbLabel = Label(frame6, text = "Policy Problem")
        policyProb = scrolledtext.ScrolledText(frame6, height = 8, width=30)
        
        policyIssueLabel = Label(frame6, text = "Policy Issue Statement")
        policyIssue = scrolledtext.ScrolledText(frame6, height = 8, width=30)
        
        frame6.place(x=40, y=10)
        policyProbLabel.grid(row=1, column=0, sticky = W, padx=7)
        policyProb.grid(row=2, column=0, sticky = W, padx=7)
        policyIssueLabel.grid(row=1, column=1, sticky = W, padx=7)
        policyIssue.grid(row=2, column=1, sticky = W, padx=7)

        def back_5():
            frame6.destroy() 
            btnBack5.destroy()
            btnNext5.destroy() 
            page_5()
        
        def next_5():
            frame6.destroy() 
            btnBack5.destroy()
            btnNext5.destroy() 
            page_7()

        btnBack5 = Button(mainProject, text = "Back", width=10, command = lambda: back_5())
        btnNext5 = Button(mainProject, text = "Next", width=10, command = lambda: next_5())
        btnBack5.place(x=140, y=170)
        btnNext5.place(x=400, y=170)

    def page_7():
        mainProject.geometry("740x500")

        # write problematic situation and undesirable effects

        frame7 = tk.LabelFrame(mainProject)

        goalsObjLabel = Label(frame7, text = "Goals and Objectives of the Proposal")
        
        goalsandObjTable=ttk.Treeview(frame7)
        goalsandObjTable["columns"]=("1","2")
        goalsandObjTable['show']='headings'
        goalsandObjTable.column("1",width=350,anchor='c')
        goalsandObjTable.column("2",width=350,anchor='c')
        goalsandObjTable.heading("1",text="Policy Goals and Objectives")
        goalsandObjTable.heading("2",text="Indicators")

        pgoLabel = Label(mainProject, text = "Policy Goals and Objectives")
        indiLabel = Label(mainProject, text = "Indicators")

        pgo = tk.Entry(mainProject, width=40) 
        indi = tk.Entry(mainProject, width=40) 

        addButton3 = tk.Button(mainProject, text='Add', width=10, command=lambda: add_data3())  
        editButton3 = tk.Button(mainProject, text="Edit", width=10, command=lambda: edit_data3())

        def show_data3(a):
            pgo.delete(0,END)
            indi.delete(0,END)

            selectedItem = goalsandObjTable.selection()[0]
            pgo.insert(0, goalsandObjTable.item(selectedItem)['values'][0])
            indi.insert(0, goalsandObjTable.item(selectedItem)['values'][1])

        goalsandObjTable.bind("<<TreeviewSelect>>", show_data3)

        def edit_data3():
            pgoText = pgo.get()                         # read policy goal and objective
            indiText = indi.get()                       # read indicator

            selected_item = goalsandObjTable.selection()[0]
            goalsandObjTable.item(selected_item, text="blub", values=(pgoText, indiText))

        def add_data3():
            pgoText = pgo.get()                         # read policy goal and objective
            indiText = indi.get()                       # read indicator

            goalsandObjTable.insert("",'end', values=(pgoText, indiText))
            pgoText.delete('1.0',END)  # reset the text entry box
            indiText.delete('1.0',END)  # reset the text entry box
            pgo.focus() 

        frame7.place(x=10, y=10)
        goalsObjLabel.grid(row=0, column=1)
        goalsandObjTable.grid(row=1, column=1)
        pgoLabel.place(x=100, y=270)
        pgo.place(x=60, y=300)
        indiLabel.place(x=510, y=270)
        indi.place(x=420, y=300)
        addButton3.place(x=130, y=330)
        editButton3.place(x=500, y=330)

        def back_6():
            frame7.destroy() 
            pgoLabel.destroy()
            pgo.destroy()
            indiLabel.destroy()
            indi.destroy()
            addButton3.destroy()
            editButton3.destroy()
            btnBack6.destroy()
            btnNext6.destroy() 
            page_6()
        
        def next_6():
            frame7.destroy() 
            pgoLabel.destroy()
            pgo.destroy()
            indiLabel.destroy()
            indi.destroy()
            addButton3.destroy()
            editButton3.destroy()
            btnBack6.destroy()
            btnNext6.destroy() 
            page_8()

        btnBack6 = Button(mainProject, text = "Back", width=10, command = lambda: back_6())
        btnNext6 = Button(mainProject, text = "Next", width=10, command = lambda: next_6())
        btnBack6.place(x=130, y=420)
        btnNext6.place(x=500, y=420)

    def page_8():
        mainProject.geometry("740x500")

        frame8 = tk.LabelFrame(mainProject)

        staAndActLabel = Label(frame8, text = "Stakeholders and Actors")
        
        staAndActTable=ttk.Treeview(frame8)
        staAndActTable["columns"]=("1","2")
        staAndActTable['show']='headings'
        staAndActTable.column("1",width=350,anchor='c')
        staAndActTable.column("2",width=350,anchor='c')
        staAndActTable.heading("1",text="Stakeholders")
        staAndActTable.heading("2",text="Actors")

        global stakeholders, actors, addButton4, editButton4
        stakeholdersLabel = Label(mainProject, text = "Stakeholders")
        actorsLabel = Label(mainProject, text = "Actors")

        stakeholders = tk.Entry(mainProject, width=40) 
        actors = tk.Entry(mainProject, width=40) 

        addButton4 = tk.Button(mainProject, text='Add', width=10, command=lambda: add_data4())  
        editButton4 = tk.Button(mainProject, text="Edit", width=10, command=lambda: edit_data4())

        def show_data4(a):
            stakeholders.delete(0,END)
            actors.delete(0,END)

            selectedItem = staAndActTable.selection()[0]
            stakeholders.insert(0, staAndActTable.item(selectedItem)['values'][0])
            actors.insert(0, staAndActTable.item(selectedItem)['values'][1])

        staAndActTable.bind("<<TreeviewSelect>>", show_data4)

        def edit_data4():
            stakeholdersText = stakeholders.get()           # read stakeholders
            actorsText = actors.get()                       # read actors

            selected_item = staAndActTable.selection()[0]
            staAndActTable.item(selected_item, text="blub", values=(stakeholdersText, actorsText))

        def add_data4():
            stakeholdersText = stakeholders.get()           # read stakeholders
            actorsText = actors.get()                       # read actors

            staAndActTable.insert("",'end', values=(stakeholdersText, actorsText))
            stakeholdersText.delete('1.0',END)  # reset the text entry box
            actorsText.delete('1.0',END)  # reset the text entry box
            stakeholders.focus() 

        frame8.place(x=10, y=10)
        staAndActLabel.grid(row=0, column=1)
        staAndActTable.grid(row=1, column=1)
        stakeholdersLabel.place(x=140, y=270)
        stakeholders.place(x=60, y=300)
        actorsLabel.place(x=520, y=270)
        actors.place(x=420, y=300)
        addButton4.place(x=130, y=330)
        editButton4.place(x=500, y=330)

        def back_7():
            global stakeholders, actors, addButton4, editButton4
            frame8.destroy()      
            btnNext7.destroy()    
            stakeholdersLabel.destroy()
            stakeholders.destroy()
            actorsLabel.destroy()
            actors.destroy()
            addButton4.destroy()
            editButton4.destroy()   
            btnBack7.destroy()
            btnNext7.destroy() 
            page_7()
        
        def next_7():
            global stakeholders, actors, addButton4, editButton4
            frame8.destroy()      
            btnNext7.destroy()    
            stakeholdersLabel.destroy()
            stakeholders.destroy()
            actorsLabel.destroy()
            actors.destroy()
            addButton4.destroy()
            editButton4.destroy() 
            btnBack7.destroy()
            btnNext7.destroy() 
            page_9()

        btnBack7 = Button(mainProject, text = "Back", width=10, command = lambda: back_7())
        btnNext7 = Button(mainProject, text = "Next", width=10, command = lambda: next_7())
        btnBack7.place(x=130, y=420)
        btnNext7.place(x=500, y=420)

    def page_9():               
        mainProject.geometry("885x515")

        frame9 = tk.LabelFrame(mainProject)
        frame9.columnconfigure(0, weight=2)
        frame9.columnconfigure(1, weight=2)
        frame9.columnconfigure(2, weight=2)
        frame9.columnconfigure(3, weight=2)
        frame9.columnconfigure(4, weight=2)
        frame9.rowconfigure(0, weight=1)
        frame9.rowconfigure(1, weight=1)
        frame9.rowconfigure(2, weight=1)
        frame9.rowconfigure(3, weight=1)
        frame9.rowconfigure(4, weight=1)
        frame9.rowconfigure(5, weight=1)
        frame9.rowconfigure(6, weight=1)
        frame9.rowconfigure(7, weight=1)
        frame9.rowconfigure(8, weight=1)
        frame9.rowconfigure(9, weight=1)

        assessAlterLabel = Label(frame9, text = "Assessment of the Policy Alternatives")
        assessAlterLabel.grid(row=0, column=0, columnspan=2)

        assessAlterTable=ttk.Treeview(frame9)
        assessAlterTable["columns"]=("1", "2")  
        assessAlterTable['show']='headings'  
        assessAlterTable.column("1", width=140, anchor='c')
        assessAlterTable.column("2", width=300, anchor='c')
        assessAlterTable.heading("1",text="Policy Alternative No.")
        assessAlterTable.heading("2",text="Policy Alternative")

        polAltNoLabel = Label(mainProject, text = "Policy Alternative No.\n")
        policyAlternativeNo = tk.Entry(mainProject, width=20) 
        polAltLabel = Label(mainProject, text = "Policy Alternative\n")
        policyAlternatives = tk.Entry(mainProject, width=50) 

        addButton5 = tk.Button(mainProject, text='Add', width=10, command=lambda: add_data5())  
        editButton5 = tk.Button(mainProject, text="Edit", width=10, command=lambda: edit_data5())
        computeButton = tk.Button(mainProject, text="Compute", width=10, command=lambda: compute())

        def show_data5(a):
            policyAlternativeNo.delete(0,END)
            policyAlternatives.delete(0,END)

            selectedItem = assessAlterTable.selection()[0]
            policyAlternativeNo.insert(0, assessAlterTable.item(selectedItem)['values'][0])
            policyAlternatives.insert(0, assessAlterTable.item(selectedItem)['values'][1])

        assessAlterTable.bind("<<TreeviewSelect>>", show_data5)

        def edit_data5():
            policyAlternativeNoText = policyAlternativeNo.get()           # read stakeholders
            policyAlternativesText = policyAlternatives.get()             # read actors

            selected_item = assessAlterTable.selection()[0]
            assessAlterTable.item(selected_item, text="blub", values=(policyAlternativeNoText, policyAlternativesText))

        def add_data5():
            policyAlternativeNoText = policyAlternativeNo.get()           # read stakeholders
            policyAlternativesText = policyAlternatives.get()             # read actors

            assessAlterTable.insert("",'end', values=(policyAlternativeNoText, policyAlternativesText))
            policyAlternativeNoText.delete('1.0',END)  # reset the text entry box
            policyAlternativesText.delete('1.0',END)  # reset the text entry box
            stakeholders.focus() 

        frame9.place(x=10, y=10)

        column3 = Label(frame9, text="Effectiveness")
        column3.grid(row=1, column=2)

        column4 = Label(frame9, text="Cost-efficiency")
        column4.grid(row=1, column=3)

        column5 = Label(frame9, text="Acceptability")
        column5.grid(row=1, column=4)

        column6 = Label(frame9, text="Criteria")
        column6.grid(row=0, column=2, columnspan=3)

        assessAlterTable.grid(row=1, rowspan=7, column=0, columnspan=2)

        polAltNoLabel.place(x=140, y=360)
        policyAlternativeNo.place(x=135, y=390)
        polAltLabel.place(x=520, y=360)
        policyAlternatives.place(x=420, y=390)
        addButton5.place(x=155, y=420)
        editButton5.place(x=530, y=420)
        computeButton.place(x=590, y=300)

        varEffec = IntVar(value=0)
        varCostEff = IntVar(value=0)
        varAccept = IntVar(value=0)
    
        R1_2 = Radiobutton(frame9, text="SLR", variable=varEffec, value=1)
        R2_2 = Radiobutton(frame9, text="MLR", variable=varEffec, value=2)
        R3_2 = Radiobutton(frame9, text="LogR", variable=varEffec, value=3)
        R4_2 = Radiobutton(frame9, text="FGD", variable=varEffec, value=4)
        R5_2 = Radiobutton(frame9, text="Tangible Cost-Benefit Analysis\nw/ Discounting", variable=varCostEff, value=1)
        R6_2 = Radiobutton(frame9, text="Tangible Cost-Benefit Analysis\nw/o Discounting", variable=varCostEff, value=2)
        R7_2 = Radiobutton(frame9, text="Intangible Cost-Benefit Analysis", variable=varCostEff, value=3)
        R8_2 = Radiobutton(frame9, text="PRINCE", variable=varAccept, value=1)
        R9_2 = Radiobutton(frame9, text="Stakeholder Analysis", variable=varAccept, value=2)

        R1_2.grid(row=3, column=2)
        R2_2.grid(row=4, column=2)
        R3_2.grid(row=5, column=2)
        R4_2.grid(row=8, column=2)
        R5_2.grid(row=4, column=3)
        R6_2.grid(row=5, column=3)
        R7_2.grid(row=8, column=3)
        R8_2.grid(row=4, column=4)
        R9_2.grid(row=8, column=4)


        def compute():

            netBenefitWithout = []
            netBenefitWith = []
            
            crite = [int(varEffec.get()), int(varCostEff.get()), int(varAccept.get())]
            print(crite)

            if int(varEffec.get()) == 1: 
                effectiveness = Toplevel(main)
                effectiveness.title("Policy Analytics 3.0 - Effectiveness: Simple LR")
                effectiveness.geometry("830x480")

            elif int(varEffec.get()) == 2: 
                effectiveness = Toplevel(main)
                effectiveness.title("Policy Analytics 3.0 - Effectiveness: Multiple LR")
                effectiveness.geometry("830x480")

            elif int(varEffec.get()) == 3: 
                effectiveness = Toplevel(main)
                effectiveness.title("Policy Analytics 3.0 - Effectiveness: LogR")
                effectiveness.geometry("830x480")

            elif int(varEffec.get()) == 4: 
                effectiveness = Toplevel(main)
                effectiveness.title("Policy Analytics 3.0 - Effectiveness: FGD")
                effectiveness.geometry("830x480")

            if int(varCostEff.get()) == 1: 
                effectiveness = Toplevel(main)
                effectiveness.title("Policy Analytics 3.0 - Cost-efficiency: Tangible Cost-Benefit Analysis w/ Discounting")
                effectiveness.geometry("830x600")

                popup = Toplevel(root)
                popup.geometry("200x200")
                popup.title("Policy Analytics 3.0 - Enter Discount Rate")


                discountLabel = Label(popup, text = "Enter discount rate (1-100): ")
                discountEntry = Entry(popup, width=10)
                discountButton = tk.Button(popup, text='Set', width=10, command=lambda: enter_discount())

                def enter_discount():
                    global discount
                    discount = int(discountEntry.get())/100
                    print(discount)
                    popup.update()
                    popup.destroy()

                discountLabel.place(x=10, y=10)
                discountEntry.place(x=10, y=70)
                discountButton.place(x=10, y=100)

                tangibleCBAwithLabel = Label(effectiveness, text = "Tangible Cost-Benefit Analysis w/ Discounting")
                tangibleCBAwithTable=ttk.Treeview(effectiveness)
                tangibleCBAwithTable["columns"]=("1","2","3","4")
                tangibleCBAwithTable['show']='headings'
                tangibleCBAwithTable.column("1",width=200,anchor='c')
                tangibleCBAwithTable.column("2",width=200,anchor='c')
                tangibleCBAwithTable.column("3",width=200,anchor='c')
                tangibleCBAwithTable.column("4",width=200,anchor='c')
                tangibleCBAwithTable.heading("1",text="Alternative")
                tangibleCBAwithTable.heading("2",text="Benefit")
                tangibleCBAwithTable.heading("3",text="Cost")
                tangibleCBAwithTable.heading("4",text="Net Benefit")

                alterLabel = Label(effectiveness, text = "Alternative")
                benefLabel = Label(effectiveness, text = "Benefit")
                costLabel = Label(effectiveness, text = "Cost")

                alternative = tk.Entry(effectiveness, width=30)
                benefit = tk.Entry(effectiveness, width=30) 
                cost = tk.Entry(effectiveness, width=30) 

                addButton = tk.Button(effectiveness, text='Add', width=10, command=lambda: add_data15())  
                editButton = tk.Button(effectiveness, text="Edit", width=10, command=lambda: edit_data15())

                def show_data15(a):
                    alternative.delete(0,END)
                    benefit.delete(0,END)
                    cost.delete(0,END)

                    selectedItem = tangibleCBAwithTable.selection()[0]
                    alternative.insert(0, tangibleCBAwithTable.item(selectedItem)['values'][0])
                    benefit.insert(0, tangibleCBAwithTable.item(selectedItem)['values'][1])
                    cost.insert(0, tangibleCBAwithTable.item(selectedItem)['values'][2])

                tangibleCBAwithTable.bind("<<TreeviewSelect>>", show_data15)

                def edit_data15():
                    alternativeText = alternative.get()                                         # read existing policy
                    benefitText = int(benefit.get())                                            # read relevant provision
                    costText = int(cost.get())                                                  # read accomplishment 
                    netBenefit = int(benefitText) - int(costText)    
                    print(netBenefit)                                                           # read assessment                 
                                            
                    selected_item = tangibleCBAwithTable.selection()[0]
                    tangibleCBAwithTable.item(selected_item, text="blub", values=(alternativeText, benefitText, costText, netBenefit))

                def add_data15():
                    alternativeText = alternative.get()                                                 # read existing policy
                    benefitText = int(benefit.get())*(1-discount)                                                        # read relevant provision
                    costText = int(cost.get())*(1-discount)                                                              # read accomplishment 
                    netBenefit = int(benefit.get())*(1-discount) - int(cost.get())*(1-discount)                     # read assessment      

                    global assessmentTuple
                    assessmentTuple = [alternativeText, benefitText, costText, netBenefit]

                    # effortList.append(efforttuple)

                    tangibleCBAwithTable.insert("",'end', values=(alternativeText, benefitText, costText, netBenefit))
                    alternativeText.delete('1.0',END)               # reset the text entry box
                    benefitText.delete('1.0',END)                   # reset the text entry box
                    costText.delete('1.0',END)                      # reset the text entry box
                    alternativeText.focus() 

                tangibleCBAwithLabel.grid(row=0, column=1)
                tangibleCBAwithTable.grid(row=1, column=1)
                alterLabel.place(x=40, y=330)
                alternative.place(x=200, y=330)
                benefLabel.place(x=40, y=390)
                benefit.place(x=200, y=390)
                costLabel.place(x=40, y=450)
                cost.place(x=200, y=450)
                addButton.place(x=450, y=390)
                editButton.place(x=450, y=450)

            elif int(varCostEff.get()) == 2: 
                effectiveness = Toplevel(main)
                effectiveness.title("Policy Analytics 3.0 - Cost-efficiency: Tangible Cost-Benefit Analysis w/o Discounting")
                effectiveness.geometry("830x600")

                tangibleCBALabel = Label(effectiveness, text = "Tangible Cost-Benefit Analysis w/o Discounting")
                tangibleCBATable=ttk.Treeview(effectiveness)
                tangibleCBATable["columns"]=("1","2","3","4")
                tangibleCBATable['show']='headings'
                tangibleCBATable.column("1",width=200,anchor='c')
                tangibleCBATable.column("2",width=200,anchor='c')
                tangibleCBATable.column("3",width=200,anchor='c')
                tangibleCBATable.column("4",width=200,anchor='c')
                tangibleCBATable.heading("1",text="Alternative")
                tangibleCBATable.heading("2",text="Benefit")
                tangibleCBATable.heading("3",text="Cost")
                tangibleCBATable.heading("4",text="Net Benefit")

                alterLabel = Label(effectiveness, text = "Alternative")
                benefLabel = Label(effectiveness, text = "Benefit")
                costLabel = Label(effectiveness, text = "Cost")

                alternative = tk.Entry(effectiveness, width=30)
                benefit = tk.Entry(effectiveness, width=30) 
                cost = tk.Entry(effectiveness, width=30) 

                addButton = tk.Button(effectiveness, text='Add', width=10, command=lambda: add_data15())  
                editButton = tk.Button(effectiveness, text="Edit", width=10, command=lambda: edit_data15())

                def show_data15(a):
                    alternative.delete(0,END)
                    benefit.delete(0,END)
                    cost.delete(0,END)

                    selectedItem = tangibleCBATable.selection()[0]
                    alternative.insert(0, tangibleCBATable.item(selectedItem)['values'][0])
                    benefit.insert(0, tangibleCBATable.item(selectedItem)['values'][1])
                    cost.insert(0, tangibleCBATable.item(selectedItem)['values'][2])

                tangibleCBATable.bind("<<TreeviewSelect>>", show_data15)

                def edit_data15():
                    alternativeText = alternative.get()                     # read existing policy
                    benefitText = int(benefit.get())                        # read relevant provision
                    costText = int(cost.get())                              # read accomplishment 
                    netBenefit = int(benefitText) - int(costText)    
                    print(netBenefit)                                       # read assessment                 
                                            
                    selected_item = tangibleCBATable.selection()[0]
                    tangibleCBATable.item(selected_item, text="blub", values=(alternativeText, benefitText, costText, netBenefit))

                def add_data15():
                    alternativeText = alternative.get()                     # read existing policy
                    benefitText = benefit.get()                             # read relevant provision
                    costText = cost.get()                                   # read accomplishment 
                    netBenefit = int(benefitText) - int(costText)                   # read assessment      

                    global assessmentTuple
                    assessmentTuple = [alternativeText, benefitText, costText, netBenefit]

                    # effortList.append(efforttuple)

                    tangibleCBATable.insert("",'end', values=(alternativeText, benefitText, costText, netBenefit))
                    alternativeText.delete('1.0',END)               # reset the text entry box
                    benefitText.delete('1.0',END)                   # reset the text entry box
                    costText.delete('1.0',END)                      # reset the text entry box
                    alternativeText.focus() 

                tangibleCBALabel.grid(row=0, column=1)
                tangibleCBATable.grid(row=1, column=1)
                alterLabel.place(x=40, y=330)
                alternative.place(x=200, y=330)
                benefLabel.place(x=40, y=390)
                benefit.place(x=200, y=390)
                costLabel.place(x=40, y=450)
                cost.place(x=200, y=450)
                addButton.place(x=450, y=390)
                editButton.place(x=450, y=450)

            elif int(varCostEff.get()) == 3:
                effectiveness = Toplevel(main)
                effectiveness.title("Policy Analytics 3.0 - Cost-efficiency: Intangible Cost-Benefit Analysis")
                effectiveness.geometry("830x600")

                intangibleCBALabel = Label(effectiveness, text = "Intangible Cost-Benefit Analysis")
                intangibleCBATable=ttk.Treeview(effectiveness)
                intangibleCBATable["columns"]=("1","2","3")
                intangibleCBATable['show']='headings'
                intangibleCBATable.column("1",width=200,anchor='c')
                intangibleCBATable.column("2",width=200,anchor='c')
                intangibleCBATable.column("3",width=200,anchor='c')
                intangibleCBATable.heading("1",text="Alternative")
                intangibleCBATable.heading("2",text="Benefit")
                intangibleCBATable.heading("3",text="Cost")

                alterLabel = Label(effectiveness, text = "Alternative")
                benefLabel = Label(effectiveness, text = "Benefit")
                costLabel = Label(effectiveness, text = "Cost")

                alternative = tk.Entry(effectiveness, width=30)
                benefit = tk.Entry(effectiveness, width=30) 
                cost = tk.Entry(effectiveness, width=30) 

                addButton = tk.Button(effectiveness, text='Add', width=10, command=lambda: add_data15())  
                editButton = tk.Button(effectiveness, text="Edit", width=10, command=lambda: edit_data15())

                def show_data15(a):
                    alternative.delete(0,END)
                    benefit.delete(0,END)
                    cost.delete(0,END)

                    selectedItem = intangibleCBATable.selection()[0]
                    alternative.insert(0, intangibleCBATable.item(selectedItem)['values'][0])
                    benefit.insert(0, intangibleCBATable.item(selectedItem)['values'][1])
                    cost.insert(0, intangibleCBATable.item(selectedItem)['values'][2])

                intangibleCBATable.bind("<<TreeviewSelect>>", show_data15)

                def edit_data15():
                    alternativeText = alternative.get()                     # read existing policy
                    benefitText = int(benefit.get())                        # read relevant provision
                    costText = int(cost.get())                              # read accomplishment 
                    netBenefit = int(benefitText) - int(costText)    
                    print(netBenefit)                                       # read assessment                 
                                            
                    selected_item = intangibleCBATable.selection()[0]
                    intangibleCBATable.item(selected_item, text="blub", values=(alternativeText, benefitText, costText, netBenefit))

                def add_data15():
                    alternativeText = alternative.get()                     # read existing policy
                    benefitText = benefit.get()                             # read relevant provision
                    costText = cost.get()                                   # read accomplishment 
                    netBenefit = int(benefitText) - int(costText)                   # read assessment      

                    global assessmentTuple
                    assessmentTuple = [alternativeText, benefitText, costText, netBenefit]

                    # effortList.append(efforttuple)

                    intangibleCBATable.insert("",'end', values=(alternativeText, benefitText, costText, netBenefit))
                    alternativeText.delete('1.0',END)               # reset the text entry box
                    benefitText.delete('1.0',END)                   # reset the text entry box
                    costText.delete('1.0',END)                      # reset the text entry box
                    alternativeText.focus() 

                intangibleCBALabel.grid(row=0, column=1)
                intangibleCBATable.grid(row=1, column=1)
                alterLabel.place(x=40, y=330)
                alternative.place(x=200, y=330)
                benefLabel.place(x=40, y=390)
                benefit.place(x=200, y=390)
                costLabel.place(x=40, y=450)
                cost.place(x=200, y=450)
                addButton.place(x=450, y=390)
                editButton.place(x=450, y=450)

            if int(varAccept.get()) == 1:
                effectiveness = Toplevel(main)
                effectiveness.title("Policy Analytics 3.0 - Effectiveness: PRINCE Method")
                effectiveness.geometry("830x480")

                stakeholderLabel = Label(effectiveness, text = "PRINCE Method")
                stakeholderTable=ttk.Treeview(effectiveness)
                stakeholderTable["columns"]=("1","2","3")
                stakeholderTable['show']='headings'
                stakeholderTable.column("1",width=200,anchor='c')
                stakeholderTable.column("2",width=200,anchor='c')
                stakeholderTable.column("3",width=200,anchor='c')
                stakeholderTable.heading("1",text="Supporters")
                stakeholderTable.heading("2",text="Neutral")
                stakeholderTable.heading("3",text="Oppositors")

                suppoLabel = Label(effectiveness, text = "Supporter")
                neutrLabel = Label(effectiveness, text = "Neutral")
                oppoLabel = Label(effectiveness, text = "Oppositor")

                suppo = tk.Entry(effectiveness, width=30)
                neutr = tk.Entry(effectiveness, width=30) 
                oppos = tk.Entry(effectiveness, width=30) 

                addButton = tk.Button(effectiveness, text='Add', width=10, command=lambda: add_data())  
                editButton = tk.Button(effectiveness, text="Edit", width=10, command=lambda: edit_data())

                def show_data():
                    suppo.delete(0,END)
                    neutr.delete(0,END)
                    oppos.delete(0,END)

                    selectedItem = stakeholderTable.selection()[0]
                    suppo.insert(0, stakeholderTable.item(selectedItem)['values'][0])
                    neutr.insert(0, stakeholderTable.item(selectedItem)['values'][1])
                    oppos.insert(0, stakeholderTable.item(selectedItem)['values'][2])

                stakeholderTable.bind("<<TreeviewSelect>>", show_data)

                def edit_data():
                    suppoText = suppo.get()                     # read supporter textbox
                    neutrText = neutr.get()                     # read neutral textbox
                    opposText = oppos.get()                     # read opposition textbox             
                                            
                    selected_item = tangibleCBATable.selection()[0]
                    tangibleCBATable.item(selected_item, text="blub", values=(suppoText, neutrText, opposText))

                def add_data():
                    suppoText = suppo.get()                     # read supporter textbox
                    neutrText = neutr.get()                     # read neutral textbox
                    opposText = oppos.get()                     # read opposition textbox    

                    global assessmentTuple
                    assessmentTuple = [suppoText, neutrText, opposText]

                    # effortList.append(efforttuple)

                    tangibleCBATable.insert("",'end', values=(suppoText, neutrText, opposText))
                    suppoText.delete('1.0',END)               # reset the text entry box
                    neutrText.delete('1.0',END)               # reset the text entry box
                    opposText.delete('1.0',END)               # reset the text entry box
                    suppoText.focus() 

                stakeholderLabel.grid(row=0, column=1)
                stakeholderTable.grid(row=1, column=1)
                suppoLabel.place(x=40, y=330)
                suppo.place(x=200, y=330)
                neutrLabel.place(x=40, y=390)
                neutr.place(x=200, y=390)
                oppoLabel.place(x=40, y=450)
                oppos.place(x=200, y=450)
                addButton.place(x=450, y=390)
                editButton.place(x=450, y=450)
            

            elif int(varAccept.get()) == 2:
                effectiveness = Toplevel(main)
                effectiveness.title("Policy Analytics 3.0 - Effectiveness: Stakeholder Analysis")
                effectiveness.geometry("830x480")

                stakeholderLabel = Label(effectiveness, text = "Stakeholder Analysis")
                stakeholderTable=ttk.Treeview(effectiveness)
                stakeholderTable["columns"]=("1","2","3")
                stakeholderTable['show']='headings'
                stakeholderTable.column("1",width=200,anchor='c')
                stakeholderTable.column("2",width=200,anchor='c')
                stakeholderTable.column("3",width=200,anchor='c')
                stakeholderTable.heading("1",text="Supporters")
                stakeholderTable.heading("2",text="Neutral")
                stakeholderTable.heading("3",text="Oppositors")

                suppoLabel = Label(effectiveness, text = "Supporter")
                neutrLabel = Label(effectiveness, text = "Neutral")
                oppoLabel = Label(effectiveness, text = "Oppositor")

                suppo = tk.Entry(effectiveness, width=30)
                neutr = tk.Entry(effectiveness, width=30) 
                oppos = tk.Entry(effectiveness, width=30) 

                addButton = tk.Button(effectiveness, text='Add', width=10, command=lambda: add_data())  
                editButton = tk.Button(effectiveness, text="Edit", width=10, command=lambda: edit_data())

                def show_data():
                    suppo.delete(0,END)
                    neutr.delete(0,END)
                    oppos.delete(0,END)

                    selectedItem = stakeholderTable.selection()[0]
                    suppo.insert(0, stakeholderTable.item(selectedItem)['values'][0])
                    neutr.insert(0, stakeholderTable.item(selectedItem)['values'][1])
                    oppos.insert(0, stakeholderTable.item(selectedItem)['values'][2])

                stakeholderTable.bind("<<TreeviewSelect>>", show_data)

                def edit_data():
                    suppoText = suppo.get()                     # read supporter textbox
                    neutrText = neutr.get()                     # read neutral textbox
                    opposText = oppos.get()                     # read opposition textbox             
                                            
                    selected_item = tangibleCBATable.selection()[0]
                    tangibleCBATable.item(selected_item, text="blub", values=(suppoText, neutrText, opposText))

                def add_data():
                    suppoText = suppo.get()                     # read supporter textbox
                    neutrText = neutr.get()                     # read neutral textbox
                    opposText = oppos.get()                     # read opposition textbox    

                    global assessmentTuple
                    assessmentTuple = [suppoText, neutrText, opposText]

                    # effortList.append(efforttuple)

                    tangibleCBATable.insert("",'end', values=(suppoText, neutrText, opposText))
                    suppoText.delete('1.0',END)               # reset the text entry box
                    neutrText.delete('1.0',END)               # reset the text entry box
                    opposText.delete('1.0',END)               # reset the text entry box
                    suppoText.focus() 

                stakeholderLabel.grid(row=0, column=1)
                stakeholderTable.grid(row=1, column=1)
                suppoLabel.place(x=40, y=330)
                suppo.place(x=200, y=330)
                neutrLabel.place(x=40, y=390)
                neutr.place(x=200, y=390)
                oppoLabel.place(x=40, y=450)
                oppos.place(x=200, y=450)
                addButton.place(x=450, y=390)
                editButton.place(x=450, y=450)
            
            def results():
                return
            

    # projectTitle.config(bg="white")
    # fontSize.config(bg="white")
    # polAnaTitle.config(bg="white")
    # probSit.config(bg="white")
    # undeEff.config(bg="white")

    # n = varNat.get()
    # l = varLoc.get()
    # o = varOrg.get()

    # quan = varRoot1.get()
    # regLi = varRoot2.get()
    # regMu = varRoot3.get()
    # regLo = varRoot4.get()
    # qual = varRoot5.get()
    # prob = varRoot6.get()
    # delp = varRoot7.get()

    # data = [projecttitle, policyanalysis, fontstyle, fontsize, n, l, o]

    # filename = projecttitle
    # fileobject = open(filename + '.pol', 'w')
    # json.dump(data, fileobject)
    # fileobject.close()


menubar = Menu(root) 

file1 = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file1) 
file1.add_command(label ='Create New', command = lambda: createNewProject())
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