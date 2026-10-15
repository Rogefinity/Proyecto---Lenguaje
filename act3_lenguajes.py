def _concatenar(l1: set, l2: set) -> set:
    if not l1: return l2
    if not l2: return l1
    return {w1 + w2 for w1 in l1 for w2 in l2}

def evaluar_lenguaje(la: list, lb: list, operacion: str, n: int = 2) -> dict:
    set_a = set(la)
    set_b = set(lb)
    op = operacion.lower()
    pasos = []

    if op == "union":
        res = sorted(list(set_a | set_b))
        teoria = "La unión de dos lenguajes L1 ∪ L2 contiene todas las cadenas que pertenecen a L1, a L2, o a ambos."
        pasos.append(f"Elementos en A: {sorted(list(set_a))}")
        pasos.append(f"Elementos en B: {sorted(list(set_b))}")
    elif op == "interseccion":
        res = sorted(list(set_a & set_b))
        teoria = "La intersección L1 ∩ L2 contiene únicamente las cadenas que pertenecen simultáneamente a L1 y L2."
        pasos.append("Se filtran los elementos comunes entre ambos conjuntos.")
    elif op == "diferencia":
        res = sorted(list(set_a - set_b))
        teoria = "La diferencia L1 - L2 contiene las cadenas que están en L1 pero no pertenecen a L2."
        pasos.append("Se eliminan de A las cadenas presentes en B.")
    elif op == "concatenacion":
        res = sorted(list(_concatenar(set_a, set_b)))
        teoria = "La concatenación L1·L2 forma cadenas uniendo cada palabra w1 ∈ L1 con cada palabra w2 ∈ L2."
        pasos.append(f"Producto cartesiano concatenado de {len(set_a)}x{len(set_b)} elementos.")
    elif op == "potencia":
        actual = {""}
        for i in range(1, n + 1):
            actual = _concatenar(actual, set_a)
            pasos.append(f"L^{i} = {sorted(list(actual))}")
        res = sorted(list(actual))
        teoria = f"La potencia L^{n} concatena el lenguaje L consigo mismo {n} veces (donde L^0 = {{ε}})."
    elif op == "kleene":
        acumulado = {"ε"}
        actual = {""}
        for i in range(1, 3):
            actual = _concatenar(actual, set_a)
            acumulado |= actual
            pasos.append(f"Nivel {i} (L^{i}): {sorted(list(actual))}")
        res = sorted(list(acumulado)) + ["..."]
        teoria = "La cerradura de Kleene (L*) es la unión infinita de todas las potencias L^k para k ≥ 0. Se muestra hasta k=2."
    elif op == "inverso":
        res = sorted([w[::-1] for w in set_a])
        teoria = "El inverso o reflejo (L^R) invierte el orden de los símbolos de cada palabra perteneciente al lenguaje."
        pasos.append("Inversión carácter por carácter de cada cadena en L1.")
    else:
        return {"error": "Operación no válida."}

    return {
        "operacion": op,
        "resultado": res,
        "cardinalidad": len(res),
        "pasos": pasos,
        "explicacion_teorica": teoria
    }
