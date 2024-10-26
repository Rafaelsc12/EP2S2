from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


def posiciona_frota_jogador():
    frota = {
        "porta-aviões": [],
        "navio-tanque": [],
        "contratorpedeiro": [],
        "submarino": []
    }
    
    tamanhos_navios = {
        "porta-aviões": 4,
        "navio-tanque": 3,
        "contratorpedeiro": 2,
        "submarino": 1
    }

    for nome, tamanho in tamanhos_navios.items():
        quantidade = 1 if nome == "porta-aviões" else (2 if nome == "navio-tanque" else (3 if nome == "contratorpedeiro" else 4))
        for _ in range(quantidade):
            while True:
                try:
                    print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
                    
                    linha = int(input("Linha (0-9): "))
                    coluna = int(input("Coluna (0-9): "))
                    
                    if not (0 <= linha <= 9 and 0 <= coluna <= 9):
                        print("Coordenadas fora dos limites! Por favor, insira valores entre 0 e 9.")
                        continue
                    
                    if nome != "submarino":
                        orientacao = int(input("Orientação (1-Vertical, 2-Horizontal): "))
                        if orientacao not in [1, 2]:
                            print("Orientação inválida! Por favor, insira 1 para Vertical ou 2 para Horizontal.")
                            continue
                        orientacao = "vertical" if orientacao == 1 else "horizontal"
                    else:
                        orientacao = "vertical"
                    
                    if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                        break
                    else:
                        print("Esta posição não está válida!")
                except ValueError:
                    print("Por favor, insira um número válido!")
    return frota


frota_oponente = {
    'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],
    'navio-tanque': [[[6, 0], [6, 1], [6, 2]], [[4, 3], [5, 3], [6, 3]]],
    'contratorpedeiro': [[[1, 6], [1, 7]], [[0, 5], [1, 5]], [[3, 6], [3, 7]]],
    'submarino': [[[2, 7]], [[0, 6]], [[9, 7]], [[7, 6]]]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
frota_jogador = posiciona_frota_jogador()
tabuleiro_jogador = posiciona_frota(frota_jogador)
jogadas_anteriores = set()
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    
    while True:
        try:
            linha = int(input("Informe a linha para atacar (0-9): "))
            if 0 <= linha <= 9:
                break
            else:
                print("Linha inválida! Por favor, insira um valor entre 0 e 9.")
        except ValueError:
            print("Por favor, insira um número válido!")

    while True:
        try:
            coluna = int(input("Informe a coluna para atacar (0-9): "))
            if 0 <= coluna <= 9:
                break
            else:
                print("Coluna inválida! Por favor, insira um valor entre 0 e 9.")
        except ValueError:
            print("Por favor, insira um número válido!")

    if (linha, coluna) in jogadas_anteriores:
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente! Por favor, escolha outra posição.")
        continue
    else:
        jogadas_anteriores.add((linha, coluna))
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == sum(len(navio) for navio in frota_oponente.values()):
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
