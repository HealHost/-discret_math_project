import heapq

def calcular_ruta_dijkstra(grafo, origen, destino):
 
    # --- Validación inicial ---
    if origen not in grafo or destino not in grafo:
        return {
            "exito": False,
            "costo_minutos": 0,
            "ruta_secuencial": [],
            "mensaje": f"Error: '{origen}' o '{destino}' no existen en el mapa."
        }

    # Preparación de variables
    tiempos = {nodo: float('infinity') for nodo in grafo}
    tiempos[origen] = 0
    nodos_previos = {}
    cola = [(0, origen)]
    
    while cola:
        tiempo_actual, nodo_actual = heapq.heappop(cola)
        
        # Si llegamos al destino, reconstruimos la ruta
        if nodo_actual == destino:
            ruta = []
            while nodo_actual in nodos_previos:
                ruta.insert(0, nodo_actual)
                nodo_actual = nodos_previos[nodo_actual]
            ruta.insert(0, origen)
            
            # --- Exito: Salida formateada para el frontend ---
            return {
                "exito": True,
                "costo_minutos": tiempos[destino],
                "ruta_secuencial": ruta,
                "mensaje": "Ruta calculada correctamente."
            }
            
        if tiempo_actual > tiempos[nodo_actual]:
            continue
            
        for vecino, tiempo_viaje in grafo[nodo_actual].items():
            tiempo_calculado = tiempo_actual + tiempo_viaje
            if tiempo_calculado < tiempos[vecino]:
                tiempos[vecino] = tiempo_calculado
                nodos_previos[vecino] = nodo_actual
                heapq.heappush(cola, (tiempo_calculado, vecino))
                
    # --- Fracaso : Si el grafo esta desconectado o la ruta es imposible ---
    return {
        "exito": False,
        "costo_minutos": 0,
        "ruta_secuencial": [],
        "mensaje": "No se encontró una conexión válida entre estas ciudades."
    }