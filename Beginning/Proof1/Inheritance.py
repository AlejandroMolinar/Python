class Persona():
    
    def __init__(self, name, age, placeResidence):
        
        self.name=name;
        self.age=age;
        self.placeResidence=placeResidence;
        
    def description(self):
        print("Name: ", self.name, "\nAge: ", self.age, "\nPLace Of Residence: ", self.placeResidence);

class Empleado(Persona):
    
    def __init__(self, salary, antiguaty, name, age, placeResidence):
        
        super().__init__(self, name, age, placeResidence);
        self.salary=salary;
        self.antiguaty=antiguaty;
        self.name=name;
        self.age=age;
        self.placeResidence=placeResidence;
        
    
    def description(self):
       
       Persona.description(self);   
       print("\nSalario: ", self.salary, "\nAntiguaty: ", self.antiguaty); 
        

Alberto= Empleado("1000", "20", "Alberto Rodriguez", "40", "Spain");