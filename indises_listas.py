lista_nombres=[]
flag=True
while flag:
     nombres = input("ingrse nombres o para terminar escriba x: ")
     if nombres == "x":
        flag=False
     else:
      cnombre=nombres.capitalize()
      if cnombre in lista_nombres:
        pass
      else: 
          lista_nombres.append(cnombre)

print(lista_nombres)
print(f"la cantidad de nombres son {len(lista_nombres)}")

for i in lista_nombres:
   print(f"{i}el numero de letras {len(i)}")