from matriz import mostrar_matrices

def alquiler(matriz):
      tipo_vehiculo = input("Tipo de vehiculo:")
      placa = input("Ingrese número de placa: ")
      for fila in matriz:
        for i, espacio in enumerate(fila):
            if espacio[0] == tipo_vehiculo and espacio == 'A':
                fila[i] = f"{tipo_vehiculo}{placa}"
                return True
        return False
       
      if alquiler (matriz):
          print ("Espacio asignado")
      else:
          print ("No hay espacios disponibles")
    