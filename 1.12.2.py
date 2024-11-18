# TEM-SE UM CONJUNTO DE DADOS CONTENDO A ALTURA E O SEXO (MASCULINO E FEMININO) DE 50 PESSOAS. 
# FAZER UM ALGORITMO QUE CALCULE E ESCREVA:
# A MAIOR E A MENOR ALTURA DO GRUPO
# A MEDIA DE ALTURA DAS MULHERES
# O NUMERO DE HOMENS

import random

def main():
    #Declaração de variaveis
    altura = float()
    pessoas = float()
    maior_altura = float()
    menor_altura = float()
    mulheres = float()
    homens = float()
    soma_altura_mulheres =  float()
    media_altura_mulheres = float()
    sexo = str()
    
    #Atribuiçao de valores iniciais
    mulheres = 0
    soma_altura_mulheres = 0
    maior_altura = 0
    menor_altura = 5 
    pessoas = 1
    
    #Gera lista para escolher o sexo
    sexos = ['MASCULINO', 'FEMININO']
    #Lista para guardar os valores a fins de curiosidade
    alturas_geradas = []
    sexos_gerados = []
    
    #Processamento de dados
    while True:
        altura = round(random.uniform(1.50, 2.00), 2)  # Gera alturas entre 1.50 e 2.00 metros
        sexo = random.choice(sexos)  # Escolhe aleatoriamente entre 'MASCULINO' e 'FEMININO'
        
        alturas_geradas.append(altura)
        sexos_gerados.append(sexo)
        
        if sexo == "FEMININO":
            soma_altura_mulheres = soma_altura_mulheres + altura
            mulheres = mulheres + 1

        if altura > maior_altura:
            maior_altura = altura
        
        if altura < menor_altura:
            menor_altura = altura
        
        pessoas = pessoas + 1
            
        if pessoas > 50:
            break
        
    media_altura_mulheres = soma_altura_mulheres/mulheres
    homens = (pessoas - mulheres)
    
    #SAIDA DE DADOS
    print(f"TODAS AS ALTURAS GERADAS: {alturas_geradas}")
    print(" ")
    print(f"TODOS OS SEXOS GERADOS: {sexos_gerados}")
    print(" ")
    print(f"A MAIOR ALTURA É: {maior_altura}")
    print(" ")
    print(f"A MENOR ALTURA É: {menor_altura}")
    print(" ")  
    print(f"A MEDIA DAS ALTURAS DAS MULHERES É DE: {media_altura_mulheres:.2}")
    print(" ")
    print(f"A QUANTIDADE DE HOMENS É: {homens}")
    
if __name__ == "__main__":
    main()
    
    
#NESTE CÓDIGO, UTILIZEI DA FUNÇÃO RANDOM PARA GERAR VALORES ALEATORIOS PARA PREENCHER AS LISTAS