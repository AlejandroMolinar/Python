import pandas as pd;

#===============================================================================
#     Table 1 
#===============================================================================

consumidores = [("A", "móvil"), ("B","móvil"),("A","Portátil"),("A", "Tablet"),
                ("B","Tablet"),("c", "Portátil"),("D", "Smartwatch"), ("E","Consola")];
con_labels = ["Consumidor", "Producto"];


con_df = pd.DataFrame.from_records(consumidores, columns= con_labels);

#===============================================================================
#     Table 2
#===============================================================================

productores = [("a","móvil"),("a","Smartwatch"), ("a", "Tablet"), ("b","Portátil"),
               ("c", "Sobremesa"), ("c","Portátil")];
prod_labels = ["Productor", "Producto"]

prod_di= pd.DataFrame.from_records(productores, columns= prod_labels);

#===============================================================================
#     Join Table
#===============================================================================

#TableJoin= pd.merge(con_df, prod_di, on="Producto", how="outer");                                            # Con el Parametro how "Outer" lo que hace es agregar todas las filas aunque este vacias

TableJoin= pd.merge(con_df, prod_di, on="Producto", how="inner");                                             # Con el Parametro how "inner" lo que hace es agregar las filas no esten vacias

TableJoin= pd.merge(con_df, prod_di, on="Producto", how="rigth");

TableJoin= pd.merge(con_df, prod_di, on="Producto", how="left");

print(TableJoin);

