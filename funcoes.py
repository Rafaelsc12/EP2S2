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
