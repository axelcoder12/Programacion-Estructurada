# Codigo de estudiante: 6B3D6677
# Ejercicio 4

Moneda = "C$"
IVA = 0.15

def agregar_producto (nombre, precio, cantidad):
    valor = precio * cantidad
    return valor

def calcular_valor_total (valor1, valor2, valor3):
    subtotal = valor1 + valor2 + valor3
    impuesto = subtotal * IVA
    total = subtotal + impuesto
    return total

def mostrar_inventario (nombre1, precio1, cantidad1, nombre2, precio2, cantidad2, nombre3, precio3, cantidad3):
    valor1 = agregar_producto (nombre1, precio1, cantidad1)
    valor2 = agregar_producto (nombre2, precio2, cantidad2)
    valor3 = agregar_producto (nombre3, precio3, cantidad3)
    
    print ("            INVENTARIO            ")
    print ("==================================")
    print (nombre1, f"\n Cantidad: {cantidad1} \n Precio: {Moneda}{precio1}")
    print (nombre2, f"\n Cantidad: {cantidad2} \n Precio: {Moneda}{precio2}")
    print (nombre3, f"\n Cantidad: {cantidad3} \n Precio: {Moneda}{precio3}")
    
    total = calcular_valor_total (valor1, valor2, valor3)
    
    print ("==================================")
    print (f"Valor total con IVA: {Moneda}{total}")
    
mostrar_inventario ("Teclado", 800, 2, "Mouse", 500, 3, "Monitor", 6000, 1)