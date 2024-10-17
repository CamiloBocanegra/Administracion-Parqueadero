from datetime import datetime


def registrar_entrada(lista_carros, lista_motos):
    placa = input("ingresa la placa del vehiculo : ").upper()
    tipo = input("ingresa el tipo de vehiculo (carro/moto)").lower()
    
    hora_entrada = datetime.now()
    
    if tipo == "carro":
        posicion = int(input("digita el numero de posicion que deseas para el carro : "))
        if  posicion >= len(lista_carros) or posicion < 0:
            print("lo siento, esta ocupado ")
            return
            
        carro = lista_carros[posicion]
                
        if carro["estado"] == "disponible ":
            carro["estado"] = "ocupado"
            carro["placa"] = placa
            carro["hora_entrada"] = hora_entrada
            carro["hora_entrada"] = hora_entrada 
            print(f" el carro con placa {placa} ha sido registro con exito en la posision {carro['numero']}. ") 
            print(f"hora de entrada : {hora_entrada}")
        else:    
            print(f"la posicion {posicion} ya esta ocupada. ")
             
    elif tipo == "moto":
        posicion = int(input("ingresa el numero de posicion para la moto"))
        if posicion >= len(lista_motos) or posicion < 0:
            print("lo siento, esta ocupado")
            return
        moto = lista_motos[posicion]
        if moto["estado"] == "Disponible":
            moto["estado"] = "ocupado"
            moto["placa"] = placa
            moto["hora_entrada"] = hora_entrada
            print(f"la moto con placa {placa} ha sido resgistrado con exito en la posicion {moto['numero']}")
            print(f"hora de entrada : {hora_entrada}")
            
        
        else:  
            print(f"  posicion {posicion} ya esta ocupada")
    else:
        print("el tipo de vehiculo que ingreso, no es valido, ingresa 'carro' o 'moto' ")  