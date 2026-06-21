import csv

def cargar_grafo_desde_csv(ruta_archivo):
    """
    Lee un archivo CSV y retorna un diccionario que representa el grafo.
    Ahora cada arista contiene múltiples pesos según el medio de transporte.
    """
    grafo = {}
    
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            origen = fila['ciudad_origen'].strip()
            destino = fila['ciudad_destino'].strip()
            
            # Capturamos los 4 tiempos convirtiéndolos a números enteros
            pesos = {
                'auto_min': int(fila['auto_min'].strip()),
                'tren_min': int(fila['tren_min'].strip()),
                'caminando_min': int(fila['caminando_min'].strip()),
                'bicicleta_min': int(fila['bicicleta_min'].strip())
            }
            
            if origen not in grafo:
                grafo[origen] = {}
            if destino not in grafo:
                grafo[destino] = {}
                
            # Guardamos el mini-diccionario de pesos en ambas direcciones
            grafo[origen][destino] = pesos
            grafo[destino][origen] = pesos
            
    return grafo