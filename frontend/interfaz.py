import streamlit as st
# streamlit es la librería que crea la página web
# con ella hacemos los menús, botones y textos de la pantalla


#Colores y diseño de la página
def aplicar_estilos():
    
    # Aquí se define cómo se ve la página: colores, tamaños, bordes, etc.
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


#Panel izquierdo con información del grupo

def mostrar_sidebar():
    # Muestra el nombre del proyecto, algoritmo e integrantes al lado izquierdo
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


#Título arriba de la pantalla

def mostrar_titulo():
    
    #Muestra el título principal y la descripción de la app
    st.markdown("Visualizador Dijkstra: Ciudades Suizas")
    st.markdown(
        "Selecciona una ciudad de origen y una ciudad de destino "
        "para encontrar la ruta más corta."
    )


#Origen, destino, tiempo y botón

def mostrar_controles(lista_ciudades, tiempo_total):
    
    # Divide la pantalla en 4 columnas y pone un control en cada una
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        
        # Menú para elegir la ciudad de partida
        st.markdown("**Ciudad de origen**")
        origen = st.selectbox(
            "", lista_ciudades,
            key="origen",
            label_visibility="collapsed"
        )

    with col2:
        
        #Menú para elegir la ciudad de llegada
        st.markdown("**Ciudad de destino**")
        destino = st.selectbox(
            "", lista_ciudades,
            key="destino",
            label_visibility="collapsed"
        )

    with col3:
        #Muestra el tiempo que tardó la ruta encontrada
        st.markdown("**Tiempo total**")
        texto = f"{tiempo_total} minutos" if tiempo_total is not None else "— minutos"
        st.markdown(
            f'<div class="caja-tiempo">{texto}</div>',
            unsafe_allow_html=True
        )

    with col4:
        #Botón que inicia el cálculo de la ruta
        st.markdown("**Calcular ruta**")
        calcular = st.button("Calcular ruta", use_container_width=True)

    #Devuelve lo que eligió el usuario y si presionó el botón
    return origen, destino, calcular


#Muestra la ruta encontrada debajo de los controles

def mostrar_ruta_optima(ruta):
    
    # Si ya se calculó una ruta, la muestra con flechas entre ciudades
    if ruta:
        st.markdown('<div class="ruta-label">Ruta óptima</div>', unsafe_allow_html=True)
        ruta_texto = " → ".join(ruta)
        st.markdown(
            f'<div class="ruta-box">{ruta_texto}</div>',
            unsafe_allow_html=True
        )