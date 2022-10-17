from tkinter import *;
from BBDD_MYSQL import *;

class BBDD_Delete():    
    def __init__(self, frame):
        
        bbdd= BBDD_MYSQL(frame);
#----------------------------------------------Text Field--------------------------------------------------------------------------#
        self.label= Label(frame, text="Delete by ID").grid(row=0, column=0);
        #---------------#
        
        self.IDTxt= Label(frame, text="ID: ").grid(row=1, column=0, padx=4, pady=4);
        self.ID= Entry(frame);
        self.ID.grid(row=1, column=0, padx=4, pady=4);
         
         
        def Panelnew():
            
            ID= self.ID.get();
            
            bbdd.Delete_Art(ID);
            
            
        
        delete= Button(frame, text="Delete Items", command=Panelnew);
        delete.grid(row=2, column=0, padx=4, pady=4, sticky="s");
        

    