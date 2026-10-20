import streamlit as st
import requests
import json

# Configuración de la página
st.set_page_config(
    page_title="Reto Integrador - Lenguajes de Computación",
    page_icon="💻",
    layout="wide"
)

# URL base de tu API FastAPI (asegúrate de que esté corriendo en el puerto 8001 o el que uses)
API_URL = "http://127.0.0.1:8001"

st.title("🚀 Reto Integrador: Sistema de Lenguajes de Computación")
st.markdown("**Equipo:** Rogelio Sotomayor, Carlos Jesús Graniel, Carlos Andrés Hernández, Nico Trujillo | **IBERO Puebla**")
st.markdown("---")

# Menú lateral para los apartados principales
st.sidebar.header("🧭 Menú de Navegación")
apartado = st.sidebar.selectbox(
    "Seleccione el apartado principal:",
    [
        "1. Lenguajes y Autómatas",
        "2. Analizador Léxico y Complejidad",
        "3. Grafos y Ordenamiento"
    ]
)

# ==============================================================================
# APARTADO 1: LENGUAJES Y AUTÓMATAS (Actividades 3 y 6)
# ==============================================================================
if apartado == "1. Lenguajes y Autómatas":
    st.header("🔤 Módulo 1: Lenguajes Formales y Autómatas")
    
    tab1, tab2 = st.tabs(["Operaciones de Lenguajes", "Evaluación de Autómatas (AFD/AFND/AFND-ε)"])
    
    with tab1:
        st.subheader("Operaciones sobre Lenguajes (Actividad 3)")
        col1, col2 = st.columns(2)
        with col1:
            l_a_str = st.text_input("Lenguaje A (separado por comas)", "a, ab, b")
            operacion = st.selectbox(
                "Operación", 
                ["union", "interseccion", "diferencia", "concatenacion", "potencia", "kleene", "inverso"]
            )
        with col2:
            l_b_str = st.text_input("Lenguaje B (separado por comas)", "b, ba, bb")
            potencia = st.number_input("Potencia (n)", min_value=0, max_value=4, value=2)
            
        if st.button("Ejecutar Operación de Lenguaje"):
            la = [x.strip() for x in l_a_str.split(",") if x.strip()]
            lb = [x.strip() for x in l_b_str.split(",") if x.strip()]
            payload = {"lenguaje_a": la, "lenguaje_b": lb, "operacion": operacion, "potencia": potencia}
            
            try:
                res = requests.post(f"{API_URL}/api/lenguajes/operar", json=payload)
                if res.status_code == 200:
                    data = res.json()
                    st.success("¡Operación realizada con éxito!")
                    st.json(data)
                    st.info(f"**Sustento teórico:** {data.get('explicacion_teorica')}")
                else:
                    st.error(f"Error en la API: {res.text}")
            except Exception as e:
                st.error(f"No se pudo conectar con el servidor FastAPI: {e}")

    with tab2:
        st.subheader("Evaluador de Autómatas por Matriz de Transición (Actividad 6)")
        tipo_aut = st.selectbox("Tipo de Autómata", ["AFD", "AFND", "AFND-e"])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            alfabeto_str = st.text_input("Alfabeto (coma)", "0, 1")
            estado_ini = st.text_input("Estado Inicial", "q0")
        with col2:
            estados_str = st.text_input("Estados (coma)", "q0, q1, q2")
            estados_fin = st.text_input("Estados Finales (coma)", "q2")
        with col3:
            palabra = st.text_input("Palabra a Evaluar", "01")
            
        st.markdown("**Matriz de Transiciones (Formato JSON)**")
        default_trans = {
            "q0": {"0": ["q0"], "1": ["q1"], "e": ["q1"]},
            "q1": {"1": ["q2"]},
            "q2": {"0": ["q2"], "1": ["q2"]}
        }
        trans_input = st.text_area("Diccionario de Transiciones", value=json.dumps(default_trans, indent=2), height=150)
        
        if st.button("Evaluar Autómata"):
            try:
                trans_dict = json.loads(trans_input)
                payload = {
                    "tipo": tipo_aut,
                    "alfabeto": [x.strip() for x in alfabeto_str.split(",")],
                    "estados": [x.strip() for x in estados_str.split(",")],
                    "estado_inicial": estado_ini.strip(),
                    "estados_finales": [x.strip() for x in estados_fin.split(",")],
                    "transiciones": trans_dict,
                    "palabra": palabra.strip()
                }
                res = requests.post(f"{API_URL}/api/automata/evaluar-matriz", json=payload)
                if res.status_code == 200:
                    data = res.json()
                    if data.get("pertenece"):
                        st.success(f"🎉 ¡La palabra '{palabra}' es ACEPTADA por el autómata!")
                    else:
                        st.warning(f"❌ La palabra '{palabra}' NO es aceptada por el autómata.")
                    st.json(data)
                else:
                    st.error(f"Error: {res.text}")
            except Exception as e:
                st.error(f"Error al procesar JSON o conectar con la API: {e}")

# ==============================================================================
# APARTADO 2: ANALIZADOR LÉXICO Y COMPLEJIDAD (Actividad 11)
# ==============================================================================
elif apartado == "2. Analizador Léxico y Complejidad":
    st.header("📊 Módulo 2: Analizador Léxico y Complejidad Algorítmica")
    
    codigo_ejemplo = """def ejemplo_complejidad(n):\n    total = 0\n    for i in range(n):\n        for j in range(n):\n            total += i * j\n    return total"""
    
    codigo_usuario = st.text_area("Código fuente en Python a analizar:", value=codigo_ejemplo, height=150)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Ejecutar Analizador Léxico"):
            files = {"file": ("codigo.py", codigo_usuario, "text/plain")}
            res = requests.post(f"{API_URL}/api/automata/analizar", files=files)
            if res.status_code == 200:
                st.success("Tokens identificados:")
                st.json(res.json())
            else:
                st.error(res.text)
                
    with col2:
        if st.button("Calcular Big-O (Cota Superior)"):
            files = {"file": ("codigo.py", codigo_usuario, "text/plain")}
            res = requests.post(f"{API_URL}/api/complejidad/big-o", files=files)
            if res.status_code == 200:
                st.success("Resultado Big-O:")
                st.text(res.text)
            else:
                st.error(res.text)
                
    with col3:
        if st.button("Calcular Big-Omega (Cota Inferior)"):
            files = {"file": ("codigo.py", codigo_usuario, "text/plain")}
            res = requests.post(f"{API_URL}/api/complejidad/big-omega", files=files)
            if res.status_code == 200:
                st.success("Resultado Big-Omega:")
                st.text(res.text)
            else:
                st.error(res.text)

# ==============================================================================
# APARTADO 3: GRAFOS Y ORDENAMIENTO (Actividades 12 y 13)
# ==============================================================================
elif apartado == "3. Grafos y Ordenamiento":
    st.header("📈 Módulo 3: Grafos, Búsqueda y Algoritmos de Ordenamiento")
    
    tab1, tab2 = st.tabs(["Búsqueda en Grafos (Act. 12)", "Comparativa de Ordenamiento (Act. 13)"])
    
    with tab1:
        st.subheader("Búsqueda Informada y No Informada")
        default_grafo = {
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
        grafo_input = st.text_area("Estructura del Grafo (JSON)", value=json.dumps(default_grafo, indent=2), height=150)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            origen = st.text_input("Nodo Origen", "A")
        with c2:
            destino = st.text_input("Nodo Destino", "J")
        with c3:
            limite = st.slider("Límite de exploración (nodos)", 0.1, 1.0, 1.0)
            
        if st.button("Comparar Algoritmos de Búsqueda (BFS, Greedy, A*)"):
            try:
                g_dict = json.loads(grafo_input)
                payload = {"grafo": g_dict, "origen": origen.strip(), "destino": destino.strip(), "limite_nodos": limite}
                res = requests.post(f"{API_URL}/search/comparar-grafos", json=payload)
                if res.status_code == 200:
                    st.success("Resultados de comparación de rutas:")
                    st.json(res.json())
                else:
                    st.error(res.text)
            except Exception as e:
                st.error(f"Error: {e}")

    with tab2:
        st.subheader("Rendimiento de Algoritmos de Ordenamiento (Actividad 13)")
        datos_str = st.text_input("Lista de números desordenados (coma)", "64, 34, 25, 12, 22, 11, 90, 5, 77, 1, 43, 88")
        algoritmos_sel = st.multiselect(
            "Seleccionar algoritmos (al menos 2):",
            ["bubble", "insertion", "selection", "merge", "quick"],
            default=["bubble", "merge", "quick"]
        )
        
        if st.button("Ejecutar Comparativa de Performance"):
            try:
                lista_datos = [int(x.strip()) for x in datos_str.split(",") if x.strip()]
                payload = {"datos": lista_datos, "algoritmos": algoritmos_sel}
                res = requests.post(f"{API_URL}/api/ordenamiento/comparar", json=payload)
                if res.status_code == 200:
                    data = res.json()
                    st.success("¡Comparativa ejecutada exitosamente!")
                    st.json(data)
                    st.info(f"**Análisis Teórico:** {data.get('explicacion_teorica')}")
                else:
                    st.error(res.text)
            except Exception as e:
                st.error(f"Error al procesar datos: {e}")