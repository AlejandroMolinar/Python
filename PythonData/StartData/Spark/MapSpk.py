import findspark
from pyspark import SparkConf, SparkContext, SQLContext;


#from pyspark.sql.types import StringType;
#import numpy as np;
#===============================================================================
#
#===============================================================================
findspark.init();

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

A= sc.parallelize(df2.select("Origin").rdd.collect());                                                  # Array paralelizado 
A.persist();                                                                                            # Hace que persistan los valores

#===============================================================================
# 
#===============================================================================

mapFunc= A.map(lambda x: (x,1));

#print(mapFunc.collect());


def funcion(x):
    if x[0] in ["SEA", "ATL", "HOU", "IND"]:
        
        return((x , 2));
    
    elif x[0] in ["DEN", "BOS"]:
        
        return((x , 3));
    
    else:
        return ((x , 1));
    
mapFunc2= A.map(funcion);

#print(mapFunc.collect());

reduceFunc= mapFunc.reduceByKey(lambda x,y: x+y); 

reduceFun2= mapFunc2.reduceByKey(lambda x,y: x+y); 
    
reduceFunc.sortBy(lambda x: x[1], ascending=False).show();
reduceFunc.sortByKey().show();
    
    
    
    
    