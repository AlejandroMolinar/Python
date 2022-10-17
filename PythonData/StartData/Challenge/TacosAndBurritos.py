import findspark
from pyspark import SparkConf, SparkContext, SQLContext;

#===============================================================================
#     id|                    address|               categories|            city|country|        cuisines|          
#    dateAdded|              dateUpdated|           keys|                  latitude|            longitude|         
#    menuPageURL|            menus.amountMax|       menus.amountMin|       menus.category|      menus.currency|
#    menus.dateSeen|         menus.description|     menus.name|            name|                ostalCode|  
#    priceRangeCurrency|     priceRangeMin|         priceRangeMax|         province|            websites
#    
#===============================================================================
findspark.init();

confSpark= SparkConf().setMaster("local[2]").setAppName("TacosAndBurritos");
sc= SparkContext(conf= confSpark); 

sqlContex= SQLContext(sc);

dfspark= sqlContex.read.format("csv").option("header", "true").option("inferSchema", "true").load("C:/Users/Alejandro Molinar/Documents/Programming/Excel/just tacos and burritos.csv");

#===============================================================================
#     Cleanning
#===============================================================================

df2= dfspark.na.drop(subset= ["cuisines"]);

df2= df2.filter("cuisines is not NULL");
df2= df2.dropDuplicates();

df2= df2.select("id","address","categories","city","country","cuisines");

A= sc.parallelize(df2.select("cuisines").rdd.collect());   

def funcMap(x):
    
    x= x[0];
    x= x.remplacw(" ", "");
    x= x.split(",");
    return x;

flameMAp= A.flatMap(funcMap);
print(flameMAp.collect());

mapFunc= flameMAp.map(lambda x: (x,1));
reduceFunc= mapFunc.reduceByKey(lambda x,y: x+y); 

print(reduceFunc.sortBy(lambda x: x[1], ascending= False));




    