class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurantes)
print(dir(restaurantes))
print(vars(restaurantes[0]))