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
    """"""

def ej5():
    """"""

def ej6():
    """"""

def ej7():
    """"""

def ej8():
    """"""

def ej9():
    """"""

def ej10():
    """"""





#------------------------------------Menu------------------------------------
def skill():
    x = int(input('[1] ejercicio \nejercicio [2]\nejercicio [3]\nejercicio [4]\nejercicio [5]\nejercicio [6]\nejercicio [7]\nejercicio [8]\nejercicio [9]\nejercicio [10]\nDigite una opcion para el ejercicio: '))
    if x == 1:
        ej1()
    elif x == 2:
        ej2()
    elif x == 3:
        ej2()
    elif x == 4:
        ej2()
    elif x == 5:
        ej2()
    elif x == 6:
        ej2()
    elif x == 7:
        ej2()
    elif x == 8:
        ej2()
    elif x == 9:
        ej2()
    elif x == 10:
        ej2()


skill()



