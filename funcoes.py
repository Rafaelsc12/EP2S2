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
    lf=define_posicoes(linha, coluna, orientacao, tamanho)
    fita=frota
    listas=[]

    while True:

        if nome not in fita.keys():
            fita[nome]=lf
        else:
            listas.append([frota[nome], lf])
        fita[nome]=listas
        i=len(nome)+1
        if len(frota)+len(nome)==i:
            break
    return fita


