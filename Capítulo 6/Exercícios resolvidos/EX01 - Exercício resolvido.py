#Feito por Felipe Braga
#Última edição em 13 de abril de 2026

vetor1 = []

#Preenchendo o vetor
for i in range(9):
    vetor1.append(int(input("Digite um número inteiro: ")))

#Exibindo o vetor
print("-=" * 25)
print("Vetor obtido: ")
for j in range(9):
    print(f"[{vetor1[j]}], ", end = '')
print("")
print("-=" * 25)
