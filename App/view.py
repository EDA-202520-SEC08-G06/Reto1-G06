import sys

import App.logic as lg 

from DataStructures.List import array_list as lt


default_limit = 1000

sys.setrecursionlimit(default_limit*10)


def new_logic():
    """
        Se crea una instancia del controlador
    """
    return lg.new_logic()


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    print("Iniciando carga de datos...")
    taxi_count, neighborhood_count, execution_time = logic.load_data(control, 'taxis.csv', 'nyc-neighborhoods.csv')
    print(f"Se cargaron {taxi_count} viajes en taxi.")
    print(f"Se cargaron {neighborhood_count} barrios.")
    print(f"Tiempo de carga: {execution_time} ms.")
    return control

    #TODO: Realizar la carga de datos
    



def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass



def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    
    low = float(input("Ingrese el valor menor del precio total a filtrar: "))
    
    high = float(input("Ingrese el valor mayor del precio total a filtrar: "))
    

    resultado = logic.req_3(control, low, high)
    

    for key, value in resultado.items():
        print(f"{key}: {value}")

    # TODO: Imprimir el resultado del requerimiento 3
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    
    filtro_costo = input("Ingrese el filtro de selección de costo ('MAYOR' o 'MENOR'): ")
    
    inicio_fecha = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    
    final_fecha = input("Ingrese la fecha final (YYYY-MM-DD): ")
    

    resultado = logic.req_4(control, filtro_costo, inicio_fecha, final_fecha)
    

    for key, value in resultado.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")

    # TODO: Imprimir el resultado del requerimiento 4



def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    
    barrio = input("Ingrese el barrio de inicio: ")
    
    inicio_fecha = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    
    fin_fecha = input("Ingrese la fecha final (YYYY-MM-DD): ")
    
    
    resultado = logic.req_6(control, barrio, inicio_fecha, fin_fecha)
    

    for key, value in resultado.items():
        if key == 'metodos_pago':
            print(f"{key}:")
            for metodo, detalles in value.items():
                print(f"  {metodo}:")
                for d_key, d_value in detalles.items():
                    print(f"    {d_key}: {d_value}")
        else:
            print(f"{key}: {value}")

    # TODO: Imprimir el resultado del requerimiento 6



# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
