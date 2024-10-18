from datetime import datetime


def registrar_entrada(lista_carros, lista_motos):
    tipo = input("ingresa el tipo de vehiculo (carro/moto): ").lower()
    placa = input("ingresa la placa del vehiculo: ").upper()
    
    hora_entrada = datetime.now()
    
    if tipo == "carro":
        posicion = int(input("digita el numero de posicion que deseas para el carro: "))-1
        if  posicion >= len(lista_carros) or posicion < 0:
            print("lo siento posicion no valida ")
            return
        
        ocupado = lista_carros[posicion]["ocupado"]
        alquilado = lista_carros[posicion]["alquilado"]
        if(ocupado):
            print("lo siento, el espacio ya esta ocupado")
            
        carro = lista_carros[posicion]
                
        if not alquilado or (alquilado and carro["placa"] == placa):
            carro["ocupado"] = True
            carro["placa"] = placa
            carro["hora_entrada"] = hora_entrada
            print(f" el carro con placa {placa} ha sido registro con exito en la posision {posicion+1}. ") 
            print(f"hora de entrada : {hora_entrada}")
        else:    
            print(f"la posicion {posicion+1} esta reservada. ")
             
    elif tipo == "moto":
        posicion = int(input("ingresa el numero de posicion para la moto: "))-1
        if posicion >= len(lista_motos) or posicion < 0:
            print("lo siento posicion no valida")
            return

        ocupado = lista_motos[posicion]["ocupado"]
        alquilado = lista_motos[posicion]["alquilado"]
        if(ocupado):
            print("lo siento, el espacio ya esta ocupado")

        moto = lista_motos[posicion]

        if not alquilado or (alquilado and moto["placa"] == placa):
            moto["ocupado"] = True
            moto["estado"] = "ocupado"
            moto["placa"] = placa
            moto["hora_entrada"] = hora_entrada
            print(f"la moto con placa {placa} ha sido resgistrado con exito en la posicion {posicion+1}")
            print(f"hora de entrada : {hora_entrada}")
            
        else:  
            print(f"la  posicion {posicion+1} esta reservada")
    else:
        print("el tipo de vehiculo que ingreso, no es valido, ingresa 'carro' o 'moto' ")  