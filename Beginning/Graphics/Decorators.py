

import math;


# Sintaxis Decoradores #

def Decorator(function_to_Decorate):
    
    def InternalDecoration(*args, **kwargs):  # El parametro '*args' es utilizado para especificar al metodo que este resibira#
                                    # mas de un parametro, y puede tener infinidadd de parametros  #
        
        # Aqui se realiza la mejor a#
        
        print("A Calculation will be Performed");
        function_to_Decorate(*args, **kwargs);
        print("Finish Solution");
        
    return InternalDecoration;



@Decorator
def Sum(num1, num2):
    
    """
    Suma dos numeros
    >>> Sum(5+4)
    9.0
    """
    
    print(num1+num2);
    
@Decorator
def Potenc(base, exponent):
    
    """
    Potencia de un numeros
    
    >>> Potencc(5+2)
    25.0
    """
    
    print(pow(base, exponent));
    
    
def Email(emailPerson):
    
    """
    Verificador de arrobas
    
    >>> Email('alejandro@gmail.com')
    False
    
    """
    
    arroba= emailPerson.count();
    
    if arroba!=1 or emailPerson.rfind('@')==(len(emailPerson)-1) or emailPerson.find('@')==0:
        return False;
    else:
        return True;
    
def Raiz(ListNum):
    
    """
    Verificador de metodod
    
    >>> lis=[]
    >>> for li in [4, 9, 16]:
    ...    lis.append(li)
    >>> Raiz(lis)
    [2.0, 3.0, 4.0]
    
    Para errores de negativos.
    
    >>> lis=[]
    >>> for li in [4, -9, 16]:
    ...    lis.append(li)
    >>> Raiz(lis)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    
    """
    return [math.sqrt(list) for list in ListNum];
        
    
    
import doctest;
doctest.testmod();

#print(Raiz([4, -9, 19]));

