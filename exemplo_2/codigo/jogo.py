from .calculadora import *

def pense_num_numero(num):
    passo_0 = num + 5
    passo_1 = passo_0 * 2
    passo_2 = passo_1 - 4
    passo_3 = passo_2 / 2
    passo_4 = passo_3 - num
    return passo_4


def pense_num_numero2(num):
    return subtracao(divisao(subtracao(multiplicacao(soma(num,5),2),4),2),num)
    
