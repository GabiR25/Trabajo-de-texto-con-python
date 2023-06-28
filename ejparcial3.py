import re

stop_words = ['el', 'la', 'de', 'que', 'y', 'en']
archivo = open('ejparcial3.txt', 'r', encoding='utf-8')
lineas = archivo.read()
lineas = lineas.lower()

lineas = re.sub(r'[^\w\s]', '', lineas)

palabras = lineas.split()
archivo.close()

palabras_sin_stopwords = [palabra for palabra in palabras if palabra not in stop_words]
texto_sin_stopwords = ' '.join(palabras_sin_stopwords)

archivo_sin_stopwords = open('ejparcial3_sin_stopwords.txt', 'w', encoding='utf-8')
archivo_sin_stopwords.write(texto_sin_stopwords)
archivo_sin_stopwords.close()

print('Archivo guardado exitosamente.')