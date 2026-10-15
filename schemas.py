from pydantic import BaseModel, Field
from typing import Dict, List, Tuple, Optional

# --- ACTIVIDAD 3: LENGUAJES ---
class LenguajesInput(BaseModel):
    lenguaje_a: List[str] = Field(..., example=["a", "ab", "b"])
    lenguaje_b: List[str] = Field(default=[], example=["b", "ba", "bb"])
    operacion: str = Field(..., description="union, interseccion, diferencia, concatenacion, potencia, kleene, inverso")
    potencia: int = Field(default=2, ge=0, le=4)

# --- ACTIVIDAD 6: AUTÓMATAS (AFD, AFND, AFND-e) ---
class AutomataInput(BaseModel):
    tipo: str = Field(..., example="AFND-e", description="AFD, AFND o AFND-e")
    alfabeto: List[str] = Field(..., example=["0", "1"])
    estados: List[str] = Field(..., example=["q0", "q1", "q2"])
    estado_inicial: str = Field(..., example="q0")
    estados_finales: List[str] = Field(..., example=["q2"])
    # Matriz de transiciones: { estado: { simbolo: [estados_destino] } } (usar "e" para epsilon)
    transiciones: Dict[str, Dict[str, List[str]]] = Field(
        ...,
        example={
            "q0": {"0": ["q0"], "1": ["q1"], "e": ["q1"]},
            "q1": {"1": ["q2"]},
            "q2": {"0": ["q2"], "1": ["q2"]}
        }
    )
    palabra: str = Field(..., example="01")

# --- ACTIVIDAD 12: GRAFOS Y BÚSQUEDA ---
class GrafoInput(BaseModel):
    grafo: Dict[str, List[Tuple[str, int]]] = Field(
        ...,
        example={
            "A": [["B", 15], ["C", 22], ["D", 10]],
            "B": [["E", 35], ["F", 18]],
            "C": [["E", 20], ["G", 45]],
            "D": [["F", 28], ["G", 30]],
            "E": [["H", 12], ["I", 25]],
            "F": [["H", 40], ["I", 15]],
            "G": [["I", 10], ["J", 50]],
            "H": [["J", 14]],
            "I": [["J", 8]],
            "J": []
        }
    )
    origen: str = Field(..., example="A")
    destino: str = Field(..., example="J")
    algoritmos: List[str] = Field(default=["bfs", "greedy", "a_star"])
    limite_nodos: float = Field(default=1.0, ge=0.1, le=1.0)

# --- ACTIVIDAD 13: ORDENAMIENTO ---
class OrdenamientoInput(BaseModel):
    datos: List[int] = Field(..., example=[64, 34, 25, 12, 22, 11, 90, 5, 77, 1, 43, 88])
    algoritmos: List[str] = Field(
        ...,
        min_length=2,
        example=["bubble", "quick", "merge"],
        description="Seleccionar al menos 2: bubble, insertion, selection, merge, quick"
    )
