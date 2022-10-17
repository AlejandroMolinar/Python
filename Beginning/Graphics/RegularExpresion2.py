import re;

cadena1= "VELASQUEZ ANTONIO";

cadena2= "VASQUEZ EDGAR ";

cadena3= "ROMERO ÁNGEL";

cadena4= "MARTINEZ CARLOS",

cadena5= "NARTINEZ IRIS";

cadena6= "3246788";

cadena7= "3246fdfd7sfsdf43sfsfs8s8fdjghgfggh";

# En el caso del 'Match' siempre busca las primera palabra, que acomparacion de 'Search' busca toda la palabra #

if re.match("Velasquez", cadena1, re.IGNORECASE):
    print("The word was found");

elif re.match(".asquez", cadena2, re.IGNORECASE):
    print("The word was found");

elif re.match(".artinez", cadena3, re.IGNORECASE):
    print("The word was found");
    
elif re.match(".artinez", cadena4, re.IGNORECASE):
    print("The word was found");
    
elif re.match(".artinez", cadena5, re.IGNORECASE):
    print("The word was found");
    
elif re.match("\d", cadena6, re.IGNORECASE):            #Verifica que las primeras Char sean numeros. 
    print("The word was found");
    
else:
    print("Nothing was Found");
    

#El 'search' puede buscar algo en especifico en un parrafo largo.#

if re.search("43", cadena7, re.IGNORECASE):
    print("The word was found");
    
else:
    print("Nothing was Found");