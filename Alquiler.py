from datetime import datetime

def alquiler(lista_carros, lista_motos):
    tipo_vehiculo = input("Tipo de vehiculo:")
    
    if tipo_vehiculo == "carro":
        lista_vehiculos = lista_carros
    elif tipo_vehiculo == "moto":
        lista_vehiculos = lista_motos
    else:
        print("tipo de vehiculo introducido no valido")
        return
    
    numero_espacio = int(input ("Ingrese número espacio que se va a alquilar:"))-1
    placa = input("Ingrese número de placa: ")


    if not lista_vehiculos [numero_espacio]["alquilado"] and not lista_vehiculos[numero_espacio]["ocupado"]:
        lista_vehiculos[numero_espacio]["hora_alquiler"] = datetime.now()
        lista_vehiculos[numero_espacio]["alquilado"] = True
        lista_vehiculos[numero_espacio]["placa"] = placa
        print(f"El espacio {numero_espacio+1} ha sido alquilado")
    else:
        print("El espacio no esta disponible")



    # if tipo_vehiculo == "Carro":
    #     lista_vehiculos = lista_carros
    # elif tipo_vehiculo == "moto":
    #     lista_vehiculos = lista_motos
    
    # if lista_vehiculos[numero_espacio]["alquilado"] != "D":
    #         print("Espacio no esta disponible")
    # else:
    #     lista_vehiculos[numero_espacio] = "A"
    #     print(f"El espacio {numero_espacio} ha sido alquilado")

     
    
 
