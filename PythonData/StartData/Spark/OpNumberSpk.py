from pyspark import SparkConf, SparkContext, SQLContext;
#from pyspark.sql.types import StringType;
from pyspark.sql.functions import mean, stddev, col;
#import numpy as np;

#===============================================================================
#
#===============================================================================
#findspark.init();

confSpark= SparkConf().setMaster("local").setAppName("My_Program");
sc= SparkContext(conf= confSpark); 

sqlContex= SQLContext(sc);

dfspark= sqlContex.read.format("csv").option("header", "true").option("inferSchema", "true").load("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows= 1000);
dfspark= dfspark.sample(fraction= 0.001, withReplacement= False);
#===============================================================================
# 
#===============================================================================

dfspark= dfspark.withColumn("ArrDelay", dfspark["ArrDelay"].cast("integer"));

df2= dfspark.na.drop(subset= ["ArrDelay", "DepDelay", "Distance"]);

df2= df2.filter("ArrDelay is not NULL");
df2= df2.dropDuplicates();  
#===============================================================================
#    Mean    -> MEdia
#    col     -> Columna
#    stddev  -> Desviacion estandas
#
#===============================================================================

list= sc.parallelize(range(1, 1000));                                                              # Obtiene dos valores a travez del rango especificado
list.reduce(lambda x, y: x+y);                                                                     # suma el primero con el segundo de la sintaxis anterior

list.sum();

mean= df2.select(mean(col("ArrDelay"))).collect();
std= df2.select(stddev(col("ArrDelay"))).collect();

print(std[0][0]);

df2.withColumn("Diference", df2["ArrDelay"] - df2["DepDelay"]).collect();                           # Se genera una nueva columna a raiz de lo especificado

df2.withColumn("Standard", (df2["ArrDelay"] - mean[0][0])/ std[0][0] ).collect();                           # Se genera una nueva columna a raiz de lo especificado