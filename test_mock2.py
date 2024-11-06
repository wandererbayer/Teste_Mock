import requests

#função faz cahamda de API (exemplo)
def obter_dados_da_api(url):
    resposta = requests.get(url)
    return resposta.json()

def test_obter_dados_da_api(mocker):
    #mockando a resposta da função request.get
    mock_response = mocker.patch('requests.get')
    #definindo um retorno ficticio para o mock
    mock_response.return_value.json.return_value = {"id": 1, "nome": "Teste"}
    #testando a função com o mock
    resultado = obter_dados_da_api("http://api.exemplo.com/dados")
    #verificando se o resultado é o esperado
    assert resultado == {"id": 1, "nome": "Teste"}