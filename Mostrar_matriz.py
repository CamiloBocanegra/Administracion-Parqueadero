
def mostrar_matrices(matriz_carros: list[dict], matriz_motos : list[dict]):
   matriz = ""
   for i in range(len(matriz_carros)):
      alquilado = matriz_carros[i]["alquilado"]
      ocupado = matriz_carros[i]["ocupado"]
      if(not ocupado and not alquilado): #disponible
         matriz += f"v{i + 1}"
         if(i < 9):
            matriz += " "
      else:
         if(ocupado):
            matriz += " O "
         else:
            matriz += " A "
      
      if((i+1)%10 != 0):
         matriz += "-"
      else:
         matriz += "\n" #salto de linea

   matriz += " *************************************** \n"

   for i in range(len(matriz_motos)):
      alquilado = matriz_motos[i]["alquilado"]
      ocupado = matriz_motos[i]["ocupado"]
      if(not ocupado and not alquilado): #disponible
         matriz += f"m{i + 1}"
         if(i < 9):
            matriz += " "
      else:
         if(ocupado):
            matriz += " O "
         else:
            matriz += " A "
      
      if( ((i+1) % 10) != 0  and i != len(matriz_motos)-1):
         matriz += "-"
      else:
         matriz += "\n" #salto de linea

   matriz + "\n"

   print(matriz)