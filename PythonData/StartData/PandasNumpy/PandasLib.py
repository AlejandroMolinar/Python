import pandas as pd;

df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Xampp/Xml-Csv/NationalNames2.csv", nrows = 1000, delimiter=";");     
 
#En nrow se pueden poner elevados, ejemplo, 1e10 = uno elevado a la 10

"""
print(df.head(5));

print(df.tail(5));

print(df.columns);

print(df.Gender);

print(df.dtypes);

print(df.values)

print(df[20:30]);

print(df["Name"]);

#===============================================================================
#     Filtros
#===============================================================================

print(df[df["Count"]>1000]);

print(df[(df["Count"]>1000) & (df["Gender"]=="M")]);

print(df[(df["Count"]>1000) | (df["Gender"]=="M")]);

print(df[df.Name.isin(["Anna", "Ben", "Ed", "laura"])]);


print(df[pd.isna(df["Count"])]);                                    # Casillas sin Llenar NaN
print(df[pd.isnull(df["Count"])]);                                  # Casillas en Null


df["CountPlus"] = df["Count"]+200;
del(df["CountPlus"]);                                               # Eliminar

print(df["CountPlus"]);

df.drop(["Id", "Gender", "Count"], axis=1);                         # Borrar varias columnas

df= df.drop(["Id", "Gender", "Count"], axis=1);                     # Guardarlo
df.drop(["Id", "Gender", "Count"], axis=1, inplace=True);           # Lo mismo que lo anterior

df.drop(999);                                                       # Para eliminar filas 

dfMax= df[df["Count"]>300]; 
dfMin= df[df["Count"]<600];

newdf= dfMax.append(dfMin);

print(newdf.Count);

#===============================================================================
#    Analisis de los datos
#===============================================================================

print(df.groupby(by= "Gender")["Count"].max());                    # maximo

print(df.groupby(by= "Gender")["Count"].min());                    # minimo

print(df.groupby(by= "Gender")["Count"].mean());                   # media

print(df.groupby(by= "Gender")["Count"].count());s                 # contador

print(df.groupby(by= "Gender")["Count"].describe());               # descripcion general

print(df.groupby(by= "Gender")["Count", "Year"].max() - df.groupby(by= "Gender")["Count", "Year"].min());  

#===============================================================================
#     Analisis con otra sintaxis 
#===============================================================================

dfId= df[df.Id.isin(range(100,300))];

myGroupBy= dfId.groupby(by= ["Year", "Gender"])["Count"];

print(myGroupBy.describe());

#===============================================================================
#    Eliminar duplicados
#===============================================================================
len(dfclean) == len(df);   

dfDuplicate= df.append(df);

dfDuplicate= dfDuplicate.sample(frac=1);                            # ordenar filas

dfclean= dfDuplicate.drop_duplicates();                              # elimina los duplicados

#===============================================================================
#     Filtros varios 
#===============================================================================

print(dfclean.drop_duplicates(subset= "Gender"));                # filtro por columna 
print(df.dropna());                                               # No muestra las filas con columna vacias
print(df.dropna(thresh=20));                                      # Si hubiese filas con elementos faltantes, el 'thresh' lo que hace es mostras tantas filas quieras
print(df.dropna(thresh=len(df.columns)-2));                       # Lo mismo pero la diferecia es que lo hace con todas las filas del archivo

print(df.dropna(subset=["Id"]));                                  #Filtra por la columna especificada las elementos vacios 

"""









