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