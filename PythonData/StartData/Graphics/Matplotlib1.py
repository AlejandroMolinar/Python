import pandas as pd;
import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt;

df= pd.read_csv("C:/Users/Alejandro Molinar/Documents/Programming/Excel/base_datos_2008.csv", nrows = 10000); 
#pd.set_option('max_columns', None);                                                            # Mostrar todas las Columnas
#pd.set_option('max_rows', None);


#===============================================================================
#    Graphics 

#    Pie/Cheese
#===============================================================================
"""
data = np.unique(df.Cancelled, return_counts= True);                                            # filtrar solo los elementos de la columna Cancelled 

plt.pie(x=data[1], 
        labels=data[0],                                                
        colors=["cyan", "purple"],
        startangle=90,                                                                          # Angulo de inicio
        radius=1);                                                                              # Radio

plt.show();

# Other Version

data = np.unique(df.DayOfWeek, return_counts= True);  
labs= [ "Thu", "Fri", "Sat", "Sun"];

plt.pie(x=data[1], 
        labels=labs,                                                
        colors=sns.color_palette("hls", 7),                                                     # Paletas de color de la clase "seaborn"
        startangle=90,                                                                          # Angulo de inicio
        radius=0.8,
        explode= (0.2,0,0,0),                                                                   # Para hacer sobresalir a un fracmento del GraficoS 
        autopct= "%1.1f%%",                                                                     # Para que aparezca los porcentajes     
        #labeldistance= 1.5,                                                                    # Para especificar las separacion de los labels
        );                                                                          
plt.legend(loc="lower right");
plt.show();


"""
#===============================================================================
#    Bubbles
#===============================================================================
"""
plt.scatter(x= df.DayofMonth, 
            y= df.ArrDelay, 
            s= df.Distance, 
            alpha=.2,                                                                           # Transparecia
            c= df.DayOfWeek.isin([6,7]));                                                       # Color de los difetentes elementos del Grafico 
plt.title("Retraso en EEUU");

plt.xlabel("Dias del Mes");
plt.xticks([0, 10, 20, 30]);

plt.ylabel("Retraso al Llegar");
plt.ylim([0,150]);

plt.text(x=20, y=120, s='My Flying');
plt.show();

"""

#===============================================================================
#     Bar Graphs
#===============================================================================
data = np.unique(df.DayOfWeek, return_counts= True);  
labs= [ "Thu", "Fri", "Sat", "Sun"];

plts= sns.barplot(x=labs, y=data[1]);

plts.set(xlabel= "Dias la semana", ylabel= "Numero de Vuelo");

plt.show();













