
def comprobate(emails):
    
    arrob=False;
    point=False;
    
    for ils in email:
        
        if(ils=="@"):
            arrob=True;
        
        if(ils=="."):
            point=True;

    if(arrob==True and point==True):
        print("Verified Email.");
        
    elif(arrob==False or point==False):
        print("Email not verified");
            
        
email=input("Introduce Email: ");
comprobate(email);

#Modularizacion

#  Para importat dodas las variables y metodos de una clase a otra lo unico que se tiene hacer es lo siguiente

# from "Nombre de la clase a importar" import * --> el asterisco quiere decir que importaras todos lo metos y variables de la clase.   
    
    
    
    
    