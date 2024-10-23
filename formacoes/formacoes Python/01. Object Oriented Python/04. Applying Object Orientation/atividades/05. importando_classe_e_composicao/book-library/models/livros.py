class Livro:
    lista_livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.lista_livros.append(self)

    def __str__(self):
        return f'O livro {self._titulo}, escrito por {self._autor}, publicado no ano de {self._ano_publicacao}'
    
    @classmethod
    def listar_livros(cls):
        print(f'{'Nome livro'.ljust(60)} | {'Autor'.ljust(60)} | {'Ano Publicacao'.ljust(60)} | Disponivel')

        for livro in cls.lista_livros:
            print(f'{livro._titulo.ljust(60)} | {livro._autor.ljust(60)} | {str(livro._ano_publicacao).ljust(60)} | {livro._disponivel}')

    @property
    def disponibilidade(self):
        return f'O livro {self._titulo}, escrito por {self._autor}, publicado no ano de {self._ano_publicacao} esta disponivel' if self._disponivel else f'O livro {self._titulo} esta indisponivel'
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.lista_livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                livros_disponiveis.append(livro)
        return f'{livros_disponiveis}'
