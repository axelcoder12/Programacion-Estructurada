# Codigo de estudiante: 6B3D6677
# Ejercicio 1

tasa_cambio = 36.6

def a_dolares(cordobas):
    cambio = cordobas / tasa_cambio
    return cambio

cordobas = 1000

resultado = a_dolares(cordobas)

print (f"Cordobas: {cordobas}")
print (f"Dolares: {resultado}")

print (dolares)

# Aparece el error "name 'dolares' is not defined" por que la vavrable fue creada dentro de la funcion
# Por tanto pertenece a una variable local