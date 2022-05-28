import sys

argumentos = sys.argv
while len(argumentos) < 4:
    if len(argumentos) < 2:
        parametro = input("Introduce el fichero: ")
        argumentos.append(parametro)
    if len(argumentos) < 3:
        parametro = input("Palabra a buscar: ")
        argumentos.append(parametro)
    if len(argumentos) < 4:
        parametro = input("Palabra nueva: ")
        argumentos.append(parametro)

original = argumentos[2]
nueva = argumentos[3]
fichero = argumentos[1]

fichero = open(ruta, "r") #abro
texto = fichero.read() #leemos
fichero.close() #cerramos

texto_final = texto.replace(original, nueva)

fichero = open(ruta, "w")
fichero.write(texto_final)
fichero.close()
