def generators(*elementos):         #El asterisco antes de la variable, significa que el usuario le puede agregar tantas variables como quiera
    for elem in elementos:
        yield elem;

def generators2(*elementos):        #El asterisco antes de la variable, significa que el usuario le puede agregar tantas variables como quiera
    for elem in elementos:
        yield from elem;            #El Yield from funciona como un for anidado, no necesita la construccion de un for

elements= generators("Madrid", "Barcelona", "Galicia", "Bilbao", "Ibiza", "Valencia");
elements2= generators2("Madrid", "Barcelona", "Galicia", "Bilbao", "Ibiza", "Valencia");

print(next(elements));
print(next(elements));
print(next(elements));
print(next(elements));

print(next(elements2));
print(next(elements2));
print(next(elements2));
print(next(elements2));a