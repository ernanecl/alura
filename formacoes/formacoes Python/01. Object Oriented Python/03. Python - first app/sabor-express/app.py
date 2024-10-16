import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_app():
    print('''
        Sabor Express      
        ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def voltar_ao_menu_principal():
    input('Digite qualquer tecla para voltar ao menu ')
    print()
    main()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante para cadastro: ')
    restaurantes.append(nome_restaurante)

    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso\n')

    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Encerrando App')

def opcao_invalida():
    exibir_subtitulo('Opcao invalida')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()