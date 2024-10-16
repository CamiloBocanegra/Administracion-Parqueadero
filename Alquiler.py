def alquiler(parqueadero, tipo_vehiculo, placa):
      for fila in parqueadero:
        for i, espacio in enumerate(fila):
            if espacio[0] == tipo_vehiculo and espacio == 'A':
                fila[i] = f"{tipo_vehiculo}{placa}"
                return True
        return False