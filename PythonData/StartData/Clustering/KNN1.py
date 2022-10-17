from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier;

import numpy as np;
import pandas as pd;


df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 1000); 

newdf= df[["ArrTime", "Distance", "TaxiOut", "ArrDelay"]].dropna();
#df= df.sample(frac=1);

cols= newdf[newdf.columns[newdf.columns != "ArrDelay"]];

filtro= newdf["ArrDelay"] > 10;

newdf["ArrDelay"][filtro] = "Delayed";
newdf["ArrDelay"][filtro==False] = "Not Delayed";

newdf["ArrDelay"].head();

#===============================================================================
#     Case 1 
#===============================================================================

nbrs_3= KNeighborsClassifier(n_neighbors=3, n_jobs= -1);

nbrs_3.fit(cols, newdf["ArrDelay"]);

predict3= nbrs_3.predict(cols);

np.mean(predict3 == newdf["ArrDelay"]);
np.mean(newdf["ArrDelay"] == "Not Delayed");

#===============================================================================
#     Case 2
#===============================================================================

nbrs_1= KNeighborsClassifier(n_neighbors=1, n_jobs= -1);
nbrs_1.fit(cols, newdf["ArrDelay"]);

predict1= nbrs_1.predict(cols);

np.mean(predict1 == newdf["ArrDelay"]);
np.mean(newdf["ArrDelay"] == "Not Delayed");


confusionMatrix= confusion_matrix(newdf["ArrDelay"], predict1);                                               # Crea un Array de la cantidad de variables dependiendo si fue True o False, y dependiendo tambien, de las predicciones 
print(confusionMatrix);