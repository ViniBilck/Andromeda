import numpy as np

## Declaração
Num = []
Teste = []
i=2
M=int(input("Número: \n"))

## Verificação de números Primos 

while (M>i):
    if M%i == 0:
        Teste.append(1)
        i+=1
    else:
        i+=1
        
if len(Teste) == 0:
    print("O número "+str(M)+" é primo")
else:
    print("O número "+str(M)+" não é primo")
    
##Para números grandes, um vetor grande será gerado, então posso acabar ajustar o código para que na 
##primeira entrada de uma divisão com resto 0 inválidar. 

