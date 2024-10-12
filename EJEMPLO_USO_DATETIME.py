
from datetime import datetime


time1 = datetime.now()
time2 = datetime.now()


while(True):
   print("1. registrar entrada \n aaaaa")
   print("2. registrar salida")
   print("3. calcular tiempo transcurrido")

   opcion_seleccionada = int(input("Digite una opcion: "))

   if(opcion_seleccionada == 1):      
      time1 = datetime.now()
      print(time1)
   elif(opcion_seleccionada == 2):
      time2 = datetime.now()
      print(time2)
   elif(opcion_seleccionada == 3):
      difference = time2-time1
      print(difference)
      print(f"dias transcurridos: {difference.days}")
      print(f"segundos transcurridos: {difference.seconds}")
      print(f"horas transcurridas {difference.seconds / 3600}")
      break