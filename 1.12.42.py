# Cálculo da distância entre dois pontos em um plano

#Processamento
def main(): 
    
    #Declaração de variáveis
    xa = float()
    ya = float()
    xb = float()
    yb = float()
    calcA = float()
    calcB = float()
    d = float()
    
    #Entrada de dados
    xa= float(input())
    ya= float(input())
    xb= float(input())
    yb= float(input())  
    
    while ((xa !=0 ) or  (ya != 0) or (xb !=0 ) or (yb !=0 )):
        calcA = (xa - xb)**2
        calcB = (ya - yb)**2
        d = ((calcA) + (calcB))**0.5     
        #saida de dados
        print("X1=%.2f Y1=%.2f X2=%.2f Y2=%.2f D=%.2f" % (xa, ya, xb, yb, d))
        
        #novas coordenadas
        xa= float(input())
        ya= float(input())
        xb= float(input())
        yb= float(input())
    
if __name__ == "__main__":
    main()