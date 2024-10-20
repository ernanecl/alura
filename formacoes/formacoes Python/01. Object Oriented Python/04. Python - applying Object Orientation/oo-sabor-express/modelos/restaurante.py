from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliacao'.ljust(20)} | Status')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧ ativo' if self._ativo else '☐ ativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        if 0 <= avaliacao._nota <= 5:
            self._avaliacao.append(avaliacao)
            print(f'A avaliacao de {avaliacao._cliente} foi de {avaliacao._nota}')
        else:
            print(f'Avaliacao de {avaliacao._nota} nao valida, a avaliacao de {avaliacao._cliente} precisa ser de 0 a 5')

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 'Sem avaliacao'
        
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media_notas = round(soma_notas / quantidade_notas,1)

        return media_notas