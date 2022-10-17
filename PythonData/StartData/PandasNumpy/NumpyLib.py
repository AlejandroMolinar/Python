import numpy as np;

#===============================================================================
#     Matrices
#===============================================================================
valoration= np.array( [ [4,9,1,0], [2,5,1,0], [6,5,9,3] ] );

valorationXYZ= np.array( [ [[4,9,1,0], [2,5,1,0], [6,5,9,3]], [[4,9,1,0], [2,5,1,0], [6,5,9,3]], [[4,9,1,0], [2,5,1,0], [6,5,9,3]] ] );

"""
#===============================================================================
#     Matriz 2 dimensiones
#===============================================================================

print(valoration);  

print(valoration[1][2]);                                        # '[1]'= Filas / '[2]'=columnas 
print(valoration[0,3]); 

#===============================================================================
#     Matriz 3 demensiones
#===============================================================================
print(valorationXYZ); 
print(valorationXYZ[0,2,1]);


print(np.zeros((3,3, 4)));                                      #Crea una matriz especificada de ceros

#===============================================================================
#     Operaciones con Arrays
#===============================================================================
print(valorationXYZ+ np.ones((3,3,4)) + np.ones((3,3,4)));

print(np.mean(valorationXYZ));                                  # Media

print(np.mean(valorationXYZ, axis=0));                          # Media por valor [0][0][0] / [0][1][0] ....
print(np.mean(valorationXYZ, axis=1));                          # Media por valor [0][0][0] / [0][0][1] ....
print(np.mean(valorationXYZ, axis=2));                          # Media por valor [0][0][0] / [0][0][1] / [0][0][2] / [0][0][4] ....

print(np.min(valorationXYZ));                                   # Minimo

print(np.max(valorationXYZ));                                   # Maximo

#===============================================================================
# Creacion de Array por numeros especificados
#===============================================================================
""" 

#print(np.reshape([1,2,3, 4,5,6, 7,8,9, 10,11,12, 13,14,15, 16,17,18], (3,2,3)));

valoration2= np.random.rand(3,3,4)*100;

print(valoration2);





