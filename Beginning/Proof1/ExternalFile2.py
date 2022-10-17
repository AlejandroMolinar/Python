import pickle;
from _io import open

listNames= ["Raquel", "BellaRaquelita", "Andrea", "Nataly", "Valentina"];

ExternalFile= open("ExFile2", "wb"); # Write Binary

pickle.dump(listNames, ExternalFile);

ExternalFile.close();

del (ExternalFile); #Elimina el proceso de los procesos, en otras palabraslo cierra. 


# ____________________Load to File____________________________________


ExternalFile2= open("ExFile2", "rb"); # read Binary

print(pickle.load(ExternalFile2));

ExternalFile2.close();

del (ExternalFile2); #Elimina el proceso de los procesos, en otras palabraslo cierra.
 