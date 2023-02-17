""" N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.

Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.

Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros. """

print('Campeones')

atleta1 = input('[!] Ingrese su nombre: ')
atleta1_m = float(input('[!] Ingrese su record: '))


atleta2 = input('[!] Ingrese su nombre: ')
atleta2_m = float(input('[!] Ingrese su record: '))


atleta3 = input('[!] Ingrese su nombre: ')
atleta3_m = float(input('[!] Ingrese su record: '))

if atleta1_m == 15.50:
    print(f'[!] Ganaste 500 millones {atleta1}')
elif atleta2_m == 15.50:
    print(f'[!] Ganaste 500 millones {atleta2}')
elif atleta3_m == 15.50:
    print(f'[!] Ganaste 500 millones {atleta3}')
