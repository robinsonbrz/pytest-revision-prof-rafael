

from ..codigo.calculadora import *


def test_quando_soma_recebe4_e_3_entao_retorna_7_pindamon():
    entrada1 = 4 # given
    entrada2 = 3 # given
    resultado = soma(entrada1, entrada2) # when
    esperado = 7 # then
    assert resultado == esperado # Then

def test_quando_subtracao_recebe_2_1_entao_retorna_1():
    assert subtracao(2, 1) == 1


def test_quando_subtracao_recebe_3_1_entao_retorna_2():
    entrada1 = 3 # given
    entrada2 = 2 # given
    resultado = subtracao(entrada1, entrada2) # when
    esperado = 1 # then
    assert resultado == esperado # Then
