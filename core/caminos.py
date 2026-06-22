import heapq # Implementa colas de prioridad

def calcular_ruta_dijkstra(grafo, origen, destino, modo_viaje):
    """
    Calcula el camino mínimo en un grafo ponderado usando Dijkstra.
    Se agregó 'modo_viaje' para elegir el peso dinámicamente.
    """
    # 1. Validaciones
    if origen not in grafo or destino not in grafo:
        return {"exito": False, "costo_minutos": 0, "ruta": [], "mensaje": "Ciudades inválidas."}
        
    # Verificar que el modo de viaje exista en los datos
    modos_validos = ['auto_min', 'tren_min', 'caminando_min', 'bicicleta_min']
    if modo_viaje not in modos_validos:
        return {"exito": False, "costo_minutos": 0, "ruta": [], "mensaje": "Modo de transporte inválido."}

    # 2. Inicialización
    tiempos = {nodo: float('infinity') for nodo in grafo} #Asigna el valor infinito como valor al nodo, porque es desconocido
    tiempos[origen] = 0 # punto de partida tiene valor 0
    nodos_previos = {} #Migas de pan para identificar ciudades visitadas
    cola = [(0, origen)] #La cola empieza con el valor 0 y ciudad de origen
    
    while cola:
        tiempo_actual, nodo_actual = heapq.heappop(cola)#Mientras haya ciudades en la fila, saca la que tenga el menor tiempo acumulado.
        
        if nodo_actual == destino:
            ruta = []
            while nodo_actual in nodos_previos: #Vuelve por la ruta de migajas
                ruta.insert(0, nodo_actual) #Va armando la lista
                nodo_actual = nodos_previos[nodo_actual]
            ruta.insert(0, origen)
            return {"exito": True, "costo_minutos": tiempos[destino], "ruta": ruta, "mensaje": "Ruta calculada."}
            
        if tiempo_actual > tiempos[nodo_actual]:#Si el tiempo que sacamos de la fila es mayor al que ya habíamos registrado,la ignoramos (continue).
            continue
            
        # 3. Relajación de aristas
        # 'pesos' ahora es un diccionario: {'auto_min': 19, 'tren_min': 23...}
        for vecino, pesos in grafo[nodo_actual].items():
            
            # Seleccionamos solo el tiempo del medio de transporte elegido
            tiempo_viaje = pesos[modo_viaje] 
            
            tiempo_calculado = tiempo_actual + tiempo_viaje
            
            if tiempo_calculado < tiempos[vecino]:
                tiempos[vecino] = tiempo_calculado #Actualiza, borra el tiempo viejo lo remplaza por el nuevo valor 
                nodos_previos[vecino] = nodo_actual#Miga de pan, Anota que la mejor forma de llegar a ese vecino es viniendo desde el nodo_actual.
                heapq.heappush(cola, (tiempo_calculado, vecino)) #Empaqueta el nuevo tiempo y nombre de la ciudad vecina (tiempo_calculado, vecino) 
                #y los mete en la cola (la fila de espera de ciudades por visitar).
                
    return {"exito": False, "costo_minutos": 0, "ruta": [], "mensaje": "Sin conexión."}