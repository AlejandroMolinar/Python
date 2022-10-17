import pandas as pd;
import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt;

df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 10000); 
df.sample(frac=0);
#pd.set_option('max_columns', None);                                                            # Mostrar todas las Columnas
#pd.set_option('max_rows', None);                                                               # Mostrar Filas

#===============================================================================
#     Graphics Joinplot                        
#===============================================================================
"""
df.dropna(subset= ["ArrDelay", "DepDelay", "Distance", "ArrTime"]);

sns.set(rc={"figure.figsize":(15, 10)});

df2 = df[df["Origin"].isin(["HOU", "ATL", "IND"])].sample(frac= 1).head(1000);

sns.jointplot(df2["DepDelay"], df2["ArrDelay"]);  
plt.show();
"""
#===============================================================================
#     Graphics Joinplot Advanced     
#===============================================================================
"""
df.dropna(subset= ["ArrDelay", "DepDelay", "Distance", "ArrTime"]);

sns.set(rc={"figure.figsize":(15, 10)});

df2 = df[df["Origin"].isin(["HOU", "ATL", "IND"])].sample(frac= 1).head(1000);

df3= df2[np.abs(df2["DepDelay"])<40];
df3= df3[np.abs(df3["ArrDelay"])<40];

#sns.jointplot(df3["DepDelay"], df3["ArrDelay"], kind="hex");                                # Muestra hexagonos en el grafico
sns.jointplot(df3["DepDelay"], df3["ArrDelay"], kind="kde");                                 # Muestra un Grafico con densidad de curvas 
plt.show();
"""
#===============================================================================
#     Graficos Heatmap
#===============================================================================
df2 = df[df["Origin"].isin(["ATL", "HOU", "IND"])];

HMdf= pd.DataFrame(df2.groupby(["Origin", "Month"], as_index= False)["DepDelay"].mean());

data= HMdf.pivot("Month", "Origin", "DepDelay");

sns.set(rc={"figure.figsize":(15, 8)});
sns.heatmap(data= data, annot= True, linewidths= .5);
plt.show();






