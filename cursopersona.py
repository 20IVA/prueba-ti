class persona:
    def __init__(self, nombre, genero, altura, edad):
       self._nombre = nombre
       self._genero = genero
       self._altura = altura
       self._edad = edad
       

    def comer(self, hora_comer):
        print(f"{self._nombre} tienes que comer {hora_comer}") 
        print("si terminaste de comer te levantas")

    def jugar(self, tienpo_jugar):
        print(f"{self._nombre} enpieza a jugar {tienpo_jugar}") 
        print("si terminas de jugar te das un baño")

    def estudiar(self, tienpo_estudiar):
        print(f"{self._nombre} enpieza a estudiar{tienpo_estudiar}") 
        print("terminando de estudiar puedes jugar ")    

hector = persona("hector", "honbre", "1.76","19")   
hector.comer ("en la mesa")

katy = persona("katy", "femenino", "1.50","15") 
katy.jugar ("1 hora")

celeste = persona("celeste", "femenino", "1.67","12") 
celeste.estudiar ("3 horas")