
<<<<<<< HEAD
TARIFA_HORA = 2000

def facturar(lista_carros, lista_motos):   
    tipo_vehiculo = input("introduzca el tipo de vehiculo: ").lower()

    if(tipo_vehiculo == "carro"):
        lista_vehiculos = lista_carros
    elif(tipo_vehiculo == "moto"):
        lista_vehiculos = lista_motos
    else:
        print("tipo de vehiculo introducido no valido")
        return
    
    placa = input("introduzca la placa: ")

    placa_encontrada = False
    espacio_encontrado = 0
    for i in range(len(lista_vehiculos)):
        if(placa == lista_vehiculos[i]["placa"]):
            placa_encontrada = True
            espacio_encontrado = i
            break

    if(not placa_encontrada):
        print("La placa no está registrada o el vehículo ya ha salido.")  
        return  
    
    ocupado = lista_vehiculos[espacio_encontrado]["ocupado"]
    alquilado = lista_vehiculos[espacio_encontrado]["alquilado"]

    if(ocupado):
        print("el vehiculo aun esta ocupando el espacio.\n debe registrar su salida primero")
        return
    
    if(alquilado):
        comienzo_alquiler = lista_vehiculos[espacio_encontrado]["hora_alquilado"]
        fin_alquiler = datetime.now()

        tiempo_ocupado = fin_alquiler - comienzo_alquiler
    else:
        hora_entrada :datetime = lista_vehiculos[espacio_encontrado]["hora_entrada"]
        hora_salida :datetime = lista_vehiculos[espacio_encontrado]["hora_salida"]

        tiempo_ocupado = hora_salida - hora_entrada  


    # Convertir tiempo a horas  
    horas_ocupadas = round(0.5+(tiempo_ocupado.total_seconds() / 3600))  

    # Calcular tarifa  
    tarifa = horas_ocupadas * TARIFA_HORA
    
    # Calcular porcentaje de ocupación  
    JORNADA_DIARIA = 22 - 6 #10pm - 6am   por ahora
    porcentaje_ocupado = horas_ocupadas / JORNADA_DIARIA

    print(f"el vehiculo estuvo estacionado {horas_ocupadas} hora/s")
    
    DESCUENTO = 0.15
    if not alquilado and porcentaje_ocupado >= 0.7:  
        tarifa = round(tarifa * (1 - DESCUENTO))  # Aplicar descuento  
        print(f"la tarifa es de {tarifa}")
        print("se le aplica un descuento por haber ocupado mas del 70% de la jornada diaria")
    
    print(f"el precio final es de {tarifa}")

    # reseteando el espacio
    lista_vehiculos[espacio_encontrado] = {
      "placa":"", 
      "alquilado":False, 
      "ocupado":False, 
      "hora_entrada":None, 
      "hora_salida":None,
      "hora_alquiler":None
    }
=======
>>>>>>> e2bf88982a33329bddde7e4c281d983a785e8e5e
