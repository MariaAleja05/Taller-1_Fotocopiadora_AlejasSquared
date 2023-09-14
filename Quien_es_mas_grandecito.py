print("-------------------------------------------------------")
print("Determinar cual número es mayor")
print("-------------------------------------------------------")
#Entradas
print("Ingrese tres números reales: ")
a=float( input("a: "))
b=float( input("b: "))
c=float( input("c: "))
#Proceso
if a > b and a > c:
  print("El número mayor es:")
  print(a) 
elif b > a and b > c:
  print("El número mayor es:")
  print(b)
elif c > a and c > b:
 print("El número mayor es:")
 print(c)