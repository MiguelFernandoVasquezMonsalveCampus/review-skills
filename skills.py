def ej1():
    """ 1. Qué operadores utiliza Python en los siguientes casos:

    A. División Modular
    B. Exponenciación
    C. División que retorne entero. """

    num1= 6
    num2= 4

    print(f'A. División Modular {num1} // {num2} = {num1 // num2}\nB. Exponenciacion {num1} ** {num2} = {num1 ** num2}\nC. División que retorne entero. {num1} // {num2} = {num1 // num2}')
 

def ej2():
    """ 2. En la jerarquía de operadores, cuáles son los que más
    prioridad tienen cuando el intérprete de Python los evalúa? """

    # ()                                mayor
    # **
    #  *, /, %, //
    #  +, -
    # <, <=, >, >=, !=, ==
    # And
    # Or                                menor

    #operadores = ['()', '**', '*', '/', '%', '//', '+', '-', '<', '<=', '>', '>=', '!=','==', 'And', 'Or']

    print('[!] los operadores van de mayor a menor: \n[!] Operacion entre parentesis: ()\n[!] Potencia: **\n[!] Multiplicación y División, módulo o residuo, División entera: *, /, %, //\n[!] Suma y resta: +,-\n[!] Operadores relacionales: <, <=, >, >=, !=, ==\n[!] Operador lógico AND: And\n[!] Operador lógico OR: Or')
 

def ej3():
    """ 3. Si hay operadores de igual precedencia, en qué orden se
    ejecutan?

    A. De izquierda a derecha
    B. De derecha a izquierda """

    num1= 9
    num2= 3


    print(f'[!] A. se ejecuta de izquierda a derecha \n[!] {num1} - {num2} tiene misma prioridad que {num1} + {num2}')

def ej4():
    """ 4. Que son las expresiones regulares en Python? """

    print("[!] Las expresiones regulares (llamadas RE, o regex, o patrones de regex) son esencialmente en un lenguaje de programación diminuto y altamente especializado incrustado dentro de Python y disponible a través del módulo re .")


def ej5():
    """ Enumere 5 tipos de datos en Python y suministre un valor de
    ejemplo de cada uno. """


    num = 1
    num2 = 2.1
    string = 'hola'
    hola = False
    lista = [1, 2, 3]

    print(f'[!] tipos de datos: \n[!] Numero entero: {num}\n[!] Float: {num2}\n[!] String: {string}\n[!] Booleano: {hola}\n[!] Lista: {lista}')
#

def ej6():
    """ 6. En sus propias palabras, qué son las funciones
    preconstruidas y proporcione 2 ejemplos. """

    mayor=max(45, 75, 65, 31)
    texto = len('hola mundo')

    print(f'[!] Las funciones pre construidas son incluidas en las librerias de python nativamente. \n[!] Ejemplos: \n[!] la funcion max, revisa cual es el numero mayor dado en una lista: {mayor}\n[!] La funcion len, revisa los caracteres de un texto: {texto}')



def ej7():
    """ 7. Cuál es la diferencia entre un condicional simple y un
    condicional compuesto? """


    simple = """
    num = 20
    if num%2 == 0:
        print('Numero par')
    """

    compuesta = """
    num = 10
    if num%2 == 0:
        print('numero par)
    else:
        print('no es un numero par')
    """


    print(f'[!] Un condicional simple tiene un solo parametro, la compuesta tiene mas de 2 si es requerido: \n\nSimple: \n{simple}\n\n Compuesta: \n{compuesta}')


def ej8():
    """ 8. Escriba un bloque cualquiera de código en Python en donde
    utilice 2 condicionales (if) anidados. """

    nombre = input('[!] Ingrese su nombre: \n[>] ')
    if len(nombre) >= 6:
        print('[!] tienes un nombre largo')
        if nombre == 'miguel':
            print('[!] te llamas igual que yo')
    else:
        print('[!] Tienes un nombre corto')

def ej9():
    """ 9. Construya un algoritmo en Python, que permita ingresar la
    información de un empleado e imprima el nombre, los
    apellidos y la antigüedad. Los datos que se deben solicitar
    son los siguientes:
    *Nombre * Teléfono *Año de ingreso a la empresa
    *Apellidos *Edad. """


    def informacion():
        nombre = input('[>] Ingrese su nombre: ')
        apellido = input('[>] Ingrese su apellido: ')
        edad = int(input('[>] ingrese su edad: '))
        telefono = input('[>] ingrese su telefono: ')
        ade = int(input('[>] Ingrese el año de ingreso a la empresa: '))
        em = 2023 - ade

        if edad < 18:
            print('[!] informacion invalida, no puedes ser menor de edad')
    
        print(f'\n[!] Bienvenido: {nombre} {apellido}\n[!] Tienes {edad} años y haz estado en esta empresa por {em} años\n[!] Tu telefono de contacto: {telefono}')

    informacion()

def ej10():
    """ 10. En su casa le solicitan que realice un algoritmo en Python,
    que permita calcular el valor a pagar por concepto de
    energía eléctrica. Los datos que se conocen son los
    siguientes:
    - Mes de consumo - Valor kw
    -Total kw consumido en el mes - estrato """


    print('[!] extrato calculator omg\n')

    def calcular():
        kw = 0
        estrato = int(input('[!] Ingrese su estrato: '))
        mes = int(input('[!] Ingrese el mes de consumo: '))
        #kw = int(input('Ingrese el valor de kw por dia: '))
        total = int(input('[!] total kw consumidos en el mes: '))
        if estrato == 1:
            kw = 297
        elif estrato == 2:
            kw = 346
        elif estrato == 3:
            kw = 588
        elif estrato == 4:
            kw = 719
        else:
            kw = 862

        if mes == 1:
            h = 'enero'
        elif mes == 2:
            h = 'febrero'
        elif mes == 3:
            h = 'marzo'
        elif mes == 4:
            h = 'abril'
        elif mes == 5:
            h = 'mayo'
        elif mes == 6:
            h = 'junio'
        elif mes == 7:
            h = 'julio'
        elif mes == 8:
            h = 'agosto'
        elif mes == 9:
            h = 'septiembre'
        elif mes == 10:
            h = 'octubre'
        elif mes == 11:
            h = 'noviembre'
        else: 
            h = 'diciembre'    
    
        t = total * kw

        print(f'\n[!] El valor total del mes {h.upper()} es :{t}')
    
    calcular()





#------------------------------------Menu------------------------------------
def skill():
    x = int(input('[1] ejercicio \nejercicio [2]\nejercicio [3]\nejercicio [4]\nejercicio [5]\nejercicio [6]\nejercicio [7]\nejercicio [8]\nejercicio [9]\nejercicio [10]\nDigite una opcion para el ejercicio: '))
    if x == 1:
        ej1()
    elif x == 2:
        ej2()
    elif x == 3:
        ej3()
    elif x == 4:
        ej4()
    elif x == 5:
        ej5()
    elif x == 6:
        ej6()
    elif x == 7:
        ej7()
    elif x == 8:
        ej8()
    elif x == 9:
        ej9()
    elif x == 10:
        ej10()


skill()



