from tkinter import *;
from tkinter import messagebox;
from tkinter import filedialog;


window= Tk();
window.title("Travel Destination");

frame= Frame(window, width=650, height=600);
frame.pack(fill="both", expand="True", padx=10, pady=10);
#__________________________Method_________________________________________#

def AboutShow():
        messagebox.showinfo("About:", "This application is Update. \nVersion: 8.12.1.1.012");

def LicenseShow():
        messagebox.showwarning("License:", "Application license: Free.\nVersion Premium is not activated.");
        
def ExitShow():
        value= messagebox.askokcancel("Exit:", "Want to exit the Application?");
        
        if(value==True):
            window.destroy();
            
def SaveAsShow():
        filedialog.asksaveasfile(title="Save As:", mode="w");
        
def NewShow():
        file= filedialog.askopenfile(title="New:", initialdir="C:/Users/Alejandro Molinar/Documents/Programming", filetypes=(("Text File", "*.txt"), ("Excel File", "*.xlsx"), ("All File", "*.*")));
        
       # photo=PhotoImage(file=file, frame);
       # img1=Label(frame, image=photo).pack();
    
    
#__________________________Menu_________________________________________#

menuBar=Menu(window);  #OJO tiene que estar em Menu ajuro en la Raiz#
window.config(menu=menuBar);

#_________Menu Items______________________#
menuFile=Menu(menuBar, tearoff=0);

menuFile.add_command(label="New", command=NewShow);
menuFile.add_command(label="Save");
menuFile.add_command(label="Save As", command=SaveAsShow);
menuFile.add_separator();
menuFile.add_command(label="Exit", command=ExitShow);

#_________Menu Items______________________#
menuEdit=Menu(menuBar, tearoff=0);

menuEdit.add_command(label="Undo");
menuEdit.add_command(label="Redo");
menuEdit.add_separator();
menuEdit.add_command(label="Copy");
menuEdit.add_command(label="Cut");
menuEdit.add_command(label="Paste");

#_________Menu Items______________________#
menuDesc=Menu(menuBar, tearoff=0);

menuDesc.add_command(label="Propeties");

#_________Menu Items______________________#
menuHel=Menu(menuBar, tearoff=0);

menuHel.add_command(label="License", command=LicenseShow);
menuHel.add_command(label="About", command=AboutShow);



menuBar.add_cascade(label="File", menu=menuFile);
menuBar.add_cascade(label="Edit", menu=menuEdit);
menuBar.add_cascade(label="Description", menu=menuDesc);
menuBar.add_cascade(label="Help", menu=menuHel);
#__________________________Check_________________________________________#
img=PhotoImage(file="images.png");
Label(frame, image=img).pack();

Label(frame, text="Activities \n").pack();
Checkbutton(frame, text="Beach").pack();
Checkbutton(frame, text="Mountain").pack();
Checkbutton(frame, text="Rural Tourism").pack();
#__________________________Radio_________________________________________#
 
Label(frame, text="\n\nCountry \n").pack();

Radiobutton(frame, text="España", value=1).pack();
Radiobutton(frame, text="Aruba", value=2).pack();
Radiobutton(frame, text="Maldivas", value=3).pack();


window.mainloop();