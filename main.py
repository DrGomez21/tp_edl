import re
from util import palabras_reservadas

regex = r'\b[a-zA-Z]+\b(?=(?:[^"]*"[^"]*")*[^"]*$)'
# Abrimos el archivo con el codigo
archivo = open('codigo.txt', 'r')
contenido = archivo.readlines()

# Creamos un diccionario para almacenar los valores.
# Clave: identificador. Valor: Lista de nro_linea
identificar_linea = {}

def actualizar_diccionario(id, nro_linea):
    ''' Actualizamos los datos del diccionario, con el identificador y número de linea recibidos '''
    # Verificamos si está ya en el diccionario
    if id not in identificar_linea:
        identificar_linea[id] = [nro_linea]
    else:
        identificar_linea[id].append(nro_linea)

def verificar_identificador(identificadores, nro_linea):
    ''' Valida que el identificador encontrado no sea una palabra reservada '''
    for identificador in identificadores:
        if identificador not in palabras_reservadas:    # Verificamos que no sea una palabra reservada de Java.
            actualizar_diccionario(identificador, nro_linea)

def buscar_identificadores():
    ''' Busca los identificadores, utilizando la exresión regular. Avanza en los numeros de linea '''
    # Primer numero de linea
    nro_linea = 1
    for line in contenido:
        identificadores = re.findall(regex, line)    # Buscamos con la regex
        verificar_identificador(identificadores, nro_linea)
        nro_linea += 1
            
def ordenar_ids():
    ''' Ordena el diccionario de identificadores de forma alfabética '''
    identificadores_ordenados = sorted(identificar_linea.keys())
    return identificadores_ordenados

def imprimir_datos():
    ''' Imprime los datos del diccionario con el formato deseado '''
    ordenados = ordenar_ids()
    for identificador in ordenados:
        lineas = ', '.join(map(str, identificar_linea[identificador]))
        print(f'{identificador}: {lineas}')

if __name__ == '__main__':
    buscar_identificadores()
    imprimir_datos()

