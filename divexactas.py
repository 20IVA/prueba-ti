flag1= True
flag2= True

while Flag1:
       try:
         a = int(input("valor 1: "))
         flag1=False
       except ValueError:
        print("te equivocaste")
print("termine mi primer loop")
print(f"mi valoe obtenido son {a}")



while flag2:
       try:
         b = int(input("valor 2: "))
         flag2=False
       except ValueError:
        print("te equivocaste")
print("termine mi segundo loop") 
print(f"mi valoe obtenido son {a}")
if (a%b)==0:
   r=f"{a} / {b} es exacta"
elif (a%b)==2:
   r=f"{a} / {b} es inexacta"   
   
   print(r)




