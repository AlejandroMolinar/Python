from tkinter import *;


root=Tk();

root.title("Windows");
#root.resizable(width, height);        Esta linea bloquea la redimencion de la ventana.
#root.iconbitmap(bitmap, default);     Para Cambiar el Icono 
#root.config(bg="cian");               Cambiar el color de la Ventana

# _____________________Frame______________________________

frame= Frame(root, width=650, height=350);
frame.pack(fill="both", expand="True", padx=10, pady=10); 

#frame.pack(side="right", anchor="n");       #Para establecer una localizacion del frame en el Panel
#frame.config(bg="blue");

    #Rellena el Frame en el Panel

#frame.config(bd="35");                     #tipo de borde
#frame.config(relief="sunken");              #agrega el borde

# _____________________Label______________________________
#.place(x=50, y=50) Lugar en el Frame

nameU= StringVar();


label= Label(frame, text="Hello World").grid(row=0, column=1, sticky="w");
#---------------#

userTxt= Label(frame, text="User: ", ).grid(row=1, column=0, padx=4, pady=4);
user= Entry(frame, textvariable = nameU).grid(row=1, column=1, padx=4, pady=4);
#---------------#

passwordTxt= Label(frame, text="Password: ").grid(row=2, column=0, padx=4, pady=4);
password= Entry(frame);
password.grid(row=2, column=1, padx=4, pady=4);
password.config(show="*");
#---------------#

fNameTxt= Label(frame, text="First Name: ").grid(row=3, column=0, padx=4, pady=4);
fName= Entry(frame).grid(row=3, column=1, padx=4, pady=4);
#---------------#

uNameTxt= Label(frame, text="Last Nombre: ").grid(row=4, column=0, padx=4, pady=4);
uName= Entry(frame).grid(row=4, column=1, padx=4, pady=4);
#---------------#

ageTxt= Label(frame, text="Age : ").grid(row=5, column=0, padx=4, pady=4);
age= Entry(frame).grid(row=5, column=1, padx=4, pady=4);
#---------------#

description= Label(frame, text="Description").grid(row=6, column=0, padx=4, pady=4);
descriptionArea= Text(frame, width=16, height=8);
descriptionArea.grid(row=6, column=1, padx=4, pady=4);
#---------------#

scroller= Scrollbar(frame, command=descriptionArea.yview);
scroller.grid(row=6, column=2, padx=4, pady=4,  sticky="nsew");
#---------------#

descriptionArea.config(yscrollcommand=scroller.set);

#imageF=PhotoImage(file="twitch.png");
#Label(frame, image=imageF).place(x=200, y=200);
def send():
    
    nameU.set("Halepepe");



button= Button(frame, text="Send", command=send);
button.grid(row=6, column=1, sticky="s");








root.mainloop();





