def crearproductos(lista_productos):
    producto = {}
    flag=True
    while flag:
        try: 
            nombreproducto = input("Nombre del producto: ")
            marcaproducto = input("Marca del producto: ")
            costoproducto = int(input("Costo del producto: "))
            cantidadproducto = int(input("Cantidad del producto: "))
       
        except ValueError:
            print("ALGO SALIO MAL INTENTALO OTRA VEZ")
        
        else:
            producto["nombre"]= nombreproducto
            producto["marca"]= marcaproducto
            producto["costo"]= costoproducto
            producto["cantidad"]= cantidadproducto
            flag_repeticion = coincidenciaproducto(nombreproducto, cantidadproducto, lista_productos)
            if not flag_repeticion:
                lista_productos.append(producto)
            producto = {}
            pregunta = input("Desea agrear mas Productos? SI/NO")
            if str(pregunta) != "SI":
                flag = False
                print(lista_productos)

    return lista_productos

def listarproductos(lista_productos):
    print('Producto | Cantidad | Precio')
    for producto in lista_productos:
        print(f"{producto.get('nombre')} | {producto.get('cantidad')} | {producto.get('costo')}")


def numerosdeentrada(mensaje):

    while True:
         try:
             numero_ingreso = input(input("mensaje"))
         except ValueError:
            print("te equivocaste esto debe ser un numero")
         else: 
             break 
    return numero_ingreso
        
def coincidenciaproducto(nombreproducto, cantidadproducto, lista_productos):
    flag = False
    for producto in lista_productos:
        if producto.get("nombre") ==nombreproducto:
            print("este producto ya esta registrado")
            producto["cantidad"] = producto.get('cantidad') + cantidadproducto
            flag = True
        return flag    