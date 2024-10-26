from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida

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
                print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
                
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
                
                if nome != "submarino":
                    orientacao = int(input("Orientação (1-Vertical, 2-Horizontal): "))
                    orientacao = "vertical" if orientacao == 1 else "horizontal"
                else:
                    orientacao = "vertical"
                
                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                    break
                else:
                    print("Esta posição não está válida!")

    print(frota)

posiciona_frota_jogador()
