# Objetos.

Para referir a un objeto en python nos encontraremos
que se tienen la identidad , que es lo que referencia
a dicho objeto a bajo nivel.

```python
  hi = "hi"
  id(hi); # 4514420256
```
* Sería la localización en la memoria RAM de nuestro equipo.
* Puede existir que se haga referencia dos variables al mismo objeto 
* Python primero accede al nombre de la variable y luego a la id.

## Mutabilidad

Un objeto se considera inmutable si dicho objeto no ha sido modificado , por consiguiente se considera mutable.

Un objeto cambia , por ejemplo :

```python
numero = 1;
numero = numero + 1;
```

Para el caso de una lista , seguiría inmutable porque:

```python
name = []; # 2132132132
name.append("paco"); # 2132132132
```
