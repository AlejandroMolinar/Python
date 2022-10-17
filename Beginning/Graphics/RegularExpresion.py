from tkinter import *;
from tkinter import messagebox;
import re;

class FindTxt():
    def __init__(self, frame):
        
        desFind= StringVar();
        
        catTxt= ("El gato doméstico​​, llamado popularmente gato, y de forma coloquial minino," 
            "michino, michi,​ micho,   ​ mizo, miz, morroño​ o morrongo, entre otros nombres,"
            "es un mamífero carnívoro de la familia Felidae.  Es una subespecie domesticada por"
            "la convivencia   con el ser humano.");
            
        dogTxt= '''El perro, ​​​ llamado perro doméstico o can, ​ y en algunos lugares coloquialmente llamado chucho,
            tuso, ​ choco, ​ entre otros; es un mamífero carnívoro de la familia de los cánidos, que constituye 
            una especie del género Canis.''';
        
        def FindAction():
            
            word= self.find.get();
            
            wordFind= re.search(word, catTxt);
            
            print(word, wordFind);
            
            if wordFind!=None:
                value= messagebox.askokcancel("Find:", "The Word(s) '{}' is in the Text".format(word));
                
            else:
                values= messagebox.askokcancel("No Find:", "The Word(s) '{}' is not found in the Text".format(word));
        
        
        self.label= Label(frame, text="Find Text")
        self.label.grid(row=0, column=1, sticky="w");
        
        self.description= Label(frame, text="Description").grid(row=2, column=0, padx=4, pady=4);
        self.descriptionArea= Text(frame, width=50, height=10);
        self.descriptionArea.grid(row=2, column=1, padx=4, pady=4);
        self.descriptionArea.insert(0.1, catTxt);
        
        
        #---------------#
        
        self.scroller= Scrollbar(frame, command=self.descriptionArea.yview);
        self.scroller.grid(row=2, column=2, padx=4, pady=4,  sticky="nsew");
        #---------------#
        
        self.descriptionArea.config(yscrollcommand=self.scroller.set);
        
        self.findTxt= Label(frame, text="User: ").grid(row=4, column=0, padx=4, pady=4);
        self.find= Entry(frame);
        self.find.grid(row=4, column=1, padx=4, pady=4);
        
        self.send= Button(frame, text="Send", command=FindAction);
        self.send.grid(row=7, column=1, sticky="s");
        


window= Tk();
window.title("User");

frame= Frame(window, width=650, height=600);
frame.pack(fill="both", expand="True", padx=30, pady=30);

FindTxt(frame);


window.mainloop();

#-------------------------------------------------------Meta CAracteres--------------------------------------------------------------------#

ListEmployer= [
        "VELÁSQUEZ ANTONIO",
        "VÁSQUEZ EDGAR ",
        "ROMERO ÁNGEL",
        "MARTÍNEZ CARLOS",
        "MARTÍNEZ IRIS",
        "GRAEF ALICIA",
        "CARDIEL MARIO",
        "BURGOS RUBÉN",
    ];

for employ in ListEmployer:
    
    #----------------Para que busque la palabra al principio de cada nombre-------------------------#
    if re.findall("^MARTÍNEZ", employ):
    
        print(employ);

    #----------------Para que busque la palabra al final de cada nombre-------------------------#

    elif re.findall("RUBÉN", employ):
    
        print(employ);
        
    #----------------Para que busque las palabras que contengan dicha letra-------------------------#
    
    if re.findall("[ñ]", employ):
    
        print(employ);
        
    #----------------Para que busque las palabras que contengan dicha letra, pero puede ser una u otra-------------------------#
    
    if re.findall("niñ[oa]s", employ):
    
        print(employ);
    
    #----------------Para que busque las palabras Con un rango especifico-------------------------#
    
    if re.findall("[o-t]", employ):
    
        print(employ);
    
    elif re.findall("^[B-N]", employ):      #Inicio y MAyus
    
        print(employ);
        
    elif re.findall("[^P-Y]$", employ):      #Final y Negacion del Rango
    
        print(employ);
        
    elif re.findall("[.:;]$", employ):      #Signos
    
        print(employ);

    elif re.findall("[0-4A-C    ]$", employ):      #Final y Negacion del Rango
    
        print(employ);



          