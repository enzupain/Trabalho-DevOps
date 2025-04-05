import pytest
from calculadora import soma, subtracao, multiplicacao, divisao
from matematica_avancada import potencia, raiz_quadrada, fatorial

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    
def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(3, 5) == -2
    
def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-2, 3) == -6
    
def test_divisao():
    assert divisao(6, 3) == 2
    assert divisao(5, 2) == 2.5
    assert divisao(5, 0) == "Erro: Divisão por zero"
    
def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(2, 0) == 1
    
def test_raiz_quadrada():
    assert raiz_quadrada(4) == 2
    assert raiz_quadrada(0) == 0
    assert raiz_quadrada(-1) == "Erro: Não é possível calcular raiz de número negativo"
    
def test_fatorial():
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(5) == 120
    assert fatorial(-1) == "Erro: Não é possível calcular fatorial de número negativo"
