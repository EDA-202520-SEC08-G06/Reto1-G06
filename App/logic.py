import csv
csv.field_size_limit(2147483647)

import math
import time
import os 
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    
    catalog = {'taxis': lt.new_list(), 
               'nyc-neighborhoods': lt.new_list()}

    return catalog



# Funciones para la carga de datos

def load_data(catalog, taxi_filename, neighborhoods_filename):
    """
    Carga los datos del reto
    """
    start_time = get_time()
    
    taxi_count = load_taxis(catalog)
    neighborhood_count = load_neighborhoods(catalog)

    end_time = get_time()
    execution_time_ms = delta_time(start_time, end_time)

    return  taxi_count, neighborhood_count, execution_time_ms

    # TODO: Realizar la carga de datos



def load_taxis (catalog):

    taxifile = data_dir + 'taxis.csv'
    input_file = csv.DictReader(open(taxifile, encoding='utf-8'))

    for taxi_trip in input_file: 
        add_taxi(catalog, taxi_trip)

    return lt.size(catalog['taxis'])


def load_neighborhoods (catalog):   

    neighborhoodsfile = data_dir + 'nyc-neighborhoods.csv'
    input_file = csv.DictReader(open(neighborhoodsfile, encoding='utf-8'))

    for neighborhood in input_file: 
        add_neighborhood(catalog, neighborhood)

    return lt.size(catalog['nyc-neighborhoods'])




def add_taxi (catalog, taxi_trip): 
    
    taxi_trip['vendor'] = int(taxi_trip['vendor'])
    taxi_trip['pickup_datetime'] = str(taxi_trip['pickup_datetime'])
    taxi_trip['dropoff_datetime'] = str(taxi_trip['dropoff_datetime'])
    taxi_trip['passenger_count'] = int(taxi_trip['passenger_count'])
    taxi_trip['trip_distance'] = float(taxi_trip['trip_distance'])
    taxi_trip['pickup_longitude'] = float(taxi_trip['pickup_longitude'])
    taxi_trip['pickup_latitude'] = float(taxi_trip['pickup_latitude'])
    taxi_trip['rate_code'] = int(taxi_trip['rate_code'])
    taxi_trip['dropoff_longitude'] = float(taxi_trip['dropoff_longitude'])
    taxi_trip['dropoff_latitude'] = float(taxi_trip['dropoff_latitude'])
    taxi_trip['payment_type'] = str(taxi_trip['payment_type'])
    taxi_trip['fare_amount'] = float(taxi_trip['fare_amount'])
    taxi_trip['extra'] = float(taxi_trip['extra'])
    taxi_trip['mta_tax'] = float(taxi_trip['mta_tax'])
    taxi_trip['tip_amount'] = float(taxi_trip['tip_amount'])
    taxi_trip['tolls_amount'] = float(taxi_trip['tolls_amount'])
    taxi_trip['improvement_surcharge'] = float(taxi_trip['improvement_surcharge'])
    taxi_trip['total_amount'] = float(taxi_trip['total_amount'])
    
    lt.add_last(catalog['taxis'], taxi_trip)

    return catalog



def add_neighborhood (catalog, neighborhood):
    
    neighborhood['borough'] = str(neighborhood['borough'])
    neighborhood['neighborhood'] = str(neighborhood['neighborhood'])
    neighborhood['latitude'] = float(neighborhood['latitude'])
    neighborhood['longitude'] = float(neighborhood['longitude'])
    
    lt.add_last(catalog['nyc-neighborhoods'], neighborhood)
    
    return catalog



# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


'''
def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass
'''



def req_3(catalog, low, high):
    """
    Retorna el resultado del requerimiento 3
    """
    
    start_time = get_time()

    filtrados_range = lt.new_list()

    
    for index in range(lt.size(catalog['taxis'])):
        
        trip = lt.get_element(catalog['taxis'], index) 

        if low <= trip['total_amount'] <= high:
            lt.add_last(filtrados_range, trip)

    
    if lt.size(filtrados_range) == 0: 
        end_time = get_time()
        return {'execution_time_ms': delta_time(start_time, end_time),
                'Observacion': 'No se han encontrado viajes en ese rango de precios.'}

    
    total_filtrados = lt.size(filtrados_range)

    sum_tiempo = 0
    sum_precio = 0
    sum_distancia = 0
    sum_tolls = 0
    passenger_counts = {}
    sum_propina = 0 
    dropoff_dates = {}


    for index in range(total_filtrados): 
        
        trip_filtrado = lt.get_element(filtrados_range, index)


        sum_tiempo += calcular_tiempo_minutos(trip_filtrado['pickup_datetime'], trip_filtrado['dropoff_datetime']) # TIEMPO EN MINUTOS 
        
        sum_precio += trip_filtrado['total_amount'] # PRECIO    
        
        sum_distancia += trip_filtrado['trip_distance'] # DISTANCIA 
        
        sum_tolls += trip_filtrado['tolls_amount'] # PEAJES
        
        
        p_count = trip_filtrado['passenger_count'] # CANTIDAD DE PASAJEROS 
        
        if p_count in passenger_counts:
            passenger_counts[p_count] = passenger_counts[p_count] + 1
        elif p_count not in passenger_counts: 
            passenger_counts[p_count] = 1
        

        sum_propina += trip_filtrado['tip_amount'] # PROPINA 
        

        dates = trip_filtrado['dropoff_datetime'][:10] # FECHA DE FINALIZACION 

        if dates in dropoff_dates:
            dropoff_dates[dates] = dropoff_dates[dates] + 1
        elif dates not in dropoff_dates: 
            dropoff_dates[dates] = 1
    

    
    resultado_date = mas_frecuente(dropoff_dates)
    date_item = resultado_date['item']
    date_count = resultado_date['count']


    resultado_passenger = mas_frecuente(passenger_counts)
    passenger_item = resultado_passenger['item']
    passenger_count = resultado_passenger['count']


    end_time = get_time()

    respuesta = {'execution_time_ms': delta_time(start_time, end_time), 
                 'Total de trayectos evaluados': total_filtrados, 
                 'Tiempo promedio (en minutos) de la duración de los trayectos': sum_tiempo/total_filtrados, 
                 'Precio total promedio (en dólares) de los trayectos': sum_precio/total_filtrados,
                 'Distancia promedio (en millas) de los trayectos': sum_distancia/total_filtrados, 
                 'Precio promedio pagado en peajes de los trayectos': sum_tolls/total_filtrados, 
                 'Número y cantidad de pasajeros más frecuente en los trayectos': str(passenger_item) + ' pasajeros con una frecuencia de ' + str(passenger_count),
                 'Cantidad de propina promedio pagada en los trayectos': sum_propina/total_filtrados,
                 'Fecha de finalización de trayecto con mayor frecuencia': str(date_item) + ' con una frecuencia de ' + str(date_count) 
                } 
    
    return respuesta
    

    # TODO: Modificar el requerimiento 3


def req_4(catalog, filtro_costo, inicio_fecha, final_fecha):
    """
    
    Retorna el resultado del requerimiento 4
    """

    start_time = get_time()
    
    filtrados_range = lt.new_list()
    
    
    for index in range(lt.size(catalog['taxis'])):
        
        trip = lt.get_element(catalog['taxis'], index)
        
        fecha_trip = trip['pickup_datetime'][:10]
        
        
        if inicio_fecha <= fecha_trip <= final_fecha:
            lt.add_last(filtrados_range, trip)
        
    

    if lt.size(filtrados_range) == 0:
        end_time = get_time()
        return {'execution_time_ms': delta_time(start_time, end_time),
                'filtro_costo': filtro_costo,
                'Observacion': 'No se encontraron trayectos en el rango de fechas especificado'}
    

    total_filtrados = lt.size(filtrados_range)


    
    combinaciones_barrios = {}
    
    
    for index in range(total_filtrados):
        
        trip = lt.get_element(filtrados_range, index)
        

        barrio_origen = identificar_barrio(catalog, trip['pickup_latitude'], trip['pickup_longitude'])
        
        barrio_destino = identificar_barrio(catalog, trip['dropoff_latitude'], trip['dropoff_longitude'])


        if barrio_origen != barrio_destino: 

            combinacion = (barrio_origen, barrio_destino)
            duracion = calcular_tiempo_minutos(trip['pickup_datetime'], trip['dropoff_datetime']) 

        
        if combinacion in combinaciones_barrios: 
            combinaciones_barrios[combinacion]['total_costo'] = combinaciones_barrios[combinacion]['total_costo'] + trip['total_amount']
            combinaciones_barrios[combinacion]['total_distancia'] = combinaciones_barrios[combinacion]['total_distancia'] + trip['trip_distance']
            combinaciones_barrios[combinacion]['total_tiempo'] = combinaciones_barrios[combinacion]['total_tiempo'] + duracion
            combinaciones_barrios[combinacion]['cantidad_trips'] = combinaciones_barrios[combinacion]['cantidad_trips'] + 1 
        
        elif combinacion not in combinaciones_barrios: 
            combinaciones_barrios[combinacion] = {'barrio_origen': barrio_origen, 
                                                  'barrio_destino': barrio_destino,
                                                  'total_costo': 0,
                                                  'total_distancia': 0,
                                                  'total_tiempo': 0,
                                                  'cantidad_trips': 0}
       


    for combinacion, datos in combinaciones_barrios.items(): # PROMEDIOS DE UNA VEZ
        
        viajes = datos['cantidad_trips']
        
        datos['costo_promedio'] = datos['total_costo'] / viajes
        datos['distancia_promedio'] = datos['total_distancia'] / viajes
        datos['tiempo_promedio'] = datos['total_tiempo'] / viajes 

    
    
    datos_combinacion = None
    combinacion_seleccionada = None
    
    
    if filtro_costo == "MAYOR":
        costo_extremo = -1
        for combinacion, datos in combinaciones_barrios.items():
            if datos['costo_promedio'] > costo_extremo:
                costo_extremo = datos['costo_promedio']
                datos_combinacion = datos
                combinacion_seleccionada = combinacion
    
    elif filtro_costo == "MENOR":
        costo_extremo = math.inf
        for combinacion, datos in combinaciones_barrios.items():
            if datos['costo_promedio'] < costo_extremo:
                costo_extremo = datos['costo_promedio']
                datos_combinacion = datos
                combinacion_seleccionada = combinacion
    
    end_time = get_time()


    resultado = {'execution_time_ms': delta_time(start_time, end_time),
                 'filtro_costo': filtro_costo,
                 'total_trayectos_filtrados': total_filtrados,
                 
                 'combinacion_barrios': {
                    'barrio_origen': combinacion_seleccionada[0],  # BARRIO ORIGEN
                    'barrio_destino': combinacion_seleccionada[1], # BARRIO DESTINO
                    'distancia_promedio': datos_combinacion['distancia_promedio'],
                    'tiempo_promedio': datos_combinacion['tiempo_promedio'],
                    'costo_total_promedio': datos_combinacion['costo_promedio']
                                        }
                }
    
    return resultado

    # TODO: Modificar el requerimiento 4


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time = get_time()
     
    filtrados_range = lt.new_list()
    

    for index in range(lt.size(catalog['taxis'])):
        
        trip = lt.get_element(catalog['taxis'], index)
        
        fecha_trip = trip['pickup_datetime'][:10]
    
        if fecha_inicial <= fecha_viaje <= fecha_final:
            lt.add_last(filtrados_range, trip)
    
    

    if lt.size(trayectos_filtrados) == 0:
        end_time = get_time()
        return {'execution_time_ms': delta_time(start_time, end_time),
                'filtro_costo': filtro_costo,
                'Observacion': 'No se encontraron trayectos en el rango de fechas especificado'}
    

    total_filtrados = lt.size(trayectos_filtrados)

    
    franjas_horarias = {}



    # TODO: Modificar el requerimiento 5



def req_6(catalog, barrio:str, inicio_fecha, fin_fecha):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time = get_time()

    filtrados_range = lt.new_list()


    for index in range(lt.size(catalog['taxis'])):
        
        trip = lt.get_element(catalog['taxis'], index)
        
        fecha_trip = trip['pickup_datetime'][:10]
        
        
        if inicio_fecha <= fecha_trip <= fin_fecha:

            barrio_trip = identificar_barrio(catalog, trip['pickup_latitude'], trip['pickup_longitude'])
            
            if barrio_trip == barrio:
                lt.add_last(filtrados_range, trip)
        
    
    if lt.size(filtrados_range) == 0:
        end_time = get_time()
        return {'execution_time_ms': delta_time(start_time, end_time),
                'Observacion': 'No se encontraron trayectos para los criterios especificados'}
    

    total_filtrados = lt.size(filtrados_range)
 

    sum_distancia = 0 
    sum_tiempo = 0 
    barrios_destino = {}
    metodos_pago = {}


    for index in range(total_filtrados): 

        trip_filtrado = lt.get_element(filtrados_range, index)


        sum_distancia += trip_filtrado['trip_distance'] # DISTANCIA 
        
        sum_tiempo += calcular_tiempo_minutos(trip_filtrado['pickup_datetime'], trip_filtrado['dropoff_datetime']) # TIEMPO EN MINUTOS 


        barrio_destino = identificar_barrio(catalog, trip_filtrado['dropoff_latitude'], trip_filtrado['dropoff_longitude']) # BARRIOS DESTINO

        if barrio_destino in barrios_destino: 
            barrios_destino[barrio_destino] = barrios_destino[barrio_destino] + 1

        elif barrio_destino not in barrios_destino: 
            barrios_destino['barrio_destino'] = 1

       
        duracion = calcular_tiempo_minutos(trip_filtrado['pickup_datetime'], trip_filtrado['dropoff_datetime'])
        
        pago = trip_filtrado['payment_type'] # METODOS DE PAGO

        if pago in metodos_pago: 
            metodos_pago[pago]['cantidad'] = metodos_pago[pago]['cantidad'] + 1
            metodos_pago[pago]['total_precio'] = metodos_pago[pago]['total_precio'] + trip['total_amount']
            metodos_pago[pago]['total_tiempo'] = metodos_pago[pago]['total_tiempo'] + duracion
        
        elif pago not in metodos_pago:
            metodos_pago[pago] = {'cantidad': 1,
                                  'total_precio': trip['total_amount'],
                                  'total_tiempo': duracion}



        info_barrio_destino_mayor_frecuencia = mas_frecuente(barrios_destino)
        barrio_mas_visitado = info_barrio_destino_mayor_frecuencia['item']

        
        metodo_mas_usado = ''
        metodo_mayor_recaudo = ''
        cantidad_trayectos_max = 0
        recaudacion_max = 0


    for metodo, datos in metodos_pago.items():
        
        if datos['cantidad'] > cantidad_trayectos_max:
            cantidad_trayectos_max = datos['cantidad']
            metodo_mas_usado = metodo
        
        if datos['total_precio'] > recaudacion_max:
            recaudacion_max = datos['total_precio']
            metodo_mayor_recaudo = metodo

    
    info_metodos = {} # INFO METODOS PAGO A MODO DE DICCIONARIO
    for metodo, datos in metodos_pago.items():
        info_metodos[metodo] = {'tipo_pago': metodo,
                                'cantidad_trayectos': datos['cantidad']'precio_promedio': datos['total_precio'] / datos['cantidad'],
                                'precio_promedio': datos['total_precio'] / datos['cantidad'],
                                'es_mas_recaudo': metodo == metodo_mayor_recaudo,
                                'tiempo_promedio': datos['total_tiempo'] / datos['cantidad']}

    end_time = get_time()

    resultado = {'execution_time_ms': delta_time(start_time, end_time),
                 'total_trayectos_filtrados': total_filtrados,
                 'distancia_promedio': sum_distancia/total_filtrados,
                 'tiempo_promedio_duracion': sum_tiempo/total_filtrados,
                 'barrio_mas_visitado_destino': barrio_mas_visitado,
                 'metodos_pago': info_metodos}
    
    return resultado

        
    # TODO: Modificar el requerimiento 6




# Funciones para medir tiempos de ejecucion


def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)



def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed




# Funciones auxiliares


def calcular_tiempo_minutos (pickup_datetime, dropoff_datetime): 
    '''
    + recibe dos fechas en formato “%Y-%m-%d HH:MM:SS”   
    = retorna el tiempo en minutos entre dos fechas
    '''

    pickup = time.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")
    dropoff = time.strptime(dropoff_datetime, "%Y-%m-%d %H:%M:%S")
    
    pickup_segundos = time.mktime(pickup)
    dropoff_segundos = time.mktime(dropoff)
    
    tiempo_minutos = (dropoff_segundos - pickup_segundos) / 60
    
    return tiempo_minutos



def mas_frecuente (conteos:dict): 
    '''
    + recibe un diccionario de conteos 
    = retorna el item con mayor frecuencia (item) junto a dicha frecuencia (count)
    '''

    mayor_frecuencia = -1
    item_con_mayor_frecuencia = ''

    for item, count in conteos.items():
        if count > mayor_frecuencia:
            mayor_frecuencia = count
            item_con_mayor_frecuencia = item
            
    return {'item': item_con_mayor_frecuencia, 'count': mayor_frecuencia}



def identificar_barrio (catalog:dict, latitud, longitud): 

    barrio_identificado = ''
    distancia_minima = math.inf

    for index in range(lt.size(catalog['nyc-neighborhoods'])):
        barrio = lt.get_element(catalog['nyc-neighborhoods'], index)
        
        distancia = calcular_distancia_haversine(latitud, longitud, barrio['latitude'], barrio['longitude'])
        
        if distancia < distancia_minima:
            distancia_minima = distancia
            barrio_identificado = barrio['neighborhood']
    
    return barrio_identificado



def calcular_distancia_haversine (latitud1, longitud1, latitud2, longitud2): 

    lat1_rad = math.radians(latitud1)
    lon1_rad = math.radians(longitud1)
    lat2_rad = math.radians(latitud2)
    lon2_rad = math.radians(longitud2)

    dif_lat = lat2_rad - lat1_rad
    dif_lon = lon2_rad - lon1_rad

    a = ((math.sin(dif_lat/2))**2) + (math.cos(lat1_rad)) * (math.cos(lat2_rad)) * (math.sin(dif_lon/2)**2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) # Esto fue lo que encontre en la formula, no se si este bien expresado

    return c * 6371 # donde 6371 representa el radio de la tierra en KM !!! 




