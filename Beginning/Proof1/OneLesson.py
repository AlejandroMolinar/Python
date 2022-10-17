import math;

array=["Pepe", "Maria", "Juan", "Andrea"]*4;  # Repetira la lista 4 veces por '*4'
 

print(array);



tupla= ("andrea", 12, 433.43, 1);
print(tupla);

print(12 in tupla); #verificar si existe un determinado elemento en la lista

print(len(tupla)); #imprime la cantidad de elementos en la lista


#diccionario
dicc={"Nombre":"Alejandro", "Apellido":"Molinar", "Edad":22, "Profesion":"Ingeniero", "Nacimiento":[17, 6, 1999]};


#nota1=input("Ingresa la Nota 1");

#nota2=input("Ingresa la Nota 2");


def recepcionDatos(nota_1 , nota_2):

    return (nota_1+nota_2)/2;


#print(recepcionDatos(int(nota1), int(nota2)));

for i in["Primavera", "Otoño", "Invierno", "Verano"]:   
    print(i);

for e in "paralelepipedo":   #Repetirá el "hola" cuantas veces tenga la palabra en el for, tambien se puede utilizar len()
    print("Hola");

for g in len("paralelepipedo"):   #Repetirá el "hola" cuantas veces tenga la palabra en el for, tambien se puede utilizar len()
    print("Hola");

for j in range(6):          #Repetirá el bucle cuantas veces diga el número adentro del "range"

    print("Hola" + str(j));

for k in range(5, 50, 3):           #Este for comenzará en 5 y terminara en 50, e irá de tres en tres (5 <Inicio>, 50 <Final>, 3 <saltos cada>)

    print(f"Valor: {k}");           #La "f" del print es para que se pueda agregar una variable al texto
    respuesta=math.sqrt(numero);

