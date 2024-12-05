print ("Hola mundo")
print ("Estoy aprendiendo Python")
print ("Esto es una suma")
numero_uno = 2
numero_dos = 4
resultado = numero_uno + numero_dos
print (resultado)
mensaje = "Hola"
mensaje += " "
mensaje += "Eduardo"
print (mensaje)

print("Concatenación:")

mensaje = "Hola"
espacio = " "
nombre = "Eduardo"
print (mensaje + espacio + nombre)

numero_uno = 2
numero_dos = 4
resultado = numero_uno + numero_dos
resultado = str(resultado)
print ("El resultado de la suma es:" + resultado)

print ("Busqueda:")
mensaje = "Hola Eduardo"
Buscar_subcadena = mensaje.find("Eduardo")
print (Buscar_subcadena)

print ("Extracción:")
mensaje = "Hola Eduardo"
extraer_subcadena = mensaje[1:8]
print (extraer_subcadena)

print ("Comparación:")
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)

mensaje_uno = "Hola"
mensaje_dos = "Eduardo"
print(mensaje_uno == mensaje_dos)