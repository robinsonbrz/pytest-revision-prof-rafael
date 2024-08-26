from ..codigo.jogo import *

def test_quando_func_pense_num_numero_recebe_qualquer_valor_1_entao_retorna_3():
    qualquer = 65
    resposta =  pense_num_numero(qualquer)
    assert resposta == 3

def test_quando_func_pense_num_numero_recebe_qualquer_valor_2_entao_retorna_3():
    qualquer = 11
    resposta =  pense_num_numero(qualquer)
    assert resposta == 3

def test_quando_func_pense_num_numero_recebe_qualquer_valor_3_entao_retorna_3():
    qualquer = 9
    resposta =  pense_num_numero(qualquer)
    assert resposta == 3

def test_quando_func_pense_num_numero_recebe_qualquer_valor_4_entao_retorna_3():
    qualquer = 1
    resposta =  pense_num_numero(qualquer)
    assert resposta == 3
