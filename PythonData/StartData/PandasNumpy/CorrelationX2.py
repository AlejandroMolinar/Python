#from scipy.stats import chi2_contingency;

import numpy as np;
import pandas as pd;


#===============================================================================
#     Class
#===============================================================================
df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 10000, delimiter=","); 
#pd.set_option('max_columns', None);                                                            # Mostrar todas las Columnas
#pd.set_option('max_rows', None);    

#===============================================================================
# 
#===============================================================================

np.random.seed(0);
df = df[df["Origin"].isin(["HOU", "ATL", "IND"])];                                              # Filtrar por elementos de una columna
df = df.sample(frac=1);                                                                         # Ordenar la tabla

df["BigDelay"] = df["ArrDelay"] > 30;                                                           # Devuelve True si los elementos de la columna 'ArrDelay' tienes un Delay de mas de 30 min y false por tener menos de eso

observator= pd.crosstab(index = df["BigDelay"], columns = df["Origin"], margins= True);         # Crea una tabla de correlacion, dejando de indice la columna 'BigDelay' y de columnas la 'Origin'                     

#print(observator);

#===============================================================================
#     Import
#===============================================================================

"""
test= chi2_contingency(observator);                                                             # Crea un array con valores de Correlacion y estadistica

expected = pd.DataFrame(test[3]);                                                               # Crea una tabla a partir de los datos de Test, asi es mas facil de observar 

expectedBest= round(expected.apply(lambda r: r/len(df) *100, axis=1), 2);                       # Redondeo de los numeros de las variable con sintaxis RARISIMA
observatorBest= round(observator.apply(lambda r: r/len(df)*100, axis=1), 2);                    # Redondeo de los numeros de las variable con sintaxis RARISIMA

print(test[1]);

"""