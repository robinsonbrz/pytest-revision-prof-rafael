from ..codigo.jogo import *
import pytest

class TestJogoFuncPenseNum:
    esperado = 3


    def test_quando_func_pense_num_numero_recebe_qualquer_valor_1_entao_retorna_3(self):
        qualquer = 65
        resposta =  pense_num_numero(qualquer)
        assert resposta == self.esperado

    def test_quando_func_pense_num_numero_recebe_qualquer_valor_2_entao_retorna_3(self):
        qualquer = 11
        resposta =  pense_num_numero(qualquer)
        assert resposta == self.esperado

    # Exceptions 
    def test_quando_func_pense_num_numero_recebe_valor_negativo_retorna_except(self):
        print("Exceção")
        qualquer = -1
        with pytest.raises(Exception):
            resposta =  pense_num_numero(qualquer)
            assert resposta == self.esperado


    def test_avalia_exception_da_func_pense_num_numero(self):
        num = -4
        with pytest.raises(Exception):
            retorno = pense_num_numero(num)
            assert retorno