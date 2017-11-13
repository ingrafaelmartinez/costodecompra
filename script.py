precio_manzanas = 2

dinero = 10

input_count = input('¿Cuántas manzanas quieres?: ')
cantidad = int(input_count)
precio_total = precio_manzanas * cantidad

res = dinero - precio_total

#print('El precio_total es ' + str(precio_total) + ' dólares')


if dinero > precio_total:
    print('Usted compró ' + str(cantidad) + ' manzanas')
    print("Tienes " + str(res) + " dólares restantes")
    
elif dinero == precio_total:
    print('Usted compró ' + str(cantidad) + ' manzanas')
    print("Tu billetera está vacía ahora")
else:
    print("No tienes suficiente dinero")
    print("No puedes comprar tantas manzanas")
