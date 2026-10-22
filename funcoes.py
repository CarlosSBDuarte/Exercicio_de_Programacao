def define_posicoes(linha, coluna, orientacao, tamanho):
    resposta = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            local = []
            local.append(linha + i)
            local.append(coluna)
            resposta.append(local)
    if orientacao == 'horizontal':
        for i in range(tamanho):
            local = []
            local.append(linha)
            local.append(coluna + i)
            resposta.append(local)

    return resposta

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    if nome not in frota:
        frota[nome] = []
        navio = define_posicoes(linha, coluna, orientacao, tamanho)
        frota[nome].append(navio)
    else:
        navio = define_posicoes(linha, coluna, orientacao, tamanho)
        frota[nome].append(navio)

    return frota