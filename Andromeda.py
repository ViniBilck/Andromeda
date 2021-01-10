##--Vinicius Lourival Bilck--##

import numpy as np
import tkinter as tk

## Declaração
Num = []
Teste = []
i=2
j=0
M=int(input("Números: \n"))
Sel=np.arange(1,M+1)
       
## Verificação de números Primos 

def verificador(x):
    i=2
    Teste=[]
    while (x>i):
        
        if x%i == 0:
            Teste.append(1)
            i+=1
        else:
            i+=1
        
    if len(Teste) == 0:
        Num.append(x)

## Valores verificados
        
for j in range(1,M+1):
    verificador(j)

## Todos os primos que compoem o conjunto natural escolhido de 1 a M --> (Usuario escolhe)

print(Num)
    

