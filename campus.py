#Path: /Documents/MiguelVasquez/Python
import os

clear = lambda: os.system('clear')
clear()

#---------------------------------------artemis--------------------------------

artemis =[]
sputnik = []

def crear_A():
    artemis.extend(['Miguel', 'Vasquez', 'Pedro', 'Eleri'])

    print(f'[!] Creado exitosamente. {artemis}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def listar_A():
    print(f'{artemis}\n')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def agregar_A():
    x = input('[?] Ingrese el nombre del camper que agregaras: ')
    artemis.append(x)
    print(f'[!] Agregado exitosamente. {artemis}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def eliminar_A():
    x = int(input('[?] Ingrese el id del camper que desease eliminar: '))
    artemis.pop(x)
    print(f'[!] Eliminado exitosamente {artemis}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def ordenar_A():
    artemis.sort()
    print(f'[!] Lista ordenada {artemis}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def buscar_A():
    x = int(input('[?] Nombre a buscar por ID: '))
    print('[! Nombre encontrado]',artemis[x])
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

#-----------------------------sputnik--------------------------------------------

def crear_S():
    sputnik.extend(['Andrea', 'Alison', 'Zapata', 'Carancho'])

    print(f'[!] Creado exitosamente. {sputnik}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def listar_S():
    print(f'{sputnik}\n')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def agregar_S():
    x = input('[?] Ingrese el nombre del camper que agregaras: ')
    sputnik.append(x)
    print(f'[!] Agregado exitosamente. {sputnik}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def eliminar_S():
    x = int(input('[?] Ingrese el id del camper que desease eliminar: '))
    sputnik.pop(x)
    print(f'[!] Eliminado exitosamente {sputnik}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def ordenar_S():
    sputnik.sort()
    print(f'[!] Lista ordenada {sputnik}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def buscar_S():
    x = int(input('[?] Nombre a buscar por ID: '))
    print('[! Nombre encontrado]',sputnik[x])
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()


def start():
    clear()
    print("[!] ----------------- Menu ----------------- ")
    print("[!] 1.CREAR GRUPO ARTEMIS:\n[!] 1.1 LISTAR CAMPERS DE ARTEMIS\n[!] 1.2 AGREGAR CAMPERS A ARTEMIS\n[!] 1.3 ELIMINAR CAMPERS DE ARTEMIS\n[!] 1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS\n[!] 1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS \n[!] 2 CREAR GRUPO SPUTNIK\n[!] 2.1 LISTAR CAMPERS DE SPUTNIK:\n[!] 2.2 AGREGAR CAMPERS A SPUTNIK\n[!] 2.3 ELIMINAR CAMPERS DE SPUTNIK\n[!] 2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK\n[!] 2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK")
    print("[!] ---------------------------------------- ")
    m = float(input('\n[>] Digite su opcion: '))
    menu(m)


def menu(x):
    if x == 1:
        crear_A()

    elif x == 1.1:
        listar_A()

    elif x == 1.2:
        agregar_A()

    elif x == 1.3:
        eliminar_A()

    elif x == 1.4:
        ordenar_A()

    elif x == 1.5:
        buscar_A()

    elif x == 2:
        crear_S()

    elif x == 2.1:
        listar_S()

    elif x == 2.2:
        agregar_S()

    elif x == 2.3:
        eliminar_S()

    elif x == 2.4:
        ordenar_S()

    elif x == 2.5:
        buscar_S()

start()
