from matriz import mostrar_matrices
from Alquiler import alquiler
# from registrar_salida import registrar_salida
# from Registrar_entrada import registrar_entrada
# from Facturar import Facturar
# from Informe import imforme_ocupacion

from datetime import datetime

# van a ser listas/matrices de diccionarios
# estado O:ocupado, A:alquilado, D:disponible
lista_carros = [
   {
      "placa":"", 
      "alquilado":False, 
      "ocupado":False, 
      "hora_entrada":None, 
      "hora_salida":None
   } for i in range(50)
]
lista_motos = [
   {
      "placa":"", 
      "alquilado":False, 
      "ocupado":False, 
      "hora_entrada":None, 
      "hora_salida":None
   } for i in range(25)
]

# ejemplos para visualizar la matriz en caso de que estos espacios estuvieran ocupados
# lista_carros[2]["estado"] = "A"
# lista_carros[33]["estado"] = "O"

# lista_motos[1]["estado"] = "A"
# lista_motos[15]["estado"] = "O"

while(True):
   print("1. Mostrar matriz del parqueadero")
   print("2. Alquiler (entrada del vehículo por placa y tipo (vehículo o moto).")
   # print("3. Registrar (hora entrada del vehículo por placa y tipo (vehículo o moto).")
#    print("4. Registrar (hora salida del vehículo por placa y tipo (vehículo o moto).")
#    print("5. Facturar")
#    print("6. Informe Ocupación (opcional)")
   print("0. Salir")

   opcion_seleccionada = int(input("Digite una opcion: "))

   if(opcion_seleccionada == 1):      
      mostrar_matrices(lista_carros, lista_motos)
   elif(opcion_seleccionada == 2):
      alquiler(lista_carros, lista_motos)
   # elif(opcion_seleccionada == 3):
   #    registrar_entrada(lista_carros, lista_motos)
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