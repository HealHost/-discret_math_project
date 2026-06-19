import csv

def cargar_grafo_desde_csv(ruta_archivo):
    """
    Lee un archivo CSV y retorna un diccionario que representa el grafo ponderado.
    """
    grafo = {}
    
    # Se abre el archivo CSV con soporte para tildes (utf-8)
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo) # DictReader lee la primera fila como las llaves del diccionario
        
        for fila in lector:
            origen = fila['ciudad_origen'].strip()
            destino = fila['ciudad_destino'].strip()
            
            tiempo_str = fila['tiempo_de_viaje_min aprox.'].replace(' minutos', '').strip()# Limpiar el texto " minutos" para quedarse solo con el número entero
            tiempo = int(tiempo_str)
            
            if origen not in grafo:  # Si la ciudad no está en el grafo, se inicializa su diccionario
                grafo[origen] = {}
            if destino not in grafo:
                grafo[destino] = {}
                
            grafo[origen][destino] = tiempo# Agregar la conexión en ambas direcciones (Grafo no dirigido)
            grafo[destino][origen] = tiempo
            
    return grafo