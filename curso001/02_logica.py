#!/usr/bin/env python3

# Datos booleanos

def datosBooleanos ():
    valorTrue = True;
    valorFalse = False;
    if(valorTrue):
        print(valorTrue)
def mayorEdad(edad):
    return edad >= 18;
def ninho(edad):
    return 5 >= edad <= 14;

datosBooleanos();
print(mayorEdad(10));
print(ninho(10));