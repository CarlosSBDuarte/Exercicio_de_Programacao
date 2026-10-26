from funcoes import posicao_valida, preenche_frota
qnt_tamanhos = {
    "porta-aviões":[1, 4],
    "navio-tanque":[2, 3],
    "contratorpedeiro":[3, 2],
    "submarino": [4, 1],
} 

frota = {}

for nome,info in qnt_tamanhos.items():
    for i in range(info[0]):
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {info[1]}')
        if nome == 'submarino':
            linha = int(input('linha:'))
            coluna = int(input('coluna:'))
            orientacao = 'vertical'
        else:
            linha = int(input('linha:'))
            coluna = int(input('coluna:'))
            orientacao = int(input('orientacao:'))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
        while posicao_valida(frota, linha, coluna, orientacao, info[1]) == False:
            print('Esta posição não está válida!')
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {info[1]}')
            if nome == 'submarino':
                linha = int(input('Qual a linha?'))
                coluna = int(input('Qual a coluna?'))
                orientacao = 'vertical'
            else:
                linha = int(input('Qual a linha?'))
                coluna = int(input('Qual a coluna?'))
                orientacao = int(input('Qual a orientacao?'))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'
        
        frota = preenche_frota(frota, nome, linha, coluna, orientacao, info[1])

print(frota)