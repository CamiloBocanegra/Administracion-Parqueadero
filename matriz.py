
def mostrar_matriz(matriz_carros: list[dict], matriz_motos : list[dict]):
   matriz = ""
   for i in range(len(matriz_carros)):

      matriz += f"v{matriz_carros[i].get("numero") + 1}"
      if(i < 9):
         matriz += " "
      
      if((i+1)%10 != 0):
         matriz += "-"
      else:
         matriz += "\n" #salto de linea

   print(matriz)