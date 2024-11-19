def main():
    #declaracao variavel  RADIOATIVO
    massaInicial = float()
    massaFinal = float()

    #declaracao variavel  TEMPO
    qtdSeg = int()
    seg = int()
    min = int()
    hr = int()

    #entrada de dados
    massaInicial = float(input("Digita a massa inicial em gramas: "))
    qtdSeg = 0

    massaFinal  =  massaInicial
    #PROCESSAMENTO DE DADOS DO LOOP
    while (massaFinal > 0.5):
        qtdSeg = qtdSeg + 50
        massaFinal = (massaFinal/2)
        
    #processamento de dados
    hr = qtdSeg//3600
    min = (qtdSeg%3600)//60
    seg = (qtdSeg%3600)%60
        
    print(f"| massa inicial: {massaInicial} | massa final {massaFinal} | horas = {hr} | minutos = {min} | segundos = {seg}|")

if __name__ == "__main__":
    main()
