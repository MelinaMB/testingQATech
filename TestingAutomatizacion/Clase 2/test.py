""""
nombre = "Matias"
edad = 30
profesion_de_usuario = "Cocinero"

edad = input("Ingresa tu edad :")
nombre = input("Ingresa tu nombre : ")
profesion_de_usuario = input("Ingresa tu profesion :")

print(f"El nombre es {nombre}")
print(f"La edad es {edad}")
print(f"La profesion {profesion_de_usuario}") 
"""

pares = []
for i in range(15) :
    numero = input("Ingresar un numero")
    resto = int(numero) % 2
    if resto == 0 :
        pares.append(numero)


print(pares)