import pymysql;

class BBDD_MYSQL:
    def __init__(self):
        
        self.connection= pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db="test"
            );
            
        self.pointer= self.connection.cursor();
        
        
#--------------------------------------------------------- Insert Clients -------------------------------------------------------------------------------------#    
    def Insert_Art(self, CÓDIGOCLIENTE, EMPRESA, DIRECCIÓN, POBLACIÓN, TELÉFONO, RESPONSABLE, HISTORIAL):
         
        try:
            self.pointer.execute("INSERT INTO clientes (CÓDIGOCLIENTE, EMPRESA, DIRECCIÓN, POBLACIÓN, TELÉFONO, RESPONSABLE, HISTORIAL)"''' 
                '''"VALUES ('{}', '{}', '{}', '{}', {}, '{}', '{}' )".format(CÓDIGOCLIENTE, EMPRESA, DIRECCIÓN, POBLACIÓN, TELÉFONO, RESPONSABLE, HISTORIAL));
            self.connection.commit();
            
            print("Element inserted successfully");
            
        except Exception as e:
            raise;
        
        
#--------------------------------------------------------- Select Clients -------------------------------------------------------------------------------------#    
    def Select_Art(self, ID):
         
        try:
            self.pointer.execute("SELECT * FROM clientes WHERE CÓDIGOCLIENTE = '{}'".format(ID));
            
            user= self.pointer.fetchone();      #Para buscar un objeto especifico en la tabla, Fetch ONE
            
            print("Client: \nItem Code: ", user[0]);
            print("Company: ", user[1]);
            print("Address: ", user[2]);
            print("Population : ", user[3]);
            print("Phone: ", user[4]);
            print("Responsible: ", user[5]);
            
                    
        except Exception as e:
            raise;
    

#--------------------------------------------------------- Select ALL Clients -------------------------------------------------------------------------------------#    
    def Select_ALL(self):
         
        try:
            self.pointer.execute("SELECT * FROM clientes");
            
            users= self.pointer.fetchall();       #Para buscar un objeto especifico en la tabla, Fetch ALL
            
            for user in users:
                
                print("Client: \nItem Code: ", user[0]);
                print("Company: ", user[1]);
                print("Address: ", user[2]);
                print("Population : ", user[3]);
                print("Phone: ", user[4]);
                print("Responsible: ", user[5]);
                print("-----------------------------------------\n");
            
                    
        except Exception as e:
            raise;
 
 
#--------------------------------------------------------- Update Clients -------------------------------------------------------------------------------------#    
    def Update_Art(self, ID, phone, responsible):
         
         
        try:
            self.pointer.execute("UPDATE clientes SET TELÉFONO= {}, RESPONSABLE= '{}' WHERE CÓDIGOCLIENTE = '{}'".format(phone, responsible, ID));
            
            
            print("Client or updated successfully:");
            
            self.connection.commit();       #Para guardar los cambios en la lista
                    
        except Exception as e:
            raise;


#--------------------------------------------------------- Delete Clients -------------------------------------------------------------------------------------#    
    def Delete_Art(self, ID):
         
         
        try:
            self.pointer.execute("DELETE FROM clientes WHERE CÓDIGOCLIENTE = '{}'".format(ID));
            
            
            print("Client Deleted successfully:");
            
            self.connection.commit();       #Para guardar los cambios en la lista
                    
        except Exception as e:
            raise;
    
    def Close(self):
        
        self.connection.close();


bbdd= BBDD_MYSQL();
#bbdd.Select_Art("CT09");

#bbdd.Insert_Art("CT41", "Banco Santander", "Chueca", "Madrid", 954543244, "Alejandro Molinar", "null");
#bbdd.Insert_Art("CT42", "Banco Santander", "Chueca", "Madrid", 954543244, "Alejandro Molinar", "null");

bbdd.Delete_Art("CT42");

#bbdd.Update_Art("CT24", 954549234, "MANUELA GUERRA");
bbdd.Select_ALL();


bbdd.Close();





