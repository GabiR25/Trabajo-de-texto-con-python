cont = 0
archivo = open('ejparcial1.txt' , 'r', encoding = 'utf-8')

for palabra in archivo.read().split():
    cont += 1

archivo.close()

print(f'En el texto, hay una cantidad de {cont} palabras')