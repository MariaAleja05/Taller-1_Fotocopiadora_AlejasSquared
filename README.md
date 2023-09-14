# Taller #1
### Fecha:  13-09-2023
### **Nombre del equipo:** Fotocopiadoras Industriales
### **Logo:** (FALTA)
### 1. El resultado de nuestro Python Beginner Quiz:
    (INGRESAR FOTO)
### 2. Realice un programa que lea tres números reales y determine cuál es el mayor.
* (EXPLICACIÓN)
```pseudocode
(COPIAR EL CÓDIGO)
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
* (EXPLICACIÓN)
```pseudocode

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
* (EXPLICACIÓN)
```pseudocode

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
* (EXPLICACIÓN)
```pseudocode

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
* (EXPLICACIÓN)
```pseudocode
(COPIAR EL CÓDIGO)
```
