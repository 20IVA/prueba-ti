from productos import Producto, input_int





lista_productos = [] 
p = Producto("nombre", "ASUS", 2000, 5)
#lista_productos.append(p)
#print(lista_productos)
#producto = lista_productos[0]
#print(producto.info())

nombre_p = input("nombre del producto: ")
marca_p = input("marca del producto: ")
precio_p = input_int("precio de productos: ","no ingresaste bien el precio ")
camtidad_p = input_int("cantidad del producto:","no ingresaste bien la cantidad ")

t = Producto(nombre_p, marca_p, precio_p, camtidad_p )
print(t.info())
lista_productos.append




