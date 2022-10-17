from sklearn.cluster import AgglomerativeClustering;
from sklearn.cluster import KMeans;
from sklearn import preprocessing;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 10000); 
df2= df[[ "ArrTime", "DepDelay"]].dropna();

#df2= df[["ArrTime", "Distance", "TaxiOut", "ArrDelay", "DepDelay"]].dropna();
"""
X_scaled= preprocessing.scale(df2);                                                                              # Estandarizacion a df

X_scaled.mean(axis= 0);                                                                                         # Axis = 0 --> fila por fila / Axis = 1 --> columna por columna

X_scaled.std(axis= 0);                                                                                          # Calculo de la desviacion estandar

print(df.iloc[2]); 

print(X_scaled[2]);

MinMax_scaler= preprocessing.MinMaxScaler([0,10]);                                                              # Se especifica un rango de valores de Minimo y Maximo 

X_trainMinMax= MinMax_scaler.fit_transform(df2);                                                                # Se transforma df con el rango especificado anteriormente 

print(pd.get_dummies(df["Origin"]));                                                                             
"""
#===============================================================================
#     Clustering
#===============================================================================
"""                                                                                                             # '.fit' establece el modelo a ejecutar
k_means= KMeans(n_clusters=4, random_state=1, n_jobs= -1).fit(df2);                                             # 'n_clusters' especiica los cluster a utilizar 
                                                                                                                # 'random_state' se utiliza para que siempre se obtenga el mismo resultado
                                                                                                                # 'n_jobs' establece el numero de procesadores                                                 
print(k_means.labels_)                                                                                          # Muestra los cluster

print(np.unique(k_means.labels_, return_counts=True));

plt.scatter(df2["ArrTime"], df2["DepDelay"], c=k_means.labels_);
plt.show();

print(k_means.cluster_centers_);
"""

#===============================================================================
# 
#===============================================================================

clstr= AgglomerativeClustering(n_clusters=4);
clstr.fit(df2);

plt.scatter(df2["ArrTime"], df2["DepDelay"], c=clstr.fit_predict(df2));
plt.show();
    
