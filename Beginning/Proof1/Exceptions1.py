from Package.ProofBasic import *; #de esta menera si importa una clase

while True:
    try:
        value1=int(input("Enter First Number: "));
        value2=int(input("Enter Second Number: "));
        break;

    except:
        print("Error, make sure the variables are numeric.");
        

operator=input("Enter the operation you want to perform with the values(Sum, Subtraction, Division, Multiplication) or (+, -, /, *): ").lower();

while True:
    if operator=="sum" or operator=="+" :
        print(sum(value1, value2));
        break;
        
    elif operator=="subtraction"  or operator=="-" :
        print(subtraction(value1, value2));
        break;
        
    elif operator=="division" or operator=="/" :
        print(division(value1, value2));
        break;
        
    elif operator=="multiplication" or operator=="*" :
        print(multiplication(value1, value2));
        break;
        
    else:
        operator=input("Enter the operation you want to perform with the values(Sum, Subtraction, Division, Multiplication) or (+, -, /, *): ").lower();


print("Successful Operation."); 



