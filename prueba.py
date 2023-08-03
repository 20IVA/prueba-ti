class Gato:
    def _init_(self, nombre, genero, color,edad):
      self._nombre = nombre
      self._genero = genero 
      self._color = color 
      self._edad = edad

    def correr(self, punto_llegada):
        print(f"{self._nombre}gato tienes que ir a {punto_llegada}") 
        print("si llegaste detente ahi")

    def dormir(self, tienpo_dormir)    
        print(f"{self._nombre}enpieza dormir {tienpo_dormir}") 

chimi = Gato("chimi", "macho", "gris",1)   
chimi.correr("ala mesa")

kitty = Gato("kitty", "henbra", "blanco",1) 
kitty.dormir("15 minutos")

         
