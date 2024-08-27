# Estudo da library Pytest

Os testes devem testar pequenas unidades de teste

On nomes dos métodos de teste devem ser muito descritivos





Anatomia do teste - 3 etapas 

Padrão de Ivan Moore, popularizado por Dan North

Metodologia GWT:
Given - Dado
When - Quando
Then - Então

Arrange Act Assert: AAA

Arrange - Organiza  - Dado
Act Ação            - Quando
Assert Verifica     - Assert

TDD Kent Beck - One Step Test


# Executando 

pytest .  # executa todos testes nas pastas a partir de .

pytest <nome-do-arquivo>                # executa apenas o arquivo
pytest <nome-do-arquivo>::<nome-metodo> # executa apenas o método do arquivo


# Flags pytest

-v          #  verbose
-x          #  interrompe ao encontrar primeiro erro
--tb=no     # Traceback print mode (auto/long/short/line/native/no)
-k          # apenas métodos de testes com nome que contenha a string 
-m          # utiliza marcadores tipo decorator from pytest import mark 
    - decorar método teste com @mark.marcadorpersonalizado
    - para executar: pytest -m "marcadorpersonalizado"
    - pode-se colocar not na string para não executar 

    @mark.skip          #  pula teste com essa marcação
    @mark.skipif        # pula em determinado contexto
    @mark.xfail         # espera falha no método (somente positivo se falhar)
    @mark.userfixture   # 
    @mark.parametrize   # avaliar diversos parametros

``` python

from pytest import mark 

@mark.parametrize(
    'entrada',
    [3, 5, 6, 8, 9 ,2]
)
def test_multiplas_somas(entrada):
    assert soma(entrada, entrada) == entrada + entrada


```

--pdb       # interrompe o código no primeiro erro, e assume modo debug para avaliar variáveis e debug
-s          # show standard output - exibe prints 


--cov=      g# 







___

# Mocking

Mock objects that simulate access of external APIs for example.

That we don't want to access externally, or we don't want to make external requests.

Maybe mail servers, external databases, external APIs
