import pickle;

class Car_Specification():

    def __init__(self, brand, model):     # Este es el contructor principal, se utliza para indentificar variables iniciales

        self.brand=brand;
        self.model=model;
        self.__largeChassis=5000;
        self.__broadChassis=1000;
        self.__wheel=4;
        self.__heigthChassis=2000;
        self.__startC=False;
        self.speedup=False;
        self.brakes=False;
       

    def startCar(self, start):
        self.__startC=start;

        if (self.startC):
            return "Car On";
        
        else:
            return "Car Off";
    
    def speedUp(self):
        return self.speedup==True;
        
        
    def brake(self):
        return self.brakes==True;
    
    def toString(self):
        print("Car specifications is Large: ", self.__largeChassis, ", Broad: ", self.__broadChassis, ", Wheels: ",
            self.__wheel, " and Heigth: ", self.__heigthChassis, ". Brand: ", self.brand, " and Model: ", self.model);

#___________________________________________________________________________________________________________________________________________

class Serialization():
    
    def __init__(self, list, band):    
        if(band):
            ExternalFile= open("CarEspecifications", "wb"); # Write Binary
            
            pickle.dump(list, ExternalFile);
            
            ExternalFile.close();
            
            del (ExternalFile); #Elimina el proceso de los procesos, en otras palabraslo cierra. 
    
        else:
            ExternalFile2= open("CarEspecifications", "rb"); # read Binary
            
            listCars= pickle.load(ExternalFile2);
            
            ExternalFile2.close();
            
            for list in listCars:
                print(list.toString());
            
            del (ExternalFile2); #Elimina el proceso de los procesos, en otras palabraslo cierra.


#___________________________________________________________________________________________________________________________________________

#class Moto(Car_Specification):
#    pass;

#moto=Moto().toString();


#___________________________________________________________________________________________________________________________________________

car1= Car_Specification("Tesla", "S");
car2= Car_Specification("Audi", "A5");
car3= Car_Specification("BMV", "M3");

listNames= [car1, car2, car3];

#Serialization(listNames, True);
Serialization(listNames, False);



