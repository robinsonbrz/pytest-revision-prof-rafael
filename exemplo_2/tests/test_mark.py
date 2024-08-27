from ..codigo.calculadora import soma

import pytest

@pytest.mark.parametrize(
    'entrada',
    [3, 5, 6, 8, 9 ,2]
)
def test_multiplas_somas(entrada):
    assert soma(entrada, entrada) == entrada + entrada

@pytest.mark.parametrize(
    'entrada, valor_esperado',
    [(2, 4), (7, 14), (1, 2), (9, 18), (3, 6)]
)
def test_multiplas_somas_tupla(entrada, valor_esperado):
    assert soma(entrada, entrada) == valor_esperado

@pytest.mark.parametrize(
    'entrada1, entrada2, valor_esperado',
    [(2, 4, 6), (7, 14, 21), (1, 2, 3), (9, 18, 27), (3, 6, 9)]
    )
def test_multiplas_somas_tupla2(entrada1, entrada2, valor_esperado):
    assert soma(entrada1, entrada2) == valor_esperado

@pytest.mark.xfail # Este teste deve falhar 
def test_deve_falhar_soma():
    entrada1 = 5
    entrada2 = 3
    valor_esperado = 7 # falhara
    assert soma(entrada1, entrada2) == valor_esperado
