import pymysql;
from tkinter import messagebox;

class BBDD_MYSQL():
    def __init__(self, frame):
        
        self.connection= pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db="test"
            );
            
        self.pointer= self.connection.cursor();
        
        self.frame= frame;
#--------------------------------------------------------- Insert Clients -------------------------------------------------------------------------------------#    
    def Insert_Art(self, Name, Year, Gender, Age, Sex, Children, Region, Salary):
         
        try:
            self.pointer.execute("INSERT INTO person_details (Name, Year, Gender, Age, Sex, Children, Region, Salary)"''' 
                '''"VALUES ('{}', '{}', '{}', '{}', {}, '{}', '{}' , '{}')".format(Name, Year, Gender, Age, Sex, Children, Region, Salary));
            self.connection.commit();
            
            messagebox.showinfo("About:","Element inserted successfully");
            
        except Exception as e:
            raise;
        
        
#--------------------------------------------------------- Select Clients -------------------------------------------------------------------------------------#    
    def Select_Art(self, ID):
         
        try:
            self.pointer.execute("SELECT * FROM person_details WHERE ID = {}".format(ID));
            
            user= self.pointer.fetchone();      #Para buscar un objeto especifico en la tabla, Fetch ONE

            print("Person Details: \nID: ", user[0]);
            print("Name: ", user[1]);
            print("Year: ", user[2]);
            print("Gender : ", user[3]);
            print("Age: ", user[4]);
            print("Sex: ", user[5]);
            print("Children: ", user[6]);
            print("Region: ", user[7]);
            print("Salary: ", user[8]);
            
                    
        except Exception as e:
            raise;
    

#--------------------------------------------------------- Select ALL Clients -------------------------------------------------------------------------------------#    
    def Select_ALL(self):
         
        try:
            self.pointer.execute("SELECT * FROM person_details");
            
            users= self.pointer.fetchall();       #Para buscar un objeto especifico en la tabla, Fetch ALL
            
            for user in users:
                
                print("Person Details: \nID: ", user[0]);
                print("Name: ", user[1]);
                print("Year: ", user[2]);
                print("Gender : ", user[3]);
                print("Age: ", user[4]);
                print("Sex: ", user[5]);
                print("Children: ", user[6]);
                print("Region: ", user[7]);
                print("Salary: ", user[8]);
                print("-----------------------------------------\n");
            
                    
        except Exception as e:
            raise;
 
 
#--------------------------------------------------------- Update Clients -------------------------------------------------------------------------------------#    
    def Update_Art(self, Name, Year, Gender, Age, Sex, Children, Region, Salary, ID):
         
         
        try:
            self.pointer.execute("UPDATE person_details SET Name= '{}', Year= '{}', Gender= '{}',"'''
            '''"age= '{}', sex= '{}', children= '{}', region= '{}', Salary= '{}' WHERE ID= '{}'".format(Name, Year, Gender, Age, Sex, Children, Region, Salary, ID));
            
            
            messagebox.showinfo("About:","Person Details or updated successfully:");

            
            self.connection.commit();       #Para guardar los cambios en la lista
                    
        except Exception as e:
            raise;


#--------------------------------------------------------- Delete Clients -------------------------------------------------------------------------------------#    
    def Delete_Art(self, ID):
         
         
        try:
            self.pointer.execute("DELETE FROM person_details WHERE ID = '{}'".format(ID));
            
            
            messagebox.showinfo("About:","Person Details or Deleted successfully:");
            
            self.connection.commit();       #Para guardar los cambios en la lista
                    
        except Exception as e:
            raise;
    
    def Close(self):
        
        self.connection.close();



