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
        print('archivo no existe, ingrese datos a cargar')
        return False

def validar(num):
    while num.isnumeric() == False:
        num = input('valor no admitido, vuelva a ingresar un número: ')
    return int(num)

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

def datos_legajo():
    lista_datos = []
    while True:
            dic_data = {}
            dic_data['Legajo'] = validar(input('Ingrese numero Legajo: '))
            dic_data['Apellido'] = input('Ingrese Apellido Legajo: ')
            dic_data['Nombre'] = input('Ingrese Nombre Legajo: ')
            lista_datos.append(dic_data)
            
            salida = input('Desea seguir ingresando datos? y/n: ')
            if salida.upper() == 'N':
                break
    return lista_datos

def acciones_legajo(path, accion='S'):
    """
    Contempla acciones a tomar sobre archivo legajo
    """
    fieldnames = ['Legajo','Apellido','Nombre']

    if accion.upper()=='A':
        with open(path, mode="a", newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames,delimiter=';',lineterminator='\r')
            for data in datos_legajo():
                writer.writerow(data)

    # sobreescritura
    elif accion.upper()=='S':
        with open(path, mode = 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames,delimiter=';',lineterminator='\r')
            writer.writeheader()
            for data in datos_legajo():
                writer.writerow(data)

    else:
        print('comando invalido ')

def main():
    """
    Programa principal
    """

    FILENAME['legajo_datos'] = input("Por favor, ingrese nombre de archivo de dato de legajo: ")
    path = os.path.join(PATH,FILENAME['legajo_datos'])
    
    if not is_file(path):
        print('por favor cree datos de archivo de legajo')
        acciones_legajo(path, 'S')

    print("Bienvenido al menú interactivo")
    while True:
        print("""\n\n
        ¿Qué queres hacer? Escribe una opción
        1) Cargar datos en tabla Datos de Legajo
        2) Mostrar gasto de viaticos realizado por legajo
        3) Salir""")
        opcion = input()

        if opcion == '1':

            if is_file(path):
                # leyendo legajo
                print('mostrando datos actuales de archivo ...')
                with open(path) as f:
                    reader = csv.reader(f)
                    for row in reader:
                        print(row)
            
            accion = input('Desea agregar(a) o sobreescribir(s) archivo? Ingrese "a" o "s": ')
            acciones_legajo(path, accion)

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