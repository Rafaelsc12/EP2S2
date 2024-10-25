def define_posicoes(linha, coluna, orientacao, tamanho):
    y=linha
    x=coluna
    lf=[]

    if orientacao=="vertical":
        while tamanho+linha>y:
            lf.append([y, x])
            y=y+1

    if orientacao=="horizontal":
        while tamanho+coluna>x:
            lf.append([y, x])
            x=x+1
    return lf

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    posicao = []
    posicao.append(define_posicoes(linha, coluna, orientacao, tamanho))
    if nome not in frota:
        frota[nome] = posicao
    else:
        indice = len(frota[nome]) - 1
        frota[nome] += posicao
        
    return frota
    
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    for navio in frota:
        for composicao in frota[navio]:
            for posicao in composicao:

                tabuleiro[posicao[0]][posicao[1]] = 1

    return tabuleiro