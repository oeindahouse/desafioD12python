#diccionario con fechas efemérides
efemerides = {'1 de Enero': 'Año Nuevo',
                '27 de Febrero': 'Terremoto en Chile',
                '8 de Marzo': 'Día de la Mujer',
                '6 de Abril': 'Cumpleaños de Nicolás',
                '21 de Mayo': 'Glorias Navales',
                '18 de Septiembre': 'Fiestas Patrias',
                '19 de Septiembre': 'Glorias del Ejercito',
                '25 de Diciembre': 'Navidad'}

#se agrega la función "title()" para poner la primera letra mayúscula, sino la otra opcion era modificar el diccionario
fecha=input("Ingrese fecha del siguiente modo (xx de Mes): ").title()
#se usa funcion replace para cambiar (De) a (de), y asi ser reconocido en el diccionario efemerides
fecha = fecha.replace('De', 'de')

print(f'Efemérides: {efemerides.get(fecha, "No hay eventos para esta fecha")}')
                