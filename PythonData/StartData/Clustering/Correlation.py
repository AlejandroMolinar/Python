import pandas as pd;
import numpy as np;
from joblib import parallel, delayed;

df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 1000, delimiter=","); 
df.sample(frac=1);
#pd.set_option('max_columns', None);                                                            # Mostrar todas las Columnas
#pd.set_option('max_rows', None);                                                               # Mostrar Filas
#===============================================================================
#     BBDD Aeropuerto
#
#    'Year', 'Month', 'DayofMonth', 'DayOfWeek', 'DepTime', 'CRSDepTime',
#    'ArrTime', 'CRSArrTime', 'UniqueCarrier', 'FlightNum', 'TailNum',
#    'ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay',
#    'DepDelay', 'Origin', 'Dest', 'Distance', 'TaxiIn', 'TaxiOut',
#    'Cancelled', 'CancellationCode', 'Diverted', 'CarrierDelay',
#    'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay'  
#===============================================================================
"""
print(df.head());

print(df.columns); 

#===============================================================================
#    Correlacion
#===============================================================================

df.dropna(inplace=True, subset=["ArrDelay", "DepDelay"]);                                       # Elimina los elementos que esten vacios en dichas Columnas

#print(np.corrcoef(df["ArrDelay"], df["DepDelay"]));                                            # Crea una matriz con la correlacion entre dos Columnas

print(np.corrcoef([df["ArrDelay"], df["DepDelay"], df["DepTime"]]));                            # Crea una correlacion con 3 Columnas

df.drop(inplace=True, columns=['Year', 'Month', 'Cancelled', 'Cancelled', 'Diverted', 'DayofMonth', 'DayOfWeek']);         # Elimina las columnas que no son numericas

corr= round(df.corr(), 3);
corr.style.background_gradient();


#===============================================================================
#     Bucle 
#===============================================================================


df= df[['CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay' ]];

def retraso_Max(fila):
    
    if np.isnan(fila).any():
        names = ['CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay' ];
        return names[fila.index(max(fila))];
    else:
        
        return "None";
        
"""





