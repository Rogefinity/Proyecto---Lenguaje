import time
import tracemalloc

def _bubble_sort(arr: list) -> list:
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def _insertion_sort(arr: list) -> list:
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def _selection_sort(arr: list) -> list:
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def _merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = _merge_sort(arr[:mid])
    right = _merge_sort(arr[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def _quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return _quick_sort(left) + middle + _quick_sort(right)

CATALOGO = {
    "bubble": ("Bubble Sort", _bubble_sort, "O(n^2)", "O(1)"),
    "insertion": ("Insertion Sort", _insertion_sort, "O(n^2)", "O(1)"),
    "selection": ("Selection Sort", _selection_sort, "O(n^2)", "O(1)"),
    "merge": ("Merge Sort", _merge_sort, "O(n log n)", "O(n)"),
    "quick": ("Quick Sort", _quick_sort, "O(n log n) prom / O(n^2) peor", "O(log n)")
}

def comparar_ordenamientos(datos: list, algoritmos: list) -> dict:
    resultados = []
    datos_ordenados = []

    for clave in algoritmos:
        clave_limpia = clave.lower().strip()
        if clave_limpia not in CATALOGO:
            continue
        nombre, funcion, big_o_t, big_o_s = CATALOGO[clave_limpia]

        tracemalloc.start()
        t0 = time.perf_counter()
        ordenado = funcion(datos)
        t1 = time.perf_counter()
        _, memoria_pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        datos_ordenados = ordenado
        resultados.append({
            "id": clave_limpia,
            "algoritmo": nombre,
            "tiempo_ms": round((t1 - t0) * 1000, 5),
            "memoria_bytes": memoria_pico,
            "complejidad_temporal": big_o_t,
            "complejidad_espacial": big_o_s
        })

    teoria = (
        "Los algoritmos cuadráticos O(n^2) como Bubble, Insertion y Selection Sort comparan elementos "
        "adyacentes con bajo uso de memoria espacial O(1), pero escalan mal con grandes volúmenes de datos. "
        "Los algoritmos Divide y Vencerás como Merge Sort y Quick Sort logran tasas O(n log n) a cambio de "
        "mayor consumo de memoria auxiliar en pilas de recursión o sub-arreglos (Trade-off Tiempo-Espacio)."
    )

    return {
        "total_elementos": len(datos),
        "datos_originales": datos,
        "datos_ordenados": datos_ordenados,
        "comparativa": resultados,
        "explicacion_teorica": teoria
    }
