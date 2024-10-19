'''
OPCOES DE CONDICIONAIS


def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if tempo < 25:
        print("Valor muito baixo. Configure um tempo maior ou igual a 25 minutos.")
    elif tempo > 45:
        print("Valor muito alto. Configure um tempo menor ou igual a 45 minutos.")
    else:
        print("Tempo configurado para", tempo, "minutos.")


def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if 25 <= tempo <= 45:
        print("Tempo configurado para", tempo, "minutos.")
    else:
        print("Valor inválido. Configure um tempo entre 25 e 45 minutos.")

##############################################################################################
        
numero = -1

try:
    for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
        numero = int(input("\nDigite um número positivo: "))
        print('\nnumero(s) invalido(s), numero(s) menor(es) que zero\n')
        
        if numero > 0:
            print(f'Você digitou: {numero}\n')
            break
except:
    print('\nopcao invalida')


numero = -1

try:
    while numero <= 0:
        numero = int(input("Digite um número positivo: "))
        
    print("Você digitou:", numero)

except:
    print('\nopcao invalida')

##############################################################################################

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

try:
  for projeto in projetos:
    print(f"Projeto: {projeto}")
except Exception as e:
  print("Ocorreu um erro:", e)


for i in range(len(projetos)):
  try:
    print(f"Projeto: {projetos[i]}")
  except IndexError:
    print("Índice fora do alcance.")


for projeto in projetos:
  if projeto:
    print(f"Projeto: {projeto}")
  else:
    print("Projeto não disponível.")


for projeto in projetos:
  try:
    print(f"Projeto: {projeto}")
  except TypeError:
    print("Projeto não disponível.")

    
##############################################################################################

encomendas = input("Digite os números das encomendas: ")
for encomenda in encomendas:
    print(encomenda)

encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
    print("Uma das entradas não é um número válido.")

encomendas = [123, 456, 789]
for encomenda in encomendas:
    print(encomenda)


encomendas = [123, "456", 789]
for i in range(len(encomendas)):
    try:
        print(int(encomendas[i]))
    except ValueError:
        print(f"A encomenda {encomendas[i]} não é um número válido.")


try:
    encomendas = []
    for i in range(3):
        encomendas.append(input(f"Digite o número da encomenda {i+1}: "))
except Exception as e:
    print(f"Erro: {e}")

##############################################################################################

livro = {
    'titulo': 'Aprendendo Python',
    'autor': 'Fabrício Silva',
    'ISBN': '12345',
    'preco': 59.90,
    'em_estoque': True
}

print(livro)

livro['preco'] = 69.90

print(livro)

livro.update({'preco' : 79.90})

print(livro)

livro.get('preco', 89.90)

print(livro)


##############################################################################################

credenciais_clientes = {
    'alice123': {'username': 'alice123', 'password': 'alic3P@ssw0rd', 'status': 'active'},
    'bob456': {'username': 'bob456', 'password': 'b0bP@ssword!', 'status': 'inactive'},
    'charlie789': {'username': 'charlie789', 'password': 'Ch@rlieP@ss9', 'status': 'active'}
}

# verificar o status de um usuário chamado 'bob456' e, caso esteja inativo, enviar um alerta.

alerta = 'Enviar alerta!' if credenciais_clientes['bob456']['status'] == 'inactive' else 'Sem alerta'
print(alerta)



##############################################################################################

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Alice", 30)
print(dir(pessoa1))
print(vars(pessoa1))


##############################################################################################


class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.duracao = 355

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')

##############################################################################################


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Pessoa: {self.nome}, {self.idade} anos"

    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', idade={self.idade})"

pessoa1 = Pessoa("Sofia", 30)
print(pessoa1)  # Saída: Pessoa: Sofia, 30 anos
print(repr(pessoa1))  # Saída: Pessoa(nome='Sofia', idade=30)


##############################################################################################

'''