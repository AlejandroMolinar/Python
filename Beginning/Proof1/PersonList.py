import pickle;

class Person():
    def __init__(self, fName, uName, gender, age):
        
        self.fName=fName;
        self.uName=uName;
        self.gender=gender;
        self.age=age;
        
        print("Add Person: ", self.fName, " ", self.uName);
     
    def __str__(self):
        return "{}, {}, {}, {}".format(self.fName, self.uName, self.gender, self.age);
    
class ListPerson():
    personL=[];
    
    def __init__(self):
        
        ExternalFile= open("ListPersonEF", "ab+"); # append Binary
        ExternalFile.seek(0);
        
        try:
            self.personL= pickle.load(ExternalFile);
            print("{} people were loaded to External File".format(len(self.personL)));
        
        except:
            print("External File Empty");        

        
        finally:
            ExternalFile.close();
          
      
    
    def addPerson(self, person):
       
       self.personL.append(person);
       self.savePerson();
       
        
    def showPerson(self):
        
        print("\n\nPeople Add:\n")
        ExternalFile2= open("ListPersonEF", "rb"); # read Binary
             
        listPeople= pickle.load(ExternalFile2);
        
        ExternalFile2.close();
        
        for list in listPeople:
            print(list);
        
        del (ExternalFile2); #Elimina el proceso de los procesos, en otras palabraslo cierra.
        
    def savePerson(self):
        
       ExternalFile3= open("ListPersonEF", "wb"); # Write Binary
           
       pickle.dump(self.personL, ExternalFile3);
          
       ExternalFile3.close();            
        
       del (ExternalFile3);
  


myList=ListPerson();


person1= Person("Andrea", "Armas", "Femenino", 30);
myList.addPerson(person1);

person2= Person("Raquel", "Mercado", "Femenino", 29);
myList.addPerson(person2);

person3= Person("Raquel", "Torres", "Femenino", 52);
myList.addPerson(person3);

myList.showPerson();



