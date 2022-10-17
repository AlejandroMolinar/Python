import findspark
from pyspark import SparkConf, SparkContext;


#from pyspark.sql.types import StringType;
#import numpy as np;
#===============================================================================
#
#===============================================================================
findspark.init();

confSpark= SparkConf().setMaster("local").setAppName("My_Program");
sc= SparkContext(conf= confSpark); 

lines= sc.textFile("C:/Users/Alejandro Molinar/Documents/ejemplo.txt");

#===============================================================================
# 
#===============================================================================
nf= sc.accumulator(0);
dg= sc.accumulator(0);

def coincidence(lines):
    global nf, dg;
    if "NFT" in lines:
        nf += 1;
        
        if "digital" in lines:
            dg += 1;
            return True; 
        
        return True;
    
    if "digital" in lines:
        dg += 1;
        return True;    
    
    else:
        
        return False;
    
values= lines.filter(coincidence).collect();

print(nf, "\n", dg);    
#===============================================================================
# 
#===============================================================================
    
mapFunc= values.map(lambda x: (x,1));

countValues= mapFunc.reduceByKey(lambda x,y: x+y); 

#print(countValues.collect());

countValues.sortBy(lambda x: x[1], ascending=False).show(5);


def funcion(x):
    if "NFT" in x and "digital" in x:
        
        return("Count", (1, 1));
    
    elif "NFT" in x:
        
        return("Count", (1, 0));
        
    elif "digital" in x:
        
        return("Count", (0, 1));
    
    else:
        return("Count", (0, 0));
    
mapFun= lines.map(funcion);

#print(mapFunc.count());

reduceFunc= mapFunc.reduceByKey(lambda x,y: (x[0]+ y[0], x[1]+y[1])).collect(); 

    

    