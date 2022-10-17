#import pandas as pd;


import findspark;
from pyspark import SparkConf, SparkContext, SQLContext;
from pyspark.sql.types import StringType;

#===============================================================================
# 
#===============================================================================

#df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 1000);


#findspark.init();

confSpark= SparkConf().setMaster("local").setAppName("My_Program");
sc= SparkContext(conf= confSpark); 

sqlContex= SQLContext(sc);

#===============================================================================
#     option()
#    "header"       -->  Para especificar que la primera fila son los titulos de las columnas
#    "inferSchema"  -->  Para que Spark intente determinar de que tipo es cada elemento de la tabla (String, int, float, etc..)
#
#===============================================================================

dfspark= sqlContex.read.format("csv").option("header", "true").option("inferSchema", "true").load("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows= 1000);

# print(dfspark.show());
# print(dfspark.head());

# print(dfspark.count());

#===============================================================================
#    fraction        --> fraccion de la tabla
#    withRemplace    --> No se puede reemplazar
#===============================================================================

dfspark= dfspark.sample(fraction= 0.001, withReplacement= False);

# print(dfspark.count());

#===============================================================================
# 
#===============================================================================

dfspark= dfspark.withColumn("ArrDelay", dfspark["ArrDelay"].cast("integer"));

df2= dfspark.na.drop(subset= ["ArrDelay", "DepDelay", "Distance"]);

df2= df2.filter("ArrDelay is not NULL");

# print(df2.count());
# print(df2.printSchema());

#===============================================================================
#    Numpy
#===============================================================================

import numpy as np;

media= np.mean(df2.select("ArrDelay").collect());

print(media);

print(df2.rdd.getNumPartitions());














