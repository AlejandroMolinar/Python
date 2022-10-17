from sklearn.naive_bayes import *;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 10000); 

df= df.dropna(subset= ["ArrDelay"]);
df= df.sample(frac=1).head(1000);

Y= df["ArrDelay"]>0;

df["Month"]= df["Month"].apply(str);                                                                                        # En cada una de las columnas especificda las convierte en String
df["DayofMonth"]= df["DayofMonth"].apply(str); 
df["DayOfWeek"]= df["DayOfWeek"].apply(str); 
df["TailNum"]= df["TailNum"].apply(str); 

X= pd.get_dummies(data= df[["Month", "DayofMonth", "DayOfWeek", "TailNum", "Origin", "Dest", "UniqueCarrier"]]);

X.head();

clf= BernoulliNB();
#clf= MultinomialNB();

clf.fit(X, Y);
Y_pred= clf.predict(X);

print(np.mean(Y==Y_pred));
print(np.mean(Y));

#===============================================================================
# 
#===============================================================================
"""
X= df[["ArrTime", "Distance", "TaxiIn", "TaxiOut"]];    # DepDelay
clf= GaussianNB();

clf.fit(X, Y);
Y_pred= clf.predict(X);

np.mean(Y==Y_pred);

np.mean(Y);
"""