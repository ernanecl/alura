'''
OPCOES DE CONDICIONAIS


def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if tempo < 25:
        print("Valor muito baixo. Configure um tempo maior ou igual a 25 minutos.")
    elif tempo > 45:
        print("Valor muito alto. Configure um tempo menor ou igual a 45 minutos.")
    else:
        print("Tempo configurado para", tempo, "minutos.")


def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if 25 <= tempo <= 45:
        print("Tempo configurado para", tempo, "minutos.")
    else:
        print("Valor inválido. Configure um tempo entre 25 e 45 minutos.")
'''

