import pytest
from calculadora import soma, subtracao, multiplicacao, divisao
from matematica_avancada import potencia, raiz_quadrada, fatorial

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(1, 1) == 0
    assert subtracao(0, 5) == -5

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-1, 1) == -1
    assert multiplicacao(0, 5) == 0

def test_divisao():
    assert divisao(6, 3) == 2
    assert divisao(5, 2) == 2.5
    assert divisao(0, 5) == 0
    assert divisao(5, 0) == "Erro: Divisão por zero"

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(0, 5) == 0

def test_raiz_quadrada():
    assert raiz_quadrada(4) == 2
    assert raiz_quadrada(0) == 0
    assert raiz_quadrada(-1) == "Erro: Não é possível calcular raiz de número negativo"

def test_fatorial():
    assert fatorial(3) == 6
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(-1) == "Erro: Não é possível calcular fatorial de número negativo"