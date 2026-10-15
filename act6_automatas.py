def cerradura_epsilon(estados_actuales: set, transiciones: dict) -> set:
    pila = list(estados_actuales)
    cerradura = set(estados_actuales)
    while pila:
        estado = pila.pop()
        destinos_e = transiciones.get(estado, {}).get("e", []) + transiciones.get(estado, {}).get("ε", [])
        for dest in destinos_e:
            if dest not in cerradura:
                cerradura.add(dest)
                pila.append(dest)
    return cerradura

def evaluar_automata(datos) -> dict:
    tipo = datos.tipo.upper()
    trans = datos.transiciones
    estados_activos = {datos.estado_inicial}
    historial_pasos = []

    if "E" in tipo or "ε" in tipo:
        estados_activos = cerradura_epsilon(estados_activos, trans)
        historial_pasos.append(f"Cerradura-ε inicial desde {datos.estado_inicial}: {sorted(list(estados_activos))}")
    else:
        historial_pasos.append(f"Estado inicial: {sorted(list(estados_activos))}")

    for simbolo in datos.palabra:
        siguientes = set()
        for est in estados_activos:
            destinos = trans.get(est, {}).get(simbolo, [])
            siguientes.update(destinos)

        if "E" in tipo or "ε" in tipo:
            siguientes = cerradura_epsilon(siguientes, trans)

        historial_pasos.append(f"Con símbolo '{simbolo}': {sorted(list(estados_activos))} -> {sorted(list(siguientes))}")
        estados_activos = siguientes

        if not estados_activos:
            break

    finales = set(datos.estados_finales)
    interseccion_final = estados_activos & finales
    pertenece = len(interseccion_final) > 0

    teoria = {
        "AFD": "Un Autómata Finito Determinista (AFD) tiene exactamente una transición por cada símbolo del alfabeto desde cualquier estado. Es decidible en tiempo lineal O(|w|).",
        "AFND": "Un Autómata Finito No Determinista (AFND) permite múltiples transiciones o ninguna para un mismo símbolo. Acepta la palabra si al menos un camino alcanza un estado final.",
        "AFND-E": "Un AFND con transiciones épsilon (AFND-ε) permite cambiar de estado sin consumir símbolos de entrada, calculando la cerradura-ε en cada paso."
    }.get(tipo, "Evaluación mediante matriz de transición de estados sobre lenguajes regulares.")

    return {
        "tipo_automata": tipo,
        "palabra": datos.palabra,
        "pertenece": pertenece,
        "estados_alcanzados": sorted(list(estados_activos)),
        "estados_aceptacion_alcanzados": sorted(list(interseccion_final)),
        "pasos_ejecucion": historial_pasos,
        "explicacion_teorica": teoria
    }
