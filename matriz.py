


def mostrar_matrices(matriz_carros: list[dict], matriz_motos : list[dict]):
   matriz = ""
   for i in range(len(matriz_carros)):
      estado_espacio = matriz_carros[i].get("estado")
      if(estado_espacio == "D"): #disponible
         matriz += f"v{matriz_carros[i].get("numero") + 1}"
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
      estado_espacio = matriz_motos[i].get("estado")
      if(estado_espacio == "D"): #disponible
         matriz += f"m{matriz_motos[i].get("numero") + 1}"
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