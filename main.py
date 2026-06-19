from core.grafos import cargar_grafo_desde_csv
from core.caminos import calcular_ruta_dijkstra

#  Def ruta relativa al archivo CSV
ruta_csv = 'data/conexiones.csv'

mi_mapa = cargar_grafo_desde_csv(ruta_csv) # Cargar grafo usando la función de grafos.py

# =======================================================
# Prueba del algoritmo:
# =======================================================
ciudad_inicio = 'Basel'   # Cambia esto por cualquier ciudad de tu CSV
ciudad_fin = 'Neuchâtel'     # Cambia esto por otra ciudad de tu CSV
# =======================================================

# Ejecutar el algoritmo usando la función de caminos.py
tiempo, recorrido = calcular_ruta_dijkstra(mi_mapa, ciudad_inicio, ciudad_fin)

# 4. Mostrar el resultado en consola (luego esto lo conectarás al frontend)
print(f"Ruta óptima: {' -> '.join(recorrido)}")
print(f"Tiempo total: {tiempo} minutos")