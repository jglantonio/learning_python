#!/usr/bin/env python3

# Un elemento mutable

meses = [
    'Enero',
    'Febrero',
    'Marzo',
    'Abril',
    'Mayo',
    'Junio',
    'Julio',
    'Agosto',
    'Septiembre',
    'Octubre',
    'Noviembre',
    'Diciembre'
];

print(meses);
print(meses[0]);
print(meses[-1]);
print(len(meses));

# Operadores de listas
# Definiendo rango desde la posicion 0 a la 4

print(meses [2:4]);
print(meses [:4]);
print(meses [4:]);

if('Miercoles' in meses):
    print ("Existe ne el array meses");
else :
    print ("No existe en el array meses");

# len(); logitud de un texto , también se puede usar para arrays

dias = [2,3,2,1,4,2,5,2,3,5,6,7,8,19];
print(len(dias));
print(max(dias));
print(min(dias));
print(sorted(dias));

# Estas funciones también sirve con arrays alfabéticos.

print(len(meses));
print(max(meses));
print(min(meses));
print(sorted(meses));

# Join de contenido en un array.

arrAux = "MOLA\n".join(meses);
print(arrAux);

arrAux.apend("otromes");
print(arrAux);