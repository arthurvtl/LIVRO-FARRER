# UM COMERCIANTE DESEJA FAZER O LEVANTAMENTO DO LUCRO DAS MERCADORES QUE ELE COMERCIZALIZA.
# PARA ISTO, MANDOU DIGITAR UMA LINHA PARA CADA MERCADODIRA COM O NOME, PREÇO DE COMPRA, E PREÇO DE VENDA DAS MESMAS
# FAZER UM ALGORITMO QUE:
# DETERMINE E ESCREVA QUANTAS MERCADORIAS PROPORCIONAM
# LUCRO < 10%
# 10% <= LUCRO <= 20%
# LUCRO > 20%
# DETERMINE E ESCREVA O VALOR TOTAL DE COMPRA E DE VENDA DE TODAS AS MERCADORIAS ASSIM COMO O LUCRO TOTAL

def main():
    compra = float()
    venda = float()
    lucro = float()
    lucro10 = float()
    lucro1020 = float()
    lucro20 = float()
    total_compra = float()
    total_venda = float()
    lucro_total = float()
    
    nome = str()
    
    lucro10 = 0
    lucro1020 = 0
    lucro20 = 0
    total_compra = 0
    total_venda = 0
    
    while True:
        nome = str(input("Digite o nome do produto: "))
        if nome == "VAZIO":
            break
        compra = float(input("Digite o preço de compra: "))
        venda = float(input("Digite o preço de venda: "))
        

        
        lucro = (venda - compra) * 100 / compra
        
        if lucro < 10:
            lucro10 = lucro10 + 1
            
        elif lucro <= 20:
            lucro1020 = lucro1020 + 1
            
        else:
            lucro20 = lucro20 + 1
        
        total_compra = total_compra + compra
        total_venda = total_venda + venda
        lucro_total = total_venda - total_compra
        
        print(f"O {nome} possui lucro menor que 10% é: {lucro10}")
        print(" ")
        print(f"O {nome} possui lucro entre 10% a 20% é: {lucro1020}")
        print(" ")
        print(f"O {nome} possui lucro maior que 20% é: {lucro20}")
        print(" ")
        print(f"O valor total de compra é de: {total_compra}")
        print(" ")
        print(f"O valor total de venda é de: {total_venda}")
        print(" ")
        print(f"O valor total do lucro é de: {lucro_total}")
    
if __name__ == "__main__":
    main()