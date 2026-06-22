import streamlit as st
# streamlit es la librería que crea la página web
# con ella hacemos los menús, botones y textos de la pantalla


# Colores y diseño de la página
# Aquí se define cómo se ve la página: colores, tamaños, bordes, etc.
def aplicar_estilos():

    st.markdown("""
    <style>
    /* Color de fondo de toda la app */
    .stApp { background-color: #0e1117; }
    /* Color del panel izquierdo */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #2a2a2a;
    }
    /* Cómo se ven los menús desplegables */
    div[data-baseweb="select"] > div {
        min-height: 52px !important;
        border-radius: 10px !important;
        background-color: #1e2130 !important;
        border-color: #3a3a4a !important;
    }
    /* Caja que muestra el tiempo total */
    .caja-tiempo {
        min-height: 52px;
        background-color: #1e2130;
        border: 1px solid #3a3a4a;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 18px;
        font-weight: bold;
        margin-top: 8px;
    }
    /* Cómo se ve el botón calcular */
    div.stButton > button {
        min-height: 52px;
        width: 100%;
        background-color: #8B1A1A;
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
        margin-top: 8px;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: #a82020;
    }
    /* Caja que muestra la ruta encontrada */
    .ruta-box {
        background-color: #161b22;
        border-left: 4px solid #cc3333;
        border-radius: 6px;
        padding: 12px 18px;
        color: white;
        font-size: 16px;
        margin-top: 8px;
    }
    /* Texto "Ruta óptima" en rojo */
    .ruta-label {
        color: #cc3333;
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 4px;
    }
    /* Línea separadora */
    hr { border-color: #2a2a2a; }
    </style>
    """, unsafe_allow_html=True)


# Panel izquierdo con información del grupo
# Muestra el nombre del proyecto, algoritmo e integrantes al lado izquierdo
def mostrar_sidebar():
    with st.sidebar:
        st.markdown("### Proyecto de\nMatemática Discreta")
        st.markdown("---")
        st.markdown("**Algoritmo utilizado:**")
        st.markdown("### Dijkstra")
        st.markdown("---")
        st.markdown("**Integrantes:**")
        st.markdown("""
- Josefa Duarte
- Keisy Epul
- Javier Gutiérrez
- María Henríquez
""")

# Muestra el título principal y la descripción de la app
def mostrar_titulo():
    st.markdown("**Visualizador Dijkstra**: Ciudades Suizas")
    st.markdown(
        "Selecciona una ciudad de origen y una ciudad de destino "
        "para encontrar la ruta más corta."
    )
# 4 Controles, ciudad origen, destino, cuadro con el tiempo total y boton de calcular
def mostrar_controles(lista_ciudades, tiempo_total):
    col1, col2, col3, col4 = st.columns([2, 2, 2, 1]) 
    
    with col1:
        origen = st.selectbox("Ciudad de Origen", lista_ciudades)
    with col2:
        destino = st.selectbox("Ciudad de Destino", lista_ciudades)
    with col3:
        opciones_transporte = {
            "Tren": "tren_min",
            "Auto": "auto_min",
            "Caminando": "caminando_min",
            "Bicicleta": "bicicleta_min"
        }
        seleccion = st.selectbox("Medio de Transporte", list(opciones_transporte.keys()))
        modo_viaje = opciones_transporte[seleccion] 
        
    with col4:
        st.write("") 
        calcular = st.button("Calcular Ruta", use_container_width=True)
    
    return origen, destino, modo_viaje, calcular

# Muestra el título principal y la descripción de la app
# Si ya se calculó una ruta, la muestra con flechas entre ciudades
def mostrar_ruta_optima(ruta):
    if ruta:
        st.markdown('<div class="ruta-label">Ruta óptima</div>', unsafe_allow_html=True)
        ruta_texto = " → ".join(ruta)
        st.markdown(
            f'<div class="ruta-box">{ruta_texto}</div>',
            unsafe_allow_html=True
        )