import pandas as pd;

data = [(1, "Joan",  "Gasull", 25, 1, "Libreta",   1.2, 0.4,  0.8,  3,  "03-02-2018"),
        (1, "Joan",  "Gasull", 25, 2, "Boligrafo", 0.4, 0.15, 0.25, 1,  "03-02-2018"),
        (1, "Joan",  "Gasull", 25, 1, "Libreta",   1.2, 0.4,  0.8,  3,  "15-02-2018"),
        (2, "Joan",  "López",  33, 2, "Bolígrafo", 0.4, 0.15, 0.25, 4,  "01-02-2018"),
        (2, "Joan",  "López",  33, 1, "Libreta",   1.2, 0.4,  0.8,  10, "05-03-2018"),
        (3, "Maria", "García", 40, 1, "Libreta",   1.2, 0.4,  0.8,  20, "13-04-2018"),
        (3, "Maria", "Garcia", 40, 2, "Boligrafo", 0.4, 0.15, 0.25, 1,  "09-02-2018"),
        (3, "Maria", "García", 40, 2, "Boligrafo", 0.4, 0.15, 0.25, 3,  "03-04-2018")];

labels = ["Comprador_id","Nombre", "Apellido", "Edad", "Producto_1d", "Producto", "Precio", "Coste", "Margen", "Cantidad","Fecha"];

df= pd.DataFrame.from_records(data, columns= labels);

buyer= df.drop_duplicates(subset="Comprador_id", keep="first");
buyer= buyer[["Comprador_id","Nombre", "Apellido", "Edad"]];

product= df.drop_duplicates(subset="Producto_1d", keep="first");
product= product[["Producto_1d", "Producto", "Precio", "Coste", "Margen"]];

buy= df[["Comprador_id", "Producto_1d", "Cantidad","Fecha"]]; 