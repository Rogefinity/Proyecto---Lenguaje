# Proyecto-Lenguaje
# Proyecto Integrador: Lenguajes de Computación
**Estudiante:** 
*Rogelio Sotomayor Carrasco - 195721*
*Carlos Jesús Graniel González - 200871*
*Carlos Andrés Hernández Díaz - 200711*
*Nico Trujillo Beristain - 200408*
**Materia:** Lenguajes de Computación — IBERO Puebla  
**Profesor:** Paulo Daniel Vázquez Mora  

## Descripción General
Repositorio unificado en **FastAPI** que integra los backends, endpoints y visualizaciones de las **Actividades 3, 6, 11, 12 y 13**, acompañando cada resultado con su explicación del proceso y sustento teórico.

## Módulos y Endpoints Integrados

1. **Módulo de Lenguajes y Autómatas (Actividades 3 y 6)**
   - `POST /api/lenguajes/operar`: Evalúa operaciones de lenguajes formales (Unión, Intersección, Diferencia, Concatenación, Potencia, Cerradura de Kleene e Inverso).
   - `POST /api/automata/evaluar-matriz`: Evalúa matrices de transición propuestas por el usuario para determinar la pertenencia de una palabra mediante un **AFD, AFND o AFND-ε**.
   - `POST /api/automata/analizar`: Analizador léxico por expresiones regulares.

2. **Módulo de Complejidad Algorítmica (Actividad 11)**
   - `POST /api/complejidad/big-o`: Analiza un archivo de código fuente línea por línea calculando su cota superior asintótica $O(g(n))$.
   - `POST /api/complejidad/big-omega`: Calcula la cota inferior asintótica $\Omega(g(n))$.

3. **Módulo de Grafos y Búsqueda Informada/No Informada (Actividad 12)**
   - `POST /search/greedy`: Algoritmo Voraz (Greedy Best-First Search).
   - `POST /search/star`: Algoritmo $A^*$ con función $f(n) = g(n) + h(n)$.
   - `POST /search/comparar-grafos`: Evalúa múltiples algoritmos (BFS, Greedy, $A^*$) sobre el mismo grafo, renderizando gráficamente el grafo ponderado con la ruta resaltada en color contrastante y tabla comparativa de camino, costo y tiempo.

4. **Módulo de Ordenamiento y Performance (Actividad 13)**
   - `POST /api/ordenamiento/comparar`: Permite seleccionar al menos 2 algoritmos de un catálogo (*Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Quick Sort*), devolviendo el conjunto ordenado, tiempo de ejecución, memoria consumida y gráfica comparativa de performance.

# Checkpoint 2. Implementación de frontend
**Estudiante:** Rogelio Sotomayor Carrasco  
**No. de cuenta:** 195721  
**Materia:** Lenguajes de Computación — IBERO Puebla  

## Descripción General
Este repositorio contiene la implementación unificada del Reto Integrador. Se integra un **Backend** desarrollado en FastAPI con una arquitectura modular para las Actividades 3, 6, 11, 12 y 13, y un **Frontend** interactivo (GUI) que permite al usuario evaluar los tres apartados principales del sistema de manera visual y funcional.

## Arquitectura del Proyecto

### 1. Backend (FastAPI)
El backend está construido con Python y utiliza `pydantic` para la validación estricta de datos. Se divide en módulos independientes:
*   `modulos/act3_lenguajes.py`: Operaciones formales de conjuntos (Unión, Intersección, Kleene, etc.).
*   `modulos/act6_automatas.py`: Evaluación de palabras mediante matrices de transición para AFD, AFND y AFND-ε.
*   `modulos/act11_complejidad.py`: Analizador léxico y cálculo asintótico de Big-O / Big-Omega.
*   `modulos/act12_grafos.py`: Búsquedas en grafos ponderados implementando BFS (no informada) y algoritmos heurísticos (Greedy Best-First Search y A*).
*   `modulos/act13_ordenamiento.py`: Catálogo de algoritmos de ordenamiento evaluando complejidad espacial y temporal.

### 2. Frontend (Interfaz Gráfica)
El frontend (`static/index.html`) está diseñado para consumir la API de forma asíncrona mediante `fetch`. Utiliza las siguientes tecnologías:
*   **TailwindCSS:** Para un diseño responsivo, limpio y estructurado.
*   **Vis-network (vis.js):** Para la renderización dinámica de los grafos ponderados, resaltando la ruta de solución encontrada por los algoritmos (BFS, Greedy o A*).
*   **Chart.js:** Para la graficación de barras que compara visualmente el tiempo de ejecución (performance) de los distintos algoritmos de ordenamiento.

## Apartados de la GUI
La interfaz muestra 3 secciones principales:
1.  **Lenguajes y Autómatas:** Formularios para evaluar la pertenencia de cadenas dadas matrices de transición en formato JSON.
2.  **Búsqueda en Grafos:** Ingreso de listas de adyacencia y nodos origen/destino para comparar rutas. Muestra el grafo renderizado y una tabla con costos, tiempos y nodos visitados.
3.  **Algoritmos de Ordenamiento:** Selección interactiva de algoritmos (Bubble, Merge, Quick, etc.) para ordenar un conjunto de datos, visualizando los tiempos de procesamiento en una gráfica en pantalla.

## Instrucciones de Ejecución
Para desplegar el proyecto localmente, ejecuta los siguientes comandos en la terminal desde la raíz del repositorio:

1. **Activar el entorno virtual:**
   ```bash
   source .venv/bin/activate
## Ejecución
```bash
source .venv/bin/activate
pip install -r requirements.txt
python3 -m uvicorn main:app --reload --port 8001
