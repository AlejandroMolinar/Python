from _io import open;


# ------Write-------

externalFile= open("ExFile.txt", "w");

externalFile.write("Me gustan los melones y los bollos, estan sabrosos. Guino Guino");

externalFile.close();

# ------Write-------

externalFile= open("ExFile.txt", "a");

externalFile.write("\nTambien me gusta los melocotones y los duraznos, que tal? Guino Guino");

externalFile.close();

# ------Read-------

externalFile2= open("ExFile.txt", "r");

text= externalFile2.read();

externalFile2.close();

print(text);

# ------ReadLine-------

#text= externalFile2.readlines();

#externalFile2.close();

#print(text);

# ------Lectura/Escritura-----

externalFile4= open("ExFile.txt", "r+");

externalFile4.seek(1); #mueve el puntero. 
externalFile.write("Cada dia que te miro me vuelve loco tu figura, cuadrado uwu");

externalFile4.seek(0);
text= externalFile4.read();

externalFile4.close();

print(text);