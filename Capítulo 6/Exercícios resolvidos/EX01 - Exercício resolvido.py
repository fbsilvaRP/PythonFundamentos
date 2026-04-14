#Feito por Felipe Braga
#Última edição em 13 de abril de 2026
import random

vetor1 = []

tam = 9 #Tamanho de vetor

''' Preenchendo o vetor manualmente

#Preenchendo o vetor
for i in range(9):
    vetor1.append(int(input("Digite um número inteiro: ")))
    
'''
#Preenchendo o vetor com valores aleatórios inteiros
for i in range(tam):
    numero = random.randint(0, 100)
    vetor1.append(numero)

#Exibindo o vetor
print("-=" * 25)
print("Vetor obtido: ")
for j in range(tam):
    print(f"[{vetor1[j]}], ", end = '')
print("")
print("-=" * 25)

#Verificando se o número no vetor é primo
for k in range(tam):
    num = vetor1[k]
    acum = 0 
    for i in range(1, num + 1):
        if(num % i == 0):
            acum = acum + 1
    if(acum == 2):
        print(f"{vetor1[k]} é primo, e sua posição é {k + 1}", end = "\n")            

