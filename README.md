# UVA-910 TV Game
## Tercera Práctica: Programación Dinámica
Problema que consiste en identificar cuántas cadenas de $m$ elementos son reconocidas por un autómata dibujado en un tapete

## Objetivo
El objetivo de esta práctica es resolver un problema utilizando programación dinámica. Como recordarán, la programación dinámica es una optimización de dividir para conquistar en la cual, cuando en la evaluación recursiva se repiten muchos cálculos, se mejora la eficiencia cambiando el orden de evaluación del árbol comenzando por las hojas y terminando en la raíz. Puede ser visto como adicionar memoria a la función recursiva, de manera que si se llama nuevamente con un parámetro ya evaluado, en lugar de ejecutar la función con  ese parámetro, se retorna el valor previamente calculado. 

## Problema
El problema a resolver se denomina *TV Game*. El enunciado lo encuentra anexo y también lo pueden consultar acá: [Online Judge - 910 TV Game](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=11&page=show_problem&problem=851). Deben implementar la solución en cualquier lenguaje de programación aceptado por el juez en línea de UVA:

- ANSI C 5.3.0 - GNU C Compiler with options: -lm -lcrypt -O2 -pipe -ansi -DONLINE_JUDGE
- JAVA 1.8.0 - OpenJDK Java
- C++ 5.3.0 - GNU C++ Compiler with options: -lm -lcrypt -O2 -pipe -DONLINE_JUDGE
- PASCAL 3.0.0 - Free Pascal Compiler
- C++11 5.3.0 - GNU C++ Compiler with options: -lm -lcrypt -O2 -std=c++11 -pipe -DONLINE_JUDGE
- PYTH3 3.5.1 - Python 3

### Traducción del enunciado
El siguiente juego de TV lo jugarán individualmente en un tipo especial de laberinto. El jugador pisará una alfombra con un dibujo como el de la fig. 1, y esperará en la posición A. Cada posición tiene dos salidas, etiquetadas con 0 y 1, que conducen a la siguiente posición. Para elegir qué salida tomar, el jugador debe responder a una pregunta. Si la respuesta es correcta, toma la salida 1; de lo contrario, toma la salida 0. Por supuesto, la respuesta puede ser deliberada o no. Por supuesto, la respuesta puede ser deliberadamente errónea si se busca el camino 0. La siguiente posición puede ser diferente o permanecer igual que antes. 

Algunas de las posiciones, indicadas con un círculo doble, son especiales. Si, exactamente después de un número predeterminado de movimientos, el jugador se sitúa en una de esas posiciones especiales gana, de lo contrario pierde.

En el ejemplo, si el número total de movimientos es $m = 2$, fallar la primera pregunta y pasar la segunda, es decir, la secuencia 01, dirige al jugador de A, la posición inicial, a B y luego a C. Esta secuencia resuelve el problema, ya que C es una posición especial, de la única manera posible. De hecho, 00 llevaría a D y 10 y 11 a E, que no son especiales. En el caso $m = 3$, no hay solución. Pero en el caso $m = 5$, hay varias soluciones disponibles, por ejemplo 01011, 01101 o 00011. Así pues, hay 3 de $2^m = 32$ formas de ganar, lo que da una idea de la probabilidad de ganar sólo eligiendo las jugadas lanzando una moneda. Nótese que si A fuera también una posición especial, habría una forma de puntuar en cero jugadas. El problema a resolver es, dado un tapete y un número de movimientos m, determinar el número de formas diferentes de puntuar, es decir, de alcanzar una de las posiciones especiales en exactamente m movimientos, a partir de la posición inicial. La posición inicial es la primera posición, marcada con A. Desde cada posición hay exactamente 2 salidas, marcadas con los símbolos 0 y 1. Desde cada posición hay exactamente 2 salidas, marcadas con los símbolos 0 y 1. Desde cada posición hay exactamente 2 salidas.

![Fig. 1.](https://github.com/EAFIT-ST0247-Estruc-de-Datos-y-Alg-II/UVA-910-TV-Game/assets/423553/ec32f2de-d0c8-4336-82c0-f39ef7c1a9a3)
Fig. 1. Juego "alfombra para uno"

## Evaluación

La evaluación está organizada de la siguiente manera:

20% - El programa debe pasar todos los casos de prueba de udebug [uDebug - UVA 910 TV Game](https://www.udebug.com/UVa/7910). Recuerden que si se registran en udebug, tienen acceso a sugerencias sobre el problema.
40% - El programa debe para los casos de prueba del onlinejudge de UVA ([https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=9&page=show_problem&problem=650](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=11&page=show_problem&problem=851))
40% - La explicación de la solución utilizada y la calidad del código. Esto incluye:
1. Descripción del algoritmo. ¿Por qué funciona?
2. Descripción del mecanismo recursivo: ¿Cuál es la variable que determina el tamaño del problema? ¿Cuáles son los casos triviales? ¿Cuál es la relación de recurrencia?
3. Se revisará también la calidad del código. Algunos ejemplos de cosas que se penalizan:
    * Utilizar variables globales
    * Incluir en los ciclos cálculos que no cambian en cada iteración
    * Nombres arbitrarios de variables o funciones (aleatorios o sin ninguna relación con la semántica de la variable o la función)
