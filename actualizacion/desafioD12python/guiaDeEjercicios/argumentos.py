import sys
type(sys.argv)

nombre=sys.argv[1]
apellido=sys.argv[2]

print(f'*** Mi nombre es {nombre}')
print(f'*** Mi apellido es {apellido}')
print(f'*** El nombre de este archivo es { sys.argv[0] }')

print("en VSC no se ve, imprime error, pero cuando lo ejecuto desde anaconda imprime **Mi nombre es -f, mi apellido y lo demás, por qué será???")

