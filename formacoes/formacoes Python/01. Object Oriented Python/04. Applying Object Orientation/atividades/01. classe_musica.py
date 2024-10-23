class Musica:
    nome = ''
    artista = ''
    genero = ''

music1 = Musica()
music1.nome = 'What I have Done'
music1.artista = 'Linkin Park'
music1.genero = 'Rock'

music2 = Musica()
music2.nome = 'Animals'
music2.artista = 'Martin Garrix'
music2.genero = 'Eletronic'

music3 = Musica()
music3.nome = 'Perfect'
music3.artista = 'Ed Sheeran'
music3.genero = 'Pop'

musicas = [music1, music2, music3]

print(musicas)
print(dir(musicas))
print(vars(musicas[0]))
print(vars(musicas[1]))
print(vars(musicas[2]))

class Musica2:
    def __init__(self, nome2='', artista2='', genero2=0):
        self.nome2 = nome2
        self.artista2 = artista2
        self.genero2 = genero2

musica4 = Musica(nome2='Eyes Closed', artista2='Imagine Dragons', genero2='Rock')
musica5 = Musica(nome2='Bangarang', artista2='Skrillex', genero2='Eletronic')
musica6 = Musica(nome2='Marry you', artista2='Bruno Mars', genero2='Pop')