import calendar
# biblioteca do calendario

def calendario(): #função 
  try: # trtamento de erro, pra digitar somente número
        ano = int(input("Digite o ano: "))

        # 
        resultado = calendar.calendar(ano, 
                                      
         w=2, #Largura da coluna do dia
         l=1, #Linhas por semana
         c=8, #Espaçamento entre meses
         m=3) #Meses por linha
        
        print(f"Calendario de {ano}")
        print(resultado)
  except ValueError:
      print("ERRO")
      print("Digite somente números.")
      
if __name__=="__main__":
    calendario()