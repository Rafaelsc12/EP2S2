def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    y=linha
    x=coluna
    lf=[]
    fita={}
    if orientacao=="vertical":
        while tamanho+linha>y:
            lf.append([y, x])
            y=y+1

    if orientacao=="horizontal":
        while tamanho+coluna>x:
            lf.append([y, x])
            x=x+1
    while True:
        if nome not in frota.keys():
            fita=nome, lf
    return fita

frota = {}
nome_navio = 'navio-tanque'
linha = 6
coluna = 1
orientacao = 'horizontal'
tamanho = 3

resultado = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(resultado)