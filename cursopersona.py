class Persona:
    def __init__(self, nombre, genero, altura, edad):
       self._nombre = nombre
       self._genero = genero
       self._altura = altura
       self._edad = edad

    def edad(self):
        self._fecha_nacimiento
        return 15
       

    def comer(self, hora_comer):
        print(f"{self._nombre} tienes que comer {hora_comer}") 
        print("si terminaste de comer te levantas")

    def jugar(self, tienpo_jugar):
        print(f"{self._nombre} enpieza a jugar {tienpo_jugar}") 
        print("si terminas de jugar te das un baño")

    def estudiar(self, tienpo_estudiar):
        print(f"{self._nombre} enpieza a estudiar{tienpo_estudiar}") 
        print("terminando de estudiar puedes jugar ")    

hector = Persona("hector", "honbre", "1.76","19")   
hector.comer ("en la mesa")

katy = Persona("katy", "femenino", "1.50","15") 
katy.jugar ("1 hora")

celeste = Persona("celeste", "femenino", "1.67","12") 
celeste.estudiar ("3 horas")





class alumno(Persona):
    def __inint__(self, nombre, genero, dni, fecha_nacimiento, peso, altura, id_estudiante, email):
        super().__inint__(nombre, genero, dni, fecha_nacimiento, peso, altura)
        self._id_estudiante = id_estudiante
        self._email = email

    def info(self): 
        print (f"{self._nombre}") 

juan = alumno ("juan", "femenino", "457685834","10/09/2000", "60")