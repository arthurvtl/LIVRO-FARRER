def main():
    tempo_padrao1 = float()
    tempo_padrao2 = float()
    tempo_padrao3 = float()
    inscricao_equipe = int()
    winner = int()
    maiorPont = int()
      
    maiorPont = 0 
    tempo_padrao1 = float(input())
    tempo_padrao2 = float(input())
    tempo_padrao3 = float(input())
    inscricao_equipe = int(input())
    
    if inscricao_equipe != 9999:
        while inscricao_equipe != 9999:
            # Inicializando os pontos totais para a equipe atual
            pontos_totais = 0
            pontos1 = 0
            pontos2 = 0
            pontos3 = 0

            print("ETAPA 1")
            
            tempo_despendido = float(input())
            diferenca1 = tempo_padrao1 - tempo_despendido
            diferenca1 = abs(diferenca1)

            if diferenca1 < 3:
                pontos1 = 100
            if 3 <= diferenca1 and diferenca1 <= 5:
                pontos1 = 80
            if diferenca1 > 5:
                pontos1 = 80 - ((diferenca1 - 5) / 5)
            
            pontos_totais += pontos1

            print("ETAPA 2")
            
            tempo_despendido = float(input())
            diferenca2 = tempo_padrao2 - tempo_despendido
            diferenca2 = abs(diferenca2)

            if diferenca2 < 3:
                pontos2 = 100
            if 3 <= diferenca2 and diferenca2 <= 5:
                pontos2 = 80
            if diferenca2 > 5:
                pontos2 = 80 - ((diferenca2 - 5) / 5)
            
            pontos_totais += pontos2

            print("ETAPA 3")
            
            tempo_despendido = float(input())
            diferenca3 = tempo_padrao3 - tempo_despendido
            diferenca3 = abs(diferenca3)


            if diferenca3 < 3:
                pontos3 = 100
            if 3 <= diferenca3 and diferenca3 <= 5:
                pontos3 = 80
            if diferenca3 > 5:
                pontos3 = 80 - ((diferenca3 - 5) / 5)
            
            pontos_totais += pontos3
            
            if pontos_totais > maiorPont:
                winner = inscricao_equipe
                maiorPont = pontos_totais
                
            

            # Exibindo o resultado final da equipe
            print(f"|PONTOS ETAPA 1: {pontos1} | PONTOS ETAPA 2: {pontos2} | PONTOS ETAPA 3: {pontos3} | QUANTIDADE TOTAL: {pontos_totais}")
            
            # Ler o próximo número de inscrição
            inscricao_equipe = int(input("Digite o número da inscrição da próxima equipe: "))

        print(f"Vencedor é a equipe {winner} e a pontuação dela foi: {maiorPont}")
    else:
        print("Não há equipe inscrita na corrida!")        

if __name__ == "__main__":
    main()
