# FAZER UM ALGORITMO QUE:
# LEIA UM NUMERO INDERTEMINADO DE LINHAS CONTENDO CADA UMA IDADE DE UM INDIVIDUO
# A ULTIMA LINHA, QUE NÃO ENTRARÁ NOS CALCULOS, CONTÉM O VALOR DA IDADE IGUAL A 0
# CALCULE E ESCREVE A IDADE MÉDIA DESSE GRUPO DE INDIVIDUOS

def main():
    #Inicilizando variaveis
    idade = int(0)
    lista_idade = [0]
    
    #Condicional - Processamet0
    while True:
        idade = int(input("Digite o valor da idade: "))
        if idade == 0:
            break
        lista_idade.insert(0,idade)
        print(lista_idade)
    
    #Processamento - Media das idades
    soma_idade = sum(lista_idade)
    media_idade = soma_idade/len(lista_idade)
    #Saida da resposta
    print(media_idade)
        

    
if __name__ == "__main__":
    main() 
        
#MEU ERRO: NÃO CONSIGO RODAR O PROGRAMA CONSIDERANDO QUE O LOOP VAI PARAR QND A IDADE FOR 0
