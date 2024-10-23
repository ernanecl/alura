from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5, 'grande')
prato_pao = Prato('Pao', 2, 'Melhor pao da cidade')

bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()

restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_pao)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()