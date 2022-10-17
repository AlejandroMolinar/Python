from sklearn.linear_model import LogisticRegression;
from sklearn.metrics import confusion_matrix;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 10000); 

df= df.dropna(subset= ["ArrDelay"]);
df= df.sample(frac=1).head(1000);
Y= df["ArrDelay"]<30;                                                                       # Devuelve True=0 si no tiene retraso y False=1 Si tuvo retraso de mas de 30 min
X= df[["DepDelay"]];


logr= LogisticRegression();                                                                 # Regresion Logisica
logr.fit(X, Y); 

Y_pred= logr.predict(X);                                                                    # Se realiza una predicion de la variables Y 

print(np.round(logr.predict_proba(X), 3));                                                  # Array de las predicciones obtenidas, mostrando asi, se retrasara o no 

print(np.mean(Y_pred == Y));                                                                # Muestra el porcentaje de las variable Y con las predicciones 
print(np.mean(Y));

confusionMatrix= confusion_matrix(Y, Y_pred);                                               # Crea un Array de la cantidad de variables dependiendo si fue True o False, y dependiendo tambien, de las predicciones 
print(confusionMatrix);