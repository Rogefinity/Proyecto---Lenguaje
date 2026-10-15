import re

TOKEN_REGEX = [
    ('RESERVADA', r'\b(if|else|elif|while|for|return|def|int|float|class|print|in|range|len)\b'),
    ('NUMERO', r'\b\d+(\.\d+)?\b'),
    ('IDENTIFICADOR', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('OPERADOR', r'[\+\-\*/=<>!]+'),
    ('SIMBOLO', r'[():;{},\[\]]'),
    ('ESPACIO', r'\s+'),
    ('DESCONOCIDO', r'.')
]

def analizar_lexico_tokens(contenido: str) -> list:
    tokens_encontrados = []
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_REGEX)
    for mo in re.finditer(tok_regex, contenido):
        tipo = mo.lastgroup
        valor = mo.group()
        if tipo == 'ESPACIO':
            continue
        elif tipo == 'DESCONOCIDO':
            tokens_encontrados.append({"tipo": "ERROR_LEXICO", "valor": valor})
        else:
            tokens_encontrados.append({"tipo": tipo, "valor": valor})
    return tokens_encontrados

def calcular_complejidad(codigo: str, notacion: str) -> str:
    lineas = codigo.split("\n")
    lineas_procesadas = []
    complejidades_encontradas = set()
    grado_maximo = 0.0
    pila_ciclos = []

    for linea in lineas:
        texto_limpio = linea.strip()
        if not texto_limpio or texto_limpio.startswith("#"):
            lineas_procesadas.append(linea)
            continue

        indentacion = len(linea) - len(linea.lstrip(' '))
        while pila_ciclos and pila_ciclos[-1][0] >= indentacion:
            pila_ciclos.pop()

        if texto_limpio.startswith("for ") or texto_limpio.startswith("while "):
            pila_ciclos.append([indentacion, 1.0])

        if "// 2" in texto_limpio or "/ 2" in texto_limpio or "*= 2" in texto_limpio:
            if pila_ciclos:
                pila_ciclos[-1][1] = 0.5

        suma_actual = sum(c[1] for c in pila_ciclos)
        grado_maximo = max(grado_maximo, suma_actual)

        if suma_actual == 0:
            comp_str = f"{notacion}(1)"
        elif suma_actual == 0.5:
            comp_str = f"{notacion}(log n)"
        elif suma_actual == 1.0:
            comp_str = f"{notacion}(n)"
        elif suma_actual == 1.5:
            comp_str = f"{notacion}(n log n)"
        else:
            comp_str = f"{notacion}(n^{int(suma_actual)})"

        complejidades_encontradas.add(comp_str)
        linea_sin_salto = linea.replace('\n', '').replace('\r', '')
        lineas_procesadas.append(f"{linea_sin_salto:<50} # {comp_str}")

    if grado_maximo == 0:
        mayor = f"{notacion}(1)"
    elif grado_maximo == 0.5:
        mayor = f"{notacion}(log n)"
    elif grado_maximo == 1.0:
        mayor = f"{notacion}(n)"
    elif grado_maximo == 1.5:
        mayor = f"{notacion}(n log n)"
    else:
        mayor = f"{notacion}(n^{int(grado_maximo)})"

    teoria = (
        "Explicación teórica: La notación Big-O representa la cota superior asintótica (peor caso) "
        "y Big-Omega (Ω) representa la cota inferior asintótica (mejor caso) cuando n → ∞. "
        "Se evalúa mediante una heurística de pila de indentación y detección de particiones logarítmicas."
    )

    resumen = "\n\n" + "="*65 + "\n"
    resumen += "RESUMEN DE COMPLEJIDAD IDENTIFICADA\n"
    resumen += "="*65 + "\n"
    resumen += f"Suma de complejidades individuales: {' + '.join(sorted(complejidades_encontradas))}\n"
    resumen += f"Complejidad de mayor grado: {mayor}\n"
    resumen += f"{teoria}\n"
    resumen += "="*65 + "\n"

    return "\n".join(lineas_procesadas) + resumen
