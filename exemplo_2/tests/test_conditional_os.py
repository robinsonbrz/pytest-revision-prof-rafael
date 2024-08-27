from ..codigo.calculadora import *
import sys

import pytest

@pytest.mark.xfail(sys.platform == 'win32', reason='Não funciona na plataforma Windows')
def test_soma_que_vai_falhar_windows_3():
    print("Teste de falha no windows")
    print(sys.platform)
    assert soma(2, 2) == 4

# Deve falhar no linux
@pytest.mark.xfail(sys.platform == 'linux', reason='Não funciona na plataforma Linux')
def test_soma_que_deve_falhar_linux_3():
    print("Teste de falha no Linux")
    print("_________________________Sistema operacional Linux: " + sys.platform)
    assert soma(2, 2) == 4

@pytest.mark.xfail
def test_soma_que_vai_falhar_2():
    assert soma(2, 2) == 5

# condições lógicas de teste
@pytest.mark.skipif(sys.platform == 'linux', reason='Não funciona na plataforma Linux')
def test_soma_que_deve_pular_no_linux():
    print("Não deve executar em linux Linux")
    assert soma(2, 2) == 4

# condições lógicas de teste
@pytest.mark.skipif(sys.platform == 'win32', reason='Não funciona na plataforma Windows')
def test_soma_que_deve_pular_no_windows():
    print("Não deve executar em Windows")
    assert soma(2, 2) == 4
