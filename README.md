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
-m          # utiliza marcadores tipo decorator import pytest 
    - decorar método teste com @pytest.markmarcadorpersonalizado
    - para executar: pytest -m "marcadorpersonalizado"
    - pode-se colocar not na string para não executar 

    @pytest.markskip          #  pula teste com essa marcação
    @pytest.markskipif        # pula em determinado contexto
    @pytest.markxfail         # espera falha no método (somente positivo se falhar)
    @pytest.markuserfixture   # 
    @pytest.markparametrize   # avaliar diversos parametros

``` python

import pytest 

@pytest.markparametrize(
    'entrada',
    [3, 5, 6, 8, 9 ,2]
)
def test_multiplas_somas(entrada):
    assert soma(entrada, entrada) == entrada + entrada


```

--pdb       # interrompe o código no primeiro erro, e assume modo debug para avaliar variáveis e debug
-s          # show standard output - exibe prints 


## Coverage

```
pip install pytest-cov
python -m pytest --cov-report html --cov .


pytest --cov    # para saber a cobertura dos testes

pytest --cov=codigo tests  # para pegar apenas os arquivos do código

pytest --cov=codigo tests --cov-report term-missing

pytest --cov=codigo .\tests\ --cov-report html



```


### Removendo warnings

devemos criar um arquivo chamado **pytest.ini** na raiz

```
[pytest]
filterwarnings =
    error
    ignore::UserWarning

```





___

# Mocking

Mock objects that simulate access of external APIs for example.

That we don't want to access externally, or we don't want to make external requests.

Maybe mail servers, external databases, external APIs
