from matriz import mostrar_matriz
# from Alquiler import alquiler
# from registrar_salida import registrar_salida
# from registrar_entrada import registrar_entrada
# from matriz import mostrar_matriz
# from Facturar import Facturar
# from Informe import imforme_ocupacion

from datetime import datetime

# van a ser listas/matrices de diccionarios
# estado O:ocupado, A:alquilado, D:disponible
lista_carros = [{"numero":i, "estado":"D"} for i in range(50)]
lista_motos = [{"numero":i, "estado":"D"} for i in range(25)]


while(True):
   print("1. Mostrar matriz del parqueadero")
#    print("2. Alquiler (entrada del vehículo por placa y tipo (vehículo o moto).")
#    print("3. Registrar (hora entrada del vehículo por placa y tipo (vehículo o moto).")
#    print("4. Registrar (hora salida del vehículo por placa y tipo (vehículo o moto).")
#    print("5. Facturar")
#    print("6. Informe Ocupación (opcional)")
   print("0. Salir")

   opcion_seleccionada = int(input("Digite una opcion: "))

   if(opcion_seleccionada == 1):      
      mostrar_matriz(lista_carros, lista_motos)
#    elif(opcion_seleccionada == 2):
#       alquiler(lista_carros, lista_motos)
#    elif(opcion_seleccionada == 3):
#       registrar_entrada(lista_carros, lista_motos)
#    elif(opcion_seleccionada == 4):
#       registrar_salida(lista_carros, lista_motos)
#    elif(opcion_seleccionada == 5):
#       facturar(lista_carros, lista_motos)
#    elif(opcion_seleccionada == 6):
#       informe_ocupacion(lista_carros, lista_motos)
   elif(opcion_seleccionada == 0):
      print("Adios. ")
      break
   else:
      print("opcion introducida no valida. ")
