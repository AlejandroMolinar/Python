from sklearn import tree;
from sklearn.ensemble import RandomForestClassifier;
import pandas as pd;
import numpy as np;


df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 1000); 

df= df.dropna(subset= ["ArrDelay"]);
df= df.sample(frac=1);

df= df.head(1000);
df_test= df.tail(1000);

#===============================================================================
#    Parametros arboles de decision:
#    Max_depth            --> Maximo de ramas especificadas
#    min_samples_split    --> Estipular el caso minimo de Particiones por casos
#    min_samples_leaf     --> Igual que el anterior
#    max_features         --> Establecer el maximo de parametros ingresados al Arbol
#===============================================================================

clf= tree.DecisionTreeClassifier();                                                         

X= df[["Distance", "ArrTime", "DepTime", "TaxiIn", "TaxiOut", "DepDelay"]];
X_test= df_test[["Distance", "ArrTime", "DepTime", "TaxiIn", "TaxiOut", "DepDelay"]];

Y= df["ArrDelay"] > 10;
Y_test= df_test["ArrDelay"] > 10;

clf= clf.fit(X, Y);
Y_pred= clf.predict(X);
Y_pred_test= clf.predict(X_test);

print(np.mean(Y == Y_pred));
print(np.mean(Y_test == Y_pred_test));

#===============================================================================
#    Parametros Ranbom Forest:
#    n_estimators         --> Numero de arboles a generar
#    max_features         --> Establecer el maximo de parametros ingresados al Arbol
#    bootstrap            --> Genera muestras aleatorias y, con ellas, arboles 
#    n_jobs               --> Utilizacion de numero maximo de porcesadores de la PC
#    
#===============================================================================

clf= RandomForestClassifier(n_estimators=10, n_jobs= -1);

clf= clf.fit(X, Y);
Y_pred_test= clf.predict(X_test);

clf.feature_importances_;

print(np.mean(Y_test == Y_pred_test))

# RandomForestRegressor()                                                                # Este metodo se utiliza cuando las variables son numericas 



