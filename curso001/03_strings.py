#!/usr/bin/env python3
# Strings y funciones para trabajar con ellos

variable = "Tengo un conejo ";
print(variable);
variable2 = "llamado POL";
print(variable2);
print(variable + variable2);
print(variable*2);

# function len

length_variable = len(variable);
print("La variable "+variable+", tiene ",length_variable);

# primera letra del string

print(variable[0]);

# Poner todas las letras en capital.

variable3 = variable+variable2;
print(variable3.title());

# islower(); son todo minusculas

print(variable3.islower());
print((variable3.lower()).islower());
