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

restaurante_praca.receber_avaliacao('Aada', 8)
restaurante_praca.receber_avaliacao('Raissa', 1.5)

restaurante_arabe.receber_avaliacao('Zahira', 9.9)
restaurante_arabe.receber_avaliacao('Emma', 7)
                   
restaurante_mexicano.receber_avaliacao('Sofia', 7.5)
restaurante_mexicano.receber_avaliacao('Caitlyn', 6.75)
restaurante_mexicano.receber_avaliacao('Elizabeth', 8.4)
                                       
restaurante_brasileiro.receber_avaliacao('Chloe', 4)
restaurante_brasileiro.receber_avaliacao('Charlotte', 5.25)

restaurante_alemao.receber_avaliacao('Emily', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()