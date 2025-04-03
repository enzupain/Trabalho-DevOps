import math

def potencia(base, expoente):
    return base ** expoente

def raiz_quadrada(numero):
    if numero < 0:
        return "Erro: Não é possível calcular raiz de número negativo"
    return math.sqrt(numero)

def fatorial(n):
    if n < 0:
        return "Erro: Não é possível calcular fatorial de número negativo"
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)