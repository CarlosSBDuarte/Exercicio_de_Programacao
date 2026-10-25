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
    
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

def posiciona_frota(info_navio):

    tabuleiro_montado = []
    for i in range(10):
        tabuleiro_montado.append([0]*10)        
             
    for navios, posicoes in info_navio.items():
       for i in range(len(posicoes)):
           for j in range(len(posicoes[i])):
               pos = posicoes[i][j]
               tabuleiro_montado[pos[0]][pos[1]] = 1

    return tabuleiro_montado

def afundados(info_embarcacoes, tabuleiro_estado_atual):
    afundado = 0
    for navio, posicoes in info_embarcacoes.items():
        for i in range(len(posicoes)):
            contagem_X = 0
            for j in range(len(posicoes[i])):
                posi = posicoes[i][j]
                if tabuleiro_estado_atual[posi[0]][posi[1]] == 'X':
                    contagem_X += 1
                else: 
                    break
            if contagem_X == len(posicoes[i]):
                afundado += 1

    return afundado

def posicao_valida(posicoes_navios, linha, coluna, orientacao, tamanho):

    navio = define_posicoes(linha, coluna, orientacao, tamanho)

    for k in range(len(navio)):
        if navio[k][0] < 0 or navio[k][0] > 9 or navio[k][1] < 0 or navio[k][1] > 9:
            return False
    
    for navios, posicoes in posicoes_navios.items():
        for i in range(len(posicoes)):
            for j in range(len(posicoes[i])):
                pos = posicoes[i][j]
                for k in range(len(navio)):
                        if pos[0] == navio[k][0] and pos[1] == navio[k][1]:
                            return False
    

    return True
            
        
                            






