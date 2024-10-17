from matriz import mostrar_matrices

def alquiler(lista_carros, lista_motos):
    tipo_vehiculo = input("Tipo de vehiculo:")
    placa = input("Ingrese número de placa: ")
    numero_espacio = int(input ("Ingrese número espacio que se va a alquilar:"))-1

    lista_vehiculos = lista_motos

    if tipo_vehiculo == "Carro":
        lista_vehiculos = lista_carros
    elif tipo_vehiculo == "moto":
        lista_vehiculos = lista_motos
    
    if lista_vehiculos[numero_espacio] != "D":
            print("Espacio no esta disponible")
    else:
        lista_vehiculos[numero_espacio] = "A"
        print(f"El espacio {numero_espacio} ha sido alquilado")

     
    
 
