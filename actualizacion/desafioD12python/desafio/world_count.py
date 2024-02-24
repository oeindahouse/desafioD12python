
#abrir el archivo lorem_ipsum.txt, r de read en codificacion utf-8
with open("lorem_ipsum.txt","r", encoding="utf-8") as file:
    texto=file.read()

#ocupar funcion set para poner solo elementos unicos, ideal para contar con len e imprimir
lorem_ipsum_texto=set(texto)
lorem_ipsus_caracteres= len(lorem_ipsum_texto)
print(f"Cantidad de carácteres diferentes que componen ** Lorem Ipsum ** es: {lorem_ipsus_caracteres}.")

lorem_ipsum_texto2=set(texto.split())
lorem_ipsum_palabras= len(lorem_ipsum_texto2)
print(f"Cantidad de palabras diferentes que componen ** Lorem Ipsum ** es: {lorem_ipsum_palabras}.")


