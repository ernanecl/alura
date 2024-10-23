# EXERCICIO 1
print("1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.")
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurantes)
print(dir(restaurantes))
print(vars(restaurantes[0]))

# EXERCICIO 2
print("\n2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.")

nome_do_restaurante = restaurante_praca.nome
print(nome_do_restaurante)

# EXERCICIO 3
print("\n3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.")

check1 = 'Restaurante esta ativo' if restaurante_praca.ativo == True else 'Nao esta ativo'
print(check1)

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

# EXERCICIO 4
print("\n4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.")

categoria = Restaurante()
print(Restaurante.categoria)

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

categoria1 = Restaurante.categoria
print(categoria1)

# EXERCICIO 5
print("\n5 - Altere o valor do atributo nome para 'Bistrô'.")

restaurante_praca.nome = 'Bistrô'
print(restaurante_praca.nome)

# EXERCICIO 6
print("\n6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.")

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

print(restaurante_pizza.nome)
print(restaurante_pizza.categoria)

# EXERCICIO 7
print("\n7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.")

check2 = f'O restaurante {restaurante_pizza.nome} é categoria Fast Food' if restaurante_pizza.categoria == 'Fast Food' else f'O restaurante {restaurante_pizza.nome} NAO é categoria Fast Food'
print(check2)

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

# EXERCICIO8
print("\n8 - Mude o estado da instância restaurante_pizza para ativo.")

print(f'O restaurante {restaurante_pizza.nome} esta com estado ativo como {restaurante_pizza.ativo}')

if restaurante_pizza.ativo == False:
    restaurante_pizza.ativo = True
    print(f'Agora o restaurante {restaurante_pizza.nome} esta com estado ativo como {restaurante_pizza.ativo}')
else:
    print(f"O restaurante {restaurante_pizza.nome} já está ativo")

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

restaurante_pizza.ativo = True

# EXERCICIO
print("\n9 - Imprima no console o nome e a categoria da instância restaurante_praca.")

print(restaurante_praca.nome)
print(restaurante_praca.categoria)

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')