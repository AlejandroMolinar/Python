from tkinter import *;
from tkinter import messagebox;
from BBDD_Insert import *;
from BBDD_Select import *;
from BBDD_Update import *;
from BBDD_Delete import *;

class Index():    
    def __init__(self, frame, menuBar, window):
        
#----------------------------------------------Actions--------------------------------------------------------------------------#

        def CreateObj():
            
            frameCreate= Frame(window, width=650, height=600);
            frameCreate.pack(fill="both", expand="True", padx=20, pady=20);
            
            BBDD_Insert(frameCreate);            
            frame.destroy();
            
        def ReadObj():
            
            frameRead= Frame(window, width=650, height=600);
            frameRead.pack(fill="both", expand="True", padx=20, pady=20);
            
            BBDD_Select(frameRead);            
            frame.destroy();
            
        def UpdateObj():
            
            frameUpdate= Frame(window, width=650, height=600);
            frameUpdate.pack(fill="both", expand="True", padx=20, pady=20);
            
            BBDD_Update(frameUpdate);            
            frame.destroy();
            
        def DeleteObj():
            
            frameDelete= Frame(window, width=650, height=600);
            frameDelete.pack(fill="both", expand="True", padx=40, pady=40);
            
            BBDD_Delete(frameDelete);            
            frame.destroy();
            
        def ExitFrame():
            
            value= messagebox.askokcancel("Exit:", "Want to exit the Application?");
        
            if(value==True):
                window.destroy();
            
        
#----------------------------------------------Menu--------------------------------------------------------------------------#
        
        #_________Menu Items______________________#
        menuInsert=Menu(menuBar, tearoff=0);
        
        menuInsert.add_command(label="New Object", command=CreateObj);
        
        
        #_________Menu Items______________________#
        menuSelect=Menu(menuBar, tearoff=0);
        
        menuSelect.add_command(label="Read Object", command=ReadObj);
        
        
        #_________Menu Items______________________#
        menuUpdate=Menu(menuBar, tearoff=0);
        
        menuUpdate.add_command(label="Update Object", command=UpdateObj);
        
        
        #_________Menu Items______________________#
        menuDelete=Menu(menuBar, tearoff=0);
        
        menuDelete.add_command(label="Delete Object", command=DeleteObj);
        
        
        #_________Menu Items______________________#
        menuHel=Menu(menuBar, tearoff=0);
        
        menuHel.add_command(label="Exit", command=ExitFrame);
        
        menuBar.add_cascade(label="Create", menu=menuInsert);
        menuBar.add_cascade(label="Read", menu=menuSelect);
        menuBar.add_cascade(label="Update", menu=menuUpdate);
        menuBar.add_cascade(label="Delete", menu=menuDelete);
        menuBar.add_cascade(label="Help", menu=menuHel);
        
        
        self.label= Label(frame, text="Person Details DataBase").grid(row=1, column=2, padx=4, pady=4, sticky="w");
        
        self.label2= Label(frame, text="You Want To Do?").grid(row=3, column=2, padx=4, pady=4, sticky="s");

        
       
# _____________________Main______________________________


window= Tk();
window.title("User");

frame= Frame(window, width=650, height=600);
frame.pack(fill="both", expand="True", padx=50, pady=50);

menuBar=Menu(window);  #OJO tiene que estar em Menu ajuro en la Raiz#
window.config(menu=menuBar);

Index(frame, menuBar, window);




window.mainloop();
        

    