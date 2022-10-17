#from sklearn import datasets;
from sklearn import linear_model;
#from sklearn.metrics import mean_squared_error; 
from sklearn.metrics import r2_score;
import pandas as pd;
#import numpy as np;

#===============================================================================
# 
#        'Year', 'Month', 'DayofMonth', 'DayOfWeek', 'DepTime', 'CRSDepTime',
#        'ArrTime', 'CRSArrTime', 'UniqueCarrier', 'FlightNum', 'TailNum',
#        'ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay',
#        'DepDelay', 'Origin', 'Dest', 'Distance', 'TaxiIn', 'TaxiOut',
#        'Cancelled', 'CancellationCode', 'Diverted', 'CarrierDelay',
#        'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay'
#
#===============================================================================


df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 1000); 

df= df.dropna(subset= ["ArrDelay"]);
df= df.sample(frac=1).head(1000);
Y= df["ArrDelay"];
X= df[["DepDelay"]];

#print(df.columns);
"""
regr= linear_model.LinearRegression()
regr.fit(X, Y);

#print("Coeficientes: ", regr.coef_);

Y_pred= regr.predict(XS);
#print("R cuadrado: ", r2_score(Y, Y_pred));

plt.scatter(X[1:1000], Y[1:1000], color= "black");
plt.plot(X[1:1000], Y_pred[1:1000], color= "Blue")
plt.show();
"""
#===============================================================================
# 
#===============================================================================

X= df[["ArrTime", "Distance", "TaxiIn", "TaxiOut"]];

df["Month"]= df["Month"].apply(str);                                                                                        # En cada una de las columnas especificda las convierte en String
df["DayofMonth"]= df["DayofMonth"].apply(str); 
df["DayOfWeek"]= df["DayOfWeek"].apply(str); 

dummies= pd.get_dummies(data= df[["Month", "DayofMonth", "DayOfWeek", "Origin", "Dest"]]);                                  # Una vaiable dummies te devuelve 1 y 0 dependiendo de si aprarece la categoria especificada 
X= dummies.add(X, fill_value= 0);

print(X.columns);

X= X.add(df[["DepDelay"]], fill_value=0);

regr= linear_model.LinearRegression()
regr.fit(X, Y); 

print("Coeficientes: ", regr.coef_);

Y_pred= regr.predict(X);
print("R cuadrado: ", r2_score(Y, Y_pred));












