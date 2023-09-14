# Taller #1
### Fecha:  13-09-2023
### **Nombre del equipo:** Fotocopiadoras Industriales
### **Logo:** (FALTA)
### 1. El resultado de nuestro Python Beginner Quiz:
    (INGRESAR FOTO)
### 2. Realice un programa que lea tres números reales y determine cuál es el mayor.
* Para este punto debíamos realizar un programa que leyera tres números reales y determinara cuál es el mayor.
  Primero declaramos que las variables que ingresara el usuario debian ser números reales (float), y posteriormente con una estructura if-elif comparamos cada una de las variables para determinar la mayor.
* Ver documento:
Quien_es_mas_grandecito.py
```pseudocode
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
```
### 3. Enunciado: Realice un programa que lea un número enteros y determine si es par o impar.
* (EXPLICACIÓN)
```pseudocode
print("-------------------------------------------------------")
print("Determinar si el número entero es par o impar")
print("-------------------------------------------------------")
#Entradas
n: int = 0
print("Ingrese un número: ")
n=int( input("n: "))
#Proceso
if n%2==0:
  print("El número ingresado es par")
else:
  print("El número ingresado es impar")
```
### 4. Enunciado: Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
* Para este punto debíamos hacer un programa que leyera dos números reales y determinara si el primero era múltiplo del segundo.
  Como en el punto #2 lo primero que hicimos fue declarar que los números que ingresara el usuario debían ser reales (float), depués con una estructura if-else condicionamos con un operador de asignacion con residuo igualado a cero.
* Ver documeto:
  Amigo_o_enemigo.py
  
```pseudocode
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
```
### 5. Enunciado: Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.
* (EXPLICACIÓN)
```pseudocode
print("-------------------------------------------------------")
print("Determinar si la suma de los dos primeros números es mayor, menor o igual que un tercer número")
print("-------------------------------------------------------")
#Entradas
primer_numero: int = 0
segundo_numero: int = 0
tercer_numero: int = 0
suma: int = 0
print("Ingrese el primer número: ")
primer_numero=int( input("primer_numero: "))
print("Ingrese el segundo número: ")
segundo_numero=int( input("segundo_numero: "))
print("Ingrese el segundo número: ")
tercer_numero=int( input("tercer_numero: "))
#Proceso
suma=primer_numero+segundo_numero
if tercer_numero>suma:
  print("El tercer número es mayor que la suma de los dos primeros números ")
elif tercer_numero<suma:
  print("El tercer número es menor que la suma de los dos primeros números ")
else:
  print("El tercer número es igual que la suma de los dos primeros números")
```
### 6. Enunciado: Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
* En este punto nuestro objetivo debía ser escribir un programa que solicitara al usuario una letra y determinara si era una vocal o una consonante.
  Con una estructura if-else y utilizando el conector or, definimos las vocales y las letras. (Tambien tuvimos en cuenta las mayúsculas, por eso se ve larguísimo :))
- Ver documento: Sonidos_y_maneras.py
```pseudocode
print("-------------------------------------------------------")
print("Determinar si una letra es vocal o consonante")
print("-------------------------------------------------------")
#Entradas
n=( input("Escriba una letra: "))
#Proceso
if n == "a" or n == "e" or n == "i" or n == "o" or n == "u" or n == "E" or n == "I" or n == "O" or n == "U" or n == "A":
    print(f"{n} Es una vocal")
elif n == "q" or n == "w"  or n == "r" or n == "t" or n == "y" or n == "p" or n == "s" or n == "d" or n == "f" or n == "g"or n == "h"or n == "j"or n == "k"or n == "l"or n == "z"or n == "x"or n == "c"or n == "v"or n == "b"or n == "n"or n == "m" or n == "Q" or n == "W"  or n == "R" or n == "T" or n == "Y" or n == "P" or n == "S" or n == "D" or n == "F" or n == "G"or n == "H"or n == "J"or n == "K"or n == "L"or n == "Z"or n == "X"or n == "C"or n == "V"or n == "B"or n == "N"or n == "M":
    print(f"{n} Es una consonante")
```
### 7. Enunciado: Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
- El promedio
- La mediana
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
- Ordenar los números de forma ascendente
- Ordenar los números de forma descendente
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número
* (EXPLICACIÓN)
```pseudocode

```
### 8. Enunciado: Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.
*  El objetivo de este punto era recibir una frecuencia de onda en Hz y determinar en que parte del espectro electromagnético se encontraba.
  Como es eperado, lo primero que hicimos fue declarar el número que ingresaba el ususario como real. Con una estructura if-elif definimos los segementos del espectro electromagnético y sus características, como que tipo de onda es y cual es su posible tamaño.
- Ver documento: Las_vibras.py
```pseudocode
print("-------------------------------------------------------")
print("Determinar en que parte del espectro electromagnético se encuentra una onda")
print("-------------------------------------------------------")
#Entradas
n=float( input("Ingrese la frecuencia de una onda en Hz: "))
#Proceso
if 10**4 <= n < 10**8:
    print(f"Una onda con frecunecia {n} es una onda como la un radio, su longitud aproximada puede ser desde los 1000 metros hasta los 2 metros")
elif 10**8 <= n < 10**12:
    print(f"Una onda con freceuncia {n} es una onda como la un microhondas, su longitud aproximada puede ser desde la estatura de un humano (2m) hasta el tamaño de una bella mariposa (1cm)")
elif 10**12 <= n < 10**15:
    print(f"Una onda con frecuencia {n} puede ser una onda infraroja o visible, su longitud aproximada puede ser desde el tamaño de la punta de una aguja (0,01cm) hasta el tamaño de un protoozo (0,5μm)")
elif 10**15 <= n < 10**16:
    print(f"Una onda con frecuencia {n} puede ser una onda visible o ultravioleta, su longitud aproximada puede ser desde el tamaño de un protoozo (0,5μm)) hasta el tamaño de una partícula (0,01μm)")
elif 10**16 <= n < 10**18:
    print(f"Una onda con frecuencia {n} puede ser unna onda ultravioleta o Rayos X, su longitud aproximada puede ser desde el tamaño de una parícula (0,01μm)) hasta el tamaño de un átomo (0,1nm)")
elif 10**18 <= n < 10**20:
    print(f"Una onda con frecuencia {n} puede ser una onda de Rayos X o Rayos Gamma, su longitud aproximada puede ser desde el tamaño de un átomo (0,1nm)) hasta el tamaño de un núcleo atómico (0,001nm)")
```
### 9. Enunciado: Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.
* (EXPLICACIÓN)
```pseudocode
print("-------------------------------------------------------")
print("Determinar la capital del pais de América ingresado")
print("-------------------------------------------------------")
#Entradas
pais: str
print("Ingrese un país de América: ")
pais=str( input("pais: "))
pais=pais.lower()
print(pais)
#Proceso
if pais=="canada" or pais=="canadá":
  print("La capital es Otawwa")
elif pais=="estados unidos":
  print("La capital es Washington DC")
elif pais=="mexico" or pais=="méxico":
  print("La capital es México DF")
elif pais=="belice":
  print("La capital es Belmopán")
elif pais=="costa rica":
  print("La capital es San José")
elif pais=="el salvador":
  print("La capital es San Salvador")
elif pais=="Guatemala":
  print("La capital es Ciudad de Guatemala")
elif pais=="Honduras":
  print("La capital es Tegucigalpa")
elif pais=="nicaragua":
  print("La capital es Mnagua")
elif pais=="panama" or pais=="panamá":
  print("La capital es Panamá")
elif pais=="argentina":
  print("La capital es Buenos Aires")
elif pais=="bolivia":
  print("La capital es Sucre")
elif pais=="brasil":
  print("La capital es Brasilia")
elif pais=="chile":
  print("La capital es Santiago de Chile")
elif pais=="colombia":
  print("La capital es Bogotá")
elif pais=="ecuador":
  print("La capital es Quito")
elif pais=="paraguay":
  print("La capital es Asunción")
elif pais=="peru" or pais=="perú":
  print("La capital es Lima")
elif pais=="surinam":
  print("La capital es Parabarimo")
elif pais=="trinidad y tobago":
  print("La capital es Puerto España")
elif pais=="uruguay":
  print("La capital es Montevideo")
elif pais=="venezuela":
  print("La capital es Caracas")
elif pais=="antigua y barbuda":
  print("La capital es Saint John")
elif pais=="bahamas":
  print("La capital es Nasáu")
elif pais=="barbados":
  print("La capital es Bridgetown")
elif pais=="cuba":
  print("La capital es La Habana")
elif pais=="dominica":
  print("La capital es Roseau")
elif pais=="granada":
  print("La capital es Saint George")
elif pais=="guyana":
  print("La capital es Georgetown")
elif pais=="haiti" or pais=="haití":
  print("La capital es Puerto Príncipe")
elif pais=="jamaica":
  print("La capital es Kingston")
elif pais=="republica conminicana":
  print("La capital es Santo Domingo")
elif pais=="san cristobal y nieves" or pais=="san cristóbal y nieves":
  print("La capital es Basseterre")
elif pais=="san vicente y las granadinas":
  print("La capital es Kingstown")
elif pais=="santa lucia" or pais=="santa lucía":
  print("La capital es Castries")
else:
  print("país no identificado")
```
### 10. Escriba un programa que dada una distancia calcule:
- El tiempo que le tomaría a la luz recorrer la distancia.
- El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
- El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
- El tiempo que le tomaría a Bolt recorrer la distancia.
* Para es código lo que hicimos fue definir cuatri variables, cada una correspondiente al tiempo que se tardaría cada uno de los elemetos. Para esto usamos siempre la misma función de dividir la ditancia por la velocidad del elemento.
- Ver docuento: Rayomakuin.py
```pseudocode
print("-------------------------------------------------------")
print("Distacias")
print("-------------------------------------------------------")
#Entradas
la_distancia=float( input("Ingrese una distancia en Kilometros: "))
#Proceso
tiempo_luz : float = la_distancia / 299792.458 #Velocidad de la Luz en km/s
print(f"El tiempo que se tardaría la luz en recorrer {la_distancia}Km es: ")
print(f"{tiempo_luz} segundos")
tiempo_sonido : float = la_distancia / 0.343 #Velocidad de el sonido en km/s
print(f"El tiempo que se tardaria el sonido en recorrer {la_distancia}Km es: ")
print(f"{tiempo_sonido} segundos")
tiempo_SSCTuatara : float = la_distancia / 460.43 #Velocidad de el SSC Tuatara en km/h
print(f"El tiempo que se tardaria el sonido en recorrer {la_distancia}Km es: ")
print(f"{tiempo_SSCTuatara} horas")
tiempo_Bolt : float = la_distancia / 45 #Velocidad de Usain Bolt en km/h
print(f"El tiempo que se tardaria el sonido en recorrer {la_distancia}Km es: ")
print(f"{tiempo_Bolt} horas")
```
