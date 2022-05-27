original = input("Esribe la palabra que quieres buscar: ")
nueva = input("Escribe la palabra por la que quieres sustituir: ")
ruta = input("Escribe la ruta del fichero: ")

fichero = open(ruta, "r") #abro
texto = fichero.read() #leemos
fichero.close() #cerramos

texto_final = texto.replace(original, nueva)

fichero = open(ruta, "w")
fichero.write(texto_final)
fichero.close()
