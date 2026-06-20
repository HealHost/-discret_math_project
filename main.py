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

#Se guarda el estado de la app entre interacciones
if "figura" not in st.session_state:
    st.session_state["figura"] = crear_grafico(grafo)
if "tiempo_total" not in st.session_state:
    st.session_state["tiempo_total"] = None
if "ruta" not in st.session_state:
    st.session_state["ruta"] = None

#Muestra el grafo en pantalla
st.plotly_chart(
    st.session_state["figura"],
    use_container_width=True,
    config={"displayModeBar": False},
)

st.divider()

#Muestra los controles y se guarda lo que eligió el usuario
origen, destino, calcular = mostrar_controles(
    lista_ciudades,
    st.session_state["tiempo_total"],
)

#Cuando el usuario presiona el botón, se calcula la ruta
if calcular:
    if origen == destino:
        st.error("El origen y el destino deben ser ciudades distintas.")
    else:
        resultado = calcular_ruta_dijkstra(grafo, origen, destino)
        if resultado["exito"]:
            st.session_state["tiempo_total"] = resultado["costo_minutos"]
            st.session_state["ruta"] = resultado["ruta_secuencial"]
            st.session_state["figura"] = crear_grafico(
                grafo,
                st.session_state["ruta"],
                origen,
                destino,
            )
            st.rerun()
        else:
            st.error(resultado["mensaje"])

#Muestra la ruta encontrada debajo de los controles
mostrar_ruta_optima(st.session_state["ruta"])