import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk, messagebox, colorchooser
from tkinter import scrolledtext 
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename, asksaveasfilename

import customtkinter as ctk

from CTkXYFrame import *
 
import textwrap
import json

import PIL
from PIL import Image, ImageTk, ImageGrab

import fpdf
from fpdf import FPDF

import reportlab

from reportlab import lib, platypus, pdfbase

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted
from reportlab.platypus import Image as RLImage
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch

import os

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sp

import sys
import os

import statsmodels.api as sm
import sklearn as skl

from sklearn.linear_model import LinearRegression, LogisticRegression

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Hamdi addition
#import tkinter.tix as tix 

global size, var, pageNumber
size = 10
global save_pdf_file_path, save_json_file_path, tree_file_path, image_filename
save_pdf_file_path = None
save_json_file_path = None
tree_file_path = None

global analysis_type
analysis_type = ""

global reg_sum
reg_sum = ""

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("themes/red.json")

root = ctk.CTk()
root.title("Policy Analytics 1.3")

# getting screen's width in pixels
hght = root.winfo_screenheight()
wth = root.winfo_screenwidth() 
print("\n width x height = %d x %d (in pixels)\n" %(wth, hght))

root.geometry(f"{wth}x{hght}")
root.state("zoomed")

main = CTkXYFrame(root, fg_color="white")
main.pack(fill="both", expand=True)

introLabel = tk.Label(main, anchor=tk.CENTER, background="white", foreground="#76090c", font=("Franklin Gothic Heavy", 16), justify="center", text = "Welcome to Policy Analytics 1.3\n")
aboutLabel = tk.Label(main, background="white", foreground="#76090c", font=("Franklin", 14), wraplength=wth-55, justify="center", text = "Policy Analytics 1.3 is a tool for learning policy analysis. This software can be used in training programs and classroom learning. It provides a step-by-step procedure that allows users to input and process basic essential data for problem structuring, forecasting and assessment of policy alternatives, recommending or prescribing the best/optimal policy alternative, designing an implementation plan, and building a monitoring and evaluation plan. Its outputs can be used in writing a complete policy issue paper. It is based on the “Elements of the Policy Issue Paper” in Annex 1 of Public Policy Analysis: An Integrated Approach by William N. Dunn (2018) with modifications based on the teaching and training experiences of its creator, Dr. Ebinezer R. Florano, Professor of Public Policy at the University of the Philippines, National College of Public Administration and Governance and Convenor of the UP CIDS Data Science for Public Policy Program (DSPPP).\n\n")
arrLabel =tk.Label(main, background="white", foreground="#76090c", font=("Franklin", 14), wraplength=wth-55, justify="center", text = "All rights reserved@2024 – UPCIDS-DSPPP\n\n")
creatorLabel = tk.Label(main, background="white", foreground="#76090c", font=("Franklin", 14), wraplength=wth-55, justify="center", text = "\n\nDr. Ebinezer R. Florano\nCreator\n")
programmerLabel = tk.Label(main, background="white", foreground="#76090c", font=("Franklin", 14), wraplength=wth-55, justify="center", text = "Bianca Mae Amurao, Emmerson Isip, Gabriel Ramos, Mohammad Hamdi Tuan, and Raphael Justin Portuguez\nProgrammers\n")
reveiwerLabel = tk.Label(main, background="white", foreground="#76090c", font=("Franklin", 14), wraplength=wth-55, justify="center", text = "Colin Rosales, Danne Nicole Pinpin, and Jean Phoebe Yao\nReviewers\n")
adminLabel = tk.Label(main, background="white", foreground="#76090c", font=("Franklin", 14), wraplength=wth-55, justify="center", text = "Lilian J. Marfil, Pedro J. Madarang, and Zhelly Ann Linsangan\nAdministrative Assistance\n")

dspppLogo = (Image.open(resource_path("logo_DSPPP.png")))
cidsLogo = (Image.open(resource_path("logo_UP_CIDS.png")))
upLogo = (Image.open(resource_path("logo_UP.png")))

up = upLogo.resize((100, 100))
dsppp = dspppLogo.resize((100, 100))

up = ImageTk.PhotoImage(up)
dsppp = ImageTk.PhotoImage(dsppp)
cids = ImageTk.PhotoImage(cidsLogo)

###
# def update_wraplength(event):
#    # Subtract some padding (e.g., 100px) to prevent edge crowding
#    new_width = event.wth - 100
#    for label in resizable_labels:
#        label.config(wraplength=new_width)

#resizable_labels = [introLabel, aboutLabel, arrLabel, creatorLabel, programmerLabel, reveiwerLabel, adminLabel]
###

# main.bind("<Configure>", update_wraplength)

introLabel.grid(row=0, column=0, padx=10) 
aboutLabel.grid(row=2, column=0, sticky="ew", padx=10)    
arrLabel.grid(row=4, column=0, sticky="ew", padx=10)     

logo_frame = tk.Frame(main, background="#ffffff")  
logo_frame.grid(row=6, column=0) 

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
logo_frame.grid_rowconfigure(0, weight=1)
logo_frame.grid_columnconfigure(0, weight=1)
logo_frame.grid_columnconfigure(1, weight=1)
logo_frame.grid_columnconfigure(2, weight=1)
logo_frame.grid_columnconfigure(3, weight=1)
logo_frame.grid_columnconfigure(4, weight=1)
logo_frame.grid_columnconfigure(5, weight=1)
logo_frame.grid_columnconfigure(6, weight=1)

upLabel = Label(logo_frame, image=up, background="#ffffff")
upLabel.grid(row=0, column=2, padx=50)  

dspppLabel = Label(logo_frame, image=dsppp, background="#ffffff")
dspppLabel.grid(row=0, column=3, padx=50)

cidsLabel = Label(logo_frame, image=cids, background="#ffffff")
cidsLabel.grid(row=0, column=4, padx=50)

creatorLabel.grid(row=8, column=0, sticky="ew")   
programmerLabel.grid(row=10, column=0, sticky="ew")   
reveiwerLabel.grid(row=12, column=0, sticky="ew")   
adminLabel.grid(row=14, column=0, sticky="ew")   
style = ttk.Style()

#    sb_ver = Scrollbar(
#        main,
#        orient=VERTICAL
#        )

#    sb_ver.pack(side=RIGHT, fill=Y)

#    main.config(yscrollcommand=sb_ver.set)
#    sb_ver.config(command=main.yview)



###Bmae addition: for saving and opening projects
global p1projecttitle, p1analysts, p1fontstyle, p1policyanalysis, p1fontsize

p1projecttitle = " "
p1analysts = " "
p1fontstyle = " "
p1policyanalysis = " "
p1fontstyle = " "
p1fontsize = 12

global p2problematicsituation, p2undesirableeffects

p2problematicsituation = ""
p2undesirableeffects = ""

global p3efforts, p3accomplishments, p3assessments
p3efforts = []
p3accomplishments = []
p3assessments = []

global p5rootcause, p5existingpolicies, p5relevantprov, p5accomplishments, p5assessments    
p5rootcause = " "
p5existingpolicies = []
p5relevantprov = []
p5accomplishments = []
p5assessments = []

global p6policyproblem, p6policyissue
p6policyproblem = " "
p6policyissue = ""

global p7policyGoalsandObjectives, p7indicators
p7policyGoalsandObjectives = []
p7indicators = []

global p8stakeholders, p8actors
p8stakeholders = []
p8actors = []

global p9altnum, p9alternatives
p9altnum = []
p9alternatives = []

global p9stakeholderDataPerAlt
p9stakeholderDataPerAlt = []

global p10spillovers, p10externalities, p10constraints, p10mitimeasures
p10spillovers = []
p10externalities = []
p10constraints = []
p10mitimeasures = []

global p11BPAdescription, p11BPAreasonSelect
p11BPAdescription = ""
p11BPAreasonSelect = ""

global p12BPAspillover, p12BPAexternality, p12BPAconstraint, p12BPAmitigatingmeasure
p12BPAspillover = ""
p12BPAexternality = ""
p12BPAconstraint = ""
p12BPAmitigatingmeasure = ""

global p13BPAwho, p13BPAwhat, p13BPAhow
p13BPAwho = ""
p13BPAwhat = ""
p13BPAhow = ""

global p14criticalActions, p14responsible, p14timeline, p14budget, p14budgetsource
p14criticalActions = []
p14responsible = []
p14timeline = []
p14budget = []
p14budgetsource = []

global p15dataSources, p15frequency, p15responsible, p15output, p15report
p15dataSources = []
p15frequency = []
p15responsible = []
p15output = []
p15report = []



# Menu setup
# def setup_menu():
#     menubar = tk.Menu(main)
#     file_menu = tk.Menu(menubar, tearoff=0)
#     file_menu.add_command(label="New", command=lambda: new_project())
#     file_menu.add_command(label="Open", command=lambda: open_project())
#     file_menu.add_command(label="Help", command=lambda: help_page())
#     menubar.add_cascade(label="File", menu=file_menu)
#     main.config(menu=menubar)

# Nasa baba yung menu set-up - Bmae

def new_project():
    global save_pdf_file_path, save_json_file_path
    save_pdf_file_path = None
    save_json_file_path = None

    global p1projecttitle, p1analysts, p1fontstyle, p1policyanalysis, p1fontsize

    p1projecttitle = " "
    p1analysts = " "
    p1fontstyle = " "
    p1policyanalysis = " "
    p1fontstyle = " "
    p1fontsize = 12

    global p2problematicsituation, p2undesirableeffects

    p2problematicsituation = ""
    p2undesirableeffects = ""

    global p3efforts, p3accomplishments, p3assessments
    p3efforts = []
    p3accomplishments = []
    p3assessments = []

    global p5rootcause, p5existingpolicies, p5relevantprov, p5accomplishments, p5assessments    
    p5rootcause = " "
    p5existingpolicies = []
    p5relevantprov = []
    p5accomplishments = []
    p5assessments = []

    global p6policyproblem, p6policyissue
    p6policyproblem = " "
    p6policyissue = ""

    global p7policyGoalsandObjectives, p7indicators
    p7policyGoalsandObjectives = []
    p7indicators = []

    global p8stakeholders, p8actors
    p8stakeholders = []
    p8actors = []

    global p9altnum, p9alternatives
    p9altnum = []
    p9alternatives = []

    global p9stakeholderDataPerAlt
    p9stakeholderDataPerAlt = []

    global p10spillovers, p10externalities, p10constraints, p10mitimeasures
    p10spillovers = []
    p10externalities = []
    p10constraints = []
    p10mitimeasures = []

    global p11BPAdescription, p11BPAreasonSelect
    p11BPAdescription = ""
    p11BPAreasonSelect = ""

    global p12BPAspillover, p12BPAexternality, p12BPAconstraint, p12BPAmitigatingmeasure
    p12BPAspillover = ""
    p12BPAexternality = ""
    p12BPAconstraint = ""
    p12BPAmitigatingmeasure = ""

    global p13BPAwho, p13BPAwhat, p13BPAhow
    p13BPAwho = ""
    p13BPAwhat = ""
    p13BPAhow = ""

    global p14criticalActions, p14responsible, p14timeline, p14budget, p14budgetsource
    p14criticalActions = []
    p14responsible = []
    p14timeline = []
    p14budget = []
    p14budgetsource = []

    global p15dataSources, p15frequency, p15responsible, p15output, p15report
    p15dataSources = []
    p15frequency = []
    p15responsible = []
    p15output = []
    p15report = []
    createNewProject()

def open_project():
    global save_pdf_file_path, save_json_file_path
    global p1projecttitle, p1analysts, p1fontstyle, p1policyanalysis, p1fontsize
    global p2problematicsituation, p2undesirableeffects
    global p3efforts, p3accomplishments, p3assessments
    global p5rootcause, p5existingpolicies, p5relevantprov, p5accomplishments, p5assessments
    global p6policyproblem, p6policyissue
    global p7policyGoalsandObjectives, p7indicators
    global p8stakeholders, p8actors
    global p9altnum, p9alternatives
    global p9stakeholderDataPerAlt
    global p10spillovers, p10externalities, p10constraints, p10mitimeasures
    global p11BPAdescription, p11BPAreasonSelect
    global p12BPAspillover, p12BPAexternality, p12BPAconstraint, p12BPAmitigatingmeasure
    global p13BPAwho, p13BPAwhat, p13BPAhow
    global p14criticalActions, p14responsible, p14timeline, p14budget, p14budgetsource
    global p15dataSources, p15frequency, p15responsible, p15output, p15report

    
    filename = tk.filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filename:
        with open(filename, "r") as f:
            data = json.load(f)
        save_pdf_file_path = data.get("save_pdf_file_path", None)
        save_json_file_path = data.get("save_json_file_path", None)
        p1projecttitle = data.get("p1projecttitle", "")
        p1analysts = data.get("p1analysts", "")
        p1fontstyle = data.get("p1fontstyle", "")
        p1fontsize = data.get("p1fontsize", 12)
        p1policyanalysis = data.get("p1policyanalysis", "")
        p2problematicsituation = data.get("p2problematicsituation", "")
        p2undesirableeffects = data.get("p2undesirableeffects", "")
        p3efforts = data.get("p3efforts", [])
        p3accomplishments = data.get("p3accomplishments", [])
        p3assessments = data.get("p3assessments", [])
        p5rootcause = data.get("p5rootcause", "")
        p5existingpolicies = data.get("p5existingpolicies", [])
        p5relevantprov = data.get("p5relevantprov", [])
        p5accomplishments = data.get("p5accomplishments", [])
        p5assessments = data.get("p5assessments", [])
        p6policyproblem = data.get("p6policyproblem", "")
        p6policyissue = data.get("p6policyissue", "")
        p7policyGoalsandObjectives = data.get("p7policyGoalsandObjectives", [])
        p7indicators = data.get("p7indicators", [])
        p8stakeholders = data.get("p8stakeholders", [])
        p8actors = data.get("p8actors", [])
        p9altnum = data.get("p9altnum", [])
        p9alternatives = data.get("p9alternatives", [])
        p9stakeholderDataPerAlt = data.get("p9stakeholderDataPerAlt", [])
        p10spillovers = data.get("p10spillovers", [])
        p10externalities = data.get("p10externalities", [])
        p10constraints = data.get("p10constraints", [])
        p10mitimeasures = data.get("p10mitimeasures", [])
        p11BPAdescription = data.get("p11BPAdescription", )
        p11BPAreasonSelect = data.get("p11BPAreasonSelect", "")
        p12BPAspillover = data.get("p12BPAspillover", "")
        p12BPAexternality = data.get("p12BPAexternality", "")
        p12BPAconstraint = data.get("p12BPAconstraint", "")
        p12BPAmitigatingmeasure = data.get("p12BPAmitigatingmeasure", "")
        p13BPAwho = data.get("p13BPAwho", "")
        p13BPAwhat = data.get("p13BPAwhat", "")
        p13BPAhow = data.get("p13BPAhow", "")
        p14criticalActions = data.get("p14criticalActions", [])
        p14responsible = data.get("p14responsible", [])
        p14timeline = data.get("p14timeline", [])
        p14budget = data.get("p14budget", [])
        p14budgetsource = data.get("p14budgetsource", [])
        p15dataSources = data.get("p15dataSources", [])
        p15frequency = data.get("p15frequency", [])
        p15responsible = data.get("p15responsible", [])
        p15output = data.get("p15output", [])
        p15report = data.get("p15report", [])

        createNewProject()

def help_page():
    help_window = tk.Toplevel(main)
    help_window.title("Help - Policy Analytics")
    help_window.geometry("800x600")
    help_text = scrolledtext.ScrolledText(help_window, height=30, width=80, wrap=tk.WORD)
    help_text.pack(padx=10, pady=10, fill="both", expand=True)
    help_content = """
    Policy Analytics Application Help
    ===============================
    This application guides you through a 15-page policy analysis process.

    Navigation:
    - Use 'Back' and 'Next' buttons to move between pages.
    - Progress is shown via a progress bar and workflow map at the top of each page.
    - Click workflow map rectangles to jump to specific pages.

    Features:
    - Add/Edit/Delete data in tables using buttons (Ctrl+Enter to add, Ctrl+Z to undo).
    - Zoom in/out using buttons for better visibility.
    - Use scrollbars for large tables.
    - Save data automatically when navigating with 'Next'.

    Page Descriptions:
    - Page 1: Set-up document (Project Title, Analysts, Font Style, Font Size, Levels of Analysis).
    - Page 2: Describe the Problematic Situation and Its Undesirable Effects.
    - Page 3: List Current Efforts, Accomplishments, and Assessments.
    - Page 4: Select statistical methods (Linear/Multiple/Logistic Regression, Problem Tree Analysis).
    - Page 5: Enter root cause and assess existing policies.
    - Page 6: Define policy problem and issue statement.
    - Page 7: List policy goals and objectives with indicators.
    - Page 8: Identify stakeholders and actors.
    - Page 9: Assess policy alternatives with effectiveness, cost-efficiency, and acceptability.
    - Page 10: Evaluate spillovers, externalities, and constraints.
    - Page 11: Describe the best policy alternative and reasons for selection.
    - Page 12: Detail spillovers, externalities, constraints, and mitigating measures for the best alternative.
    - Page 13: Specify legislation, implementers, and funding for the best alternative.
    - Page 14: Create a policy implementation plan.
    - Page 15: Develop a monitoring and evaluation plan.

    Shortcuts:
    - Ctrl+Z: Undo last action (where applicable).
    - Ctrl+Enter: Add data to tables.
    - Tab: Cycle through input fields.
    """
    help_text.insert(tk.INSERT, help_content)
    help_text.config(state="disabled")

def wrap(string, length=40):
    return '\n'.join(textwrap.wrap(string, length))

def createNewProject():
    global pageNumber
    pageNumber = 0

    global filename, fileobject
    global p4summaryPDF
    p4summaryPDF = " "

    mainProject = Toplevel(root)
    mainProject.transient(root)           # Attach to root
    mainProject.grab_set()                # Make it modal (disables root interaction)
    mainProject.lift()                    # Raise it to the top
    mainProject.focus_force()             # Bring focus
    mainProject.attributes("-topmost", 1) # Stay on top initially
    mainProject.after(10, lambda: mainProject.attributes("-topmost", 0))  # Release topmost after lift

    # mainProject = CTkXYFrame(root, fg_color="white")
    # mainProject.pack(fill="both", expand=True)

    
    varRoot1 = tk.IntVar()
    varRoot2 = tk.IntVar()
    varRoot3 = tk.IntVar()
    varRoot4 = tk.IntVar()
    varRoot5 = tk.IntVar()
    varRoot6 = tk.IntVar()
    varRoot7 = tk.IntVar()

    status = ttk.Label(mainProject, text="")
    
    ##global p1projecttitle, p1analysts, p1fontstyle, p1policyanalysis, p1fontstyle, p1fontsize
    ##p1projecttitle = " "
    ##p1analysts = " "
    ##p1fontstyle = " "
    ##p1policyanalysis = " "
    ##p1fontstyle = " "
    ##p1fontsize = 12

    color = ("", "#000000")  # Default color for ShapeEditorApp
    discount = 0.05  # Default discount rate
    
    # Tooltip class
    class ToolTip:
        def __init__(self, widget, text):
            self.widget = widget
            self.text = text
            self.tip_window = None
            self.widget.bind("<Enter>", self.show_tip)
            self.widget.bind("<Leave>", self.hide_tip)

        def show_tip(self, event=None):
            if self.tip_window or not self.text:
                return
            x, y, _, _ = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + int(25*(wth/1920))
            y += self.widget.winfo_rooty() + int(25*(wth/1920))
            self.tip_window = tw = tk.Toplevel(self.widget)
            tw.wm_overrideredirect(True)
            tw.wm_geometry(f"+{x}+{y}")
            label = tk.Label(tw, text=self.text, justify="left", background="#ffffe0", relief="solid", borderwidth=1)
            label.pack()

        def hide_tip(self, event=None):
            if self.tip_window:
                self.tip_window.destroy()
                self.tip_window = None

    def setup_page_common(page_num, title, frame, widgets_to_destroy, back_func, next_func):
        mainProject.state('zoomed')
        style.configure('Treeview', rowheight=120)
        style.configure("TButton", foreground="black", font=("Calibri", int(12*(wth/1920))))

        # Canvas with scrollbars
        canvas = tk.Canvas(mainProject)
        scrollbar_y = ttk.Scrollbar(mainProject, orient="vertical", command=canvas.yview)
        scrollbar_x = ttk.Scrollbar(mainProject, orient="horizontal", command=canvas.xview)
        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Zoom functionality
        scale = 1.0
        def zoom_in():
            nonlocal scale
            scale *= 1.1
            canvas.scale("all", 0, 0, 1.1, 1.1)
            canvas.configure(scrollregion=canvas.bbox("all"))
        def zoom_out():
            nonlocal scale
            scale /= 1.1
            canvas.scale("all", 0, 0, 1/1.1, 1/1.1)
            canvas.configure(scrollregion=canvas.bbox("all"))
        zoom_in_button = ttk.Button(mainProject, text="Zoom In", command=zoom_in())
        zoom_out_button = ttk.Button(mainProject, text="Zoom Out", command=zoom_out())
        zoom_in_button.place(relx=0.01, rely=0.01)
        zoom_out_button.place(relx=0.08, rely=0.01)

        # Progress bar and workflow map
        progress = ttk.Progressbar(mainProject, length=200, maximum=15, value=page_num)
        progress.place(relx=0.01, rely=0.05)
        progress_label = tk.Label(mainProject, text=f"Page {page_num} of 15: {title}", font=("Calibri", int(14*(wth/1920)), "bold"))
        progress_label.place(relx=0.01, rely=0.08)
        workflow_canvas = tk.Canvas(mainProject, height=50, width=750)
        workflow_canvas.place(relx=0.01, rely=0.12)
        for i in range(1, 16):
            x = (i-1)*50
            workflow_canvas.create_rectangle(x, 10, x+40, 40, fill="lightblue" if i == page_num else "gray")
            workflow_canvas.create_text(x+20, 25, text=str(i))
            workflow_canvas.tag_bind(i, "<Button-1>", lambda e, p=i: jump_to_page(p))

        def jump_to_page(p):
            global pageNumber
            pageNumber = p
            for widget in mainProject.winfo_children():
                widget.destroy()
            globals()[f"page_{p}"]()

        # Navigation buttons
        btn_back = ttk.Button(mainProject, text="Back", command=back_func)
        btn_next = ttk.Button(mainProject, text="Next", command=next_func)
        ToolTip(btn_back, "Go to the previous page")
        ToolTip(btn_next, "Proceed to the next page")
        btn_back.place(relx=0.4, rely=0.95)
        btn_next.place(relx=0.5, rely=0.95)
        widgets_to_destroy.extend([canvas, scrollbar_y, scrollbar_x, zoom_in_button, zoom_out_button, progress, progress_label, workflow_canvas, btn_back, btn_next])

    def page_1():
        global pageNumber 
        pageNumber = 1
        mainProject.title("Create New Project")
        mainProject.geometry(f"{730}x{225}")

        # Progress indicator
        progress_label = tk.Label(mainProject, text="Page 1 of 15: Set-up document", font=("Calibri", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        frame1 = tk.LabelFrame(mainProject)

        blank = Label(mainProject, text = "  ")

        projectTitleLabel1 = Label(frame1, text = "Project Title", font=("Calibri", 10))
        projectTitle = Entry(frame1, font=("Calibri", 10), width=30)

        analystNameLabel1 = Label(frame1, text = "Analyst", font=("Calibri", 10))
        analystName = Entry(frame1, font=("Calibri", 10), width=30)

        polAnaTitleLabel1 = Label(frame1, text = "Policy Analysis Title", font=("Calibri", 10))
        polAnaTitle = Entry(frame1, font=("Calibri", 10), width=30)

        settingsLabel = Label(frame1, text = "Settings", font=("Calibri", 10))
        fontStyleLabel = Label(frame1, text = "Choose font style: ", font=("Calibri", 10))
        fontSizeLabel = Label(frame1, text = "Choose font size: ", font=("Calibri", 10))
        indentationLabel = Label(frame1, text = "Choose indentation: ", font=("Calibri", 10))
        
        font.families()
        fonts = list(font.families())
        fonts.sort()

        fontsList = ttk.Combobox(frame1, font=("Calibri", 10), width=30, values=fonts)
        fontSize = Entry(frame1, font=("Calibri", 10), width=10)
        indentation = Entry(frame1, font=("Calibri", 10), width=10)


        levelsLabel1 = Label(frame1, text = "Levels of Analysis ", font=("Calibri", 10))

        varNat = tk.IntVar()
        varLoc = tk.IntVar()
        varOrg = tk.IntVar()

        national = tk.Checkbutton(frame1, text='National', font=("Calibri", 10), variable=varNat, onvalue=1, offvalue=0)
        local = tk.Checkbutton(frame1, text='Local', font=("Calibri", 10), variable=varLoc, onvalue=1, offvalue=0)
        organizational = tk.Checkbutton(frame1, text='Organizational', font=("Calibri", 10), variable=varOrg, onvalue=1, offvalue=0)

        # font=("Calibri",10))
        frame1.place(x=20, y=20)
        projectTitleLabel1.grid(row=2, column=0, padx=int(7*(wth/1920)))
        projectTitle.grid(row=3, column=0, padx=int(7*(wth/1920)))
        analystNameLabel1.grid(row=2, column=1, padx=int(7*(wth/1920)))
        analystName.grid(row=3, column=1, padx=int(7*(wth/1920)))
        polAnaTitleLabel1.grid(row=2, column=2, padx=int(7*(wth/1920)))
        polAnaTitle.grid(row=3, column=2, padx=int(7*(wth/1920)))
        settingsLabel.grid(row=5, column=0)
        fontStyleLabel.grid(row=6, column=0, sticky = W, padx=int(7*(wth/1920)))
        fontsList.grid(row=6, column=1, sticky = W, padx=int(7*(wth/1920)))
        fontSizeLabel.grid(row=7, column=0, sticky = W, padx=int(7*(wth/1920)))
        fontSize.grid(row=7, column=1, sticky = W, padx=int(7*(wth/1920)))
        indentationLabel.grid(row=8, column=0, sticky = W, padx=int(7*(wth/1920)))
        indentation.grid(row=8, column=1, sticky = W, padx=int(7*(wth/1920)))
        levelsLabel1.grid(row=5, column=2, padx=int(7*(wth/1920)))
        national.grid(row=6, column=2, sticky = W, padx=int(56*(wth/1920)))
        local.grid(row=7, column=2, sticky = W, padx=int(56*(wth/1920)))
        organizational.grid(row=8, column=2, sticky = W, padx=int(56*(wth/1920)))

        projectTitle.insert(0, p1projecttitle)
        analystName.insert(0, p1analysts)
        polAnaTitle.insert(0, p1policyanalysis)
        fontsList.set(p1fontstyle)
        fontSize.insert(0, str(p1fontsize))

        def clear_page_1():
            projectTitle.config(bg="white")
            fontSize.config(bg="white")
            analystName.config(bg="white")
            polAnaTitle.config(bg="white")
            fontsList.set('')
            
            projectTitle.delete(0, END)
            polAnaTitle.delete(0, END)
            analystName.delete(0, END)
            fontSize.delete(0, END)
            indentation.delete(0, END)

        def create_project():    
            global p1projecttitle, p1analysts, p1fontstyle, p1policyanalysis, p1fontstyle, p1fontsize
            p1projecttitle = projectTitle.get()
            if not p1projecttitle.strip():
                status.config(
                    text="Enter project title",
                    foreground="red",
                )
                return
            
            p1fontstyle = fontsList.get()

            p1fontsize = fontSize.get()
            if p1fontsize.isnumeric() == False:
                status.config(
                    text="Enter font size",
                    foreground="red",
                )
                return

            p1fontsize = int(p1fontsize)

            p1analysts = analystName.get()
            if not p1analysts.strip():
                status.config(
                    text="Enter analyst name",
                    foreground="red",
                )
                return
                    
            p1policyanalysis = polAnaTitle.get()
            if not p1policyanalysis.strip():
                status.config(
                    text="Enter policy analysis title",
                    foreground="red",
                )
                return
            
            save()
            
            global pageNumber
            pageNumber += 1
            print(pageNumber)
            frame1.destroy()
            btnCreate.destroy() 
            btnClear1.destroy()  
            page_2()
            
        btnCreate = Button(mainProject, text = "Create", width=10, font=("Calibri", 10), command = lambda: create_project())
        btnClear1 = Button(mainProject, text = "Clear", width=10, font=("Calibri", 10), command = lambda: clear_page_1())
        btnCreate.place(x=380, rely=0.8)
        btnClear1.place(x=190, rely=0.8)
        status.place(x=int(10*(wth/1920)), rely=0.9)
    page_1()

    def page_2():                                                               # write problematic situation and undesirable effects

        status = Label(mainProject, text="")
        status.place(x=10, y=170)

        mainProject.geometry("600x220")

        ### Progress indicator
        frame2 = tk.LabelFrame(mainProject)
        progress_label = tk.Label(mainProject, text="Page 2 of 15: Problematic Situation and Its Undesirable Effects.", font=("Calibri", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        status.config(text="")

        probSitLabel = Label(frame2, text = "Problematic Situation", font=("Calibri", 10))
        probSit = scrolledtext.ScrolledText(frame2, height=8, font=("Consolas", int(10)), width=30)
        
        undeEffLabel = Label(frame2, text = "Undesirable Effects", font=("Calibri", 10))
        undeEff = scrolledtext.ScrolledText(frame2, height=8, font = ("Consolas", int(10)), width=30)
        
        frame2.place(x=40, y=10)
        probSitLabel.grid(row=1, column=0, sticky = W, padx=int(7*(wth/1920)))
        probSit.grid(row=2, column=0, sticky = W, padx=int(7*(wth/1920)))
        undeEffLabel.grid(row=1, column=1, sticky = W, padx=int(7*(wth/1920)))
        undeEff.grid(row=2, column=1, sticky = W, padx=int(7*(wth/1920)))

        probSit.insert("1.0", p2problematicsituation)
        undeEff.insert("1.0", p2undesirableeffects)
        
        def back_1():
            global pageNumber
            pageNumber -= 1
            print(pageNumber)
            frame2.destroy() 
            btnBack1.destroy()
            btnNext1.destroy() 
            progress_label.destroy()
            save()
            page_1()
        
        def next_1():
            global pageNumber
            pageNumber += 1
            print(pageNumber)

            global p2problematicsituation, p2undesirableeffects
            p2problematicsituation = probSit.get("1.0", tk.END)
            if not p2problematicsituation.strip():
                status.config(
                text="Enter problematic\nsituation",
                foreground="red",
            )
                return
                    
            p2undesirableeffects = undeEff.get("1.0", tk.END)
            if not p2undesirableeffects.strip():
                status.config(
                text="Enter undesirable\neffects",
                foreground="red",
            )
                return
    
            save()

            frame2.destroy() 
            btnBack1.destroy()
            btnNext1.destroy() 
            progress_label.destroy()
            page_3()

        btnBack1 = Button(mainProject, text = "Back", font=("Calibri", 10), width=10, command = lambda: back_1())
        btnNext1 = Button(mainProject, text = "Next", font=("Calibri", 10), width=10, command = lambda: next_1())
        btnBack1.place(x=110, y=170)
        btnNext1.place(x=370, y=170)
    
 
    def page_3():
        global p3efforts, p3accomplishments, p3assessments
        mainProject.geometry("1250x700")
        page_width = int(1250*(wth/1920))
        page_height = int(700*(wth/1920))
        
        style = ttk.Style()
        style.configure('Treeview', rowheight=int(160), font=('Arial', int(10)))
        style.configure("TButton", foreground="black", font=("Arial", int(10)))  # Set button text to black

        # Undo stack
        undo_stack = []

        # Canvas with scrollbars
        canvas = tk.Canvas(mainProject)
        canvas.pack(fill="both", expand=True)
        frame3 = tk.LabelFrame(canvas)
        canvas.create_window((0, 0), window=frame3, anchor="nw")
        def configure_canvas(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        frame3.bind("<Configure>", configure_canvas)

        # Zoom functionality
        scale = 1.0
        def zoom_in():
            nonlocal scale
            scale *= 1.1
            canvas.scale("all", 0, 0, 1.1, 1.1)
            canvas.configure(scrollregion=canvas.bbox("all"))
        def zoom_out():
            nonlocal scale
            scale /= 1.1
            canvas.scale("all", 0, 0, 1/1.1, 1/1.1)
            canvas.configure(scrollregion=canvas.bbox("all"))
        zoom_in_button = ttk.Button(mainProject, text="Zoom In", command=zoom_in())
        zoom_out_button = ttk.Button(mainProject, text="Zoom Out", command=zoom_out())
        zoom_in_button.place(x=10, y=10)
        zoom_out_button.place(x=100, y=10)



        # Treeview with scrollbars
        currEffLabel = tk.Label(frame3, font=("",int(10)), text="Current Efforts/Measures of the Government to Solve the Situational Problem")
        effortsTable = ttk.Treeview(frame3, selectmode="browse", height=2)
        effortsTable["columns"] = ("1", "2", "3")
        effortsTable['show'] = 'headings'
        effortsTable.column("1", width=int(200), anchor='c', stretch=True)
        effortsTable.column("2", width=int(700), anchor='c', stretch=True)
        effortsTable.column("3", width=int(300), anchor='c', stretch=True)
        effortsTable.heading("1", text="Efforts/Measures")
        effortsTable.heading("2", text="Accomplishments")
        effortsTable.heading("3", text="Assessments")
        sb_y = ttk.Scrollbar(frame3, orient="vertical", command=effortsTable.yview)
        sb_x = ttk.Scrollbar(frame3, orient="horizontal", command=effortsTable.xview)
        effortsTable.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)
        currEffLabel.grid(row=0, column=0, columnspan=2)
        effortsTable.grid(row=1, column=0)
        sb_y.grid(row=1, column=1, sticky="ns")

        # Input fields
        effoLabel = tk.Label(mainProject, text="Effort", font=("Arial", 10))
        accoLabel = tk.Label(mainProject, text="Accomplishment", font=("Arial", 10))
        asseLabel = tk.Label(mainProject, text="Assessment", font=("Arial", 10))
        effort = scrolledtext.ScrolledText(mainProject, font = ("Consolas", int(11)), height=9, width=40)
        accomplishment = scrolledtext.ScrolledText(mainProject, font = ("Consolas", int(11)), height=9, width=40)
        assessment = scrolledtext.ScrolledText(mainProject, font = ("Consolas", int(11)), height=9, width=40)
        effoLabel.place(x=195, y=390)
        effort.place(x=50, y=429)
        accoLabel.place(x=563, y=390)
        accomplishment.place(x=450, y=420)
        asseLabel.place(x=975, y=390)
        assessment.place(x=850, y=420)

        # Buttons with tooltips
        addButton = ttk.Button(mainProject, text="Add", style="TButton", command=lambda: add_data())
        ToolTip(addButton, "Add a new entry to the table")
        editButton = ttk.Button(mainProject, text="Edit", style="TButton", command=lambda: edit_data(), state="disabled")
        ToolTip(editButton, "Edit the selected table entry")
        deleteButton = ttk.Button(mainProject, text="Delete", style="TButton", command=lambda: delete_data(), state="disabled")
        ToolTip(deleteButton, "Delete the selected table entry")
        btnBack2 = ttk.Button(mainProject, text="Back", style="TButton", command=lambda: back_2())
        ToolTip(btnBack2, "Go to the previous page")
        btnNext2 = ttk.Button(mainProject, text="Next", style="TButton", command=lambda: next_2())
        ToolTip(btnNext2, "Proceed to the next page")
        addButton.place(x=490, y=590)
        editButton.place(x=585, y=590)
        deleteButton.place(x=680, y=590)
        btnBack2.place(x=490, y=650)
        btnNext2.place(x=680, y=650)

        if not effortsTable.get_children():
            for e, a, s in zip(p3efforts, p3accomplishments, p3assessments):
                effortsTable.insert("", "end", values=(wrap(e), wrap(a), wrap(s)))
                
        # Event handlers
        def show_data(a):
            effort.delete("1.0", tk.END)
            accomplishment.delete("1.0", tk.END)
            assessment.delete("1.0", tk.END)
            selectedItem = effortsTable.selection()
            if selectedItem:
                editButton.config(state="normal")
                deleteButton.config(state="normal")
                effort.insert(tk.INSERT, effortsTable.item(selectedItem[0])['values'][0])
                accomplishment.insert(tk.INSERT, effortsTable.item(selectedItem[0])['values'][1])
                assessment.insert(tk.INSERT, effortsTable.item(selectedItem[0])['values'][2])
            else:
                editButton.config(state="disabled")
                deleteButton.config(state="disabled")
        effortsTable.bind("<<TreeviewSelect>>", show_data)

        def add_data():
            effortText = effort.get("1.0", tk.END).strip()
            accomplishmentText = accomplishment.get("1.0", tk.END).strip()
            assessmentText = assessment.get("1.0", tk.END).strip()
            if not (effortText and accomplishmentText and assessmentText):
                messagebox.showerror("Error", "Please fill out all fields")
                return
            item_id = effortsTable.insert("", 'end', values=(wrap(effortText), wrap(accomplishmentText), wrap(assessmentText)))
            undo_stack.append(("add", item_id))
            p3efforts.append(effortText)
            p3accomplishments.append(accomplishmentText)
            p3assessments.append(assessmentText)
            effort.delete("1.0", tk.END)
            accomplishment.delete("1.0", tk.END)
            assessment.delete("1.0", tk.END)
            effort.focus()
            save()

        def edit_data():
            effortText = effort.get("1.0", tk.END).strip()
            accomplishmentText = accomplishment.get("1.0", tk.END).strip()
            assessmentText = assessment.get("1.0", tk.END).strip()
            if not (effortText and accomplishmentText and assessmentText):
                messagebox.showerror("Error", "Please fill out all fields")
                return
            selected_item = effortsTable.selection()[0]
            old_values = effortsTable.item(selected_item)['values']
            undo_stack.append(("edit", selected_item, old_values))
            effortsTable.item(selected_item, values=(effortText, accomplishmentText, assessmentText))
            p3efforts[effortsTable.index(selected_item)] = effortText
            p3accomplishments[effortsTable.index(selected_item)] = accomplishmentText
            p3assessments[effortsTable.index(selected_item)] = assessmentText
            save()

        def delete_data():
            selected_item = effortsTable.selection()
            if selected_item:
                item_id = selected_item[0]
                old_values = effortsTable.item(item_id)['values']
                index = effortsTable.index(item_id)
                undo_stack.append(("delete", item_id, old_values, index))
                effortsTable.delete(item_id)
                p3efforts.pop(index)
                p3accomplishments.pop(index)
                p3assessments.pop(index)
                effort.delete("1.0", tk.END)
                accomplishment.delete("1.0", tk.END)
                assessment.delete("1.0", tk.END)
                editButton.config(state="disabled")
                deleteButton.config(state="disabled")
            else:
                messagebox.showwarning("Warning", "Please select an item to delete")
            save()

        def undo():
            if not undo_stack:
                return
            action, *data = undo_stack.pop()
            if action == "add":
                item_id = data[0]
                effortsTable.delete(item_id)
                p3efforts.pop()
                p3accomplishments.pop()
                p3assessments.pop()
            elif action == "edit":
                item_id, old_values = data
                effortsTable.item(item_id, values=old_values)
                index = effortsTable.index(item_id)
                p3efforts[index] = old_values[0]
                p3accomplishments[index] = old_values[1]
                p3assessments[index] = old_values[2]
            elif action == "delete":
                item_id, old_values, index = data
                effortsTable.insert("", index, iid=item_id, values=old_values)
                p3efforts.insert(index, old_values[0])
                p3accomplishments.insert(index, old_values[1])
                p3assessments.insert(index, old_values[2])
            save()

        # Keyboard shortcuts
        frame3.bind("<Control-z>", lambda event: undo())
        frame3.bind("<Control-Return>", lambda event: add_data())
        effort.bind("<Tab>", lambda event: accomplishment.focus_set())
        accomplishment.bind("<Tab>", lambda event: assessment.focus_set())
        assessment.bind("<Tab>", lambda event: addButton.focus_set())

        ### Progress indicator
        progress_label = tk.Label(frame3, text="Page 3 of 15: Current Efforts", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        def back_2():
            global pageNumber
            pageNumber -= 1
            print(pageNumber)
            for widget in mainProject.winfo_children():
                widget.destroy()
            page_2()

        def next_2():
            global pageNumber
            pageNumber += 1
            print(pageNumber)
            for widget in mainProject.winfo_children():
                widget.destroy()
            save()
            page_4()

    def page_4():
        mainProject.geometry("660x250")
        # Progress indicator
        progress_label = tk.Label(mainProject, text="Page 4 of 15: Select Statistical Methods", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")
        frame4 = tk.LabelFrame(mainProject)

        global var, analysis_type
        var = IntVar()
            
        StatisticalMethod = Label(mainProject, text = "Statistical Method", font=("Calibri", 14))
        Qualita = Label(frame4, text="Qualitative", font=("Arial", 10))
        Quantita = Label(frame4, text="Quantitative", font=("Arial", 10))
        R1 = Radiobutton(frame4, text="Linear Regression", font=("Arial", 10), variable=var, value=1)
        R2 = Radiobutton(frame4, text="Multiple Regression", font=("Arial", 10), variable=var, value=2)
        R3 = Radiobutton(frame4, text="Logistic Regression", font=("Arial", 10), variable=var, value=3)
        R4 = Radiobutton(frame4, text="Problem Tree Analysis", font=("Arial", 10), variable=var, value=4)

        StatisticalMethod.place(x=275, y=15)
        frame4.place(x=190, y=50)
        Quantita.grid(row=1, column=0)
        Qualita.grid(row=1, column=1)
        R1.grid(row=2, column=0)
        R2.grid(row=3, column=0)
        R3.grid(row=4, column=0)
        R4.grid(row=2, column=1)

        def analyses():
            global reg_sum
            global analysis_type                    
            if (int(var.get()) == 1):
                analysis = Toplevel(main)
                analysis.transient(root)
                analysis.grab_set()
                analysis.lift()
                analysis.focus_force()
                analysis.attributes("-topmost", 1)
                analysis.after(10, lambda: analysis.attributes("-topmost", 0))
                analysis.title("Analysis - Linear Regression")
                analysis.geometry("1000x680")
                analysis_type = "Linear Regression"

                filename = askopenfilename(filetypes=[("CSV Files", "*.csv")])

                if filename == "":
                    page_4()
                df = pd.read_csv(filename, usecols=[0,1])
                X_train = df.iloc[:, [0]]
                y_train = df.iloc[:, [1]]

                print(df)

                column_names = list(df.columns)

                model = sm.OLS(y_train, sm.add_constant(X_train)).fit()

                lb1 = Label(analysis,text=model.summary(), font=("Consolas", 10), justify="left")
                lb1.pack()

                reg = skl.linear_model.LinearRegression().fit(X_train[:], y_train[:])

                divider  = "\n******************************************************************************\n"
                regTitle = "                       skLearn Linear Regression Results                        \n"
                lb2 = Label(analysis,text=divider+regTitle, font=("Consolas", 10), justify="left")
                lb2.pack()

                score = "Score:        " + str(round(float(reg.score(X_train, y_train)), 5))
                global interceptLR, coefficientLR, interceptLRDisplay, coefficientLRDisplay
                interceptLRDisplay = "\nIntercept:    " + str(round(float(reg.intercept_), 5))
                interceptLR = float(reg.intercept_)
                coefficientLRDisplay = "\nCoefficient:  " + str(round(float(reg.coef_), 5))
                coefficientLR = float(reg.coef_)

                summary = score + interceptLRDisplay + coefficientLRDisplay
                lb3 = Label(analysis,text=summary, font=("Consolas", 10), justify="left")
                lb3.pack()

                global p4summaryPDF
                p4summaryPDF = divider + regTitle + summary

                reg_sum = regTitle + summary
                
                plt.scatter(X_train, y_train, color = "m", marker = "o", s = 30)

                # plotting the regression line
                plt.plot(X_train, reg.predict(X_train), color = "g")

                # putting labels
                plt.xlabel(column_names[0])
                plt.ylabel(column_names[1])
                image_filename = "page4_plot.png"
                plt.savefig(image_filename)
                plt.show()
                page_5()

            elif(int(var.get()) == 2):
                analysis = Toplevel(main)
                analysis.transient(root)
                analysis.grab_set()
                analysis.lift()
                analysis.focus_force()
                analysis.attributes("-topmost", 1)
                analysis.after(10, lambda: analysis.attributes("-topmost", 0))
                analysis.title("Analysis - Multiple Regression Summary 1")
                analysis.geometry(f"{int(1000*(wth/1920))}x{680}")
                analysis_type = "Multiple Regression"

                analysis2 = Toplevel(main)
                analysis2.title("Analysis - Multiple Regression Summary 2")
                analysis2.geometry("1200x680")
                analysis2 = Toplevel(main)
                analysis2.transient(root)
                analysis2.grab_set()
                analysis2.lift()
                analysis2.focus_force()
                analysis2.attributes("-topmost", 1)
                analysis2.after(10, lambda: analysis.attributes("-topmost", 0))

                filename = askopenfilename(filetypes=[("CSV Files", "*.csv")])
                df = pd.read_csv(filename)

                data_x = df.iloc[:, 0:2]
                data_x1 = df.iloc[:, [0]]
                data_x2 = df.iloc[:, [1]]
                data_y = df.iloc[:, [2]]

                data_x = sm.add_constant(data_x)

                ks = sm.OLS(data_y, data_x)
                ks_res =ks.fit()
                ks_res.summary()
                
                print(ks_res.summary())

                lb1 = Label(analysis, text=ks_res.summary(), font=("Consolas", 10), justify="left")
                lb1.pack()

                column_headers = list(df.columns.values)

                dividerA  = "******************************************************************************\n"
                regTitleA = "          skLearn Multiple Regression Results - "+column_headers[0]+"           \n"
                lb2 = Label(analysis2, text=dividerA+regTitleA, font=("Consolas", 10), justify="left")
                lb2.pack()

                reg1 = skl.linear_model.LinearRegression().fit(data_x1, data_y)

                score = "Score:        " + str(reg1.score(data_x1, data_y))
                global interceptMR1, coefficientMR1
                interceptMR1Display = "\nIntercept:    " + str(reg1.intercept_)
                coefficientMR1Display = "\nCoefficient:  " + str(reg1.coef_)
                interceptMR1 = float(reg1.intercept_)
                coefficientMR1 = float(reg1.coef_)

                summary3 = score + interceptMR1Display + coefficientMR1Display 
                lb3 = Label(analysis2, text=summary3, font=("Consolas",10), justify="left")
                lb3.pack()

                dividerB  = "******************************************************************************\n"
                regTitleB = "          skLearn Multiple Regression Results - "+column_headers[1]+"            \n"
                lb4 = Label(analysis2, text=dividerB+regTitleB, font=("Consolas", 10), justify="left")
                lb4.pack()

                reg2 = skl.linear_model.LinearRegression().fit(data_x2, data_y)

                score = "Score:        " + str(reg2.score(data_x2, data_y))
                global interceptMR2, coefficientMR2
                interceptMR2Display = "\nIntercept:    " + str(reg2.intercept_)
                coefficientMR2Display = "\nCoefficient:  " + str(reg2.coef_)
                interceptMR2 = float(reg2.intercept_)
                coefficientMR2 = float(reg2.coef_)

                summary4 = score + interceptMR2Display + coefficientMR2Display
                lb5 = Label(analysis2, text=summary4, font=("Consolas",10), justify="left")
                lb5.pack()

                reg_sum = regTitleA + summary3 + "    \n    \n" + regTitleB + summary4

                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.scatter(data_x1, data_x2, data_y, c='blue', marker='o')

                # set your labels
                ax.set_xlabel(column_headers[0])
                ax.set_ylabel(column_headers[1])
                ax.set_zlabel(column_headers[2])

                plt.savefig('regplot.png')
                image_filename = "page4_plot.png"
                plt.savefig(image_filename)
                plt.show()

                page_5()
                

                # l = tk.Label(frame, text="Hello", font="-size 50")
                # l.pack()

                # l = tk.Label(frame, text="World", font="-size 50")
                # l.pack()

                # l = tk.Label(frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
                # l.pack()

            elif(int(var.get()) == 3):
                analysis = Toplevel(main)
                analysis.transient(root)
                analysis.grab_set()
                analysis.lift()
                analysis.focus_force()
                analysis.attributes("-topmost", 1)
                analysis.after(10, lambda: analysis.attributes("-topmost", 0))
                analysis.title("Analysis - Logistic Regression Summary 1")
                analysis.geometry("830x480")

                analysis2 = Toplevel(main)
                analysis2.transient(root)
                analysis2.grab_set()
                analysis2.lift()
                analysis2.focus_force()
                analysis2.attributes("-topmost", 1)
                analysis2.after(10, lambda: analysis.attributes("-topmost", 0))
                analysis2.title("Analysis - Logistic Regression Summary 2")
                analysis2.geometry("830x480")
                analysis_type = "Logistic Regression"

                filename = askopenfilename(filetypes=[("CSV Files", "*.csv")])
                df = pd.read_csv(filename)
                X_train = df.iloc[:, [0]]
                y_train = df.iloc[:, [1]]

                X_train = sm.add_constant(X_train)
                print("111")
                print(X_train.max()[1])
                print("111")

                column_names = list(df.columns)

                logit_model = sm.Logit(y_train, X_train).fit()

                lb1 = Label(analysis,text=logit_model.summary(), font=("Consolas", 10), justify="left")
                lb1.pack()

                reg = skl.linear_model.LogisticRegression().fit(X_train[:], y_train[:])

                divider  = "\n******************************************************************************\n"
                regTitle = "                       skLearn Logistic Regression Results                        "
                lb2 = Label(analysis,text=divider+regTitle, font=("Consolas", 10), justify="left")
                lb2.pack()

                score = "Score:        " + str(round(float(reg.score(X_train, y_train)), 5))
                global interceptLogR, coefficientConstLogR, coefficientXLogR, interceptLogRDisplay, coefficientLogRDisplay
                interceptLogRDisplay = "\nIntercept:    " + str(reg.intercept_)
                print(interceptLogRDisplay)
                coefficientLogRDisplay = "\nCoefficient:  " + str(reg.coef_)
                print(coefficientLogRDisplay)
                interceptLogR = float(reg.intercept_)
                coefficientConstLogR = float(reg.coef_[0][0])
                coefficientXLogR = float(reg.coef_[0][1])

                summary2 = score + interceptLogRDisplay + coefficientLogRDisplay
                lb3 = Label(analysis,text=summary2, font=("Consolas", 10), justify="left")
                lb3.pack()

                lb4 = Label(analysis2,text=logit_model.summary2(), font=("Consolas", 10), justify="left")
                lb4.pack()
                
                reg_sum = summary2

                X_train = df.iloc[:, [0]]
                plt.scatter(X_train, y_train, color = "m", marker = "o", s = 30)

                X_train = sm.add_constant(X_train)
                X_test = np.arange(0, int(X_train.max()[1]), 0.1)
                y_test = sp.special.expit(X_test * reg.coef_[0][1] + reg.intercept_[0])
                plt.plot(X_test, y_test, label="Logistic Regression Model", color="red", linewidth=3)
                plt.savefig('regplot.png')
                image_filename = "page4_plot.png"
                plt.savefig(image_filename)
                plt.show() 
                page_5()
            
            elif(int(var.get()) == 4):
                analysis = Toplevel(main)
                analysis.title("Analysis - Problem Tree Analysis")
                analysis.geometry("830x480")
                analysis_type = "Problem Tree Analysis"

                # Ensure it's in front
                analysis.transient(root)
                analysis.grab_set()
                analysis.lift()
                analysis.focus_force()
                analysis.attributes("-topmost", 1)
                analysis.after(10, lambda: analysis.attributes("-topmost", 0))

                class ShapeEditorApp:
                    def __init__(self, root):
                        global textValue
                        textValue = StringVar()
                        italic_font = font.Font(family="Arial", size=10, slant="italic")

                        self.root = root
                        self.root.title("Problem Tree Analysis")

                        # Create Canvas widget with scrollbars
                        self.canvas_frame = tk.Frame(root)
                        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
                        
                        self.scroll_x = tk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL)
                        self.scroll_y = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL)
                        self.canvas = tk.Canvas(self.canvas_frame, bg="white", 
                                            xscrollcommand=self.scroll_x.set, 
                                            yscrollcommand=self.scroll_y.set)
                        self.scroll_x.config(command=self.canvas.xview)
                        self.scroll_y.config(command=self.canvas.yview)
                        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
                        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
                        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                        # Initialize variables
                        self.current_shape = None
                        self.start_x = None
                        self.start_y = None
                        self.current_shape_item = None
                        self.pen_active = False
                        self.eraser_active = False
                        self.color = "black"
                        self.undo_stack = []
                        self.redo_stack = []
                        self.zoom_level = 1.0
                        self.max_undo = 50  # Limit to prevent excessive memory use

                        # Create buttons
                        self.color_button = tk.Button(root, text="Color", command=self.choose_color)
                        self.pen_button = tk.Button(root, text='Pen', command=self.use_pen)
                        self.eraser_button = tk.Button(root, text="Eraser", command=self.use_eraser)
                        self.rect_button = tk.Button(root, text="Rectangle", command=self.create_rectangle)
                        self.circle_button = tk.Button(root, text="Arrow", command=self.create_arrow)
                        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
                        self.undo_button = tk.Button(root, text="Undo", command=self.undo)
                        self.redo_button = tk.Button(root, text="Redo", command=self.redo)
                        self.zoom_in_button = tk.Button(root, text="Zoom In", command=self.zoom_in)
                        self.zoom_out_button = tk.Button(root, text="Zoom Out", command=self.zoom_out)
                        self.save_button = tk.Button(root, text="Save", command=self.save_canvas)
                        self.text_frame = tk.Frame(root, height=100, width=200, relief=tk.SUNKEN, borderwidth=3)
                        self.text_entry = tk.Entry(self.text_frame, textvariable=textValue, bg="white", width=20)
                        self.text_note = tk.Label(root, text="* Right click on canvas to paste text", font=italic_font, fg="gray")
                        
                        # Pack buttons
                        self.pen_button.pack(side=tk.LEFT)
                        self.eraser_button.pack(side=tk.LEFT)
                        self.clear_button.pack(side=tk.LEFT)
                        self.color_button.pack(side=tk.LEFT)
                        self.rect_button.pack(side=tk.LEFT)
                        self.circle_button.pack(side=tk.LEFT)
                        self.undo_button.pack(side=tk.LEFT)
                        self.redo_button.pack(side=tk.LEFT)
                        self.zoom_in_button.pack(side=tk.LEFT)
                        self.zoom_out_button.pack(side=tk.LEFT)
                        self.save_button.pack(side=tk.LEFT)
                        self.text_frame.pack(side=tk.LEFT)                         
                        self.text_entry.pack(side=tk.LEFT)
                        self.text_note.pack(side=tk.LEFT)

                        # Bind mouse events
                        self.canvas.bind("<Button-1>", self.start_draw)
                        self.canvas.bind("<B1-Motion>", self.draw_shape)
                        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
                        self.canvas.bind("<Button-2>", self.add_text)
                        self.canvas.bind("<Button-3>", self.add_text)
                        self.canvas.bind("<MouseWheel>", self.zoom)

                        # Initial scroll region
                        self.canvas.config(scrollregion=(0, 0, 1000, 1000))  # Large initial region

                    def add_text(self, event):
                        item = self.canvas.create_text(event.x, event.y, text=textValue.get() or "", fill=self.color)
                        self.save_state()
                        self.redo_stack.clear()
                        print(f"Added text, undo_stack size: {len(self.undo_stack)}")

                    def use_pen(self):
                        self.pen_active = True
                        self.eraser_active = False
                        self.current_shape = None

                    def use_eraser(self):
                        self.pen_active = False
                        self.eraser_active = True
                        self.current_shape = None

                    def choose_color(self):
                        color_tuple = colorchooser.askcolor(title="Choose color")
                        if color_tuple[1]:
                            self.color = color_tuple[1]

                    def create_rectangle(self):
                        self.pen_active = False
                        self.eraser_active = False
                        self.current_shape = "rectangle"

                    def create_arrow(self):
                        self.pen_active = False
                        self.eraser_active = False
                        self.current_shape = "arrow"

                    def start_draw(self, event):
                        self.start_x = event.x
                        self.start_y = event.y
                        if self.pen_active or self.eraser_active:
                            return
                        if self.current_shape == "rectangle":
                            self.current_shape_item = self.canvas.create_rectangle(
                                self.start_x, self.start_y, self.start_x, self.start_y, outline=self.color
                            )
                        elif self.current_shape == "arrow":
                            self.current_shape_item = self.canvas.create_line(
                                self.start_x, self.start_y, self.start_x, self.start_y, fill=self.color, arrow="last", width=5
                            )

                    def draw_shape(self, event):
                        if self.pen_active or self.eraser_active:
                            item = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, 
                                                        fill=self.color if self.pen_active else "white", 
                                                        width=2 if self.pen_active else 10)
                            self.save_state_for_stroke(item)  # Save state for each stroke
                            self.redo_stack.clear()
                            self.start_x, self.start_y = event.x, event.y
                        elif self.current_shape_item:
                            x, y = event.x, event.y
                            self.canvas.coords(self.current_shape_item, self.start_x, self.start_y, x, y)

                    def stop_draw(self, event):
                        if self.current_shape_item or self.pen_active or self.eraser_active:
                            self.save_state()  # Save final state for non-pen/eraser actions
                            self.redo_stack.clear()
                            print(f"Stopped draw, undo_stack size: {len(self.undo_stack)}")
                        self.current_shape_item = None
                        self.pen_active = False
                        self.eraser_active = False

                    def clear_canvas(self):
                        self.save_state()
                        self.canvas.delete("all")
                        self.redo_stack.clear()
                        self.update_scroll_region()
                        print(f"Cleared canvas, undo_stack size: {len(self.undo_stack)}")

                    def save_state(self):
                        items = []
                        for item in self.canvas.find_all():
                            item_type = self.canvas.type(item)
                            coords = self.canvas.coords(item)
                            config = {k: v[-1] for k, v in self.canvas.itemconfig(item).items() if k in ["fill", "outline", "text", "width", "arrow"]}
                            if item_type == "line":
                                items.append(("line", coords, {"fill": config.get("fill", "black"), "width": config.get("width", 2), "arrow": config.get("arrow", "none")}))
                            elif item_type == "rectangle":
                                items.append(("rectangle", coords, {"outline": config.get("outline", "black")}))
                            elif item_type == "text":
                                items.append(("text", coords, {"text": config.get("text", ""), "fill": config.get("fill", "black")}))
                        if items:
                            if len(self.undo_stack) >= self.max_undo:
                                self.undo_stack.pop(0)  # Remove oldest state if limit reached
                            self.undo_stack.append(items)
                        self.update_scroll_region()

                    def save_state_for_stroke(self, item):
                        item_type = self.canvas.type(item)
                        coords = self.canvas.coords(item)
                        config = {k: v[-1] for k, v in self.canvas.itemconfig(item).items() if k in ["fill", "width"]}
                        if item_type == "line" and len(self.undo_stack) < self.max_undo:
                            self.undo_stack.append([("line", coords, {"fill": config.get("fill", "black"), "width": config.get("width", 2)})])
                        self.update_scroll_region()

                    def undo(self):
                        if self.undo_stack:
                            state = self.undo_stack.pop()
                            self.redo_stack.append([(self.canvas.type(item), self.canvas.coords(item), {k: v[-1] for k, v in self.canvas.itemconfig(item).items() if k in ["fill", "outline", "text", "width", "arrow"]}) for item in self.canvas.find_all()])
                            self.canvas.delete("all")
                            for item_type, coords, config in state:
                                if item_type == "line":
                                    self.canvas.create_line(*coords, fill=config["fill"], width=config.get("width", 2), arrow=config.get("arrow", "none"))
                                elif item_type == "rectangle":
                                    self.canvas.create_rectangle(*coords, outline=config["outline"])
                                elif item_type == "text":
                                    self.canvas.create_text(coords[0], coords[1], text=config["text"], fill=config["fill"])
                            self.update_scroll_region()
                            print(f"Undo performed, undo_stack size: {len(self.undo_stack)}, redo_stack size: {len(self.redo_stack)}")

                    def redo(self):
                        if self.redo_stack:
                            state = self.redo_stack.pop()
                            self.undo_stack.append([(self.canvas.type(item), self.canvas.coords(item), {k: v[-1] for k, v in self.canvas.itemconfig(item).items() if k in ["fill", "outline", "text", "width", "arrow"]}) for item in self.canvas.find_all()])
                            self.canvas.delete("all")
                            for item_type, coords, config in state:
                                if item_type == "line":
                                    self.canvas.create_line(*coords, fill=config["fill"], width=config.get("width", 2), arrow=config.get("arrow", "none"))
                                elif item_type == "rectangle":
                                    self.canvas.create_rectangle(*coords, outline=config["outline"])
                                elif item_type == "text":
                                    self.canvas.create_text(coords[0], coords[1], text=config["text"], fill=config["fill"])
                            self.update_scroll_region()
                            print(f"Redo performed, undo_stack size: {len(self.undo_stack)}, redo_stack size: {len(self.redo_stack)}")

                    def zoom_in(self):
                        self.zoom_level *= 1.2
                        self.canvas.scale("all", self.canvas.canvasx(0), self.canvas.canvasy(0), 1.2, 1.2)
                        self.update_scroll_region()

                    def zoom_out(self):
                        self.zoom_level /= 1.2
                        if self.zoom_level > 0.1:
                            self.canvas.scale("all", self.canvas.canvasx(0), self.canvas.canvasy(0), 1/1.2, 1/1.2)
                            self.update_scroll_region()

                    def zoom(self, event):
                        if event.delta > 0:
                            self.zoom_in()
                        else:
                            self.zoom_out()

                    def save_canvas(self):
                        global tree_file_path
                        # Get the canvas coordinates on screen
                        self.canvas.update()  # Make sure the canvas is up-to-date
                        x = self.canvas.winfo_rootx()
                        y = self.canvas.winfo_rooty()
                        x1 = x + self.canvas.winfo_width()
                        y1 = y + self.canvas.winfo_height()
                    
                        # Grab the canvas area from the screen
                        image = ImageGrab.grab(bbox=(x, y, x1, y1))

                        image_filename = "page4_plot.png"
                        image.save(image_filename)
                    
                        # Ask for file path to save
                        tree_file_path = tk.filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
                        if tree_file_path:
                            image.save(tree_file_path)
                            messagebox.showinfo("Saved", f"Canvas saved as {os.path.basename(tree_file_path)}")

                    def update_scroll_region(self):
                        region = self.canvas.bbox("all")
                        if region:
                            self.canvas.config(scrollregion=region)
                        else:
                            self.canvas.config(scrollregion=(0, 0, 1000, 1000))

                app = ShapeEditorApp(analysis)

                page_5()

        def back_3():
            global pageNumber
            pageNumber -= 1
            print(pageNumber)
            frame4.destroy() 
            frame4.forget() 
            btnBack3.destroy()
            btnNext3.destroy() 
            page_3()
        
        def next_3():
            global pageNumber
            pageNumber += 1
            print(pageNumber)
            frame4.destroy()
            frame4.forget()
            progress_label.destroy()
            btnBack3.destroy()
            btnNext3.destroy() 
            analyses()


        btnBack3 = Button(mainProject, text = "Back", font=("Calibri", 10), width=int(10*(wth/1920)), command = lambda: back_3())
        btnNext3 = Button(mainProject, text = "Next", font=("Calibri", 10), width=int(10*(wth/1920)), command = lambda: next_3())
        btnBack3.place(x=190, y=170)
        btnNext3.place(x=380, y=170)

    def page_5(): 
        global p5rootcause, p5existingpolicies, p5relevantprov, p5accomplishments, p5assessments  
        mainProject.state('zoomed')
        style.configure('Treeview', rowheight=240)

        ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 5 of 15: Root Cause", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        frame5 = tk.LabelFrame(mainProject)

        status = ttk.Label(mainProject, text="")
        status.place(x=10, y=700)
        
        rootCauseLabel = Label(frame5, text = "Root Cause of the Problem")
        rootCause = Entry(frame5, width=int(200))

        rootCause.insert(0, p5rootcause)

        assessmentLabel = Label(frame5, text = "Assessment of Existing Policies that Address the Root Cause")
        assessmentTable=ttk.Treeview(frame5, selectmode="browse", height=2)
        assessmentTable["columns"]=("1","2","3","4")
        assessmentTable['show']='headings'
        assessmentTable.column("1",width=int(350),anchor='c')
        assessmentTable.column("2",width=int(700),anchor='c')
        assessmentTable.column("3",width=int(445),anchor='c')
        assessmentTable.column("4",width=int(395),anchor='c')
        assessmentTable.heading("1",text="Existing Policy")
        assessmentTable.heading("2",text="Relevant Provision(s)")
        assessmentTable.heading("3",text="Accomplishments")
        assessmentTable.heading("4",text="Assessment")

        existLabel = Label(mainProject, text = "Existing Policy")
        releLabel = Label(mainProject, text = "Relevant Provision")
        accompLabel2 = Label(mainProject, text = "Accomplishment")
        assessLabel2 = Label(mainProject, text = "Assessment")

        existingPolicy = scrolledtext.ScrolledText(mainProject, font=("Consolas", 10), height = 9, width= 40)
        relevantProvision = scrolledtext.ScrolledText(mainProject, font=("Consolas", 10), height = 9, width= 40)
        accomplishment2 = scrolledtext.ScrolledText(mainProject, font=("Consolas", 10), height = 9, width= 40)
        assessment2 = scrolledtext.ScrolledText(mainProject, font=("Consolas", 10), height = 9, width= 40)

        addButton2 = tk.Button(mainProject, text='Add', width=10, command=lambda: add_data2())  
        editButton2 = tk.Button(mainProject, text="Edit", width=10, command=lambda: edit_data2())

        if len(p5existingpolicies) == len(p5relevantprov) == len(p5accomplishments) == len(p5assessments):
            if not assessmentTable.get_children():
                if len(p5existingpolicies) == len(p5relevantprov) == len(p5accomplishments) == len(p5assessments):
                    for ep, rp, ac, asmt in zip(p5existingpolicies, p5relevantprov, p5accomplishments, p5assessments):
                        assessmentTable.insert("", "end", values=(
                            wrap(ep.strip()),
                            wrap(rp.strip()),
                            wrap(ac.strip()),
                            wrap(asmt.strip())
                        ))

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
            existingPolicyText = existingPolicy.get("1.0", tk.END).strip()
            relevantProvisionText = relevantProvision.get("1.0", tk.END).strip()
            accomplishment2Text = accomplishment2.get("1.0", tk.END).strip()
            assessment2Text = assessment2.get("1.0", tk.END).strip()

            if not (existingPolicyText and relevantProvisionText and accomplishment2Text and assessment2Text):
                messagebox.showerror("Error", "Please fill out all fields before editing.")
                return

            selected = assessmentTable.selection()
            if not selected:
                messagebox.showwarning("Warning", "No entry selected for editing.")
                return

            item_id = selected[0]
            index = assessmentTable.index(item_id)  # Find index in table (same as list index)

            # Update the table row
            assessmentTable.item(item_id, values=(
                wrap(existingPolicyText),
                wrap(relevantProvisionText),
                wrap(accomplishment2Text),
                wrap(assessment2Text)
            ))

            # Update the global lists
            p5existingpolicies[index] = existingPolicyText
            p5relevantprov[index] = relevantProvisionText
            p5accomplishments[index] = accomplishment2Text
            p5assessments[index] = assessment2Text

            # Clear text fields after editing
            existingPolicy.delete("1.0", tk.END)
            relevantProvision.delete("1.0", tk.END)
            accomplishment2.delete("1.0", tk.END)
            assessment2.delete("1.0", tk.END)
            existingPolicy.focus()
            save()

        def add_data2():
            existingPolicyText = existingPolicy.get("1.0", tk.END)               # read existing policy
            relevantProvisionText = relevantProvision.get("1.0", tk.END)         # read relevant provision
            accomplishment2Text = accomplishment2.get("1.0", tk.END)             # read accomplishment 
            assessment2Text = assessment2.get("1.0", tk.END)                     # read assessment      

            p5existingpolicies.append(existingPolicyText)
            p5relevantprov.append(relevantProvisionText)
            p5accomplishments.append(accomplishment2Text)
            p5assessments.append(assessment2Text)

            assessmentTable.insert("", 'end', values=(
                wrap(existingPolicyText),
                wrap(relevantProvisionText),
                wrap(accomplishment2Text),
                wrap(assessment2Text)
            ))

            existingPolicy.delete('1.0', END)
            relevantProvision.delete('1.0', END)
            accomplishment2.delete('1.0', END)
            assessment2.delete('1.0', END)
            existingPolicy.focus()
            save()

        frame5.place(x=10, y=10)
        rootCauseLabel.grid(row=0, column=1)
        rootCause.grid(row=1, column=1)
        assessmentLabel.grid(row=2, column=1)
        assessmentTable.grid(row=3, column=1)
        existLabel.place(x=150, y=750)
        existingPolicy.place(x=40, y=780)
        releLabel.place(x=520, y=750)
        relevantProvision.place(x=410, y=780)
        accompLabel2.place(x=900, y=750)
        accomplishment2.place(x=780, y=780)
        assessLabel2.place(x=1280, y=750)
        assessment2.place(x=1150, y=780)
        addButton2.place(x=1600, y=800)
        editButton2.place(x=1750, y=800)

        

        def back_4():
            global pageNumber
            pageNumber -= 1
            print(pageNumber)
            mainProject.state('normal')
            frame5.destroy() 
            existLabel.destroy()
            existingPolicy.destroy()
            existingPolicy.place_forget()
            releLabel.destroy()
            relevantProvision.destroy()
            relevantProvision.place_forget()
            accompLabel2.destroy()
            accomplishment2.destroy()
            accomplishment2.place_forget()
            assessLabel2.destroy()
            assessment2.destroy()
            assessment2.place_forget()
            btnBack4.destroy()
            btnNext4.destroy() 
            addButton2.destroy()
            editButton2.destroy()
            save()
            page_4()
            

        def next_4():
            global pageNumber
            pageNumber += 1
            print(pageNumber)
            global p5rootcause
            p5rootcause = rootCause.get()
            if not p5rootcause.strip():
                status.config(
                    text="Enter root cause",
                    foreground="red",
                )
                return
            
            mainProject.state('normal')
            frame5.destroy() 
            existLabel.destroy()
            existingPolicy.destroy()
            existingPolicy.place_forget()
            releLabel.destroy()
            relevantProvision.destroy()
            relevantProvision.place_forget()
            accompLabel2.destroy()
            accomplishment2.destroy()
            accomplishment2.place_forget()
            assessLabel2.destroy()
            assessment2.destroy()
            assessment2.place_forget()
            btnBack4.destroy()
            btnNext4.destroy() 
            addButton2.destroy()
            editButton2.destroy()
            save()
            page_6()

        btnBack4 = Button(mainProject, text = "Back", width=10, command = lambda: back_4())
        btnNext4 = Button(mainProject, text = "Next", width=10, command = lambda: next_4())
        btnBack4.place(x=1600, y=900)
        btnNext4.place(x=1750, y=900)
        status.place(x=10, y=700)

    def page_6():                                               # write problematic situation and undesirable effects

        global p6policyproblem, p6policyissue

        mainProject.state('normal')
        mainProject.geometry("660x220")

        style.configure('Treeview', rowheight=320)

        ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 6 of 15: Policy Problem and Issue Statement", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        frame6 = tk.LabelFrame(mainProject)

        status = ttk.Label(mainProject, text="")
        status.place(x=10, y=700)

        policyProbLabel = Label(frame6, text = "Policy Problem")
        policyProb = scrolledtext.ScrolledText(frame6, height=8, width=30)
        
        policyIssueLabel = Label(frame6, text = "Policy Issue Statement")
        policyIss = scrolledtext.ScrolledText(frame6, height=8, width=30)
        
        frame6.place(x=40, y=10)
        status.place(x=10, y=170)
        policyProbLabel.grid(row=1, column=0, sticky = W, padx=7)
        policyProb.grid(row=2, column=0, sticky = W, padx=7)
        policyIssueLabel.grid(row=1, column=1, sticky = W, padx=7)
        policyIss.grid(row=2, column=1, sticky = W, padx=7)

        policyProb.insert("1.0", p6policyproblem)
        policyIss.insert("1.0", p6policyissue)

        def back_5():
            global pageNumber
            pageNumber -= 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            save()
            page_5()

        def next_5():
            global pageNumber, p6policyissue, p6policyproblem
            p6policyproblem = policyProb.get("1.0", tk.END)
            if not p6policyproblem.strip():
                status.config(
                text="Enter policy\nproblem",
                foreground="red",
            )
                return
                    
            p6policyissue = policyIss.get("1.0", tk.END)
            if not p6policyissue.strip():
                status.config(
                text="Enter policy\nissue statement",
                foreground="red",
            )
                return
            pageNumber += 1
            print(pageNumber)
            frame6.destroy() 
            btnBack5.destroy()
            btnNext5.destroy() 
            save()
            page_7()

        btnBack5 = Button(mainProject, text = "Back", width=10, command = lambda: back_5())
        btnNext5 = Button(mainProject, text = "Next", width=10, command = lambda: next_5())
        btnBack5.place(x=140, y=170)
        btnNext5.place(x=400, y=170)


    def page_7():
        global p7policyGoalsandObjectives, p7indicators

        mainProject.geometry("900x600")
        style.configure('Treeview', rowheight=40)

        # Main container
        frame7 = tk.LabelFrame(mainProject, text="Goals and Objectives of the Proposal", font=("Arial", int(12*(wth/1920)), "bold"))
        frame7.pack(padx=20, pady=20, fill="both")

        status = ttk.Label(mainProject, text="")
        status.place(relx=0.02, rely=0.92)

        # Treeview
        goals_and_obj_table = ttk.Treeview(frame7, selectmode="browse", height=5)
        goals_and_obj_table["columns"] = ("1", "2")
        goals_and_obj_table['show'] = 'headings'
        goals_and_obj_table.column("1", width=350, anchor='c')
        goals_and_obj_table.column("2", width=500, anchor='c')
        goals_and_obj_table.heading("1", text="Policy Goals and Objectives")
        goals_and_obj_table.heading("2", text="Indicators")

        sb_y = ttk.Scrollbar(frame7, orient="vertical", command=goals_and_obj_table.yview)
        sb_x = ttk.Scrollbar(frame7, orient="horizontal", command=goals_and_obj_table.xview)
        goals_and_obj_table.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)

        goals_and_obj_table.grid(row=1, column=0, sticky="nsew")
        sb_y.grid(row=1, column=1, sticky="ns")
        sb_x.grid(row=2, column=0, sticky="ew")

        frame7.grid_rowconfigure(1, weight=1)
        frame7.grid_columnconfigure(0, weight=1)

        # Input section
        pgo_label = tk.Label(mainProject, text="Policy Goals and Objectives")
        indi_label = tk.Label(mainProject, text="Indicators")
        pgo = tk.Entry(mainProject, width=40)
        indi = scrolledtext.ScrolledText(mainProject, height=3, width=55)
        add_button = ttk.Button(mainProject, text="Add", command=lambda: add_data3())
        edit_button = ttk.Button(mainProject, text="Edit", state="disabled", command=lambda: edit_data3())
        delete_button = ttk.Button(mainProject, text="Delete", state="disabled", command=lambda: delete_data3())
        ToolTip(add_button, "Add a new entry to the table")
        ToolTip(edit_button, "Edit the selected table entry")
        ToolTip(delete_button, "Delete the selected table entry")

        pgo_label.place(relx=0.1, rely=0.5)
        pgo.place(relx=0.05, rely=0.55)
        indi_label.place(relx=0.55, rely=0.5)
        indi.place(relx=0.45, rely=0.55)
        add_button.place(relx=0.35, rely=0.75, anchor="s")
        edit_button.place(relx=0.5, rely=0.75, anchor="s")
        delete_button.place(relx=0.65, rely=0.75, anchor="s")

        # Populate table
        if len(p7policyGoalsandObjectives) == len(p7indicators):
            for goal, indicator in zip(p7policyGoalsandObjectives, p7indicators):
                goals_and_obj_table.insert("", "end", values=(goal.strip(), indicator.strip()))

        undo_stack = []

        def show_data3(a):
            pgo.delete(0, tk.END)
            indi.delete("1.0", tk.END)
            selected_item = goals_and_obj_table.selection()
            if selected_item:
                edit_button.config(state="normal")
                delete_button.config(state="normal")
                values = goals_and_obj_table.item(selected_item[0])['values']
                pgo.insert(0, values[0])
                indi.insert("1.0", values[1])
            else:
                edit_button.config(state="disabled")
                delete_button.config(state="disabled")

        def add_data3():
            pgo_text = pgo.get().strip()
            indi_text = indi.get("1.0", tk.END).strip()
            if not (pgo_text and indi_text):
                messagebox.showerror("Error", "Please fill out all fields")
                return
            item_id = goals_and_obj_table.insert("", 'end', values=(pgo_text, indi_text))
            undo_stack.append(("add", item_id))
            p7policyGoalsandObjectives.append(pgo_text)
            p7indicators.append(indi_text)
            pgo.delete(0, tk.END)
            indi.delete("1.0", tk.END)
            pgo.focus()

        def edit_data3():
            pgo_text = pgo.get().strip()
            indi_text = indi.get("1.0", tk.END).strip()
            if not (pgo_text and indi_text):
                messagebox.showerror("Error", "Please fill out all fields")
                return
            selected_item = goals_and_obj_table.selection()[0]
            old_values = goals_and_obj_table.item(selected_item)['values']
            undo_stack.append(("edit", selected_item, old_values))
            goals_and_obj_table.item(selected_item, values=(pgo_text, indi_text))
            index = goals_and_obj_table.index(selected_item)
            p7policyGoalsandObjectives[index] = pgo_text
            p7indicators[index] = indi_text

        def delete_data3():
            selected_item = goals_and_obj_table.selection()
            if selected_item:
                item_id = selected_item[0]
                index = goals_and_obj_table.index(item_id)
                old_values = goals_and_obj_table.item(item_id)['values']
                undo_stack.append(("delete", item_id, old_values, index))
                goals_and_obj_table.delete(item_id)
                p7policyGoalsandObjectives.pop(index)
                p7indicators.pop(index)
                pgo.delete(0, tk.END)
                indi.delete("1.0", tk.END)
                edit_button.config(state="disabled")
                delete_button.config(state="disabled")
            else:
                messagebox.showwarning("Warning", "Please select an item to delete")

        def undo():
            if not undo_stack:
                return
            action, *data = undo_stack.pop()
            if action == "add":
                goals_and_obj_table.delete(data[0])
                p7policyGoalsandObjectives.pop()
                p7indicators.pop()
            elif action == "edit":
                item_id, old_values = data
                goals_and_obj_table.item(item_id, values=old_values)
                index = goals_and_obj_table.index(item_id)
                p7policyGoalsandObjectives[index] = old_values[0]
                p7indicators[index] = old_values[1]
            elif action == "delete":
                item_id, old_values, index = data
                goals_and_obj_table.insert("", index, iid=item_id, values=old_values)
                p7policyGoalsandObjectives.insert(index, old_values[0])
                p7indicators.insert(index, old_values[1])

        goals_and_obj_table.bind("<<TreeviewSelect>>", show_data3)
        mainProject.bind("<Control-z>", lambda e: undo())
        mainProject.bind("<Control-Return>", lambda e: add_data3())
        pgo.bind("<Tab>", lambda e: indi.focus_set())
        indi.bind("<Tab>", lambda e: add_button.focus_set())

        def back_6():
            global pageNumber
            save()
            pageNumber -= 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            page_6()

        def next_6():
            global pageNumber
            save()
            pageNumber += 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            page_8()

        btnBack6 = Button(mainProject, text="Back", width=10, command=back_6)
        btnNext6 = Button(mainProject, text="Next", width=10, command=next_6)
        btnBack6.place(relx=0.35, rely=0.85, anchor="s")
        btnNext6.place(relx=0.65, rely=0.85, anchor="s")

        ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 7 of 15: Goals and Objectives of the Proposal", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")


    def page_8():

        global p8stakeholders, p8actors
        mainProject.state('normal') 
        mainProject.geometry("800x700")
        frame8 = tk.LabelFrame(mainProject, text="Stakeholders and Actors", font=("Arial", 12, "bold"))
        undo_stack = []

        ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 8 of 15: Stakeholders and Actors", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")


        style.configure("TButton", font=("Arial", 10))

        # Place frame
        frame8.place(x=40, y=10)

        # Table
        sta_and_act_table = ttk.Treeview(frame8, selectmode="browse", height=10)
        sta_and_act_table["columns"] = ("1", "2")
        sta_and_act_table['show'] = 'headings'
        sta_and_act_table.column("1", width=350, anchor='c')
        sta_and_act_table.column("2", width=350, anchor='c')
        sta_and_act_table.heading("1", text="Stakeholders")
        sta_and_act_table.heading("2", text="Actors")
        sb_y = ttk.Scrollbar(frame8, orient="vertical", command=sta_and_act_table.yview)
        sta_and_act_table.configure(yscrollcommand=sb_y.set)
        sta_and_act_table.grid(row=0, column=0, sticky="nsew")
        sb_y.grid(row=0, column=1, sticky="ns")

        # Load existing data into table
        if len(p8stakeholders) == len(p8actors):
            for s, a in zip(p8stakeholders, p8actors):
                sta_and_act_table.insert("", "end", values=(s.strip(), a.strip()))

        # Input Fields
        stakeholders_label = tk.Label(mainProject, text="Stakeholder:")
        stakeholders_label.place(x=60, y=500)
        stakeholders = tk.Entry(mainProject, width=35)
        stakeholders.place(x=170, y=500)

        actors_label = tk.Label(mainProject, text="Actor:")
        actors_label.place(x=480, y=500)
        actors = tk.Entry(mainProject, width=35)
        actors.place(x=540, y=500)

        # Buttons
        add_button = ttk.Button(mainProject, text="Add", command=lambda: add_data4())
        edit_button = ttk.Button(mainProject, text="Edit", state="disabled", command=lambda: edit_data4())
        delete_button = ttk.Button(mainProject, text="Delete", state="disabled", command=lambda: delete_data4())
        btnBack8 = ttk.Button(mainProject, text="Back", command=lambda: back_7())
        btnNext8 = ttk.Button(mainProject, text="Next", command=lambda: next_7())

        add_button.place(x=250, y=550)
        edit_button.place(x=370, y=550)
        delete_button.place(x=490, y=550)
        btnBack8.place(x=250, y=600)
        btnNext8.place(x=490, y=600)

        # Table selection
        def show_data4(a):
            stakeholders.delete(0, tk.END)
            actors.delete(0, tk.END)
            selected_item = sta_and_act_table.selection()
            if selected_item:
                edit_button.config(state="normal")
                delete_button.config(state="normal")
                values = sta_and_act_table.item(selected_item[0])['values']
                stakeholders.insert(0, values[0])
                actors.insert(0, values[1])
            else:
                edit_button.config(state="disabled")
                delete_button.config(state="disabled")

        sta_and_act_table.bind("<<TreeviewSelect>>", show_data4)

        # Data logic
        def add_data4():
            stakeholders_text = stakeholders.get().strip()
            actors_text = actors.get().strip()
            if not (stakeholders_text and actors_text):
                messagebox.showerror("Error", "Please fill out all fields")
                return
            item_id = sta_and_act_table.insert("", 'end', values=(stakeholders_text, actors_text))
            undo_stack.append(("add", item_id))
            p8stakeholders.append(stakeholders_text)
            p8actors.append(actors_text)
            stakeholders.delete(0, tk.END)
            actors.delete(0, tk.END)
            stakeholders.focus()

        def edit_data4():
            stakeholders_text = stakeholders.get().strip()
            actors_text = actors.get().strip()
            if not (stakeholders_text and actors_text):
                messagebox.showerror("Error", "Please fill out all fields")
                return
            selected_item = sta_and_act_table.selection()[0]
            old_values = sta_and_act_table.item(selected_item)['values']
            undo_stack.append(("edit", selected_item, old_values))
            sta_and_act_table.item(selected_item, values=(stakeholders_text, actors_text))
            index = sta_and_act_table.index(selected_item)
            p8stakeholders[index] = stakeholders_text
            p8actors[index] = actors_text

        def delete_data4():
            selected_item = sta_and_act_table.selection()
            if selected_item:
                item_id = selected_item[0]
                index = sta_and_act_table.index(item_id)
                old_values = sta_and_act_table.item(item_id)['values']
                undo_stack.append(("delete", item_id, old_values, index))
                sta_and_act_table.delete(item_id)
                p8stakeholders.pop(index)
                p8actors.pop(index)
                stakeholders.delete(0, tk.END)
                actors.delete(0, tk.END)
                edit_button.config(state="disabled")
                delete_button.config(state="disabled")
            else:
                messagebox.showwarning("Warning", "Please select an item to delete")

        def undo():
            if not undo_stack:
                return
            action, *data = undo_stack.pop()
            if action == "add":
                sta_and_act_table.delete(data[0])
                p8stakeholders.pop()
                p8actors.pop()
            elif action == "edit":
                item_id, old_values = data
                sta_and_act_table.item(item_id, values=old_values)
                index = sta_and_act_table.index(item_id)
                p8stakeholders[index] = old_values[0]
                p8actors[index] = old_values[1]
            elif action == "delete":
                item_id, old_values, index = data
                sta_and_act_table.insert("", index, iid=item_id, values=old_values)
                p8stakeholders.insert(index, old_values[0])
                p8actors.insert(index, old_values[1])

        # Navigation
        def back_7():
            global pageNumber
            pageNumber -= 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            save()
            page_7()

        def next_7():
            global pageNumber
            pageNumber += 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            save()
            page_9()

        mainProject.bind("<Control-z>", lambda e: undo())
        mainProject.bind("<Control-Return>", lambda e: add_data4())
        stakeholders.bind("<Tab>", lambda e: actors.focus_set())
        actors.bind("<Tab>", lambda e: add_button.focus_set())

    def page_9():   
        global p9alternatives, p9altnum
        mainProject.state('normal') 
        mainProject.geometry("870x545")

        ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 9 of 15: Assessment of the Policy Alternatives", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw") 

        style.configure('Treeview', rowheight=15)

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

        assessAlterTable=ttk.Treeview(frame9, height=10)
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
            selected_item = assessAlterTable.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "Please select an entry to edit.")
                return

            policyAlternativeNoText = policyAlternativeNo.get().strip()
            policyAlternativesText = policyAlternatives.get().strip()

            if not (policyAlternativeNoText and policyAlternativesText):
                messagebox.showerror("Error", "Please fill out both fields.")
                return

            item_id = selected_item[0]
            index = assessAlterTable.index(item_id)

            # Update Treeview row
            assessAlterTable.item(item_id, values=(policyAlternativeNoText, policyAlternativesText))

            # Update in-memory lists
            p9altnum[index] = policyAlternativeNoText
            p9alternatives[index] = policyAlternativesText

            # Clear fields
            policyAlternativeNo.delete(0, END)
            policyAlternatives.delete(0, END)
            policyAlternativeNo.focus()

            save()


        def add_data5():
            policyAlternativeNoText = policyAlternativeNo.get().strip()
            policyAlternativesText = policyAlternatives.get().strip()

            if not (policyAlternativeNoText and policyAlternativesText):
                messagebox.showerror("Error", "Please fill out both fields.")
                return

            # Append to lists
            p9altnum.append(policyAlternativeNoText)
            p9alternatives.append(policyAlternativesText)

            # Add to table
            assessAlterTable.insert("", 'end', values=(policyAlternativeNoText, policyAlternativesText))

            # Clear input fields
            policyAlternativeNo.delete(0, END)
            policyAlternatives.delete(0, END)
            policyAlternativeNo.focus()

            save()


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

        polAltNoLabel.place(x=135, y=300)
        policyAlternativeNo.place(x=135, y=330)
        polAltLabel.place(x=520, y=300)
        policyAlternatives.place(x=420, y=330)
        addButton5.place(x=265, y=400)
        editButton5.place(x=550, y=400)
        computeButton.place(x=590, y=250)

        varEffec = IntVar(value=0)
        varCostEff = IntVar(value=0)
        varAccept = IntVar(value=0)
    
        R1_2 = Radiobutton(frame9, text="SLR", variable=varEffec, value=1)
        R2_2 = Radiobutton(frame9, text="MR", variable=varEffec, value=2)
        R3_2 = Radiobutton(frame9, text="LogR", variable=varEffec, value=3)
        R4_2 = Radiobutton(frame9, text="FGD", variable=varEffec, value=4)
        R5_2 = Radiobutton(frame9, text="Tangible Cost-Benefit Analysis\nw/ Discounting", variable=varCostEff, value=1)
        R6_2 = Radiobutton(frame9, text="Tangible Cost-Benefit Analysis\nw/o Discounting", variable=varCostEff, value=2)
        R7_2 = Radiobutton(frame9, text="Intangible Cost-Benefit Analysis", variable=varCostEff, value=3)
        R8_2 = Radiobutton(frame9, text="PRINCE Method", variable=varAccept, value=1)
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

        if len(p9altnum) == len(p9alternatives):
            for num, alt in zip(p9altnum, p9alternatives):
                assessAlterTable.insert("", "end", values=(num.strip(), alt.strip()))

        def back_8():
            global pageNumber
            pageNumber -= 1
            print(pageNumber)
            frame9.destroy()       
            polAltLabel.destroy()
            policyAlternatives.destroy()
            polAltNoLabel.destroy()
            policyAlternativeNo.destroy()
            addButton5.destroy()
            editButton5.destroy()   
            computeButton.destroy()   
            btnBack8.destroy()
            btnNext8.destroy()
            save()
            page_8()

        def next_8():
            frame9.destroy()       
            polAltLabel.destroy()
            policyAlternatives.destroy()
            polAltNoLabel.destroy()
            policyAlternativeNo.destroy()
            addButton5.destroy()
            editButton5.destroy()   
            computeButton.destroy()   
            btnBack8.destroy()
            btnNext8.destroy()
            save()
            page_10()

        def compute():
            print(p9alternatives)
            netBenefitWithout = []
            netBenefitWith = []
            
            crite = [int(varEffec.get()), int(varCostEff.get()), int(varAccept.get())]
            print(crite)

            if int(varEffec.get()) == 1: 
                def windowPerAlt(a, policyAlt):
                    effectiveness1 = Toplevel(main)
                    effectiveness1.title("Effectiveness: Simple LR")
                    effectiveness1.geometry("830x480")
                    
                    equation = "y = "+str(coefficientLR)+"x + "+str(interceptLR)+"\n"
                    equationWithLabel = Label(effectiveness1, text="\nEquation  :  "+equation, font="Consolas", justify="left")
                    equationWithLabel.pack()

                    simpleLRLabel = Label(effectiveness1, text = "Alternative " + str(a+1) + " - " + policyAlt)
                    simpleLRTable=ttk.Treeview(effectiveness1)
                    simpleLRTable["columns"]=("1","2","3")
                    simpleLRTable['show']='headings'
                    simpleLRTable.column("1",width=130,anchor='c')
                    simpleLRTable.column("2",width=130,anchor='c')
                    simpleLRTable.column("3",width=130,anchor='c')
                    simpleLRTable.heading("1",text="Year")
                    simpleLRTable.heading("2",text="X")
                    simpleLRTable.heading("3",text="Y")

                    yearLabel = Label(effectiveness1, text = "Year")
                    inputXLabel = Label(effectiveness1, text = "X")

                    year = tk.Entry(effectiveness1, width=30)
                    inputX = tk.Entry(effectiveness1, width=30) 

                    addButton = tk.Button(effectiveness1, text='Add', width=10, command=lambda: add_data())  
                    editButton = tk.Button(effectiveness1, text="Edit", width=10, command=lambda: edit_data())

                    years = []

                    def show_data(a):
                        year.delete(0,END)
                        inputX.delete(0,END)

                        selectedItem = simpleLRTable.selection()[0]
                        year.insert(0, simpleLRTable.item(selectedItem)['values'][0])
                        inputX.insert(0, simpleLRTable.item(selectedItem)['values'][1])

                    simpleLRTable.bind("<<TreeviewSelect>>", show_data)    

                    am = 0
                    def edit_data():
                        yearText = year.get()                                   # get year

                        selected_item = simpleLRTable.selection()[0]

                        years.pop(simpleLRTable.index(selected_item))
                        years.insert(simpleLRTable.index(selected_item), int(yearText))

                        inputXText = float(inputX.get())                                                    # get X
                        outputYText = float(inputX.get())*float(coefficientLR) + float(interceptLR)         # compute for Y
                        
                        simpleLRTable.item(selected_item, text="blub", values=(yearText, inputXText, outputYText))

                    def add_data():
                        yearText = year.get()                                   # get year
                        inputXText = int(inputX.get())                        # get benefit
                        outputYText = float(inputX.get())*float(coefficientLR) + float(interceptLR)         # compute for Y

                        years.append(int(yearText))

                        year.delete(0,END)
                        inputX.delete(0,END)

                        global assessmentTuple
                        assessmentTuple = [yearText, inputXText, outputYText]

                        # effortList.append(efforttuple)

                        simpleLRTable.insert("",'end', values=(yearText, inputXText, outputYText))
                        yearText.delete('1.0',END)                      # reset the text entry box
                        inputX.delete('1.0',END)                        # reset the text entry box
                        yearText.focus() 
                    
                    simpleLRLabel.pack()
                    simpleLRTable.pack()
                    yearLabel.place(x=210, y=360)
                    year.place(x=300, y=360)
                    inputXLabel.place(x=210, y=420)
                    inputX.place(x=300, y=420)
                    addButton.place(x=540, y=360)
                    editButton.place(x=540, y=420)

                a = 0

                while (a < len(p9alternatives)):
                    windowPerAlt(a, p9alternatives[a])
                    a += 1

            elif int(varEffec.get()) == 2: 
                def window1PerAlt(a, policyAlt):
                    effectivenessMR1 = Toplevel(main)
                    effectivenessMR1.title("Effectiveness: MR1")
                    effectivenessMR1.geometry("830x480")
                    
                    equation = "y = "+str(coefficientMR1)+"x + "+str(interceptMR1)+"\n"
                    equationWithLabel = Label(effectivenessMR1, text="\nEquation  :  "+equation, font="Consolas", justify="left")
                    equationWithLabel.pack()

                    MR1Label = Label(effectivenessMR1, text = "Alternative " + str(a+1) + " - " + policyAlt)
                    MR1Table=ttk.Treeview(effectivenessMR1)
                    MR1Table["columns"]=("1","2","3")
                    MR1Table['show']='headings'
                    MR1Table.column("1",width=130,anchor='c')
                    MR1Table.column("2",width=130,anchor='c')
                    MR1Table.column("3",width=130,anchor='c')
                    MR1Table.heading("1",text="Year")
                    MR1Table.heading("2",text="X")
                    MR1Table.heading("3",text="Y")

                    yearLabel = Label(effectivenessMR1, text = "Year")
                    inputXLabel = Label(effectivenessMR1, text = "X")

                    year = tk.Entry(effectivenessMR1, width=30)
                    inputX = tk.Entry(effectivenessMR1, width=30) 

                    addButton = tk.Button(effectivenessMR1, text='Add', width=10, command=lambda: add_data())  
                    editButton = tk.Button(effectivenessMR1, text="Edit", width=10, command=lambda: edit_data())

                    years = []

                    def show_data(a):
                        year.delete(0,END)
                        inputX.delete(0,END)

                        selectedItem = MR1Table.selection()[0]
                        year.insert(0, MR1Table.item(selectedItem)['values'][0])
                        inputX.insert(0, MR1Table.item(selectedItem)['values'][1])

                    MR1Table.bind("<<TreeviewSelect>>", show_data)    

                    am = 0
                    def edit_data():
                        yearText = year.get()                                   # get year

                        selected_item = MR1Table.selection()[0]

                        years.pop(MR1Table.index(selected_item))
                        years.insert(MR1Table.index(selected_item), int(yearText))

                        inputXText = float(inputX.get())                                                    # get X
                        outputYText = float(inputX.get())*float(coefficientMR1) + float(interceptMR1)         # compute for Y
                        
                        MR1Table.item(selected_item, text="blub", values=(yearText, inputXText, outputYText))

                    def add_data():
                        yearText = year.get()                                   # get year
                        inputXText = int(inputX.get())                        # get benefit
                        outputYText = float(inputX.get())*float(coefficientMR1) + float(interceptMR2)         # compute for Y

                        years.append(int(yearText))

                        year.delete(0,END)
                        inputX.delete(0,END)

                        global assessmentTuple
                        assessmentTuple = [yearText, inputXText, outputYText]

                        # effortList.append(efforttuple)

                        MR1Table.insert("",'end', values=(yearText, inputXText, outputYText))
                        yearText.delete('1.0',END)                      # reset the text entry box
                        inputX.delete('1.0',END)                        # reset the text entry box
                        yearText.focus() 
                    
                    MR1Label.pack()
                    MR1Table.pack()
                    yearLabel.place(x=210, y=360)
                    year.place(x=300, y=360)
                    inputXLabel.place(x=210, y=420)
                    inputX.place(x=300, y=420)
                    addButton.place(x=540, y=360)
                    editButton.place(x=540, y=420)

                def window2PerAlt(a, policyAlt):
                    effectivenessMR2 = Toplevel(main)
                    effectivenessMR2.title("Effectiveness: MR2")
                    effectivenessMR2.geometry("830x480")
                    
                    equation = "y = "+str(coefficientMR2)+"x + "+str(interceptMR2)+"\n"
                    equationWithLabel = Label(effectivenessMR2, text="\nEquation  :  "+equation, font="Consolas", justify="left")
                    equationWithLabel.pack()

                    MR2Label = Label(effectivenessMR2, text = "Alternative " + str(a+1) + " - " + policyAlt)
                    MR2Table=ttk.Treeview(effectivenessMR2)
                    MR2Table["columns"]=("1","2","3")
                    MR2Table['show']='headings'
                    MR2Table.column("1",width=130,anchor='c')
                    MR2Table.column("2",width=130,anchor='c')
                    MR2Table.column("3",width=130,anchor='c')
                    MR2Table.heading("1",text="Year")
                    MR2Table.heading("2",text="X")
                    MR2Table.heading("3",text="Y")

                    yearLabel = Label(effectivenessMR2, text = "Year")
                    inputXLabel = Label(effectivenessMR2, text = "X")

                    year = tk.Entry(effectivenessMR2, width=30)
                    inputX = tk.Entry(effectivenessMR2, width=30) 

                    addButton = tk.Button(effectivenessMR2, text='Add', width=10, command=lambda: add_data())  
                    editButton = tk.Button(effectivenessMR2, text="Edit", width=10, command=lambda: edit_data())

                    years = []

                    def show_data(a):
                        year.delete(0,END)
                        inputX.delete(0,END)

                        selectedItem = MR2Table.selection()[0]
                        year.insert(0, MR2Table.item(selectedItem)['values'][0])
                        inputX.insert(0, MR2Table.item(selectedItem)['values'][1])

                    MR2Table.bind("<<TreeviewSelect>>", show_data)    

                    am = 0
                    def edit_data():
                        yearText = year.get()                                   # get year

                        selected_item = MR2Table.selection()[0]

                        years.pop(MR2Table.index(selected_item))
                        years.insert(MR2Table.index(selected_item), int(yearText))

                        inputXText = float(inputX.get())                                                    # get X
                        outputYText = float(inputX.get())*float(coefficientMR2) + float(interceptMR2)         # compute for Y
                        
                        MR2Table.item(selected_item, text="blub", values=(yearText, inputXText, outputYText))

                    def add_data():
                        yearText = year.get()                                   # get year
                        inputXText = int(inputX.get())                        # get benefit
                        outputYText = float(inputX.get())*float(coefficientMR2) + float(interceptMR2)         # compute for Y

                        years.append(int(yearText))

                        year.delete(0,END)
                        inputX.delete(0,END)

                        global assessmentTuple
                        assessmentTuple = [yearText, inputXText, outputYText]

                        # effortList.append(efforttuple)

                        MR2Table.insert("",'end', values=(yearText, inputXText, outputYText))
                        yearText.delete('1.0',END)                      # reset the text entry box
                        inputX.delete('1.0',END)                        # reset the text entry box
                        yearText.focus() 
                    
                    MR2Label.pack()
                    MR2Table.pack()
                    yearLabel.place(x=210, y=360)
                    year.place(x=300, y=360)
                    inputXLabel.place(x=210, y=420)
                    inputX.place(x=300, y=420)
                    addButton.place(x=540, y=360)
                    editButton.place(x=540, y=420)

                a = 0

                while (a < len(p9alternatives)):
                    window1PerAlt(a, p9alternatives[a])
                    window2PerAlt(a, p9alternatives[a])
                    a += 1

            elif int(varEffec.get()) == 3: 
                def windowPerAlt(a, policyAlt):
                    effectivenessLogR = Toplevel(main)
                    effectivenessLogR.title("Effectiveness: LogR")
                    effectivenessLogR.geometry("830x480")
                    
                    equation = "y = "+str(coefficientXLogR)+"x + "+str(interceptLogR+coefficientConstLogR)+"\n"
                    equationWithLabel = Label(effectivenessLogR, text="\nEquation  :  "+equation, font="Consolas", justify="left")
                    equationWithLabel.pack()

                    LogRLabel = Label(effectivenessLogR, text = "Alternative " + str(a+1) + " - " + policyAlt)
                    LogRTable=ttk.Treeview(effectivenessLogR)
                    LogRTable["columns"]=("1","2","3")
                    LogRTable['show']='headings'
                    LogRTable.column("1",width=130,anchor='c')
                    LogRTable.column("2",width=130,anchor='c')
                    LogRTable.column("3",width=130,anchor='c')
                    LogRTable.heading("1",text="Year")
                    LogRTable.heading("2",text="X")
                    LogRTable.heading("3",text="Y")

                    yearLabel = Label(effectivenessLogR, text = "Year")
                    inputXLabel = Label(effectivenessLogR, text = "X")

                    year = tk.Entry(effectivenessLogR, width=30)
                    inputX = tk.Entry(effectivenessLogR, width=30) 

                    addButton = tk.Button(effectivenessLogR, text='Add', width=10, command=lambda: add_data())  
                    editButton = tk.Button(effectivenessLogR, text="Edit", width=10, command=lambda: edit_data())

                    years = []

                    def show_data(a):
                        year.delete(0,END)
                        inputX.delete(0,END)

                        selectedItem = LogRTable.selection()[0]
                        year.insert(0, LogRTable.item(selectedItem)['values'][0])
                        inputX.insert(0, LogRTable.item(selectedItem)['values'][1])

                    LogRTable.bind("<<TreeviewSelect>>", show_data)    

                    am = 0
                    def edit_data():
                        yearText = year.get()                                   # get year

                        selected_item = LogRTable.selection()[0]

                        years.pop(LogRTable.index(selected_item))
                        years.insert(LogRTable.index(selected_item), int(yearText))

                        inputXText = float(inputX.get())                                                                            # get X
                        log_odds = float(inputX.get())*float(coefficientXLogR) + float(interceptLogR+coefficientConstLogR)          # compute for Y
                        odds = np.exp(log_odds)
                        outputYText = odds / (1 + odds)
                        
                        LogRTable.item(selected_item, text="blub", values=(yearText, inputXText, outputYText))

                    def add_data():
                        yearText = year.get()                                   # get year
                        
                        years.append(int(yearText))

                        inputXText = float(inputX.get())                                                                            # get X
                        log_odds = float(inputX.get())*float(coefficientXLogR) + float(interceptLogR+coefficientConstLogR)          # compute for Y
                        odds = np.exp(log_odds)
                        outputYText = odds / (1 + odds)

                        year.delete(0,END)
                        inputX.delete(0,END)

                        global assessmentTuple
                        assessmentTuple = [yearText, inputXText, outputYText]

                        # effortList.append(efforttuple)

                        LogRTable.insert("",'end', values=(yearText, inputXText, outputYText))
                        year.delete(0,END)                      # reset the text entry box
                        inputX.delete(0,END)                        # reset the text entry box
                        yearText.focus() 
                    
                    LogRLabel.pack()
                    LogRTable.pack()
                    yearLabel.place(x=210, y=360)
                    year.place(x=300, y=360)
                    inputXLabel.place(x=210, y=420)
                    inputX.place(x=300, y=420)
                    addButton.place(x=540, y=360)
                    editButton.place(x=540, y=420)

                a = 0

                while (a < len(p9alternatives)):
                    windowPerAlt(a, p9alternatives[a])
                    a += 1

            elif int(varEffec.get()) == 4: 
                effectiveness4 = Toplevel(main)
                effectiveness4.title("Effectiveness: FGD")
                effectiveness4.geometry("830x480")

            if int(varCostEff.get()) == 1: 
                popup = Toplevel(root)
                popup.geometry("200x200")
                popup.title("Enter Discount Rate")

                discountLabel = Label(popup, text = "Enter discount rate (1-100): ")
                discountEntry = Entry(popup, width=10)
                discountButton = tk.Button(popup, text='Set', width=10, command=lambda: enter_discount())

                def enter_discount():
                    global discount
                    discount = int(discountEntry.get())/100
                    print(discount)
                    popup.update()
                    popup.destroy()
                
                def windowPerAlt(a, policyAlt):
                    nu = 0
                    tangiblePerAlternative = Toplevel(main)
                    tangiblePerAlternative.title("Tangible BCA with Discounting: Alternative " + str(a+1) + " - " + policyAlt)
                    tangiblePerAlternative.geometry("810x600")

                    totalDiscBenefit = 0
                    totalDiscCost = 0

                    analysisFrame = tk.LabelFrame(tangiblePerAlternative)

                    yearlytangibleCBAwithLabel = Label(analysisFrame, text = "Alternative " + str(a+1) + " - " + policyAlt)
                    yearlytangibleCBAwithTable=ttk.Treeview(analysisFrame)
                    yearlytangibleCBAwithTable["columns"]=("1","2","3","4","5","6")
                    yearlytangibleCBAwithTable['show']='headings'
                    yearlytangibleCBAwithTable.column("1",width=130,anchor='c')
                    yearlytangibleCBAwithTable.column("2",width=130,anchor='c')
                    yearlytangibleCBAwithTable.column("3",width=130,anchor='c')
                    yearlytangibleCBAwithTable.column("4",width=130,anchor='c')
                    yearlytangibleCBAwithTable.column("5",width=130,anchor='c')
                    yearlytangibleCBAwithTable.column("6",width=130,anchor='c')
                    yearlytangibleCBAwithTable.heading("1",text="Year")
                    yearlytangibleCBAwithTable.heading("2",text="Benefit")
                    yearlytangibleCBAwithTable.heading("3",text="Cost")
                    yearlytangibleCBAwithTable.heading("4",text="df")
                    yearlytangibleCBAwithTable.heading("5",text="Discounted Benefit")
                    yearlytangibleCBAwithTable.heading("6",text="Discounted Cost")

                    yearLabel = Label(tangiblePerAlternative, text = "Year")
                    benefLabel = Label(tangiblePerAlternative, text = "Benefit")
                    costLabel = Label(tangiblePerAlternative, text = "Cost")
                    totalLabel = Label(tangiblePerAlternative, text = "Total: ")

                    year = tk.Entry(tangiblePerAlternative, width=30)
                    benefit = tk.Entry(tangiblePerAlternative, width=30) 
                    cost = tk.Entry(tangiblePerAlternative, width=30) 

                    addButton = tk.Button(tangiblePerAlternative, text='Add', width=10, command=lambda: add_data())  
                    editButton = tk.Button(tangiblePerAlternative, text="Edit", width=10, command=lambda: edit_data())
                    computeTotalButton = tk.Button(tangiblePerAlternative, text="Compute Total", width=50, command=lambda: compute_total())

                    years = []

                    def show_data(a):
                        year.delete(0,END)
                        benefit.delete(0,END)
                        cost.delete(0,END)

                        selectedItem = yearlytangibleCBAwithTable.selection()[0]
                        year.insert(0, yearlytangibleCBAwithTable.item(selectedItem)['values'][0])
                        benefit.insert(0, yearlytangibleCBAwithTable.item(selectedItem)['values'][1])
                        cost.insert(0, yearlytangibleCBAwithTable.item(selectedItem)['values'][2])

                    yearlytangibleCBAwithTable.bind("<<TreeviewSelect>>", show_data)    

                    am = 0
                    def edit_data():
                        nonlocal nu, totalDiscBenefit, totalDiscCost
                        yearText = year.get()                                   # get year


                        selected_item = yearlytangibleCBAwithTable.selection()[0]
                        
                        totalDiscBenefit -= round(float(yearlytangibleCBAwithTable.item(selected_item)['values'][4]), 2)
                        totalDiscCost -= round(float(yearlytangibleCBAwithTable.item(selected_item)['values'][5]), 2)

                        years.pop(yearlytangibleCBAwithTable.index(selected_item))
                        years.insert(yearlytangibleCBAwithTable.index(selected_item), int(yearText))

                        benefitText = float(benefit.get())                        # get benefit
                        costText = float(cost.get())                              # get cost
                        df = round(1/((1+discount)**(int(yearText) - int(years[0]))), 5)
                        discountedBenefit = round(float(benefitText)*df, 2)                 # compute for and set discountedBenefit 
                        discountedCost = round(float(costText)*df, 2)                       # compute for and set discountedCost

                        totalDiscBenefit += discountedBenefit
                        totalDiscCost += discountedCost
                        print(totalDiscBenefit, totalDiscCost)

                        yearlytangibleCBAwithTable.item(selected_item, text="blub", values=(yearText, benefitText, costText, df, discountedBenefit, discountedCost))

                    def add_data():
                        nonlocal nu, totalDiscBenefit, totalDiscCost
                        print(year.get())
                        print(benefit.get())
                        print(cost.get())

                        yearText = year.get()                                   # get year
                        benefitText = float(benefit.get())                        # get benefit
                        costText = float(cost.get())                              # get cost

                        years.append(int(yearText))

                        year.delete(0,END)
                        benefit.delete(0,END)
                        cost.delete(0,END)
                        df = round(1/((1+discount)**nu), 5)                               # set df to discount function
                        discountedBenefit = round(float(benefitText)*df, 2)                 # compute for and set discountedBenefit 
                        discountedCost = round(float(costText)*df, 2)                       # compute for and set discountedCost
                        nu += 1

                        totalDiscBenefit += discountedBenefit
                        totalDiscCost += discountedCost
                        print(totalDiscBenefit, totalDiscCost)

                        global assessmentTuple
                        assessmentTuple = [yearText, benefitText, costText, df, discountedBenefit, discountedCost]

                        # effortList.append(efforttuple)

                        yearlytangibleCBAwithTable.insert("",'end', values=(yearText, benefitText, costText, df, discountedBenefit, discountedCost))
                        yearText.delete('1.0',END)               # reset the text entry box
                        benefitText.delete('1.0',END)                   # reset the text entry box
                        costText.delete('1.0',END)                      # reset the text entry box
                        yearText.focus() 

                    def compute_total():
                        popupTotal = Toplevel(tangiblePerAlternative)
                        popupTotal.geometry("400x280")
                        popupTotal.title("Totals")

                        totDBLabel = Label(popupTotal, text = "Total Discounted Benefits:   ")
                        totDCLabel = Label(popupTotal, text = "Total Discounted Costs:    ")
                        BCRatioLabel = Label(popupTotal, text = "Benefit-Cost Ratio:   ")

                        BCRatio = round(float(totalDiscBenefit/totalDiscCost), 2)
                        
                        totDBLabel2 = Label(popupTotal, text = str(totalDiscBenefit))
                        totDCLabel2 = Label(popupTotal, text = str(totalDiscCost))
                        BCRatioLabel2 = Label(popupTotal, text = str(BCRatio))

                        totDBLabel.place(x=70, y=40)
                        totDCLabel.place(x=70, y=100)
                        BCRatioLabel.place(x=70, y=160)
                        totDBLabel2.place(x=260, y=40)
                        totDCLabel2.place(x=260, y=100)
                        BCRatioLabel2.place(x=260, y=160)
                    
                    analysisFrame.place(x=10, y=10)
                    yearlytangibleCBAwithLabel.grid(row=0, column=1)
                    yearlytangibleCBAwithTable.grid(row=1, column=1)
                    yearLabel.place(x=100, y=330)
                    year.place(x=260, y=330)
                    benefLabel.place(x=100, y=390)
                    benefit.place(x=260, y=390)
                    costLabel.place(x=100, y=450)
                    cost.place(x=260, y=450)
                    addButton.place(x=550, y=390)
                    editButton.place(x=550, y=450)
                    computeTotalButton.place(x=220, y=540)

                a = 0

                while (a < len(p9alternatives)):
                    windowPerAlt(a, p9alternatives[a])
                    a += 1

                discountLabel.place(x = 25, y = 10)
                discountEntry.place(x = 70, y = 50)
                discountButton.place(x = 63, y = 100)

            elif int(varCostEff.get()) == 2: 
                def windowPerAlt(a, policyAlt):
                    nu = 0
                    tangibleWithoutPerAlternative = Toplevel(main)
                    tangibleWithoutPerAlternative.title("Tangible BCA without Discounting: Alternative " + str(a+1) + " - " + policyAlt)
                    tangibleWithoutPerAlternative.geometry("620x600")
                    
                    analysisFrame = tk.LabelFrame(tangibleWithoutPerAlternative)

                    yearlytangibleCBAwithoutLabel = Label(analysisFrame, text = "Alternative " + str(a+1) + " - " + policyAlt)
                    yearlytangibleCBAwithoutTable=ttk.Treeview(analysisFrame)
                    yearlytangibleCBAwithoutTable["columns"]=("1","2","3")
                    yearlytangibleCBAwithoutTable['show']='headings'
                    yearlytangibleCBAwithoutTable.column("1",width=200,anchor='c')
                    yearlytangibleCBAwithoutTable.column("2",width=200,anchor='c')
                    yearlytangibleCBAwithoutTable.column("3",width=200,anchor='c')
                    yearlytangibleCBAwithoutTable.heading("1",text="Year")
                    yearlytangibleCBAwithoutTable.heading("2",text="Benefit")
                    yearlytangibleCBAwithoutTable.heading("3",text="Cost")

                    yearLabel = Label(tangibleWithoutPerAlternative, text = "Year")
                    benefLabel = Label(tangibleWithoutPerAlternative, text = "Benefit")
                    costLabel = Label(tangibleWithoutPerAlternative, text = "Cost")

                    year = tk.Entry(tangibleWithoutPerAlternative, width=30)
                    benefit = tk.Entry(tangibleWithoutPerAlternative, width=30) 
                    cost = tk.Entry(tangibleWithoutPerAlternative, width=30) 

                    addButton = tk.Button(tangibleWithoutPerAlternative, text='Add', width=10, command=lambda: add_data())  
                    editButton = tk.Button(tangibleWithoutPerAlternative, text="Edit", width=10, command=lambda: edit_data())

                    def show_data(a):
                        year.delete(0,END)
                        benefit.delete(0,END)
                        cost.delete(0,END)

                        selectedItem = yearlytangibleCBAwithoutTable.selection()[0]
                        year.insert(0, yearlytangibleCBAwithoutTable.item(selectedItem)['values'][0])
                        benefit.insert(0, yearlytangibleCBAwithoutTable.item(selectedItem)['values'][1])
                        cost.insert(0, yearlytangibleCBAwithoutTable.item(selectedItem)['values'][2])

                    yearlytangibleCBAwithoutTable.bind("<<TreeviewSelect>>", show_data)    

                    def edit_data():
                        yearText = year.get()                                   # get year
                        benefitText = int(benefit.get())                        # get benefit
                        costText = int(cost.get())                              # get cost

                        selected_item = yearlytangibleCBAwithoutTable.selection()[0]
                        yearlytangibleCBAwithoutTable.item(selected_item, text="blub", values=(yearText, benefitText, costText))

                    def add_data():
                        nonlocal nu

                        yearText = year.get()                                   # get year
                        benefitText = int(benefit.get())                        # get benefit
                        costText = int(cost.get())                              # get cost

                        year.delete(0,END)
                        benefit.delete(0,END)
                        cost.delete(0,END)
                        nu += 1
                        global assessmentTuple
                        assessmentTuple = [yearText, benefitText, costText]

                        yearlytangibleCBAwithoutTable.insert("",'end', values=(yearText, benefitText, costText))
                        yearText.delete('1.0',END)               # reset the text entry box
                        benefitText.delete('1.0',END)                   # reset the text entry box
                        costText.delete('1.0',END)                      # reset the text entry box
                        yearText.focus() 
                    
                    analysisFrame.place(x=10, y=10)
                    yearlytangibleCBAwithoutLabel.grid(row=0, column=1)
                    yearlytangibleCBAwithoutTable.grid(row=1, column=1)
                    yearLabel.place(x=40, y=330)
                    year.place(x=200, y=330)
                    benefLabel.place(x=40, y=390)
                    benefit.place(x=200, y=390)
                    costLabel.place(x=40, y=450)
                    cost.place(x=200, y=450)
                    addButton.place(x=450, y=390)
                    editButton.place(x=450, y=450)

                a = 0

                while (a < len(p9alternatives)):
                    windowPerAlt(a, p9alternatives[a])
                    a += 1

            elif int(varCostEff.get()) == 3:
                def windowPerAlt(a, policyAlt):
                    nu = 0
                    intangiblePerAlternative = Toplevel(main)
                    intangiblePerAlternative.title("Intangible BCA: Alternative " + str(a+1) + " - " + policyAlt)
                    intangiblePerAlternative.geometry("830x600")
                
                a = 0

                while (a < len(p9alternatives)):
                    windowPerAlt(a, p9alternatives[a])
                    a += 1

            if int(varAccept.get()) == 1:
                def windowPerAlt(a, policyAlt):
                    princeMethod = Toplevel(main)
                    princeMethod.title("PRINCE Method: Alternative " + str(a+1) + " - " + policyAlt)
                    princeMethod.geometry("670x600")

                    # analysisFrame = tk.LabelFrame(princeMethod)
# 
                    # princeLabel = Label(analysisFrame, text = "PRINCE Method")
                    # princeTable=ttk.Treeview(analysisFrame)
                    # princeTable["columns"]=("1","2","3","4","5")
                    # princeTable['show']='headings'
                    # princeTable.column("1",width=130,anchor='c')
                    # princeTable.column("2",width=130,anchor='c')
                    # princeTable.column("3",width=130,anchor='c')
                    # princeTable.column("4",width=130,anchor='c')
                    # princeTable.column("5",width=130,anchor='c')
                    # princeTable.heading("1",text="Player")
                    # princeTable.heading("2",text="Issue Position")
                    # princeTable.heading("3",text="Power")
                    # princeTable.heading("4",text="Priority")
                    # princeTable.heading("5",text="PRINCE Score")
# 
                    # playerLabel = Label(princeMethod, text = "Player")
                    # issueposLabel = Label(princeMethod, text = "Issue\nPosition")
                    # powerLabel = Label(princeMethod, text = "Power")
                    # prioLabel = Label(princeMethod, text = "Priority")
# 
                    # player = tk.Entry(princeMethod, width=30)
                    # issuepos = tk.Entry(princeMethod, width=30) 
                    # power = tk.Entry(princeMethod, width=30) 
                    # prio = tk.Entry(princeMethod, width=30) 
# 
                    # addButton = tk.Button(princeMethod, text='Add', width=10, command=lambda: add_data())  
                    # editButton = tk.Button(princeMethod, text="Edit", width=10, command=lambda: edit_data())
# 
                    # def show_data(a):
                    #     player.delete(0,END)
                    #     issuepos.delete(0,END)
                    #     power.delete(0,END)
                    #     prio.delete(0,END)
# 
                    #     selectedItem = princeTable.selection()[0]
                    #     player.insert(0, princeTable.item(selectedItem)['values'][0])
                    #     issuepos.insert(0, princeTable.item(selectedItem)['values'][1])
                    #     power.insert(0, princeTable.item(selectedItem)['values'][2])
                    #     prio.insert(0, princeTable.item(selectedItem)['values'][3])
# 
                    # princeTable.bind("<<TreeviewSelect>>", show_data)
# 
                    # def edit_data():
                    #     playerText = player.get()                               # read player textbox
                    #     issueposText = int(issuepos.get())                      # read issue position textbox
                    #     powerText = int(power.get())                            # read power textbox        
                    #     prioText = int(prio.get())                              # read priority textbox     
# 
                    #     grades = [issueposText, powerText, prioText]
                    #     pc = 1
                    #     for g in grades:
                    #         if g != 0:
                    #             pc *= g       
                    #                             
                    #     selected_item = princeTable.selection()[0]
                    #     princeTable.item(selected_item, text="blub", values=(playerText, issueposText, powerText, prioText, pc))
# 
                    # def add_data():
                    #     playerText = player.get()                               # read player textbox
                    #     issueposText = int(issuepos.get())                      # read issue position textbox
                    #     powerText = int(power.get())                            # read power textbox        
                    #     prioText = int(prio.get())                              # read priority textbox 
# 
                    #     grades = [issueposText, powerText, prioText]
                    #     pc = 1
                    #     for g in grades:
                    #         if g != 0:
                    #             pc *= g 
# 
                    #     global assessmentTuple
                    #     assessmentTuple = [playerText, issueposText, powerText, prioText]
# 
                    #     princeTable.insert("",'end', values=(playerText, issueposText, powerText, prioText, pc))
                    #     player.delete(0,END)
                    #     issuepos.delete(0,END)
                    #     power.delete(0,END)
                    #     prio.delete(0,END)
                    #     player.focus() 
# 
                    # analysisFrame.place(x=10, y=10)
                    # princeLabel.grid(row=0, column=1)
                    # princeTable.grid(row=1, column=1)
                    # playerLabel.place(x=40, y=330)
                    # player.place(x=200, y=330)
                    # issueposLabel.place(x=40, y=390)
                    # issuepos.place(x=200, y=390)
                    # powerLabel.place(x=40, y=450)
                    # power.place(x=200, y=450)
                    # prioLabel.place(x=40, y=510)
                    # prio.place(x=200, y=510)
                    # addButton.place(x=450, y=390)
                    # editButton.place(x=450, y=450)

                a = 0

                while (a < len(p9alternatives)):
                    windowPerAlt(a, p9alternatives[a])
                    a += 1    

            elif int(varAccept.get()) == 2:
                global p9stakeholderDataPerAlt
                def windowPerAlt(a, policyAlt):
                    stakeholderWindow = Toplevel(main)
                    stakeholderWindow.title("Stakeholder Analysis: Alternative " + str(a+1) + " - " + policyAlt)
                    stakeholderWindow.geometry("790x600")

                    p9stakeholderDataPerAlt.append([]) 

                    analysisFrame = tk.LabelFrame(stakeholderWindow)

                    stakeholderLabel = Label(analysisFrame, text = "Stakeholder Analysis")
                    stakeholderTable=ttk.Treeview(analysisFrame)
                    stakeholderTable["columns"]=("1","2","3","4")
                    stakeholderTable['show']='headings'
                    stakeholderTable.column("1",width=190,anchor='c')
                    stakeholderTable.column("2",width=190,anchor='c')
                    stakeholderTable.column("3",width=190,anchor='c')
                    stakeholderTable.column("4",width=190,anchor='c')
                    stakeholderTable.heading("1",text="Players (Stakeholder + Actor)")
                    stakeholderTable.heading("2",text="Positions/Stands")
                    stakeholderTable.heading("3",text="Motivations/Values/Beliefs")
                    stakeholderTable.heading("4",text="Sources of Power")

                    player_stakeactorLabel = Label(stakeholderWindow, text = "Player (Stakeholder + Actor)")
                    positionLabel = Label(stakeholderWindow, text = "Position/Stand")
                    motivationLabel = Label(stakeholderWindow, text = "Motivation/Value/Belief")
                    sourceLabel = Label(stakeholderWindow, text = "Source")

                    player_stakeactor = tk.Entry(stakeholderWindow, width=30)
                    position = tk.Entry(stakeholderWindow, width=30) 
                    motivation = tk.Entry(stakeholderWindow, width=30) 
                    source = tk.Entry(stakeholderWindow, width=30) 

                    addButton = tk.Button(stakeholderWindow, text='Add', width=10, command=lambda: add_data())  
                    editButton = tk.Button(stakeholderWindow, text="Edit", width=10, command=lambda: edit_data())

                    def show_data(a):
                        player_stakeactor.delete(0,END)
                        position.delete(0,END)
                        motivation.delete(0,END)
                        source.delete(0,END)

                        selectedItem = stakeholderTable.selection()[0]
                        player_stakeactor.insert(0, stakeholderTable.item(selectedItem)['values'][0])
                        position.insert(0, stakeholderTable.item(selectedItem)['values'][1])
                        motivation.insert(0, stakeholderTable.item(selectedItem)['values'][2])
                        source.insert(0, stakeholderTable.item(selectedItem)['values'][3])


                    stakeholderTable.bind("<<TreeviewSelect>>", show_data)
                    if a < len(p9stakeholderDataPerAlt):
                        for row in p9stakeholderDataPerAlt[a]:
                            stakeholderTable.insert("", "end", values=row)

                    def edit_data():
                        player_stakeactorText = player_stakeactor.get()     # read player(s + a) textbox
                        positionText = position.get()                       # read position textbox
                        motivationText = motivation.get()                   # read motivation textbox        
                        sourceText = source.get()                           # read source textbox     
    
                        selected_item = stakeholderTable.selection()[0]
                        stakeholderTable.item(selected_item, text="blub", values=(player_stakeactorText, positionText, motivationText, sourceText))

                    def add_data():
                        player_stakeactorText = player_stakeactor.get()
                        positionText = position.get()
                        motivationText = motivation.get()
                        sourceText = source.get()

                        stakeholderTable.insert("", 'end', values=(
                            player_stakeactorText, positionText, motivationText, sourceText))

                        # Save to the corresponding sublist using index `a`
                        p9stakeholderDataPerAlt[a].append([
                            player_stakeactorText,
                            positionText,
                            motivationText,
                            sourceText
                        ])

                        player_stakeactor.delete(0, END)
                        position.delete(0, END)
                        motivation.delete(0, END)
                        source.delete(0, END)

                        player_stakeactor.focus()

                    save()
                    analysisFrame.place(x=10, y=10)
                    stakeholderLabel.grid(row=0, column=1)
                    stakeholderTable.grid(row=1, column=1)
                    player_stakeactorLabel.place(x=40, y=330)
                    player_stakeactor.place(x=200, y=330)
                    positionLabel.place(x=40, y=390)
                    position.place(x=200, y=390)
                    motivationLabel.place(x=40, y=450)
                    motivation.place(x=200, y=450)
                    sourceLabel.place(x=40, y=510)
                    source.place(x=200, y=510)
                    addButton.place(x=450, y=390)
                    editButton.place(x=450, y=450)

                a = 0

                while (a < len(p9alternatives)):
                    windowPerAlt(a, p9alternatives[a])
                    a += 1    


        btnNext8 = Button(mainProject, text = "Next", width=10, command = lambda: next_8())
        btnNext8.place(x=550, y=440)         
        btnBack8 = Button(mainProject, text = "Back", width=10, command = lambda: back_8())
        btnBack8.place(x=265, y=440)      

    def page_10():

        global p10spillovers, p10externalities, p10constraints, p10mitimeasures
        mainProject.state('zoomed') 
        frame10 = tk.LabelFrame(mainProject)
        widgets_to_destroy = [frame10]
        undo_stack = []

        ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 10 of 15: Assessments of the Policy Alternatives: Spillovers, Externalities, and Constraints", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        frame10.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.55)

        assessPALabel = tk.Label(frame10, text="Assessments of the Policy Alternatives: Spillovers, Externalities, and Constraints", font=("Arial", 12, "bold"))
        assessPATable = ttk.Treeview(frame10, selectmode="browse")
        assessPATable["columns"] = ("1", "2", "3", "4", "5")
        assessPATable['show'] = 'headings'
        assessPATable.column("1", width=300, anchor='c')
        assessPATable.column("2", width=250, anchor='c')
        assessPATable.column("3", width=180, anchor='c')
        assessPATable.column("4", width=140, anchor='c')
        assessPATable.column("5", width=180, anchor='c')
        assessPATable.heading("1", text="Alternative")
        assessPATable.heading("2", text="Spillovers")
        assessPATable.heading("3", text="Externalities")
        assessPATable.heading("4", text="Constraints")
        assessPATable.heading("5", text="Mitigating Measures")
        sb_y = ttk.Scrollbar(frame10, orient="vertical", command=assessPATable.yview)
        sb_x = ttk.Scrollbar(frame10, orient="horizontal", command=assessPATable.xview)
        assessPATable.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)

        assessPALabel.grid(row=0, column=0, columnspan=2, pady=10)
        assessPATable.grid(row=1, column=0, sticky="nsew")
        sb_y.grid(row=1, column=1, sticky="ns")
        sb_x.grid(row=2, column=0, sticky="ew")
        frame10.grid_columnconfigure(0, weight=1)
        frame10.grid_rowconfigure(1, weight=1)

        alternaLabel = tk.Label(mainProject, text="Alternative")
        spillovLabel = tk.Label(mainProject, text="Spillovers")
        externaLabel = tk.Label(mainProject, text="Externalities")
        constraLabel = tk.Label(mainProject, text="Constraints")
        mitmeasLabel = tk.Label(mainProject, text="Mitigating Measures")
        alternative = tk.Entry(mainProject, width=50)
        spillover = scrolledtext.ScrolledText(mainProject, height=4, width=25)
        externality = scrolledtext.ScrolledText(mainProject, height=4, width=25)
        constraint = scrolledtext.ScrolledText(mainProject, height=4, width=25)
        mitimeasure = scrolledtext.ScrolledText(mainProject, height=4, width=25)
        addButton10 = ttk.Button(mainProject, text="Add", command=lambda: add_data10())
        editButton10 = ttk.Button(mainProject, text="Edit", state="disabled", command=lambda: edit_data10())
        deleteButton10 = ttk.Button(mainProject, text="Delete", state="disabled", command=lambda: delete_data10())

        ToolTip(addButton10, "Add a new entry to the table")
        ToolTip(editButton10, "Edit the selected table entry")
        ToolTip(deleteButton10, "Delete the selected table entry")

        alternaLabel.place(relx=0.38, rely=0.60)
        alternative.place(relx=0.45, rely=0.60)

        spillovLabel.place(relx=0.05, rely=0.65)
        spillover.place(relx=0.05, rely=0.70)

        externaLabel.place(relx=0.30, rely=0.65)
        externality.place(relx=0.30, rely=0.70)

        constraLabel.place(relx=0.55, rely=0.65)
        constraint.place(relx=0.55, rely=0.70)

        mitmeasLabel.place(relx=0.80, rely=0.65)
        mitimeasure.place(relx=0.80, rely=0.70)

        addButton10.place(relx=0.40, rely=0.82, anchor='s')
        editButton10.place(relx=0.50, rely=0.82, anchor='s')
        deleteButton10.place(relx=0.60, rely=0.82, anchor='s')

        # Clear existing rows to prevent duplication
        for row in assessPATable.get_children():
            assessPATable.delete(row)

        # Always insert one row per alternative
        for i, alt in enumerate(p9alternatives):
            spill = p10spillovers[i] if i < len(p10spillovers) else ""
            ext = p10externalities[i] if i < len(p10externalities) else ""
            cons = p10constraints[i] if i < len(p10constraints) else ""
            miti = p10mitimeasures[i] if i < len(p10mitimeasures) else ""

            assessPATable.insert(
                "", "end",
                values=(f"Alt {i+1}: {alt}", spill, ext, cons, miti)
            )

        def show_data10(a):
            alternative.delete(0, tk.END)
            spillover.delete("1.0", tk.END)
            externality.delete("1.0", tk.END)
            constraint.delete("1.0", tk.END)
            mitimeasure.delete("1.0", tk.END)
            selected_item = assessPATable.selection()
            if selected_item:
                editButton10.config(state="normal")
                deleteButton10.config(state="normal")
                values = assessPATable.item(selected_item[0])['values']
                alternative.insert(0, values[0])
                spillover.insert("1.0", values[1])
                externality.insert("1.0", values[2])
                constraint.insert("1.0", values[3])
                mitimeasure.insert("1.0", values[4])
            else:
                editButton10.config(state="disabled")
                deleteButton10.config(state="disabled")

        def add_data10():
            texts = [
                alternative.get().strip(),
                spillover.get("1.0", tk.END).strip(),
                externality.get("1.0", tk.END).strip(),
                constraint.get("1.0", tk.END).strip(),
                mitimeasure.get("1.0", tk.END).strip()
            ]
            if not all(texts):
                messagebox.showerror("Error", "Please fill out all fields")
                return
            item_id = assessPATable.insert("", 'end', values=texts)
            undo_stack.append(("add", item_id))
            alternative.delete(0, tk.END)
            spillover.delete("1.0", tk.END)
            externality.delete("1.0", tk.END)
            constraint.delete("1.0", tk.END)
            mitimeasure.delete("1.0", tk.END)
            alternative.focus()

        def edit_data10():
            texts = [
                alternative.get().strip(),
                spillover.get("1.0", tk.END).strip(),
                externality.get("1.0", tk.END).strip(),
                constraint.get("1.0", tk.END).strip(),
                mitimeasure.get("1.0", tk.END).strip()
            ]
            if not all(texts):
                messagebox.showerror("Error", "Please fill out all fields")
                return
            selected_item = assessPATable.selection()[0]
            old_values = assessPATable.item(selected_item)['values']
            undo_stack.append(("edit", selected_item, old_values))
            assessPATable.item(selected_item, values=texts)

        def delete_data10():
            selected_item = assessPATable.selection()
            if selected_item:
                item_id = selected_item[0]
                old_values = assessPATable.item(item_id)['values']
                undo_stack.append(("delete", item_id, old_values))
                assessPATable.delete(item_id)
                alternative.delete(0, tk.END)
                spillover.delete("1.0", tk.END)
                externality.delete("1.0", tk.END)
                constraint.delete("1.0", tk.END)
                mitimeasure.delete("1.0", tk.END)
                editButton10.config(state="disabled")
                deleteButton10.config(state="disabled")
            else:
                messagebox.showwarning("Warning", "Please select an item to delete")

        def undo():
            if not undo_stack:
                return
            action, *data = undo_stack.pop()
            if action == "add":
                assessPATable.delete(data[0])
            elif action == "edit":
                item_id, old_values = data
                assessPATable.item(item_id, values=old_values)
            elif action == "delete":
                item_id, old_values = data
                assessPATable.insert("", "end", iid=item_id, values=old_values)

        assessPATable.bind("<<TreeviewSelect>>", show_data10)
        mainProject.bind("<Control-z>", lambda e: undo())
        mainProject.bind("<Control-Return>", lambda e: add_data10())
        alternative.bind("<Tab>", lambda e: spillover.focus_set())
        spillover.bind("<Tab>", lambda e: externality.focus_set())
        externality.bind("<Tab>", lambda e: constraint.focus_set())
        constraint.bind("<Tab>", lambda e: mitimeasure.focus_set())
        mitimeasure.bind("<Tab>", lambda e: addButton10.focus_set())

        def back_9():
            global pageNumber
            pageNumber -= 1
            for widget in mainProject.winfo_children():
                widget.destroy()

            save()
            page_9()

        def next_9():
            global pageNumber, p10spillovers, p10externalities, p10constraints, p10mitimeasures

            # Reset the lists
            p10spillovers = []
            p10externalities = []
            p10constraints = []
            p10mitimeasures = []

            # Extract values from all rows
            for row_id in assessPATable.get_children():
                values = assessPATable.item(row_id)['values']
                if len(values) >= 5:
                    p10spillovers.append(values[1])
                    p10externalities.append(values[2])
                    p10constraints.append(values[3])
                    p10mitimeasures.append(values[4])

            save()
            pageNumber += 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            page_11()

        btnBack9 = Button(mainProject, text="Back", width=10, command=lambda: back_9())
        btnNext9 = Button(mainProject, text="Next", width=10, command=lambda: next_9())
        btnBack9.place(relx=0.4, rely=0.90, anchor="s")
        btnNext9.place(relx=0.6, rely=0.90, anchor="s")

    def page_11():

        global p11BPAdescription, p11BPAreasonSelect
        mainProject.state('normal') 
        mainProject.geometry("750x380")

         ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 11 of 15: Best/Optimal Policy Alternative", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        
        frame11 = tk.LabelFrame(mainProject, text="Best/Optimal Policy Alternative", font=("Arial", 12, "bold"))
        frame11.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.75)

        # Status Label
        status = ttk.Label(mainProject, text="", font=("Arial", 10))
        status.place(relx=0.01, rely=0.88)

        # Widgets inside frame11
        descrLabel = tk.Label(frame11, text="Description", font=("Arial", 11))
        descr = scrolledtext.ScrolledText(frame11, height=8, width=40)
        descr.insert("1.0", p11BPAdescription)

        reaSelLabel = tk.Label(frame11, text="Reasons for Selection", font=("Arial", 11))
        reaSel = scrolledtext.ScrolledText(frame11, height=8, width=40)
        reaSel.insert("1.0", p11BPAreasonSelect)

        # Grid layout
        descrLabel.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
        descr.grid(row=1, column=0, padx=10)

        reaSelLabel.grid(row=0, column=1, sticky="w", padx=10, pady=(10, 2))
        reaSel.grid(row=1, column=1, padx=10)


        def back_10():
            global pageNumber
            pageNumber -= 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            save()
            page_10()

        def next_10():
            global pageNumber, p11BPAdescription, p11BPAreasonSelect
            p11BPAdescription = descr.get("1.0", tk.END).strip()
            p11BPAreasonSelect = reaSel.get("1.0", tk.END).strip()

            if not p11BPAdescription:
                status.config(text="Enter description", foreground="red")
                return
            if not p11BPAreasonSelect:
                status.config(text="Enter reason for selection", foreground="red")
                return

            pageNumber += 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            save()
            page_12()

        # Navigation Buttons
        btnBack10 = tk.Button(mainProject, text="Back", width=12, command=back_10)
        btnNext10 = tk.Button(mainProject, text="Next", width=12, command=next_10)
        btnBack10.place(relx=0.35, rely=0.85, anchor="s")
        btnNext10.place(relx=0.65, rely=0.85, anchor="s")

    def page_12():

        global p12BPAspillover, p12BPAexternality, p12BPAconstraint, p12BPAmitigatingmeasure

        mainProject.geometry("750x420")  # Increased height to make all content visible

         ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 12 of 15: Details of the Best/Optimal Policy Alternative", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        frame12 = tk.LabelFrame(mainProject, text="Details of the Best/Optimal Policy Alternative", font=("Arial", 11))
        frame12.place(relx=0.01, rely=0.02, relwidth=0.96, relheight=0.75)  # Increased height

        status = ttk.Label(mainProject, text="")
        status.place(relx=0.01, rely=0.92)

        # Labels and inputs
        spilloverLabel = tk.Label(frame12, text="Spillover")
        spillover = scrolledtext.ScrolledText(frame12, height=7, width=40)

        externalityLabel = tk.Label(frame12, text="Externalities")
        externality = scrolledtext.ScrolledText(frame12, height=7, width=40)

        constraintLabel = tk.Label(frame12, text="Constraints")
        constraint = scrolledtext.ScrolledText(frame12, height=7, width=40)

        mitiMeasureLabel = tk.Label(frame12, text="Mitigating Measures")
        mitiMeasure = scrolledtext.ScrolledText(frame12, height=7, width=40)

        # Layout inside frame12
        spilloverLabel.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
        spillover.grid(row=1, column=0, padx=10)

        externalityLabel.grid(row=0, column=1, sticky="w", padx=10, pady=(10, 2))
        externality.grid(row=1, column=1, padx=10)

        constraintLabel.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 2))
        constraint.grid(row=3, column=0, padx=10)

        mitiMeasureLabel.grid(row=2, column=1, sticky="w", padx=10, pady=(10, 2))
        mitiMeasure.grid(row=3, column=1, padx=10)


        # Pre-fill from global if available
        spillover.insert("1.0", p12BPAspillover.strip())
        externality.insert("1.0", p12BPAexternality.strip())
        constraint.insert("1.0", p12BPAconstraint.strip())
        mitiMeasure.insert("1.0", p12BPAmitigatingmeasure.strip())

        # Navigation buttons
        def back_11():
            global pageNumber, p12BPAspillover, p12BPAexternality, p12BPAconstraint, p12BPAmitigatingmeasure

            # Retrieve values
            p12BPAspillover = spillover.get("1.0", tk.END).strip()
            p12BPAexternality = externality.get("1.0", tk.END).strip()
            p12BPAconstraint = constraint.get("1.0", tk.END).strip()
            p12BPAmitigatingmeasure = mitiMeasure.get("1.0", tk.END).strip()

            pageNumber -= 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            save()
            page_11()

        def next_11():
            global pageNumber, p12BPAspillover, p12BPAexternality, p12BPAconstraint, p12BPAmitigatingmeasure

            # Retrieve values
            p12BPAspillover = spillover.get("1.0", tk.END).strip()
            p12BPAexternality = externality.get("1.0", tk.END).strip()
            p12BPAconstraint = constraint.get("1.0", tk.END).strip()
            p12BPAmitigatingmeasure = mitiMeasure.get("1.0", tk.END).strip()

            # Validation
            if not p12BPAspillover:
                status.config(text="Enter spillover", foreground="red")
                return
            if not p12BPAexternality:
                status.config(text="Enter externality", foreground="red")
                return
            if not p12BPAconstraint:
                status.config(text="Enter constraint", foreground="red")
                return
            if not p12BPAmitigatingmeasure:
                status.config(text="Enter mitigating measure", foreground="red")
                return

            save()
            pageNumber += 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            page_13()

        btnBack11 = tk.Button(mainProject, text="Back", width=10, command=back_11)
        btnNext11 = tk.Button(mainProject, text="Next", width=10, command=next_11)
        btnBack11.place(relx=0.4, rely=0.85, anchor="s")
        btnNext11.place(relx=0.6, rely=0.85, anchor="s")

    def page_13():

        global p13BPAwhat, p13BPAwho, p13BPAhow

        mainProject.geometry("750x420")  # Increased height to fit all inputs

        ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 13 of 15: Implementation Requirements", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        frame13 = tk.LabelFrame(mainProject, text="Implementation Requirements", font=("Arial", 11))
        frame13.place(relx=0.01, rely=0.02, relwidth=0.96, relheight=0.75)

        status = ttk.Label(mainProject, text="")
        status.place(relx=0.01, rely=0.92)

        # Title
        p13Label = tk.Label(mainProject, text="Requirements for the Implementation of the Best/Optimal Policy Alternative", font=("Arial", 12, "bold"))
        p13Label.place(relx=0.02, rely=0.01)

        # Labels and ScrolledText widgets
        p13whatLabel = tk.Label(frame13, text="What type of legislation is needed? Why?")
        p13what = scrolledtext.ScrolledText(frame13, height=7, width=40)

        p13whoLabel = tk.Label(frame13, text="Who will implement? Why?")
        p13who = scrolledtext.ScrolledText(frame13, height=7, width=40)

        p13howLabel = tk.Label(frame13, text="How much to implement and where to source funds?")
        p13how = scrolledtext.ScrolledText(frame13, height=7, width=85)  # Spans two columns

        # Layout inside frame13
        p13whatLabel.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
        p13what.grid(row=1, column=0, padx=10, pady=(0, 10))

        p13whoLabel.grid(row=0, column=1, sticky="w", padx=10, pady=(10, 2))
        p13who.grid(row=1, column=1, padx=10, pady=(0, 10))

        p13howLabel.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=(5, 2))
        p13how.grid(row=3, column=0, columnspan=2, padx=10)

        # Pre-fill values
        p13what.insert("1.0", p13BPAwhat.strip())
        p13who.insert("1.0", p13BPAwho.strip())
        p13how.insert("1.0", p13BPAhow.strip())

        # Navigation Buttons
        def back_12():
            global pageNumber
            pageNumber -= 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            save()
            page_12()

        def next_12():
            global pageNumber, p13BPAwhat, p13BPAwho, p13BPAhow

            p13BPAwhat = p13what.get("1.0", tk.END).strip()
            p13BPAwho = p13who.get("1.0", tk.END).strip()
            p13BPAhow = p13how.get("1.0", tk.END).strip()

            if not p13BPAwhat:
                status.config(text="Enter the type of legislation needed", foreground="red")
                return
            if not p13BPAwho:
                status.config(text="Enter who will implement", foreground="red")
                return
            if not p13BPAhow:
                status.config(text="Enter how much to implement", foreground="red")
                return

            save()
            pageNumber += 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            page_14()

        btnBack13 = tk.Button(mainProject, text="Back", width=10, command=back_12)
        btnNext13 = tk.Button(mainProject, text="Next", width=10, command=next_12)
        btnBack13.place(relx=0.4, rely=0.85, anchor="s")
        btnNext13.place(relx=0.6, rely=0.85, anchor="s")


    def page_14():

        global p14criticalActions, p14responsible, p14timeline, p14budget, p14budgetsource
        frame14 = tk.LabelFrame(mainProject)
        mainProject.state('zoomed')

        ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 14 of 15: Policy Implementation Plan", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        widgets_to_destroy = [frame14]
        undo_stack = []

        frame14.place(x=10, y=10, relwidth=0.98, relheight=0.60)

        implementationPlanLabel = tk.Label(frame14, text="Policy Implementation Plan", font=("Arial", 12, "bold"))
        implementationPlanTable = ttk.Treeview(frame14, selectmode="browse", height=8)
        implementationPlanTable["columns"] = ("1", "2", "3", "4", "5")
        implementationPlanTable['show'] = 'headings'
        implementationPlanTable.column("1", width=250, anchor='c')
        implementationPlanTable.column("2", width=220, anchor='c')
        implementationPlanTable.column("3", width=150, anchor='c')
        implementationPlanTable.column("4", width=100, anchor='c')
        implementationPlanTable.column("5", width=180, anchor='c')
        implementationPlanTable.heading("1", text="Critical Actions")
        implementationPlanTable.heading("2", text="Responsible/Accountable Units")
        implementationPlanTable.heading("3", text="Timeframes")
        implementationPlanTable.heading("4", text="Budgets")
        implementationPlanTable.heading("5", text="Budget Sources")
        sb_y = ttk.Scrollbar(frame14, orient="vertical", command=implementationPlanTable.yview)
        sb_x = ttk.Scrollbar(frame14, orient="horizontal", command=implementationPlanTable.xview)
        implementationPlanTable.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)

        # UI
        critALabel = tk.Label(mainProject, text="Critical Action")
        raUnitLabel = tk.Label(mainProject, text="Responsible/\nAccountable Unit", justify="left")
        timeframeLabel = tk.Label(mainProject, text="Timeframe")
        budgetLabel = tk.Label(mainProject, text="Budget")
        budgSoLabel = tk.Label(mainProject, text="Budget Source")
        criticalAction = scrolledtext.ScrolledText(mainProject, height=4, width=30)
        respaccoUnit = scrolledtext.ScrolledText(mainProject, height=4, width=30)
        timeframe = scrolledtext.ScrolledText(mainProject, height=4, width=30)
        budget = scrolledtext.ScrolledText(mainProject, height=4, width=30)
        budgetSource = scrolledtext.ScrolledText(mainProject, height=4, width=30)
        addButton14 = ttk.Button(mainProject, text="Add", command=lambda: add_data14())
        editButton14 = ttk.Button(mainProject, text="Edit", state="disabled", command=lambda: edit_data14())
        deleteButton14 = ttk.Button(mainProject, text="Delete", state="disabled", command=lambda: delete_data14())

        # Place Treeview to fully occupy frame14 (except for the title)
        implementationPlanLabel.place(relx=0.01, rely=0.01)
        
        # Full-width and height minus a bit of margin for padding
        implementationPlanTable.place(relx=0.01, rely=0.10, relwidth=0.96, relheight=0.80)
        
        # Scrollbars aligned to right and bottom of the Treeview
        sb_y.place(relx=0.97, rely=0.10, relheight=0.80)
        sb_x.place(relx=0.01, rely=0.90, relwidth=0.96)

        
        # Define common positions for 5 columns (evenly spaced)
        positions = [0.02, 0.22, 0.42, 0.62, 0.82]

        # Labels
        critALabel.place(relx=positions[0], rely=0.65)
        raUnitLabel.place(relx=positions[1], rely=0.65)
        timeframeLabel.place(relx=positions[2], rely=0.65)
        budgetLabel.place(relx=positions[3], rely=0.65)
        budgSoLabel.place(relx=positions[4], rely=0.65)

        # Inputs (under each label)
        criticalAction.place(relx=positions[0], rely=0.70)
        respaccoUnit.place(relx=positions[1], rely=0.70)
        timeframe.place(relx=positions[2], rely=0.70)
        budget.place(relx=positions[3], rely=0.70)
        budgetSource.place(relx=positions[4], rely=0.70)

        addButton14.place(relx=0.4, rely=0.85, anchor="s")
        editButton14.place(relx=0.5, rely=0.85, anchor="s")
        deleteButton14.place(relx=0.6, rely=0.85, anchor="s")

        # Load data if available
        if len(p14criticalActions) == len(p14responsible) == len(p14timeline) == len(p14budget) == len(p14budgetsource):
            for ca, ra, tl, bdg, src in zip(p14criticalActions, p14responsible, p14timeline, p14budget, p14budgetsource):
                implementationPlanTable.insert("", "end", values=(ca, ra, tl, bdg, src))

        # Table logic
        def show_data14(a):
            criticalAction.delete("1.0", tk.END)
            respaccoUnit.delete("1.0", tk.END)
            timeframe.delete("1.0", tk.END)
            budget.delete("1.0", tk.END)
            budgetSource.delete("1.0", tk.END)
            selected_item = implementationPlanTable.selection()
            if selected_item:
                editButton14.config(state="normal")
                deleteButton14.config(state="normal")
                values = implementationPlanTable.item(selected_item[0])['values']
                criticalAction.insert("1.0", values[0])
                respaccoUnit.insert("1.0", values[1])
                timeframe.insert("1.0", values[2])
                budget.insert("1.0", values[3])
                budgetSource.insert("1.0", values[4])
            else:
                editButton14.config(state="disabled")
                deleteButton14.config(state="disabled")

        def add_data14():
            texts = [criticalAction.get("1.0", tk.END).strip(),
                     respaccoUnit.get("1.0", tk.END).strip(),
                     timeframe.get("1.0", tk.END).strip(),
                     budget.get("1.0", tk.END).strip(),
                     budgetSource.get("1.0", tk.END).strip()]
            if not all(texts):
                messagebox.showerror("Error", "Please fill out all fields")
                return
            item_id = implementationPlanTable.insert("", 'end', values=texts)
            undo_stack.append(("add", item_id))
            criticalAction.delete("1.0", tk.END)
            respaccoUnit.delete("1.0", tk.END)
            timeframe.delete("1.0", tk.END)
            budget.delete("1.0", tk.END)
            budgetSource.delete("1.0", tk.END)
            criticalAction.focus()

        def edit_data14():
            texts = [criticalAction.get("1.0", tk.END).strip(),
                     respaccoUnit.get("1.0", tk.END).strip(),
                     timeframe.get("1.0", tk.END).strip(),
                     budget.get("1.0", tk.END).strip(),
                     budgetSource.get("1.0", tk.END).strip()]
            if not all(texts):
                messagebox.showerror("Error", "Please fill out all fields")
                return
            selected_item = implementationPlanTable.selection()[0]
            old_values = implementationPlanTable.item(selected_item)['values']
            undo_stack.append(("edit", selected_item, old_values))
            implementationPlanTable.item(selected_item, values=texts)

        def delete_data14():
            selected_item = implementationPlanTable.selection()
            if selected_item:
                item_id = selected_item[0]
                old_values = implementationPlanTable.item(item_id)['values']
                undo_stack.append(("delete", item_id, old_values))
                implementationPlanTable.delete(item_id)
                criticalAction.delete("1.0", tk.END)
                respaccoUnit.delete("1.0", tk.END)
                timeframe.delete("1.0", tk.END)
                budget.delete("1.0", tk.END)
                budgetSource.delete("1.0", tk.END)
                editButton14.config(state="disabled")
                deleteButton14.config(state="disabled")

        def undo():
            if not undo_stack:
                return
            action, *data = undo_stack.pop()
            if action == "add":
                implementationPlanTable.delete(data[0])
            elif action == "edit":
                item_id, old_values = data
                implementationPlanTable.item(item_id, values=old_values)
            elif action == "delete":
                item_id, old_values = data
                implementationPlanTable.insert("", "end", iid=item_id, values=old_values)

        implementationPlanTable.bind("<<TreeviewSelect>>", show_data14)
        mainProject.bind("<Control-z>", lambda e: undo())
        mainProject.bind("<Control-Return>", lambda e: add_data14())

        # Navigation
        def back_13():
            global pageNumber
            pageNumber -= 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            page_13()

        def next_13():
            global pageNumber
            # Save data to global lists
            p14criticalActions.clear()
            p14responsible.clear()
            p14timeline.clear()
            p14budget.clear()
            p14budgetsource.clear()

            for item in implementationPlanTable.get_children():
                values = implementationPlanTable.item(item)['values']
                if len(values) == 5:
                    p14criticalActions.append(values[0])
                    p14responsible.append(values[1])
                    p14timeline.append(values[2])
                    p14budget.append(values[3])
                    p14budgetsource.append(values[4])

            save()
            pageNumber += 1
            for widget in mainProject.winfo_children():
                widget.destroy()
            page_15()

        btnBack14 = Button(mainProject, text="Back", width=10, command=back_13)
        btnNext14 = Button(mainProject, text="Next", width=10, command=next_13)
        btnBack14.place(relx=0.4, rely=0.90, anchor="s")
        btnNext14.place(relx=0.6, rely=0.90, anchor="s")


        #setup_page_common(14, "Policy Implementation Plan", frame14, widgets_to_destroy, back_13, next_13)
        ##try:
        ##    with open("page14_data.json", "r") as f:
        ##        data = json.load(f)
        ##        for item in data.get("plan", []):
        ##            implementationPlanTable.insert("", "end", values=item)
        ##except FileNotFoundError:
        ##    pass

    def page_15():
        global p7policyGoalsandObjectives, p7indicators
        global p15dataSources, p15frequency, p15responsible, p15output, p15report

        ### Progress indicator
        progress_label = tk.Label(mainProject, text="Page 15 of 15: Policy Assessment: Monitoring and Evaluation Plan", font=("Arial", 10), fg="gray")
        progress_label.place(relx=0.02, rely=0.90, anchor="nw")

        frame15 = tk.LabelFrame(mainProject)
        widgets_to_destroy = [frame15]
        undo_stack = []

        frame15.place(x=10, y=10, relwidth=0.98, relheight=0.6)

        policyAssessmentLabel = tk.Label(frame15, text="Policy Assessment: Monitoring and Evaluation Plan", font=("Arial", 12, "bold"))

        policyAssessmentTable = ttk.Treeview(frame15, selectmode="browse")
        policyAssessmentTable["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        policyAssessmentTable['show'] = 'headings'

        for i, col in enumerate(["Goals and Objectives", "SMART Indicators", "Sources of Data", "Data Collection Frequencies",
                                 "Unit-In-Charge", "M&E Outputs", "M&E Report Users"], 1):
            policyAssessmentTable.heading(str(i), text=col)
            policyAssessmentTable.column(str(i), anchor='center', width=180)

        sb_y = ttk.Scrollbar(frame15, orient="vertical", command=policyAssessmentTable.yview)
        sb_x = ttk.Scrollbar(frame15, orient="horizontal", command=policyAssessmentTable.xview)
        policyAssessmentTable.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)

        # Labels + Input Fields
        labels = [
            "Goal and Objective", "SMART Indicator", "Source of Data", "Data Collection Frequency",
            "Unit-In-Charge", "M&E Outputs", "M&E Report Users"
        ]
        fields = []
        positions = [0.02, 0.1633, 0.3067, 0.45, 0.5933, 0.7367, 0.88]
        for i, label in enumerate(labels):
            tk.Label(mainProject, text=label).place(relx=positions[i], rely=0.63)
            entry = scrolledtext.ScrolledText(mainProject, height=4, width=20)
            entry.place(relx=positions[i], rely=0.68)
            fields.append(entry)

        def clear_fields():
            for f in fields:
                f.delete("1.0", tk.END)
            fields[0].focus()

        def add_data15():
            values = [f.get("1.0", tk.END).strip() for f in fields]
            if not all(values[:2]):
                messagebox.showerror("Missing Fields", "Goals and SMART indicators are required.")
                return
            policyAssessmentTable.insert("", "end", values=values)
            p7policyGoalsandObjectives.append(values[0])
            p7indicators.append(values[1])
            p15dataSources.append(values[2])
            p15frequency.append(values[3])
            p15responsible.append(values[4])
            p15output.append(values[5])
            p15report.append(values[6])
            clear_fields()
            save()

        def edit_data15():
            selected = policyAssessmentTable.selection()
            if not selected:
                return
            values = [f.get("1.0", tk.END).strip() for f in fields]
            policyAssessmentTable.item(selected[0], values=values)
            index = policyAssessmentTable.index(selected[0])
            p7policyGoalsandObjectives[index] = values[0]
            p7indicators[index] = values[1]
            p15dataSources[index] = values[2]
            p15frequency[index] = values[3]
            p15responsible[index] = values[4]
            p15output[index] = values[5]
            p15report[index] = values[6]
            clear_fields()
            save()

        def show_data15(event):
            selected = policyAssessmentTable.selection()
            if selected:
                values = policyAssessmentTable.item(selected[0])["values"]
                for f, v in zip(fields, values):
                    f.delete("1.0", tk.END)
                    f.insert("1.0", v)

        def delete_data15():
            selected = policyAssessmentTable.selection()
            if not selected:
                return
            index = policyAssessmentTable.index(selected[0])
            policyAssessmentTable.delete(selected[0])
            del p7policyGoalsandObjectives[index]
            del p7indicators[index]
            del p15dataSources[index]
            del p15frequency[index]
            del p15responsible[index]
            del p15output[index]
            del p15report[index]
            clear_fields()
            save()

        add_btn = ttk.Button(mainProject, text="Add", command=add_data15)
        edit_btn = ttk.Button(mainProject, text="Edit", command=edit_data15)
        delete_btn = ttk.Button(mainProject, text="Delete", command=delete_data15)
        add_btn.place(relx=0.4, rely=0.85, anchor="s")
        edit_btn.place(relx=0.5, rely=0.85, anchor="s")
        delete_btn.place(relx=0.6, rely=0.85, anchor="s")

        policyAssessmentLabel.place(relx=0.01, rely=0.01)

        # Table maximized inside the frame
        policyAssessmentTable.place(relx=0.01, rely=0.10, relwidth=0.96, relheight=0.80)

        # Scrollbars aligned to the table's right and bottom
        sb_y.place(relx=0.97, rely=0.10, relheight=0.80)
        sb_x.place(relx=0.01, rely=0.90, relwidth=0.96)

        # Insert rows, filling missing p15 fields with ""
        max_rows = len(p7policyGoalsandObjectives)
        for i in range(max_rows):
            values = [
            p7policyGoalsandObjectives[i] if i < len(p7policyGoalsandObjectives) else "",
            p7indicators[i] if i < len(p7indicators) else "",
            p15dataSources[i] if i < len(p15dataSources) else "",
            p15frequency[i] if i < len(p15frequency) else "",
            p15responsible[i] if i < len(p15responsible) else "",
            p15output[i] if i < len(p15output) else "",
            p15report[i] if i < len(p15report) else "",
            ]
            policyAssessmentTable.insert("", "end", values=values)

        policyAssessmentTable.bind("<<TreeviewSelect>>", show_data15)

        def back_14():
            global pageNumber
            pageNumber -= 1
            for w in mainProject.winfo_children():
                w.destroy()
            save()
            page_14()

        def next_14():
            global pageNumber
            pageNumber += 1
            for w in mainProject.winfo_children():
                w.destroy()
            save()
            messagebox.showinfo("Done", "You have completed the policy planning process.")
            mainProject.destroy()
            save()
            save_pdf()
            new_project()

        btnBack14 = ttk.Button(mainProject, text="Back", command=back_14)
        btnNext14 = ttk.Button(mainProject, text="Finish", command=next_14)
        btnBack14.place(relx=0.4, rely=0.90, anchor="s")
        btnNext14.place(relx=0.6, rely=0.90, anchor="s")


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

def save():
    global pageNumber, save_json_file_path, p1projecttitle

    if save_json_file_path is None:
        save_json_file_path = asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON FILES", "*.json")],
            initialfile=p1projecttitle + ".json",
            title="Save Project As"
        )
    if not save_json_file_path:
        return

    # Dump data into JSON
    data = {
        "save_pdf_file_path": save_pdf_file_path,
        "save_json_file_path": save_json_file_path,
        "p1projecttitle": p1projecttitle,
        "p1analysts": p1analysts,
        "p1fontstyle": p1fontstyle,
        "p1policyanalysis": p1policyanalysis,
        "p1fontsize": p1fontsize,
        "p2problematicsituation": p2problematicsituation,
        "p2undesirableeffects": p2undesirableeffects,
        "p3efforts": p3efforts,
        "p3accomplishments": p3accomplishments,
        "p3assessments": p3assessments,
        "p5rootcause": p5rootcause,
        "p5existingpolicies": p5existingpolicies,
        "p5relevantprov": p5relevantprov,
        "p5accomplishments": p5accomplishments,
        "p5assessments": p5assessments,
        "p6policyproblem": p6policyproblem,
        "p6policyissue": p6policyissue,
        "p7policyGoalsandObjectives": p7policyGoalsandObjectives,
        "p7indicators": p7indicators,
        "p8stakeholders": p8stakeholders,
        "p8actors": p8actors,
        "p9altnum": p9altnum,
        "p9alternatives": p9alternatives,
        "p9stakeholderDataPerAlt": p9stakeholderDataPerAlt,
        "p10spillovers": p10spillovers,
        "p10externalities": p10externalities,
        "p10constraints": p10constraints,
        "p10mitimeasures": p10mitimeasures,
        "p11BPAdescription": p11BPAdescription,
        "p11BPAreasonSelect": p11BPAreasonSelect,
        "p12BPAspillover": p12BPAspillover,
        "p12BPAexternality": p12BPAexternality,
        "p12BPAconstraint": p12BPAconstraint,
        "p12BPAmitigatingmeasure": p12BPAmitigatingmeasure,
        "p13BPAwhat": p13BPAwhat,
        "p13BPAwho": p13BPAwho,
        "p13BPAhow": p13BPAhow,
        "p14criticalActions": p14criticalActions,
        "p14responsible": p14responsible,
        "p14timeline": p14timeline,
        "p14budget": p14budget,
        "p14budgetsource": p14budgetsource,
        "p15dataSources": p15dataSources,
        "p15frequency": p15frequency,
        "p15responsible": p15responsible,
        "p15output": p15output,
        "p15report": p15report
    }

    with open(save_json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
 
def save_pdf():
    # Generate the PDF

    global save_pdf_file_path, p1projecttitle, p1fontstyle, p1fontsize, p1policyanalysis, p1analysts, p2problematicsituation, p2undesirableeffects, p3efforts, p3accomplishments, p3assessments, p5accomplishments, p5assessments, p5existingpolicies, p5relevantprov, p6policyproblem, p6policyissue, p7policyGoalsandObjectives, p7indicators, p8stakeholders, p8actors, p9altnum, p9alternatives, p9stakeholderDataPerAlt, p10spillovers, p10externalities, p10constraints, p10mitimeasures, p11BPAdescription, p11BPAreasonSelect, p12BPAspillover, p12BPAexternality, p12BPAconstraint, p12BPAmitigatingmeasure, p13BPAwhat, p13BPAwho, p13BPAhow, p14budget, p14budgetsource, p14criticalActions, p14responsible, p14timeline, p15dataSources, p15frequency, p15responsible, p15output, p15report


    if save_pdf_file_path is None:
        save_pdf_file_path = asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile=p1projecttitle + ".pdf",
            title="Save PDF As"
        )

    if not save_pdf_file_path:
        return

    # Define page dimensions (A4 by default, landscape)
    PAGE_WIDTH, PAGE_HEIGHT = A4
    PAGE_WIDTH, PAGE_HEIGHT = PAGE_HEIGHT, PAGE_WIDTH  # Landscape orientation

    # Assume these variables are defined as in the original code
    # p1fontstyle, p1fontsize, p1projecttitle, p1policyanalysis, p1analysts, save_pdf_file_path, etc.

    try:
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Italic', 'ariali.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-BoldItalic', 'arialbi.ttf'))
        pdfmetrics.registerFontFamily('Arial',
                                      normal='Arial',
                                      bold='Arial-Bold',
                                      italic='Arial-Italic',
                                      boldItalic='Arial-BoldItalic')
    except Exception as e:
        print(f"Error registering Arial font: {e}. Please ensure 'arial.ttf', 'arialbd.ttf', 'ariali.ttf', and 'arialbi.ttf' are accessible.")
        # Fallback to Helvetica if Arial registration fails
        p1fontstyle = 'Helvetica'

    # Create PDF
    pdf = SimpleDocTemplate(
        save_pdf_file_path,
        pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        leftMargin=10*mm,
        rightMargin=10*mm,
        topMargin=15*mm,
        bottomMargin=15*mm
    )

    # Define styles
    title_style = ParagraphStyle(
        name='Title',
        fontName=p1fontstyle if p1fontstyle in ['Arial', 'Helvetica', 'Times'] else 'Helvetica',
        fontSize=int(p1fontsize) + 2,
        leading=int(p1fontsize) + 4,
        alignment=TA_LEFT
    )
    bold_style = ParagraphStyle(
        name='Bold',
        fontName=p1fontstyle if p1fontstyle in ['Arial', 'Helvetica', 'Times'] else 'Helvetica',
        fontSize=int(p1fontsize),
        leading=int(p1fontsize) + 2,
        alignment=TA_LEFT
    )
    normal_style = ParagraphStyle(
        name='Normal',
        fontName=p1fontstyle if p1fontstyle in ['Arial', 'Helvetica', 'Times'] else 'Helvetica',
        fontSize=int(p1fontsize),
        leading=int(p1fontsize) + 2,
        alignment=TA_LEFT,
        leftIndent=10
    )
    table_header_style = ParagraphStyle(
        name='TableHeader',
        fontName=p1fontstyle if p1fontstyle in ['Arial', 'Helvetica', 'Times'] else 'Helvetica',
        fontSize=int(p1fontsize),
        leading=int(p1fontsize) + 2,
        alignment=TA_CENTER
    )
    table_cell_style = ParagraphStyle(
        name='TableCell',
        fontName=p1fontstyle if p1fontstyle in ['Arial', 'Helvetica', 'Times'] else 'Helvetica',
        fontSize=int(p1fontsize) - 1,
        leading=int(p1fontsize) + 1,
        alignment=TA_LEFT
    )

    # Elements to build the PDF
    elements = []

    # Helper function to create tables
    def create_table(page_title, column_data, col_widths=None):
        elements.append(Paragraph(page_title, title_style))
        elements.append(Spacer(1, 5*mm))

        # Prepare table data
        columns = list(column_data.keys())
        max_rows = max(len(column_data[col]) for col in columns)
        table_data = [[Paragraph(col, table_header_style) for col in columns]]

        # Add rows
        for i in range(max_rows):
            row = [
                Paragraph(str(column_data[col][i]) if i < len(column_data[col]) else "", table_cell_style)
                for col in columns
            ]
            table_data.append(row)

        # Calculate column widths if not provided
        if col_widths is None:
            col_widths = [(PAGE_WIDTH - 20*mm) / len(columns)] * len(columns)

        # Create table
        table = Table(table_data, colWidths=col_widths)
        table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 5*mm))

    # Helper function to add section
    def add_section(page_title, content_dict):
        elements.append(Paragraph(page_title, title_style))
        elements.append(Spacer(1, 4*mm))

        for label, value in content_dict.items():
            if not value:
                continue
            elements.append(Paragraph(label, bold_style))
            if isinstance(value, list):
                for item in value:
                    elements.append(Paragraph(f"    {item}", normal_style))
            else:
                elements.append(Paragraph(f"    {value}", normal_style))
            elements.append(Spacer(1, 2*mm))

    # Page 1: Cover page
    estimated_content_height = (int(p1fontsize) + 4) * 3 # Roughly 3 lines with their leading

    # Calculate vertical spacing to push content to the center
    # PAGE_HEIGHT is used for vertical positioning
    vertical_spacer_height = (PAGE_WIDTH - estimated_content_height) / 4

    elements.append(Spacer(1, vertical_spacer_height))

    # All paragraph styles for the cover page should have TA_CENTER alignment
    cover_title_style = ParagraphStyle('CoverTitle', parent=title_style, alignment=TA_CENTER)
    cover_subtitle_style = ParagraphStyle('CoverSubtitle', parent=title_style, alignment=TA_CENTER)
    cover_normal_style = ParagraphStyle('CoverNormal', parent=normal_style, alignment=TA_CENTER)

    elements.append(Paragraph("Policy Analysis", cover_title_style))
    elements.append(Paragraph(p1policyanalysis, cover_subtitle_style))
    elements.append(Paragraph(p1analysts, cover_normal_style))


    elements.append(PageBreak())

    # Page 2
    add_section("Problematic Situation and Its Undesirable Effects", {
        "Problematic Situation": p2problematicsituation,
        "Undesirable Effects": p2undesirableeffects
    })
    elements.append(PageBreak())

    # Page 3
    create_table("Current Efforts", {
        "Current Efforts": p3efforts,
        "Accomplishments": p3accomplishments,
        "Assessments": p3assessments
    })
    elements.append(PageBreak())

    global analysis_type, p4summaryPDF, reg_sum
    # Page 4
    elements.append(Paragraph("Statistical Analysis", title_style))
    elements.append(Paragraph(f"Selected Statistical Method: {analysis_type}", bold_style))
    elements.append(Spacer(1, 0.2 * inch))

    if reg_sum.strip():
        elements.append(Preformatted(reg_sum, normal_style))
        elements.append(Spacer(1, 12))

    # Path to your saved image file
    image_path = "page4_plot.png"

    try:
        # Create an Image object
        # You might need to adjust width and height or use 'scale'
        # For example, to fit it within certain dimensions while maintaining aspect ratio:
        # img = Image(image_path, width=4*inch, height=3*inch, kind='proportional')
        # Or specify a fixed width/height and let ReportLab scale proportionally
        img = RLImage(image_path)
        if analysis_type == "Problem Tree Analysis":
            img.drawWidth = 3.5 * inch
            # Move image to the left by setting left alignment (x=0)
            img.hAlign = 'LEFT'
        else:
            img.drawWidth = 5.5*inch # Set desired width

        elements.append(img)
        elements.append(Spacer(1, 0.2 * inch)) # Add some space after the image

    except Exception as e:
        print(f"Error inserting image: {e}")
        # Optionally, add a placeholder text if image insertion fails
        elements.append(Paragraph("Image could not be loaded.", normal_style))
    
    elements.append(PageBreak())


    # Page 5
    elements.append(Paragraph("Root Cause and Existing Policies", title_style))
    elements.append(Spacer(1, 5*mm))
    elements.append(Paragraph("Root Cause", bold_style))
    elements.append(Paragraph(f"    {p5rootcause}", normal_style))
    elements.append(Spacer(1, 5*mm))
    # Table
    col_labels = ["Existing Policies", "Relevant Provisions", "Accomplishments", "Assessments"]
    col_data = [p5existingpolicies, p5relevantprov, p5accomplishments, p5assessments]
    create_table("", {label: data for label, data in zip(col_labels, col_data)})
    elements.append(PageBreak())

    # Page 6
    add_section("Policy Problem and Issue Statement", {
        "Policy Problem": p6policyproblem,
        "Policy Issue Statement": p6policyissue
    })
    elements.append(PageBreak())

    # Page 7
    create_table("Goals and Objectives of the Proposal", {
        "Policy Goals and Objectives": p7policyGoalsandObjectives,
        "Indicators": p7indicators
    })
    elements.append(PageBreak())

    # Page 8
    create_table("Stakeholders and Actors", {
        "Stakeholders": p8stakeholders,
        "Actors": p8actors
    })
    elements.append(PageBreak())

    # Page 9
    create_table("Policy Alternatives", {
        "Alternative Number": p9altnum,
        "Alternatives": p9alternatives
    })

    for i in enumerate(p9alternatives):
        # For each alternative, if stakeholder data exists, create a table for it
        if i[0] < len(p9stakeholderDataPerAlt):
            stakeholder_data = p9stakeholderDataPerAlt[i[0]]
            if stakeholder_data:  # Only add table if there is data
            # Transpose stakeholder_data into columns
                players = [row[0] for row in stakeholder_data]
                positions = [row[1] for row in stakeholder_data]
                motivations = [row[2] for row in stakeholder_data]
                sources = [row[3] for row in stakeholder_data]
                create_table(
                    f"Stakeholder Analysis for Alternative {i[0]+1}: {p9alternatives[i[0]]}",
                    {
                    "Players": players,
                    "Positions": positions,
                    "Motivations": motivations,
                    "Sources of Power": sources
                    }
                )
        
    elements.append(PageBreak())

    # Page 10
    elements.append(Paragraph("Assessment of Policy Alternatives", title_style))
    elements.append(Spacer(1, 5*mm))
    headers = ["Alternative", "Spillover", "Externalities", "Constraints", "Mitigating Measures"]
    columns = [p9alternatives, p10spillovers, p10externalities, p10constraints, p10mitimeasures]
    col_widths = [(PAGE_WIDTH - 20*mm) * w for w in [0.20, 0.20, 0.20, 0.20, 0.20]]
    create_table("", {header: col for header, col in zip(headers, columns)}, col_widths=col_widths)
    elements.append(PageBreak())

    # Page 11
    add_section("Best/Optimal Policy Alternative", {
        "Description": p11BPAdescription,
        "Reasons for Selection": p11BPAreasonSelect
    })
    elements.append(PageBreak())

    # Page 12
    add_section("Details of the Best/Optimal Policy Alternative", {
        "Spillover": p12BPAspillover,
        "Externality": p12BPAexternality,
        "Constraint": p12BPAconstraint,
        "Mitigating Measures": p12BPAmitigatingmeasure
    })
    elements.append(PageBreak())

    # Page 13
    add_section("Implementation Requirements", {
        "What type of legislation is needed? Why?": p13BPAwhat,
        "Who will implement? Why?": p13BPAwho,
        "Implementation Cost and Source": p13BPAhow
    })
    elements.append(PageBreak())

    # Page 14
    create_table("Policy Implementation Plan", {
        "Critical Actions": p14criticalActions,
        "Responsible/Accountable Units": p14responsible,
        "Timeframes": p14timeline,
        "Budgets": p14budget,
        "Budget Sources": p14budgetsource
    })
    elements.append(PageBreak())

    # Page 15
    elements.append(Paragraph("Monitoring and Evaluation Plan", title_style))
    elements.append(Spacer(1, 4*mm))
    create_table("", {"Goals and Objectives": p7policyGoalsandObjectives, 
                      "SMART Indicators": p7indicators, 
                      "Data Source": p15dataSources,
                      "Frequency": p15frequency,
                      "Units-In-Charge": p15responsible,
                      "M&E Output": p15output,
                      "M&E Report Users": p15report  
                      })

    # Build PDF
    pdf.build(elements)

def print_file():
    pdffilename = save_pdf_file_path
    print(pdffilename)
    os.startfile(pdffilename, 'print')
    
def print_file():

    pdffilename = p1projecttitle+".pdf"
    print(pdffilename)

    # Open input PDF file
    os.startfile(pdffilename, 'Print')

def quit():
    
    global pageNumber
    pageNumber = 0
    print(pageNumber)
    sys.exit()

menubar = Menu(root) 

file1 = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', font = ("Calibri", 12), menu = file1) 
file1.add_command(label ='Create New', font = ("Calibri", 12), command = lambda: new_project())
file1.add_command(label ='Open Project', font = ("Calibri", 12), command = lambda: open_project())
file1.add_command(label ='Save', font = ("Calibri", 12), command = lambda: save()) 
file1.add_command(label ='Print', font = ("Calibri", 12), command = lambda: print_file()) 
file1.add_separator() 
file1.add_command(label ='Help', font = ("Calibri", 12), command = lambda: help_page()) 
file1.add_command(label ='Exit', font = ("Calibri", 12), command = lambda: quit())

root.config(menu=menubar)

root.mainloop()
