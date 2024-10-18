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