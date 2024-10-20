from models.livros import Livro

livro_hp4 = Livro('Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000)
livro_sa2 = Livro("O Senhor dos Anéis - As Duas Torres", "J.R.R. Tolkien", 1954)
livro_hp1 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)
livro_sa3 = Livro('O Senhor dos Anéis - O Retorno do Rei', 'J.R.R. Tolkien', 1955)
livro_gt5 = Livro('As Crônicas de Gelo e Fogo - A Dança dos Dragões', 'George R.R. Martin', 2011)

print(livro_hp4)

livro_hp4.emprestar()
print(livro_hp4)

livros_2000 = Livro.verificar_disponibilidade(2000)
print(livros_2000)

Livro.listar_livros()
print(livro_hp4.disponibilidade)