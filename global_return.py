# Codigo de estudiante: 6B3D6677
# Ejercicio 2

# Utilizando global

saldo = 500

def retirar(monto):
    global saldo
    saldo = saldo - monto
    return saldo

retirar(100)

print ("======= USANDO GLOBAL =======")
print (f"Saldo restante: {saldo}")


# Utilizando return

def retirar (saldo,monto): 
    saldo = saldo - monto
    return saldo 

saldo = 500 

saldo = retirar (saldo, 100)

print ("----- USANDO RETURN ------")
print (f"Saldo restante: {saldo}")

# Yo preferiria usar la opcion B aunque sea mas larga, pero asi no dependo de variables globales
# Lo que puede llegar a ser confuso en codigos grandes 