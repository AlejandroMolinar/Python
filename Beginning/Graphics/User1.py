from tkinter import *;
import tkinter as tk;



class User():    
    def __init__(self, frame):
        
        userU= StringVar();
        fNameU= StringVar();
        uNameU= StringVar();
        ageU= StringVar();
        descU= StringVar();
         
        label= Label(frame, text="Hello World").grid(row=0, column=1, sticky="w");
        #---------------#
        
        userTxt= Label(frame, text="User: ").grid(row=1, column=0, padx=4, pady=4);
        user= Entry(frame);
        user.grid(row=1, column=1, padx=4, pady=4);
        
        #---------------#
        
        passwordTxt= Label(frame, text="Password: ").grid(row=2, column=0, padx=4, pady=4);
        password= Entry(frame);     
        password.grid(row=2, column=1, padx=4, pady=4);
        password.config(show="*");
        #---------------#
        
        fNameTxt= Label(frame, text="First Name: ").grid(row=3, column=0, padx=4, pady=4);
        fName= Entry(frame);
        fName.grid(row=3, column=1, padx=4, pady=4);
        
        #---------------#
        
        uNameTxt= Label(frame, text="Last Nombre: ").grid(row=4, column=0, padx=4, pady=4);
        uName= Entry(frame);
        uName.grid(row=4, column=1, padx=4, pady=4);
        
        #---------------#
        
        ageTxt= Label(frame, text="Age : ").grid(row=5, column=0, padx=4, pady=4);
        age= Entry(frame);
        age.grid(row=5, column=1, padx=4, pady=4);
        
        #---------------#
        
        description= Label(frame, text="Description").grid(row=6, column=0, padx=4, pady=4);
        descriptionArea= Text(frame, width=16, height=8);
        descriptionArea.grid(row=6, column=1, padx=4, pady=4);
        
        #---------------#
        
        scroller= Scrollbar(frame, command=descriptionArea.yview);
        scroller.grid(row=6, column=2, padx=4, pady=4,  sticky="nsew");
        #---------------#
        
        descriptionArea.config(yscrollcommand=scroller.set);
        #---------------#
        
        def Panelnew():
            
            userU.set(user.get());
            fNameU.set(fName.get());
            uNameU.set(uName.get());
            ageU.set(age.get());
            descU.set(descriptionArea.get("1.0", END));
            
            
            
            print("Date: \nUser:", userU.get(), "\nFirst Name:", fName.get(), "\nLast Name:", uName.get(), "\nAge:", ageU.get(), "\nDescription:", descU.get());
        
        button= Button(frame, text="Send", command=Panelnew);
        button.grid(row=7, column=1, sticky="s");
        
        
    def printUser(self, user, fName, uname):
        
        print("Hello, {} {} your User is: {}".format(fName, uname, user));
      
# _____________________Main______________________________


window= Tk();
window.title("User");

frame= Frame(window, width=650, height=600);
frame.pack(fill="both", expand="True", padx=10, pady=10);

User(frame);


window.mainloop();
        

    