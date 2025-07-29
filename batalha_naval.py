# Criação do tabuleiro 5x5
tabuleiro = [['~' for _ in range(5)] for _ in range(5)]

# Posiciona navios manualmente (exemplo: 3 posições horizontais e 3 verticais)
# Horizontal no topo
tabuleiro[0][0] = 'N'
tabuleiro[0][1] = 'N'
tabuleiro[0][2] = 'N'

# Vertical na coluna 4
tabuleiro[1][4] = 'N'
tabuleiro[2][4] = 'N'
tabuleiro[3][4] = 'N'

acertos = 0

print("Bem-vindo à Batalha Naval (Nível Novato)!")
print("Você deve acertar os navios escondidos.")

# Rodadas de ataque
for tentativa in range(6):
    print("\nTabuleiro:")
    for linha in tabuleiro:
        print(' '.join(['~' if cel != 'X' and cel != '*' else cel for cel in linha]))

    linha = int(input("Escolha a linha (0 a 4): "))
    coluna = int(input("Escolha a coluna (0 a 4): "))

    if tabuleiro[linha][coluna] == 'N':
        print("💥 Acertou!")
        tabuleiro[linha][coluna] = 'X'
        acertos += 1
    elif tabuleiro[linha][coluna] in ['X', '*']:
        print("⚠️ Já atacou aqui!")
    else:
        print("🌊 Errou!")
        tabuleiro[linha][coluna] = '*'

print(f"\nFim de jogo! Total de acertos: {acertos}")
