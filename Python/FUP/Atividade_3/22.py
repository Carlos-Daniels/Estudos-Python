"""
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas
do chamado triangulo de Floyd. Para n = 6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
def traiangulo_floyd(n):
    num = 1 
    for i in range(1, n + 1):
        for j in range(1 , i + 1):
            print(num, end = " ")
            num += 1
        print()

#exemplo de uso
n = int(input("Digite o valor de n: "))
traiangulo_floyd(n)