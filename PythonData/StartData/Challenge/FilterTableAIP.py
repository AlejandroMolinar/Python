from sklearn.cluster import KMeans; 
from sklearn.ensemble._forest import RandomForestRegressor

import matplotlib.pyplot as plt;
import pandas as pd;


#import numpy as np;
#===============================================================================
# 
#        'Year',                 'Month',               'DayofMonth',         'DayOfWeek',         'DepTime',     
#        'CRSDepTime',           'ArrTime',             'CRSArrTime',         'UniqueCarrier',     'FlightNum',         
#        'TailNum',              'ActualElapsedTime',   'CRSElapsedTime',     'AirTime',            'ArrDelay',
#        'DepDelay',             'Origin',              'Dest',               'Distance',           'TaxiIn', 
#        'TaxiOut',              'Cancelled',           'CancellationCode',   'Diverted',           'CarrierDelay',
#        'WeatherDelay',         'NASDelay',            'SecurityDelay',      'LateAircraftDelay'
#
#===============================================================================
df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 10000); 

df= df.dropna(subset= ["Distance","ArrDelay"]);
df= df.sample(frac=1).head(10000);

df= df[df.ArrDelay > 120];
df= df[df.Distance > 2000];

k_means= KMeans(n_clusters=4, n_jobs= -1).fit(df[["Distance","ArrDelay"]]);                                             

plt.scatter(df["ArrDelay"], df["Distance"], c= k_means.labels_);
plt.xlabel("Retraso");
plt.ylabel("Dintance");
plt.show();

#===============================================================================
# 
#===============================================================================

df["Group"] = KMeans.labels_;

dfGroup= df[df["Group"]==5];

dfGroup.groupby(["DayOfWeek"])["DepDelay"].describe();


dfGroup["Month"]= dfGroup["Month"].apply(str);                                                                                        # En cada una de las columnas especificda las convierte en String
dfGroup["DayofMonth"]= dfGroup["DayofMonth"].apply(str); 
dfGroup["DayOfWeek"]= dfGroup["DayOfWeek"].apply(str); 


dummies= pd.get_dummies(dfGroup[["Month", "DayofMonth", "DayOfWeek", "UniqueCarrier", "Origin", "Dest"]]);                                  # Una vaiable dummies te devuelve 1 y 0 dependiendo de si aprarece la categoria especificada 
X= dummies.add(dfGroup[["TaxiIn", "TaxiOut", "DepTime"]], fill_value= 0);

#===============================================================================
# 
#===============================================================================

clf= RandomForestRegressor(n_estimators=10, n_jobs= -1).fit(X, dfGroup["ArrDelay"]);

importance= clf.feature_importances_;

X.columns[importance == max(importance)];

np.corrcoef(dfGroup["DepTime"] ,dfGroup["ArrDelay"])







