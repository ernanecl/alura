import requests  # Importando a biblioteca requests para realizar requisições HTTP
import json # Importando o modulo json para trabalhar com dados em formato JSON

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'  # URL da API que contém os dados dos restaurantes
response = requests.get(url)  # Fazendo uma requisição GET para a URL e armazenando a resposta em 'response'

print(response)  # Imprimindo a resposta completa (para fins de depuração)

if response.status_code == 200:  # Verificando se a requisição foi bem-sucedida (código de status 200)
    dados_json = response.json()  # Convertendo a resposta JSON para um dicionário Python
    dados_restaurante = {}  # Criando um dicionário para armazenar os dados dos restaurantes, organizados por nome
    #print(dados_json)

    # Iterando sobre os dados JSON
    for item in dados_json: 
        nome_do_restaurante = item['Company'] # Obtendo o nome do restaurante a partir do item atual
        #contador += 1

        # Verificando se o restaurante já existe no dicionário
        if nome_do_restaurante not in dados_restaurante:
            # Se não existe, cria uma nova entrada no dicionário
            dados_restaurante[nome_do_restaurante] = []

        # Adiciona um novo item ao restaurante no dicionário
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

    print(dados_restaurante)  # Imprimindo o dicionário final com os dados dos restaurantes organizados por nome
else:
    print(f'O erro foi {response.status_code}')  # Imprimindo o código de status do erro caso a requisição falhe

# Iteração sobre o dicionário: Inicia um loop for para percorrer todas as chaves e valores do dicionário dados_restaurante.
# Desempacotamento: A cada iteração, a chave (nome do restaurante) é atribuída à variável nome_do_restaurante e o valor (lista de itens) é atribuído à variável dados.
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json' # string formatada (f-string) para o nome do arquivo, usando o nome do restaurante como base e adicionando a extensão .json
    # Abre um arquivo para escrita ('w') com o nome gerado anteriormente.
    # Gerenciamento de recursos: O with garante que o arquivo seja fechado corretamente, mesmo que ocorra alguma exceção.
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        # json.dump(): Função do módulo json que converte um objeto Python (no caso, a lista dados) em uma string JSON e a escreve em um arquivo.
        # dados: A lista de itens do restaurante atual.
        # arquivo_restaurante: O arquivo onde os dados serão escritos.
        # indent=4: Define a indentação do JSON para facilitar a leitura (opcional).
        json.dump(dados, arquivo_restaurante, indent=4)