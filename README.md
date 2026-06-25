# Ruta Mínima en Suiza: Grafos Ponderados y Dijkstra

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![Plotly](https://img.shields.io/badge/Plotly-Visualizaci%C3%B3n-3f4f75)

Este repositorio contiene el código fuente de un sistema interactivo diseñado para modelar la red de transporte de 15 ciudades suizas.
El proyecto aplica la teoría de grafos para calcular la ruta de tiempo mínimo entre un origen y un destino, ajustando los pesos dinámicamente según el medio de transporte.

Desarrollado para la asignatura de Matemáticas Discretas (ICINF1103) de la Universidad Católica de Temuco.

---

## Características Principales

* **Modelamiento Matemático:** El sistema representa las ciudades como un grafo ponderado no dirigido $G = (V, E, w)$.
* **Pesos Dinámicos:** La función de peso $w$ representa el tiempo de viaje en minutos y se recalcula en tiempo real si el usuario elige viajar en Tren, Auto, Bicicleta o Caminando.
* **Algoritmo de Dijkstra:** Implementación eficiente utilizando una estructura de datos de cola de prioridad (Min-Heap), logrando una complejidad temporal de $\mathcal{O}(|E| + |V| \log |V|)$.
* **Visualización Interactiva:** Renderizado dinámico del grafo y resaltado de la ruta óptima en la interfaz web.

---

## Equipo de Desarrollo

| Integrante | Rol en el Proyecto |
| :--- | :--- |
| **Maria Henriquez** | Datos y modelamiento matemático |
| **Keisy Epul** | Backend, lógica y algoritmia |
| **Josefa Duarte** | Frontend y visualización de datos |
| **Javier Gutierrez** | Integración y gestión de repositorio |

---

## Datos y Topología

El modelo incluye 15 ciudades principales de Suiza:
*Zúrich, Ginebra, Berna, Lucerna, Basilea, Lausana, Lugano, San Galo, Winterthur, Biena, Coira, Friburgo, Neuchâtel, Sion y Bellinzona.*

El conjunto de aristas está compuesto por al menos 20 conexiones reales. Los tiempos de viaje base se extraen del archivo de persistencia ubicado en `data/conexiones.csv`.

---

## Estructura del Proyecto

El código sigue una arquitectura modular separando la lógica, los datos y la presentación:

```text
.
├── README.md
├── requerimientos.txt
├── .gitignore
├── main.py                  # Orquestador principal
├── core/
│   ├── grafos.py            # Instanciación de listas de adyacencia
│   └── caminos.py           # Lógica del algoritmo de Dijkstra
├── data/
│   └── conexiones.csv       # Persistencia de nodos y pesos
└── frontend/
    ├── interfaz.py          # Componentes de Streamlit
    └── visualizacion.py     # Renderizado de Plotly


## Instalación

```bash
git clone https://github.com/HealHost/-discret_math_project.git
cd -discret_math_project
```
Se recomienda crear un entorno virtual. Luego, instala las dependencias necesarias:


```bash
pip install -r requerimientos.txt
```

## Ejecución

Para levantar la aplicación web en tu entorno local, ejecuta el siguiente comando en tu terminal:

```bash
streamlit run main.py
```

Nota de troubleshooting: Si te aparece el error `command not found: streamlit`, utiliza el modulo de python directamente:

```bash
python -m streamlit run main.py
```

Esto abre la aplicación en el navegador para elegir origen, destino y medio de transporte, y ver la ruta de tiempo mínimo.

**Alternativa desde VS Code:** en el menú superior, ve a `Run` → `Run Without Debugging`.
