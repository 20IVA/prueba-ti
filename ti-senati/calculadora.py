def suma (a, b):
    return a+b
def resta(a, b):
    return a-b
def multiplicacion(a, b):
    return a*b
def divicion(a, b):
    return a/b

def input_int(mensaje):
    while True:
        try:
           v = int(input(mensaje))
        except ValueError:
            pass
        else:
            return v   
        #break

input_int("ingrese un valor: ")    

menu = """
    canculadora
opciones
1. sumar
2. restar
3. multiplicar
4. dividir
5. salir
"""

while True:
    print(menu)
    try:
        opcion = int(input("elige la opcion: "))
    except ValueError:
        print("esa opcion es incorrecta")    
    else:
        if opcion in [1,2,3,4,5]:
            a = input_int("ingrese el primer valor: ")
            b = input_int("ingrese el segundo valor: ")
            if opcion == 1:
                print(f"el resultado es {suma(a,b)}")
            break
        else: 
            print ("no exixte esa opcion")
