original = "tizas"
nueva = "yesos"

fichero = open("fichero.txt", "r") #abro
texto = fichero.read() #leemos
fichero.close() #cerramos

texto_final = texto.replace(original, nueva)

fichero = open("fichero.txt", "w")
fichero.write(texto_final)
fichero.close()
