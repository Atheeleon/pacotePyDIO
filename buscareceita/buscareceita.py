import requests

def busca(cnpj):

    url = f"https://minhareceita.org/{cnpj}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    cliente = response.json()
    print(cliente)
    if 'message' in cliente:
        dados = {
            'cnpj': cnpj,
            'razao': 'nao encontrado',
            'nome': '',
            'cidade': '',
            'uf': '',
            'bairro': '',
            'rua': '',
            'numero': '',
            'email': '',
            'telefone 1': '',
            'telefone 2': '',
            'segmento': '',
            'cadastro': '',
            'matriz/filial': '',
        }
        return dados