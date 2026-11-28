# -*- coding: utf-8 -*-
# fase2_caminhos.py — Fase 2: funções, custo de um caminho e os valores g, h e f.
# Rode com: python fase2_caminhos.py

# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: função que devolve o custo de UMA estrada -----
# DEF inicia uma FUNÇÃO (uma receita esperando para ser usada),
#    com os parametros informados por quem chama a FUNÇÃO, que 
#    é um conjunto de código que só vai executar caso for chamado
#    pelo seu nome que foi definido depois de DEF.
# Algo como:
#   FUNÇÃO - NOME_DA_FUNÇÃO (PARAMETROS)
#   DEF - CUSTO_DA_ESTRADA(ORIGEM, DESTINO)
# nesse caso, informa que os dois nomes de cidades
#    encaminhados por quem chamou a função, criando
#    as variáveis ORIGEM e DESTINO e atribuindo a elas
#    os nomes que serão usados de referência para fazer uma
#    busca no DICIONÁRIO>MAPA_ROMENIA

def custo_da_estrada(origem, destino):
# """...""" logo na primeira linha da função é chamado de docstring. Um comentário
#   oficial que explica o que a função faz
#
    """Devolve os km da estrada origem -> destino, ou None se ela não existe."""
# 
# cenário caso a origem seja ARAD, o FOR vai DESEMPACOTAR a primeira TUPLA e atribuir:
# PARA VIZINHO (ZERIND), custo (75) no MAPA_ROMENIA[ARAD]:
# 
# TOda vez que rodar o FOR, ele vai desempacotar para o IF abaixo comparar
#   se é o que foi definido nos parametros da FUNÇÃO CUSTO_DA_ESTRADA
    for vizinho, custo in mapa_romenia[origem]:
        # SE VIZINHO == DESTINO (ZERID - caso o parametro DESTINO fosse definido no
        # momento que chamar a função)
        if vizinho == destino:
            # VIZINHO = DESTINO, retorne o CUSTO (75 - segundo item da TUPLA do
            #   primeiro item da LISTA da primeira CHAVE nomeada ARAD)
            return custo
            # caso VIZINHO e DESTINO não sejam iguais, o programa volta para o FOR lá
            #    em cima e passa para o próximo vizinho (SIBIU - nesse exemplo aqui)
            #    e iria comparar novamente até VIZINHO ser igual DESTINO e retornar
            #    o valor do segundo item da TUPLA (140)
    # esse para caso não encontrar o destino, não retornar nada
    return None

# ----- PASSO 3: função que soma o custo de um caminho inteiro -----
def custo_do_caminho(caminho):
    """Recebe uma lista de cidades e devolve a soma das estradas, em km."""
    # iniciando a FUNÇÃO com a variável TOTAL recebendo 0, para servir de
    #    acumulador e ir somando os km do caminho a partir do zero.
    total = 0
    #
    # iniciando o FOR com a variável I usando RANGE (ferramenta nativa do
    #    Python que gera uma sequência de NÚMEROS INTEIROS começando do 0).
    # Aqui, CAMINHO é uma LISTA simples só com os nomes das cidades da viagem
    #    (ex: ['Arad', 'Sibiu', 'Fagaras', 'Bucharest'] -> 4 cidades).
    # Usamos len(caminho) - 1 porque entre 4 cidades existem apenas 3 estradas,
    #    então o range(3) faz o I valer 0, depois 1 e depois 2.
    for i in range(len(caminho) - 1):
        # o FOR já avança o I sozinho a cada volta.
        # Aqui pegamos a cidade atual (caminho[i]) e a próxima cidade da LISTA
        #    (caminho[i + 1]) para chamar a FUNÇÃO custo_da_estrada e somar
        #    os KM devolvidos dentro da variável TOTAL.
        total = total + custo_da_estrada(caminho[i], caminho[i + 1])
    # e aqui ele retorna apenas o TOTAL que a variável ficou ao final do loop
    return total


# ----- PASSO 4: testar as funções -----
# Na primeira linha, o print chama a função custo_da_estrada e envia para ela
#    os parametros ARAD e SIBIU, que ao finalizar a função vai trazer o valor
#    dos km para sair de ARAD e ir até SIBIU
#
# Na segunda linha, o print chama a mesma função, porém com o parametro
#    BUCHAREST e retornando, nesse caso, o valor de NONE e que não
#    existe estrada direta

print('Arad -> Sibiu custa', custo_da_estrada('Arad', 'Sibiu'), 'km')
print('Arad -> Bucharest custa', custo_da_estrada('Arad', 'Bucharest'), '(não existe estrada direta)')

# cria a variavel POR_FAGARAS é tipo LISTA, com os dados ja definidos
# mesma coisa a variável POR_PITESTI

por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']

print()
# o comando JOIN junta todo o texto dentro de uma LISTA e junta tudo
#    em uma única frase só, adicionando '->' entre cada texto
# e no segundo PRINT chama a FUNÇÃO CUSTO_DO_CAMINHO, enviando e LISTA
#    POR_FAGARAS para exibir a distancia desse caminho
# Os outros dois PRINT's faz o mesmo, só que usando a LISTA
#    POR_PITESTI
print('Caminho por Fagaras:', ' -> '.join(por_fagaras))
print('  custo =', custo_do_caminho(por_fagaras), 'km')
print('Caminho por Pitesti:', ' -> '.join(por_pitesti))
print('  custo =', custo_do_caminho(por_pitesti), 'km')


# ----- PASSO 5: g(n), h(n) e f(n) ao longo de um caminho -----
# Aqui vamos fazer uma nova FUNÇÃO, chamada MOSTRAR_G_H_F, onde
#    G (Já andado), H(Qnto falta) e faz o calculo F = G + H
def mostrar_g_h_f(caminho):
    """Para cada cidade do caminho imprime g (já andado), h (falta) e f = g + h."""
# Usando o RANGE + LEN para determinar a qntd de LOOPS do FOR,
#    sem usar -1, pois queremos exibir todas as cidades do caminho
    print(f'  {"cidade":<15} {"g(n)":>5} {"h(n)":>5} {"f(n)":>5}')
    for i in range(len(caminho)):
        cidade = caminho[i]
        g = custo_do_caminho(caminho[:i + 1])
        h = heuristica_bucareste[cidade]
        f = g + h
        print(f'  {cidade:<15} {g:>5} {h:>5} {f:>5}')


print()
# Senti necessidade de adicionar esse PRINT abaixo
# para entender melhor cada 
print("G (Já andado), H(Qnto falta) e F = G + H")
print()
print('Valores ao longo do caminho por Fagaras:')
mostrar_g_h_f(por_fagaras)
print()
print('Valores ao longo do caminho por Pitesti:')
mostrar_g_h_f(por_pitesti)