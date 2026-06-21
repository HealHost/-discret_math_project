#Dibuja el mapa de ciudades en la pantalla
import plotly.graph_objects as go

# Posición de cada ciudad en el dibujo (coordenada x, coordenada y)

POSICIONES = {
    "Zúrich":       (6.5,  7.5),
    "Winterthur":   (8.0,  7.5),
    "Sankt Gallen": (9.5,  7.0),
    "Basilea":      (5.5,  9.0),
    "Lucerne":      (6.5,  6.0),
    "Bern":         (4.5,  6.5),
    "Biel":         (3.8,  7.2),
    "Neuchâtel":    (2.8,  7.2),
    "Friburgo":     (4.5,  5.5),
    "Lausanne":     (2.2,  5.5),
    "Ginebra":      (1.5,  4.0),
    "Sion":         (3.5,  4.0),
    "Bellinzona":   (7.0,  3.5),
    "Lugano":       (7.0,  2.5),
    "Chur":         (8.5,  5.0),
}


def crear_grafico(grafo, ruta=None, origen=None, destino=None, modo_viaje='tren_min'): #Dibuja el mapa con ciudades y conexiones.
  
    # Lista con todo lo que se va a mostrar en el dibujo
    elementos = []

    #Dibuja las líneas entre ciudades
    
    for ciudad_a, vecinos in grafo.items():
        for ciudad_b, pesos_transporte in vecinos.items():
            minutos_totales = pesos_transporte[modo_viaje]
            
             # Formateamos el tiempo para que se lea mejor (horas y minutos)
            horas = minutos_totales // 60
            minutos_restantes = minutos_totales % 60
            
            if horas > 0:
                if minutos_restantes > 0:
                    texto_tiempo = f"{horas} h {minutos_restantes} min"
                else:
                    texto_tiempo = f"{horas} h" # Si es una hora exacta
            else:
                texto_tiempo = f"{minutos_totales} min" # Si no alcanza a ser 1 hora
            # Solo dibujamos en una dirección para no repetir líneas
            if ciudad_a > ciudad_b:
                continue

            # Posición de cada ciudad en el dibujo
            
            x0, y0 = POSICIONES[ciudad_a]
            x1, y1 = POSICIONES[ciudad_b]

            # Revisamos si esta línea es parte de la ruta encontrada
            
            en_la_ruta = (
                ruta is not None and
                ciudad_a in ruta and
                ciudad_b in ruta and
                abs(ruta.index(ciudad_a) - ruta.index(ciudad_b)) == 1
            )

            # Si está en la ruta va roja y gruesa, si no va gris y delgada
            if en_la_ruta:
                color_linea = "#8B1A1A"
                grosor = 4
                color_numero = "#cc3333"
                
            else:
                color_linea = "#555555"
                grosor = 1.5
                color_numero = "#aaaaaa"

            # Dibujamos la línea entre las dos ciudades
            
            elementos.append(go.Scatter(
                x = [x0, x1, None],
                y = [y0, y1, None],
                mode = "lines",
                line = dict(color = color_linea, width = grosor),
                showlegend = False,
            ))

    #Para los minutos en el medio de la línea.
            medio_x = (x0 + x1) / 2
            medio_y = (y0 + y1) / 2
            elementos.append(go.Scatter(
                x = [medio_x],
                y = [medio_y],
                mode = "text",
                text = [texto_tiempo], # Usamos nuestro nuevo texto formateado
                textfont = dict(color = color_numero, size = 11),
                showlegend = False,
            ))

    #Dibuja los círculos de cada ciudad.
    for ciudad, (x, y) in POSICIONES.items():

        #Las ciudades en la ruta se ven más grandes y doradas.
        if ruta and ciudad in ruta:
            color_circulo = "#D4A96A"
            tamaño = 18
        else:
            color_circulo = "#C8B89A"
            tamaño = 14

        elementos.append(go.Scatter(
            x = [x],
            y = [y],
            mode = "markers+text",
            marker = dict(size=tamaño, color=color_circulo),
            text = [ciudad],
            textposition = "top center",
            textfont = dict(color = "white", size = 11),
            showlegend = False,
        ))

    #Figura
    figura = go.Figure(data = elementos)

    figura.update_layout(
        paper_bgcolor = "#0e1117",
        plot_bgcolor = "#0e1117",
        margin = dict(l = 0, r = 0, t = 0, b = 0),
        xaxis = dict(showgrid = False, zeroline = False, showticklabels = False, range = [0.5, 10.5]),
        yaxis = dict(showgrid = False, zeroline = False, showticklabels = False, range = [1.5, 10.0],),
        height = 380,
        dragmode = False,
    )

    return figura