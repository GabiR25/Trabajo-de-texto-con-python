archivo = open('ejparcial2.txt','r',encoding = 'utf-8')

lineas = archivo.read()
lineas = lineas.lower()
palabras = lineas.split()

archivo.close()

diccionario = {}
for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

for palabra in diccionario:
    frecuencia = diccionario[palabra]
    if frecuencia > 1:
        print(f'La palabra {palabra} aparece {frecuencia} veces')
    else:
        print(f'La palabra {palabra} aparece {frecuencia} vez')