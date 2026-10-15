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

## Ejecución
```bash
source .venv/bin/activate
pip install -r requirements.txt
python3 -m uvicorn main:app --reload --port 8001
