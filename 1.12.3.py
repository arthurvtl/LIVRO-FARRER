#A CONVERSÃO DE GRAUS FARENHEIT PARA CENTÍGRADOS É OBTIDA POR
# C = (5/9) *( F - 32)
# FAZER UM ALGORITMO QUE CALCULE E ESCREVA UMA TABELA DE CENTÍGRADOS EM FUNÇÃO DE GRAUS FARENHEIT
# VARIE DE 50 A 150 de 1 em 1

def main():
    f = float()
    c = float()
    
    for f in range(50, 151, 1):
        c = (5/9) * (f - 32)
        print(f"{c:.2f}")
    
    
    
if __name__ == "__main__":
    main()