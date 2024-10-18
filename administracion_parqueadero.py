from mostrar_matriz import mostrar_matrices
from alquiler import alquiler
from registrar_entrada import registrar_entrada
from registrar_salida import registrar_salida
from facturar import facturar
# from Informe import imforme_ocupacion

from datetime import datetime

# van a ser listas de diccionarios
lista_carros = [
   {
      "placa":"", 
      "alquilado":False, 
      "ocupado":False, 
      "hora_entrada":None, 
      "hora_salida":None,
      "hora_alquiler":None
   } for i in range(50)
]
lista_motos = [
   {
      "placa":"", 
      "alquilado":False, 
      "ocupado":False, 
      "hora_entrada":None, 
      "hora_salida":None,
      "hora_alquiler":None
   } for i in range(25)
]

# not lista_carros[2]["alquilado"] and not lista_carros[2]["ocupado"] == espacio 2 esta disponible

while(True):
   print("***********************************************************************")
   print("1. Mostrar matriz del parqueadero")
   print("2. Alquiler (entrada del vehículo por placa y tipo (vehículo o moto).")
   print("3. Registrar (hora entrada del vehículo por placa y tipo (vehículo o moto).")
   print("4. Registrar (hora salida del vehículo por placa y tipo (vehículo o moto).")
   print("5. Facturar")
#    print("6. Informe Ocupación (opcional)")
   print("0. Salir")

   try:
      opcion_seleccionada = int(input("Digite una opcion: "))
   except ValueError:
      opcion_seleccionada = -1

   if(opcion_seleccionada == 1):      
      mostrar_matrices(lista_carros, lista_motos)
   elif(opcion_seleccionada == 2):
      alquiler(lista_carros, lista_motos)
   elif(opcion_seleccionada == 3):
      registrar_entrada(lista_carros, lista_motos)
   elif(opcion_seleccionada == 4):
      registrar_salida(lista_carros, lista_motos)
   elif(opcion_seleccionada == 5):
      facturar(lista_carros, lista_motos)
   # elif(opcion_seleccionada == 6):
   #    informe_ocupacion(lista_carros, lista_motos)
   elif(opcion_seleccionada == 0):
      print("Adios. ")
      break
   else:
      print("OPCION INTRODUCIDA NO VALIDA!!!")