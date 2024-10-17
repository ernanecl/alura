# EXERCICIO 1
print('1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.')

personal_data = {'Name':'Zahira','Age':'25 years old','City':'Ajman'}
print(f'\n{personal_data['Name']}\n{personal_data['Age']}\n{personal_data['City']}\n')
print(personal_data.keys())
print(personal_data.values())

# Imprimindo todas as chaves
print('\nTodas as chaves:', personal_data.keys())

# Convertendo para lista
key_list = list(personal_data.keys())
print("\nLista de chaves:", key_list)

# Iterando sobre as chaves e valores
for key, value in personal_data.items():
    print(f"\n{key}: {value}")

################################################################################################################

# EXERCICIO 2
print('''
      2 - Utilizando o dicionário criado no item 1:
      Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
      Adicione um campo de profissão para essa pessoa;
      Remova um item do dicionário.
      ''')

personal_data.update({'Age' : '29 years old'})

for key, value in personal_data.items():
    print(f"\n{key}: {value}")

print('\n#############################################################################\n')

personal_data.update({'Profession' : 'Businesswoman'})
personal_data['Height'] = 1.72

for key, value in personal_data.items():
    print(f"\n{key}: {value}")

print('\n#############################################################################\n')

del personal_data['Height']
personal_data['Weight'] = ''

for key, value in personal_data.items():
    print(f"\n{key}: {value}")

################################################################################################################

# EXERCICIO 3
print('3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.')

for x in range(1, 6, +1):
    numbers_and_their_squares = {f'Number: {int(x)}':f'Number squared: {int(x*x)}'}

    for key, value in numbers_and_their_squares.items():
        print(f"\n{key} | {value}")

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

################################################################################################################

# EXERCICIO 4
print('4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.')

profiles = [{'Name':'Zahira','Age':'29 years old','City':'Ajman','Profession' : 'Businesswoman','Height':1.73},
            {'Name':'Aada','Age':'20 years old','City':'Kazan','Profession':'Aeronautical Engineer'},
            {'Name':'Raissa','Age':'27 years old','City':'Oulu','Profession':'Doctor'},
            {'Name':'Sofia','Age':'33 years old','City':'Merida','Profession':'Professional Cook'}
]

profile1 = profiles[1]
check1 = 'key exists' if 'Profession' in profile1 else 'key does not exists'

print(type(profile1))
print(profile1)
print(check1)

################################
#OUTRAS SOLUCOES PARA A QUESTAO#
################################

##########
#METODO 1#
##########
profile2 = profiles[0]

if 'Height' in profile2:
    print('\n\nA chave "Height" existe no dicionário.')
    print(f'{profile2}\n\n')
else:
    print('\n\nA chave "Height" não existe no dicionário.')
    print(f'{profile2}\n\n')


##########
#METODO 2#
##########
profile3 = profiles[2]

check2 = profile3.get('Profession', 'No infortion')
print(check2)  # Saída: Não informada (já que a chave 'profissao' não existe)
print(f'{profile3}\n\n')

##########
#METODO 3#
##########
profile4 = profiles[3]

try:
    check3 = profile4['Profession']
    print(check3)
except KeyError:
    print("A chave 'Profession' não existe.")

################################################################################################################

# EXERCICIO 5
print('5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.')


def count_words(phrase):
    '''
    Args:
    professional_profile: A frase a ser analisada.

    Returns:
    Um dicionário onde as chaves são as palavras e os valores são as suas frequências.
    '''

    # Limpa a frase, removendo pontuação e convertendo para minúsculas
    words = phrase.lower().split()

    # Cria um dicionário para armazenar as frequências
    frequency = {}

    # Itera sobre cada palavra e incrementa a contagem no dicionário
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Exemplo de uso:
phrase = 'Professional Profile: Eu me chamo Aada, sou uma profissional altamente qualificada em projeto, desenvolvimento e análise de aeronaves, com sólidos conhecimentos em aerodinâmica, estruturas e sistemas aeronáuticos. Engenheira aeronáutica especialista em design, desenvolvimento e análise de aeronaves. Graduada em Engenharia Aeronáutica com conhecimentos em aerodinâmica, estruturas e sistemas aeronáuticos.'
result = count_words(phrase)
print(result)


#############################
#OUTRO METODO PARA A QUESTAO#
#############################

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)