auto = {
    "marca": "Toyota",
    "modelo":"hilux",
    "numeroAccidentes": 1,
    "estado": True,
    "colores":["negro", "gris"],

}

# keys
#values
#get

for llave, valor in auto.itens():
    print(llave, valor)
    print(auto.get("modelo"))

auto["estado"]= False
lista_colores = auto.get("colores")
lista_colores.append("azul")
auto["colores"] = lista_colores

auto["transmision"]


producto = {
    "marca": "Toyota",
    "modelo":"hilux",
    "costo": 0,
    "cantiad":0,
   }   

lista_productos = []

for i in range(2):
       producto["nombre"]="laptop Asus"
       producto["marca"]="asus"
       producto["costo"]=1000
       producto["cantidad"]=10

       lista_productos.append(producto)
