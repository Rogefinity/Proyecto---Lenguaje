import time

def _calcular_costo_ruta(grafo: dict, ruta: list) -> int:
    if len(ruta) < 2:
        return 0
    costo = 0
    for i in range(len(ruta) - 1):
        u, v = ruta[i], ruta[i + 1]
        for vecino, peso in grafo.get(u, []):
            if vecino == v:
                costo += peso
                break
    return costo

def bfs_search(grafo: dict, origen: str, destino: str, limite: float) -> dict:
    t0 = time.perf_counter()
    limite_nodos = max(1, int(len(grafo) * limite))
    cola = [[origen]]
    visitados = []
    ruta_final = []
    solucion = False

    while cola and len(visitados) < limite_nodos:
        camino = cola.pop(0)
        nodo = camino[-1]
        if nodo not in visitados:
            visitados.append(nodo)
            if nodo == destino:
                ruta_final = camino
                solucion = True
                break
            for vecino, _ in grafo.get(nodo, []):
                if vecino not in visitados:
                    cola.append(camino + [vecino])

    t1 = time.perf_counter()
    costo = _calcular_costo_ruta(grafo, ruta_final) if solucion else 0
    S_n = len(grafo) + len(visitados) + len(cola)
    return {
        "algoritmo": "BFS (Búsqueda en Anchura)",
        "nodos_visitados": len(visitados),
        "orden_visitados": visitados,
        "solucion": solucion,
        "ruta": ruta_final,
        "costo_camino": costo,
        "tiempo_ms": round((t1 - t0) * 1000, 4),
        "T_n": f"{(t1 - t0):.6f} s",
        "S_n": f"O({S_n})",
        "explicacion_teorica": "BFS explora el grafo por niveles utilizando una cola FIFO. Es completo y óptimo en número de pasos (saltos), pero no considera los pesos de las aristas."
    }

def greedy_best_first_search(grafo: dict, origen: str, destino: str, limite: float) -> dict:
    t0 = time.perf_counter()
    visitados = []
    ruta = []
    nodo_actual = origen
    limite_nodos = max(1, int(len(grafo) * limite))

    while nodo_actual != destino and len(visitados) < limite_nodos:
        if nodo_actual not in visitados:
            visitados.append(nodo_actual)
            ruta.append(nodo_actual)
        vecinos = grafo.get(nodo_actual, [])
        opciones = [v for v in vecinos if v[0] not in visitados]
        if not opciones:
            break
        vecino_optimo = min(opciones, key=lambda x: x[1])
        nodo_actual = vecino_optimo[0]

    if nodo_actual == destino:
        ruta.append(destino)
        visitados.append(destino)
        solucion = True
    else:
        solucion = False

    t1 = time.perf_counter()
    costo = _calcular_costo_ruta(grafo, ruta) if solucion else 0
    S_n = len(grafo) + len(visitados) + len(ruta)
    return {
        "algoritmo": "Greedy Best-First Search (Voraz)",
        "nodos_visitados": len(visitados),
        "orden_visitados": visitados,
        "solucion": solucion,
        "ruta": ruta if solucion else [],
        "costo_camino": costo,
        "tiempo_ms": round((t1 - t0) * 1000, 4),
        "T_n": f"{(t1 - t0):.6f} s",
        "S_n": f"O({S_n})",
        "explicacion_teorica": "La búsqueda voraz selecciona siempre el vecino con el menor costo inmediato local. Es sumamente rápida y ahorra memoria, pero no garantiza encontrar la solución óptima global."
    }

def _heuristica(nodo: str, destino: str, grafo: dict) -> int:
    if nodo == destino:
        return 0
    vecinos = grafo.get(nodo, [])
    if not vecinos:
        return 9999
    return min(vecinos, key=lambda x: x[1])[1]

def a_star_search(grafo: dict, origen: str, destino: str, limite: float) -> dict:
    t0 = time.perf_counter()
    limite_nodos = max(1, int(len(grafo) * limite))
    open_list = [(_heuristica(origen, destino, grafo), 0, origen, [origen])]
    closed_list = []
    solucion = False
    ruta_final = []
    costo_final = 0

    while open_list and len(closed_list) < limite_nodos:
        open_list.sort(key=lambda x: x[0])
        f_act, g_act, nodo_actual, camino = open_list.pop(0)

        if nodo_actual in closed_list:
            continue
        closed_list.append(nodo_actual)

        if nodo_actual == destino:
            solucion = True
            ruta_final = camino
            costo_final = g_act
            break

        for vecino, peso in grafo.get(nodo_actual, []):
            if vecino not in closed_list:
                g_nuevo = g_act + peso
                h_nuevo = _heuristica(vecino, destino, grafo)
                open_list.append((g_nuevo + h_nuevo, g_nuevo, vecino, camino + [vecino]))

    t1 = time.perf_counter()
    S_n = len(grafo) + len(closed_list) + len(open_list)
    return {
        "algoritmo": "A* (Búsqueda Estrella)",
        "nodos_visitados": len(closed_list),
        "orden_visitados": closed_list,
        "solucion": solucion,
        "ruta": ruta_final,
        "costo_camino": costo_final,
        "tiempo_ms": round((t1 - t0) * 1000, 4),
        "T_n": f"{(t1 - t0):.6f} s",
        "S_n": f"O({S_n})",
        "explicacion_teorica": "A* evalúa f(n) = g(n) + h(n), equilibrando el costo real acumulado g(n) y la estimación heurística h(n). Si h(n) es admisible, garantiza encontrar el camino de costo mínimo óptimo."
    }

