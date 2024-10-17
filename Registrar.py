from datetime import datetime

# Función para registrar la salida y calcular la tarifa  
def registrar_salida(lista_carros, lista_motos):  
    # if placa not in registro_entrada:  
    #     print("La placa no está registrada o el vehículo ya ha salido.")  
    #     return  
    tipo_vehiculo = input("Introduzca el tipo: ").lower()

    if(tipo_vehiculo == "carro"):
        lista_vehiculos = lista_carros
    elif(tipo_vehiculo == "moto"):
        lista_vehiculos = lista_motos
    else:
        print("tipo de vehiculo introducido no valido")
        return
    
    placa = input("Introduzca la placa: ")
    
    placa_encontrada = False
    espacio_encontrado = 0
    for i in range(len(lista_vehiculos)):
      if(lista_vehiculos[i]["placa"] == placa):
        placa_encontrada = True
        espacio_encontrado = i
        break

    if(not placa_encontrada):
        print("La placa no está registrada o el vehículo ya ha salido.")  
        return  
    
    estacionamiento = lista_vehiculos[espacio_encontrado]
    if(estacionamiento["ocupado"] == True):
        estacionamiento["ocupado"] = False
        estacionamiento["hora_salida"] = datetime.now()
        print(f"se registro la salida del vehiculo con placa {estacionamiento["placa"]}")
        tiempo_ocupado   = datetime.now() - estacionamiento["hora_entrada"]
        horas_ocupadas = round(0.5+(tiempo_ocupado.total_seconds() / 3600))
        print(f"el vehiculo estuvo estacionado {horas_ocupadas} hora/s")
    else:
        print("el vehiculo no se encuentra en el estacionamiento")
        return