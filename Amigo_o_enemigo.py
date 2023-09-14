print("-------------------------------------------------------")
print("Determinar cual número es mayor")
print("-------------------------------------------------------")
#Entradas
print("Ingrese dos números reales: ")
a=float( input("a: "))
b=float( input("b: "))
#Proceso
if a % b == 0:
    print(f"{a} Es múltiplo de {b}")
else:
    print(f"{a} No es múltiplo de {b}")