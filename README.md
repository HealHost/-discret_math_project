# -discret_math_project
# Ruta Mínima en Suiza

Proyecto de Matemáticas Discretas que modela 15 ciudades suizas como un grafo ponderado G = (V, E, w) y calcula la ruta de costo mínimo entre dos ciudades mediante una interfaz gráfica.

## Integrantes y roles

| Integrante | Rol |
|---|---|
| Maria Henriquez | Datos y modelamiento |
| Keisy Epul | Backend y algoritmia |
| Josefa Duarte | Frontend y visualización |
| Javier Gutierrez | Integración y gestión |

## Ciudades

Zúrich, Ginebra, Berna, Lucerna, Basilea, Lausana, Lugano, San Galo, Winterthur, Biena, Coira, Friburgo, Neuchâtel, Sion, Bellinzona.

## Datos

El grafo está compuesto por 15 ciudades y 20 conexiones. El peso de cada conexión corresponde al **tiempo de viaje en tren (minutos)**, obtenido de [Rail Europe](https://www.raileurope.com).

Los datos se encuentran en `data/conexiones.csv`.

## Estructura del repositorio

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── core/
│   ├── __init__.py
│   ├── grafo.py
│   └── caminos.py
├── data/
│   └── conexiones.csv
└── frontend/
    ├── __init__.py
    ├── interfaz.py
    └── visualizacion.py
```

## Instalación

```bash
git clone https://github.com/HealHost/-discret_math_project.git
cd -discret_math_project
pip install -r requirements.txt
```

## Ejecución

Una vez instaladas las dependencias, ejecuta:

```bash
python main.py
```

Esto abre la interfaz gráfica para elegir origen y destino, y ver la ruta de costo mínimo.
