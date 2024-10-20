from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_arabe = Restaurante('Al-Shabab', 'Arabe')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_brasileiro = Restaurante('bom de garfo', 'brasileiro')
restaurante_argentino = Restaurante('Ella', 'argentino')
restaurante_alemao = Restaurante('Munich', 'alemao')

restaurante_praca.alternar_estado()
restaurante_arabe.alternar_estado()
restaurante_mexicano.alternar_estado()
restaurante_brasileiro.alternar_estado()
restaurante_alemao.alternar_estado()

restaurante_praca.receber_avaliacao('Aada', 3)
restaurante_praca.receber_avaliacao('Raissa', 1.5)

restaurante_arabe.receber_avaliacao('Zahira', 2.9)
restaurante_arabe.receber_avaliacao('Emma', 3)
                   
restaurante_mexicano.receber_avaliacao('Sofia', 4.5)
restaurante_mexicano.receber_avaliacao('Caitlyn', 3.75)
restaurante_mexicano.receber_avaliacao('Elizabeth', 3.4)
                                       
restaurante_brasileiro.receber_avaliacao('Chloe', 4)
restaurante_brasileiro.receber_avaliacao('Charlotte', 4.25)

restaurante_alemao.receber_avaliacao('Emily', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()