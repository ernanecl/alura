import os

restaurantes = [{'nome':'Praca', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Arabe', 'ativo':False}]

def exibir_nome_app():
    '''Exibe o nome do app na tela'''

    print('''
        Sabor Express      
        ''')

def exibir_opcoes():
    '''Exibi os itens disponiveis no menu principal'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    '''Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    
    input('\nDigite qualquer tecla para voltar ao menu ')
    print()
    main()
    
def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    - Ativo

    Output:
    - Adiciona novo restaurante, categoria e estado a lista de restaurante
    '''
    
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante para cadastro: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')

    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)

    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso\n')

    voltar_ao_menu_principal()

def listar_restaurante():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''

    exibir_subtitulo('Listando restaurantes')

    print(f'{' Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status do restaurante')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''

    exibir_subtitulo('Alternando estado restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')

    voltar_ao_menu_principal()

def finalizar_app():
    '''Essa função é responsável por encerrar o app'''

    exibir_subtitulo('Encerrando App')

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''

    exibir_subtitulo('Opcao invalida')
    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal que inicia o programa'''

    os.system('clear')
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()