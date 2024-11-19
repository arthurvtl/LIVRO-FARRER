def main():
    #declaracao de variaveis
    paisA = int()
    paisB = int()
    taxaA = int()
    taxaB = int()

    #entrada de dados
    paisA = 90000000
    paisB = 200000000
    taxaA = 0.03
    taxaB = 0.015
    
    #contador
    anos = 0

    #processamento
    while paisA <= paisB:
        paisA += paisA * taxaA
        paisB += paisB * taxaB
        anos += 1
    
    #saida de dados
    print(f"O país A irá superar o país B em população em {anos} anos.")
        

        
if __name__ == "__main__":
    main()