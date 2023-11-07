# Dinamic Programing-UVA-910-TV GAME-SOLUTION

1. Descripción del algoritmo. ¿Por qué funciona?

>El algoritmo comienza desde la posición inicial y llama a `generador_formas(posicion_inicial, m)` para calcular la cantidad de formas de ganar el juego con `m` movimientos disponibles.
El algoritmo utiliza una función recursiva llamada generador_formas, que toma dos parámetros: `posicionActual` y `m_restantes`. `posicionActual` representa la posición actual del jugador en el juego, y `m_restantes` es el número de movimientos restantes que el jugador puede hacer.
La función calcula la cantidad de formas en las que el jugador puede ganar el juego desde la posición actual con los movimientos restantes. Utiliza una memoria `Ranteriores` (un diccionario) para almacenar los resultados previamente calculados y evitar recalculos innecesarios.
El algoritmo recorre todas las posibles elecciones de movimiento ('0' o '1') desde la posición actual, verifica si la próxima posición es válida (no es '-') y luego llama recursivamente a `generador_formas` con la nueva posición y `m_restantes` - 1. Suma todas las formas posibles desde las elecciones y almacena el resultado en la memoria `Ranteriores`.

2. Descripción del mecanismo recursivo: ¿Cuál es la variable que determina el tamaño del problema? ¿Cuáles son los casos triviales? ¿Cuál es la relación de recurrencia?

>La variable que determina el tamaño del problema es `m_restantes`, que representa el número de movimientos restantes en el juego. Cuando `m_restantes` llega a cero, se considera un caso base y se retorna 1 si la posición actual es una posición de victoria ('x') o 0 si no lo es.
Los casos triviales son cuando `m_restantes` es igual a cero, y la relación de recurrencia se encuentra en el bucle que recorre las posibles elecciones de movimiento ('0' o '1') y llama a `generador_formas` recursivamente con `m_restantes` - 1.