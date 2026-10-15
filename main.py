from fastapi import FastAPI, UploadFile, File
from fastapi.responses import PlainTextResponse, JSONResponse

from schemas import LenguajesInput, AutomataInput, GrafoInput, OrdenamientoInput
from modulos.act3_lenguajes import evaluar_lenguaje
from modulos.act6_automatas import evaluar_automata
from modulos.act11_complejidad import analizar_lexico_tokens, calcular_complejidad
from modulos.act12_grafos import bfs_search, greedy_best_first_search, a_star_search
from modulos.act13_ordenamiento import comparar_ordenamientos

app = FastAPI(title="Proyecto Integrador - Lenguajes de Computación")

@app.get("/")
def estado_servidor():
    return {"mensaje": "API Activa", "docs": "/docs"}

@app.post("/api/lenguajes/operar")
def endpoint_lenguajes(datos: LenguajesInput):
    return evaluar_lenguaje(datos.lenguaje_a, datos.lenguaje_b, datos.operacion, datos.potencia)

@app.post("/api/automata/evaluar-matriz")
def endpoint_evaluar_automata(datos: AutomataInput):
    return evaluar_automata(datos)

@app.post("/api/automata/analizar")
async def endpoint_analizar_lexico(file: UploadFile = File(...)):
    contenido = (await file.read()).decode("utf-8")
    return JSONResponse(content={"tokens": analizar_lexico_tokens(contenido)})

@app.post("/api/complejidad/big-o", response_class=PlainTextResponse)
async def endpoint_big_o(file: UploadFile = File(...)):
    contenido = (await file.read()).decode("utf-8")
    return calcular_complejidad(contenido, "O")

@app.post("/api/complejidad/big-omega", response_class=PlainTextResponse)
async def endpoint_big_omega(file: UploadFile = File(...)):
    contenido = (await file.read()).decode("utf-8")
    return calcular_complejidad(contenido, "Ω")

@app.post("/search/greedy")
def endpoint_greedy(datos: GrafoInput):
    return greedy_best_first_search(datos.grafo, datos.origen, datos.destino, datos.limite_nodos)

@app.post("/search/star")
def endpoint_star(datos: GrafoInput):
    return a_star_search(datos.grafo, datos.origen, datos.destino, datos.limite_nodos)

@app.post("/search/comparar-grafos")
def endpoint_comparar_grafos(datos: GrafoInput):
    resultados = [
        bfs_search(datos.grafo, datos.origen, datos.destino, datos.limite_nodos),
        greedy_best_first_search(datos.grafo, datos.origen, datos.destino, datos.limite_nodos),
        a_star_search(datos.grafo, datos.origen, datos.destino, datos.limite_nodos)
    ]
    return {"origen": datos.origen, "destino": datos.destino, "resultados": resultados}

@app.post("/api/ordenamiento/comparar")
def endpoint_ordenamiento(datos: OrdenamientoInput):
    return comparar_ordenamientos(datos.datos, datos.algoritmos)

