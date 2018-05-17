#!/usr/bin/env python3

print("Media de dias que se les dedica al trabajo");

total = 0;

dia = input("Horas en Lunes : ");
total= total + int(dia);
dia = input("Horas en Martes : ");
total= total + int(dia);
dia = input("Horas en Miercoles : ");
total= total + int(dia);
dia = input("Horas en Jueves : ");
total= total + int(dia);
dia = input("Horas en Viernes : ");
total= total + int(dia);

media = total/5;

print("Horas totales %s"%media);