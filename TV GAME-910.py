def formas_de_ganar(posiciones, m):
    Ranteriores = {}

    def generador_formas(posicionActual, m_restantes):
        if m_restantes == 0:
            return 1 if posiciones[posicionActual][3] == 'x' else 0

        key = (posicionActual, m_restantes)
        if key in Ranteriores:
            return Ranteriores[key]

        cantidad = 0
        for choice in ['0', '1']:
            siguiente_posicion = posiciones[posicionActual][1 if choice == '0' else 2]
            if siguiente_posicion != '-':
                cantidad += generador_formas(ord(siguiente_posicion) - ord('A'), m_restantes - 1)

        Ranteriores[key] = cantidad
        return cantidad

    posicion_inicial = 0
    return generador_formas(posicion_inicial, m)

try:
    while True:
        # Leer y descartar líneas en blanco o saltos de línea antes de n
        while True:
            line = input().strip()
            if line:
                n = int(line)
                break

        posiciones = []  # Almacenar las posiciones
        for _ in range(n):
            line = input().strip()
            posiciones.append(line.split())

        m = int(input())  # Leemos el valor de m después de las posiciones
        result = formas_de_ganar(posiciones, m)
        print(result)

except ValueError:
    pass
except EOFError:
    pass