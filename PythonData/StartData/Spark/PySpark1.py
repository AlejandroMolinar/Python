import findspark;
from pyspark import SparkConf, SparkContext;

findspark.init();

confSpark= SparkConf().setMaster("local").setAppName("My_Program");

sc= SparkContext(conf= confSpark);

lines= sc.textFile("C:/Users/Alejandro Molinar/Documents/ejemplo.txt");

#===============================================================================
# 
#===============================================================================

#result= lines.filter(lambda line: "para" in line);    

#print(result.take(1));
#print(result.count());
#print(lines.first());

#===============================================================================
#     Int
#===============================================================================

result2= lines.filter(lambda x: (i.isdigit() for i in x));

print(result2.take(1));


#result2= lines.filter(lambda x: not (i.isdigit() for i in x)).take(2);                  # lugares que no hay numeros

#===============================================================================
#     Crea un nuevo Lines con un 10% del contenido original, por el parapero "fraction".
#     withRemplacement permine o bloquea el remplazo
#===============================================================================

#lines2= lines.sample(fraction= 0.1, withRemplacement= False);                                           

#lines2.first();
