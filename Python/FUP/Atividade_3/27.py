"""
Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial
exponencial desse número. Um fatorial exponencial é um inteiro positivo n elevado à
potência de n − 1 , que por sua vez é elevado à potência de n − 2 e assim por diante. Ou seja:
n (n−1)^(n−2)^···^1
"""
def fatorial_exponencial(n):
    if n == 0 or n == 1:
        return 1 
    resultado = 1
    for i in range (n, 0, -1):
        resultado = i ** resultado

    return resultado

#exemplo de uso
n = int(input("Digite o numero ineiro positivo n: "))
resultado = fatorial_exponencial(n)
print(f" fatorial exponencial de {n} é : {resultado}")