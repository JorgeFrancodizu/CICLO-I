# CICLO-I
Python

Reto 1: Grupo P82
Número máximo de ficheros: 1
Tipo de trabajo: Individual
Melquiades y su ritmo Ya conocimos al abuelo Melquiades, un abuelo con bastante Flow😎.
En su búsqueda por encontrar nuevas formas de hacer reggaeton, se dio cuenta que
podría categorizar el nivel de perreo dependiendo de la cantidad de BPM que posea el ritmo.

Para ello tuvo en cuenta las siguientes características musicales.

-La primera característica que encuentra es el Pulso (P), el cual es la unidad
más básica que se usa para medir el tiempo y será un número entero.

-La segunda característica que usa don Melquiades es el Tempo(T) y lo propone
Diciendo que: el doble del valor de la primera característica (P) es igual 
al valor de la segunda característica (T) menos cuatro.

-Para hallar los BPM toma como relación el Pulso(P) y Tempo(T) de la
siguiente forma:  cinco veces la cantidad de BPM es igual a la suma de los
valores obtenidos en la primera y segunda característica, P y T respectivamente.

-Para clasificar el nivel de perreo don Bunny Melquiades tomara en cuenta el valor
de los BPM. Si el valor de los BPM está entre 0 y 20, el nivel de perreo será uno. 
Si el valor se encuentra entre 21 y 30, sería un nivel dos. En caso de que el 
valor de BPM este entre 31 y 50 será categorizado como nivel tres. Finalmente, 
si el valor de BPM es mayor a 51, será un nivel cuatro.


Elabora un programa que permita, dado el pulso, conocer los valores obtenidos en las 
diferentes características (P, T, BPM), así como en qué nivel de perreo se encuentra.

Nota: El valor de las características musicales son números enteros, en caso de necesitarlo se puede usar la función de parte entera.


Entrada
La entrada es un número que representa el pulso del ritmo de la canción.

Salida
Tres enteros separados por espacio que representan los valores para cada uno de las características musicales (P, T, BPM). 
En la siguiente línea en letras el nivel de perreo de la canción.

ENTRADA

SALIDA

97

97 198 59

cuatro

87

87 178 53

cuatro
