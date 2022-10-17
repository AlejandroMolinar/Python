from tkinter import *;

class Calculator():
    def __init__(self, frame):
        
        numScreen1=StringVar();
        numScreen2=StringVar();
        signal=StringVar();
        
        #__________________________Screen_________________________________________#
        screen= Entry(frame, width=35, textvariable=numScreen2);
        screen.grid(padx=10, pady=10, sticky="n", columnspan=5);
        screen.config(background="black", fg="#03f943", justify="right");
        #__________________________Action_________________________________________#
        def NumScreen(num):
            
            #Me daba el error "UnboundLocalError: local variable 'signal' referenced before assignment" porque teniea que asignar que la variable sea global, es decir, "global signal"#
            
            if(num=="+" or num=="-" or num=="*" or num=="/"):
                signal.set(num);                
                numScreen1.set(numScreen2.get());
                numScreen2.set(0);
                
            elif(num=="="):
                print("yes");

                if(signal.get()=="+"):
                    num1=numScreen1.get();
                    num2=numScreen2.get();
                    
                    resultado=int(num1) + int(num2);
                    numScreen2.set(resultado);
                    
                elif(signal.get()=="-"):
                    num1=numScreen1.get();
                    num2=numScreen2.get();
                    
                    resultado=int(num1) - int(num2);
                    numScreen2.set(resultado);
                    
                elif(signal.get()=="*"):
                    num1=numScreen1.get();
                    num2=numScreen2.get();
                    
                    resultado=int(num1) * int(num2);
                    numScreen2.set(resultado);
                    
                elif(signal.get()=="/"):
                    num1=numScreen1.get();
                    num2=numScreen2.get();
                    
                    resultado=int(num1) / int(num2);
                    numScreen2.set(resultado);
                
            else:
                if(screen.get()=="0"):
                   numScreen2.set(num);
                else:
                    numScreen2.set(screen.get() + num);
        
        
        #__________________________Number_________________________________________#
        
        button1= Button(frame, text="1", width=5, command=lambda:NumScreen("1"));
        button1.grid(row=1, column=1, padx=4, pady=4);
        
        button2= Button(frame, text="2", width=5, command=lambda:NumScreen("2"));
        button2.grid(row=1, column=2, padx=4, pady=4);
        
        button3= Button(frame, text="3", width=5, command=lambda:NumScreen("3"));
        button3.grid(row=1, column=3, padx=4, pady=4);
        
        button4= Button(frame, text="4", width=5, command=lambda:NumScreen("4"));
        button4.grid(row=2, column=1, padx=4, pady=4);
        
        button5= Button(frame, text="5", width=5, command=lambda:NumScreen("5"));
        button5.grid(row=2, column=2, padx=4, pady=4);
        
        button6= Button(frame, text="6", width=5, command=lambda:NumScreen("6"));
        button6.grid(row=2, column=3, padx=4, pady=4);
        
        button7= Button(frame, text="7", width=5, command=lambda:NumScreen("7"));
        button7.grid(row=3, column=1, padx=4, pady=4);
        
        button8= Button(frame, text="8", width=5, command=lambda:NumScreen("8"));
        button8.grid(row=3, column=2, padx=4, pady=4);
        
        button9= Button(frame, text="9", width=5, command=lambda:NumScreen("9"));
        button9.grid(row=3, column=3, padx=4, pady=4);
        
        button0= Button(frame, text="0", width=5, command=lambda:NumScreen("0"));
        button0.grid(row=4, column=2, padx=4, pady=4);
        
        #__________________________Symbols_________________________________________#
        
        buttonMore= Button(frame, text="+", width=5, command=lambda:NumScreen("+"));
        buttonMore.grid(row=1, column=4, padx=4, pady=4);
        
        buttonLess= Button(frame, text="-", width=5, command=lambda:NumScreen("-"));
        buttonLess.grid(row=2, column=4, padx=4, pady=4);
        
        buttonMult= Button(frame, text="*", width=5, command=lambda:NumScreen("*"));
        buttonMult.grid(row=3, column=4, padx=4, pady=4);
        
        buttonDiv= Button(frame, text="/", width=5, command=lambda:NumScreen("/"));
        buttonDiv.grid(row=4, column=4, padx=4, pady=4);
        
        buttonSame= Button(frame, text="=", width=5, command=lambda:NumScreen("="));
        buttonSame.grid(row=4, column=3, padx=4, pady=4);
        
        buttonPoint= Button(frame, text=".", width=5);
        buttonPoint.grid(row=4, column=1, padx=4, pady=4);
        
        

window= Tk();
window.title("Calculator");

frame= Frame(window, width=650, height=600);
frame.pack(fill="both", expand="True", padx=10, pady=10);

Calculator(frame);


window.mainloop();
        