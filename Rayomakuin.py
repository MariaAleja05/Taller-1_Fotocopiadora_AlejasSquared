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
