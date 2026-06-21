import streamlit as st
from core.grafos import cargar_grafo_desde_csv
from core.caminos import calcular_ruta_dijkstra
from frontend.visualizacion import crear_grafico
from frontend.interfaz import (
    aplicar_estilos,
    mostrar_sidebar,
    mostrar_titulo,
    mostrar_controles,
    mostrar_ruta_optima,
)

#Configuración general de la página 
st.set_page_config(
    page_title="Visualizador Dijkstra",
    layout="wide",
)

#Aplicamos los colores y estilos
aplicar_estilos()

#Mostramos el título apenas carga la página
mostrar_titulo()

#Mostramos el panel izquierdo con info del grupo
mostrar_sidebar()

# Cargamos las ciudades y conexiones desde el archivo CSV
grafo = cargar_grafo_desde_csv("data/conexiones.csv")
lista_ciudades = sorted(grafo.keys())

# Variables de estado (aseguramos guardar origen y destino)
if "tiempo_total" not in st.session_state:
    st.session_state["tiempo_total"] = None
if "ruta" not in st.session_state:
    st.session_state["ruta"] = None
if "modo_viaje" not in st.session_state:
    st.session_state["modo_viaje"] = "tren_min"
if "origen" not in st.session_state:
    st.session_state["origen"] = lista_ciudades[0]
if "destino" not in st.session_state:
    st.session_state["destino"] = lista_ciudades[0]

# ==========================================
# 1. MOSTRAR EL MAPA PRIMERO (ARRIBA)
# ==========================================
figura_actual = crear_grafico(
    grafo,
    st.session_state["ruta"],
    st.session_state["origen"],
    st.session_state["destino"],
    modo_viaje=st.session_state["modo_viaje"]
)
st.plotly_chart(figura_actual, use_container_width=True, config={"displayModeBar": False})

# --- NUEVO: Mostrar el tiempo total debajo del mapa de forma destacada ---
if st.session_state["tiempo_total"] is not None:
    t_total = st.session_state["tiempo_total"]
    horas = t_total // 60
    mins = t_total % 60
    if horas > 0:
        texto_tiempo = f"{horas} h {mins} min" if mins > 0 else f"{horas} h"
    else:
        texto_tiempo = f"{t_total} min"
        
    st.markdown(
        f"""
        <div style="display: flex; justify-content: right; margin-top: -10px; margin-bottom: 10px;">
            <div style="background-color: #1E212B; padding: 10px 25px; border-radius: 50px; border: 1px solid #333333; box-shadow: 0px 4px 6px rgba(0,0,0,0.3);">
                <span style="color: #ffffff; font-size: 15px; margin-right: 8px;">Tiempo estimado de viaje:</span>
                <span style="color: #D4A96A; font-size: 16px; font-weight: bold;">{texto_tiempo}</span>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
# --------------------------------------------------------------------------

st.divider()

# ==========================================
# 2. MOSTRAR LOS CONTROLES (ABAJO DEL MAPA)
# ==========================================
origen, destino, modo_viaje_seleccionado, calcular = mostrar_controles(
    lista_ciudades,
    st.session_state["tiempo_total"],
)

# ==========================================
# 3. LÓGICA DEL BOTÓN CALCULAR
# ==========================================
if calcular:
    if origen == destino:
        st.error("El origen y el destino deben ser ciudades distintas.")
    else:
        resultado = calcular_ruta_dijkstra(grafo, origen, destino, modo_viaje_seleccionado)
        
        if resultado["exito"]:
            # Guardamos los nuevos datos en memoria
            st.session_state["tiempo_total"] = resultado["costo_minutos"]
            st.session_state["ruta"] = resultado["ruta"]
            st.session_state["modo_viaje"] = modo_viaje_seleccionado
            st.session_state["origen"] = origen
            st.session_state["destino"] = destino
            
            # Forzamos recarga para actualizar el mapa de arriba
            st.rerun() 
        else:
            st.error(resultado["mensaje"])

# ==========================================
# 4. MOSTRAR LA RUTA ÓPTIMA TEXTUAL
# ==========================================
mostrar_ruta_optima(st.session_state["ruta"])