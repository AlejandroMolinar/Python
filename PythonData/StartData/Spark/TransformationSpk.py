from pyspark import SparkConf, SparkContext, SQLContext;
#from pyspark.sql.types import StringType;
import numpy as np;

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

print(df2.select("ArrDelay").filter("ArrDelay > 60").show(5));
#===============================================================================
# 
#===============================================================================

meanSpk= np.mean(df2.select('ArrDelay').collect()); 
df2.select("ArrDelay").rdd.map(lambda x: (x - meanSpk)**2).show(10);

print(df2.groupBy("DayOfWeek").count().show());

print(df2.groupBy("DayOfWeek").mean("ArrDelay").show());

#===============================================================================
# 
#===============================================================================

print(df2.select("Origin").rdd.distinct().show());

print(df2.select("Origin").rdd.distinct().count());

print(df2.orderBy(df2.ArrDelay.desc()).show());

#===============================================================================
# 
#===============================================================================

print(df2.select("ArrDelay").describe().show());
print(df2.select("Origin").rdd.countByValue());

print(df2.select("ArrDelay").rdd.max());
print(df2.select("Origin").rdd.collect());

print(df2.crosstab("DayOfWeek", "Origin").show(2));













