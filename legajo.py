import os
import csv

PATH = './src/'
FILENAME = {
    'legajo_datos' : 'legajo_datos.csv',
    'viaticos': 'viaticos.csv'
}


def is_file(path):
    print(f'validando archivo: {path}')
    if os.path.isfile(path):
        print('archivo existe')
        return True
    else:
        print('archivo no existe')
        return False


def ingreso_ruta():
    if not os.path.isdir(path):
        os.mkdir(path)


def gastos_legajo(path, codigo_legado, path2):
    """
    docstring
    """

    # recuperando datos del primer archivo
    dic_datos = {}
    with open(path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file,delimiter=';')
        for line in csv_reader:
            if line['Legajo'] == codigo_legado:
                dic_datos = line
                break
    
    if dic_datos:
        dic_datos['Gastos'] = 0
    else:
        print('Codigo legajo {codigo_legado} no encontrado, vuelva a intentar...')
        return None

    print(dic_datos)
    # archivo viaticos legajo
    with open(path2, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file,delimiter=';')
        for line in csv_reader:
            if line['Legajo'] == codigo_legado :
                dic_datos['Gastos'] += int(line['Gastos'])
    
    # procesando salida de proceso
    if dic_datos['Gastos'] > 5000:
        dic_datos['Sobregasto'] = dic_datos['Gastos'] - 5000
        print("Legajo {Legajo} : {Nombre} {Apellido}, gastó {Gastos} y se ha pasado del presupuesto por ${Sobregasto}".format(**dic_datos) )
    else:
        print("Legajo {Legajo} : {Nombre} {Apellido}, gastó ${Gastos}".format(**dic_datos) )

def legajo_datos(path):
    """
    Contempla acciones a tomar sobre archivo legajo
    """

    if is_file(path):
        pass
    else:
        input('')


    pass

def main():
    """
    Programa principal
    """

    # ruta = input("Por favor ingrese las rutas del archivo a cargar: ")

    path = os.path.join(PATH,FILENAME['legajo_datos'])
    # path = './src/legajo_datos.csv'

    is_file(path)

    print("Bienvenido al menú interactivo")
    while True:
        print("""\n\n
        ¿Qué queres hacer? Escribe una opción
        1) Cargar datos en tabla Datos de Legajo
        2) Mostrar gasto de viaticos realizado por legajo
        3) Salir""")
        opcion = input()

        if opcion == '1':

            legajo_datos(path)
        
        elif opcion == '2':
            codigo_legado = input('Ingrese el código de Legajo a buscar ...\n')

            # solicito el otro archivo
            path2 = os.path.join(PATH,FILENAME['viaticos'])

            # procesando solicitud
            gastos_legajo(path, codigo_legado, path2)

        elif opcion =='3':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")

# Ejecucion programa principal
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)