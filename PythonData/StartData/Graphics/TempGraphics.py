import pandas as pd;
import numpy as np;
import seaborn as sns;
import time;
import datetime;
import matplotlib.pyplot as plt;


df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 10000, delimiter=","); 
#pd.set_option('max_columns', None);                                                            # Mostrar todas las Columnas
#pd.set_option('max_rows', None);                                                               # Mostrar Filas
#===============================================================================
"""
times= [];

for i in np.arange(len(df)):
    times.append(datetime.datetime(year= 2008, month= df.loc[i, "Month"], day= df.loc[i, "DayofMonth"]));
    
df["Time"] = times;

data= df.groupby(by= ["Time"])["DepDelay", "ArrDelay"].mean();

sns.lineplot(data=data);
plt.show();
"""
#===============================================================================
#     Graphics Lineplot
#===============================================================================
"""
df2 = df[df["Origin"].isin(["HOU", "ATL", "IND"])];

times= [];

for i in df2.index:
    times.append(datetime.datetime(year= 2008, month= df2.loc[i, "Month"], day= df2.loc[i, "DayofMonth"]));             # Este sintaxis funciona para pasarle a la lista 'times' el año, mes, dia y horas  

df2["Time"] = times;

sns.set(rc={"figure.figsize":(15, 10)});                                                                                # Ajusta eltamaño del grafico
    
sns.lineplot(x= "Time", y= "ArrDelay", hue= "Origin", data=df2);                                                        # El parametro 'hue' lo que hace es filtrar por la lista Origin
plt.show();  
"""
#===============================================================================
#     Graphics Distplot
#===============================================================================
"""
df.dropna(subset= ["ArrDelay", "DepDelay", "Distance"], inplace= True);

sns.displot(df["Distance"], kde= False, bins= 100);                                                                     # El parametro 'kde' activa/desactiva la opcion de 
plt.show();
"""
#===============================================================================
#     Graphics kdeplot
#===============================================================================
"""
df.dropna(subset= ["ArrDelay", "DepDelay", "Distance"], inplace= True);

sns.kdeplot(df["ArrDelay"]);
sns.kdeplot(df["DepDelay"]);

plt.xlim(-500, 500);
plt.show();
"""

#===============================================================================
#     Graphics Boxplot
#===============================================================================

df2 = df[df["Origin"].isin(["HOU", "ATL", "IND"])].sample(frac= 1).head(1000);

sns.boxplot(x= "DepDelay", y="Origin", data= df2);
plt.xlim(-20, 150);
plt.show();






















