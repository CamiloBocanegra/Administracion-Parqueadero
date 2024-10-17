


def mostrar_matrices(matriz_carros: list[dict], matriz_motos : list[dict]):
   matriz = ""
   for i in range(len(matriz_carros)):
      estado_espacio = matriz_carros[i]
      if(estado_espacio == "D"): #disponible
         matriz += f"v{i + 1}"
         if(i < 9):
            matriz += " "
      else:
         matriz += " "+estado_espacio+" "
      
      if((i+1)%10 != 0):
         matriz += "-"
      else:
         matriz += "\n" #salto de linea

   matriz += " *************************************** \n"

   for i in range(len(matriz_motos)):
      estado_espacio = matriz_motos[i]
      if(estado_espacio == "D"): #disponible
         matriz += f"m{i + 1}"
         if(i < 9):
            matriz += " "
      else:
         matriz += " "+estado_espacio+" "
      
      if( ((i+1) % 10) != 0  and i != len(matriz_motos)-1):
         matriz += "-"
      else:
         matriz += "\n" #salto de linea

   matriz + "\n"

   print(matriz)