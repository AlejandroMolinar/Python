from tkinter import *;
from BBDD_MYSQL import *;
from tkinter.ttk import Separator;

class BBDD_Select():    
    def __init__(self, frame):
        
        bbdd= BBDD_MYSQL(frame);
#----------------------------------------------Text Field--------------------------------------------------------------------------#

        def ReadItem():
            
            n1= self.ID.get();
            
            bbdd.Select_Art(n1);
        
        def ReadAll():
            
            bbdd.Select_ALL();
            
            
    #--------------------------------Select Item----------------------------------------#     
        self.label= Label(frame, text="Read by ID").grid(row=0, column=0);
        #---------------#
        
        self.IDTxt= Label(frame, text="ID: ").grid(row=1, column=0, padx=4, pady=4);
        self.ID= Entry(frame);
        self.ID.grid(row=1, column=0, padx=4, pady=4);
        
        #---------------#
        send= Button(frame, text="Send", command=ReadItem);
        send.grid(row=3, column=0, padx=10, pady=10);
        
        
        self.separate= Separator(frame, orient='horizontal');
        self.separate.place(relx=0, rely=0.6, relwidth=1, relheight=1)
        
    #--------------------------------Select All----------------------------------------#   
        self.label= Label(frame, text="Read All").grid(row=8, column=0);
        #---------------#
        
        sendAll= Button(frame, text="Read All", command=ReadAll);
        sendAll.grid(row=10, column=0, padx=4, pady=4);
        

    