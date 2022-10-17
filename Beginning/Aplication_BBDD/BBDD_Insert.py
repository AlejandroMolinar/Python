from tkinter import *;
from BBDD_MYSQL import *;
import tkinter as ttk;

class BBDD_Insert():    
    def __init__(self, frame):
        
        bbdd= BBDD_MYSQL();
        
#----------------------------------------------Text Field--------------------------------------------------------------------------#

        self.label= Label(frame, text="Insert Item").grid(row=0, column=1, sticky="w");
        #---------------#
        
        self.nameTxt= Label(frame, text="Name: ").grid(row=1, column=0, padx=4, pady=4);
        self.name= Entry(frame);
        self.name.grid(row=1, column=1, padx=4, pady=4);
        
        #---------------#
        
        self.yearTxt= Label(frame, text="Year: ").grid(row=2, column=0, padx=4, pady=4);
        self.year= Entry(frame);     
        self.year.grid(row=2, column=1, padx=4, pady=4);
        
        #---------------#
        
        self.genderTxt= Label(frame, text="Gender").grid(row=3, column=0, padx=4, pady=4);
        self.gender= Entry(frame);
        self.gender.grid(row=3, column=1, padx=4, pady=4);
        
        #---------------#
        
        self.ageTxt= Label(frame, text="Age").grid(row=4, column=0, padx=4, pady=4);
        self.age= Entry(frame);
        self.age.grid(row=4, column=1, padx=4, pady=4);
        
        #---------------#
        
        self.sexTxt= Label(frame, text="Sex").grid(row=5, column=0, padx=4, pady=4);
        self.sex= Entry(frame);
        self.sex.grid(row=5, column=1, padx=4, pady=4);
        
        #---------------#
        
        self.childrenTxt= Label(frame, text="Children").grid(row=6, column=0, padx=4, pady=4);
        self.children= Entry(frame);
        self.children.grid(row=6, column=1, padx=4, pady=4);
        
        #---------------#
        
        self.regionTxt= Label(frame, text="Region").grid(row=7, column=0, padx=4, pady=4);
        self.region= Entry(frame);
        self.region.grid(row=7, column=1, padx=4, pady=4);
        
        #---------------#
        
        self.salaryTxt= Label(frame, text="Salary").grid(row=8, column=0, padx=4, pady=4);
        self.salary= Entry(frame);
        self.salary.grid(row=8, column=1, padx=4, pady=4);
        
        #---------------#
         
        def Panelnew():
            
            name= self.name.get();
            year= self.year.get();
            gender= self.gender.get();
            age= self.age.get();
            sex= self.sex.get();
            children= self.children.get();
            region= self.region.get();
            salary= self.salary.get();
            
            bbdd.Insert_Art(name, year, gender, age, sex, children, region, salary);
            
            
        
        send= Button(frame, text="Send", command=Panelnew);
        send.grid(row=9, column=2, padx=4, pady=4, sticky="s");
        
        delete= Button(frame, text="Delete");
        delete.grid(row=9, column=0, padx=4, pady=4, sticky="s");

        

    