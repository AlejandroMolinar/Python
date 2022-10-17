import sqlite3;

connection=sqlite3.connect("BBDD_Test");

pointer=connection.cursor();

#pointer.execute("Create table Products (NamePro varchar(50), Precio int, Seccion varchar(50))")

#pointer.execute("Insert into Products values ('Balon', 15, 'Deportes')"); 
#pointer.executemany("Insert into Products values (?, ?, ?)");

#pointer.execute('''
#    Create table Products (
#    IDPro varchar(10) Primary Key,
#    NamePro varchar(50), 
#    Precio int, 
#    Seccion varchar(50))
##''');

product=[
    
    ("AR1","Ball", 15, "Sport"),
    ("AR2","Racket", 30, "Sport"),
    ("AR3","Tights", 7, "Clothing"),
    ("AR4","Hammer", 15, "Tools")
    
    
]

pointer.executemany("Insert into Products values (?, ?, ?, ?)", product);

connection.commit();