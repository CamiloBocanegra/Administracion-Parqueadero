def alquiler(matriz_parqueadero, tipo_vehiculo,espacio_alquilar, placa):
 
  # Busca un espacio disponible para el tipo de vehículo
  for fila in range(len(matriz_parqueadero)):
    for columna in range(len(matriz_parqueadero[0])):
      if matriz_parqueadero[fila][columna] == 'D':  
        # Marca el espacio como alquilado y registra la hora de entrada
        matriz_parqueadero[fila][columna] = 'A'
        hora_entrada = obtener_hora_actual()  # Aquí debes implementar la función para obtener la hora actual
        # ... (guardar la hora de entrada asociada al espacio, por ejemplo, en un diccionario)
        return True
      
    tipos_vehiculos = {
    "carro": ["A1", "B3", "C5"],
    "moto": ["M1", "M2", "M3"],
    "camioneta": ["C1", "C2"]
}


  # Si no se encontró ningún espacio disponible
  return False