# -*- coding: utf-8 -*
# fase1_explorar.py — Fase 1: navegar nos dados, sem nenhuma busca ainda.
# Rode com:  python fase1_explorar.py

 
# ----- PASSO 1: trazer os dados do arquivo mapa.py ----
#
#do arquivo MAPA importe MAPA_ROMENIA e HEURISTICA_BUCARESTE
from mapa import mapa_romenia, heuristica_bucareste 

# ----- PASSO 2: quantas cidades existem? ----
#
# escreva na tela "Quantidade de cidade no mapa: X"
#   len(palavra reservada no python para ele entender que precisa contar
#   quantas CHAVEs (nesse caso, cidades) tem dentro do dicionário MAPA_ROMENIA)"
print('Quantidade de cidades no mapa:', len(mapa_romenia))

# escreve na tela "Quantidade de h(n): X"
print('Quantidade de valores de h(n):', len(heuristica_bucareste))


# ----- PASSO 3: olhar o valor guardado em uma CHAVE ----
# aqui cria uma variável chamada VIZINHOS_ARAD onde recebe os dados
#   que contém dentro da primeira CHAVE: ARAD, dentro do dicionário 
#   MAPA_ROMENIA, isso serve para ler uma CHAVE do dicionário
vizinhos_arad = mapa_romenia['Arad']

# mostra uma linha vazia, em branco. Serve para pular linha
print()

# aqui mostra na tela quais são os vizinhos da CHAVE ARAD
print('Vizinhos de Arad:', vizinhos_arad)

# aqui exibe o tipo que a variável VIZINHOS_ARAD é,
#   o que aqui nesse caso é uma variável do tipo LISTA,
#   que nesse caso é uma LISTA com TUPLAS (LISTAs que não mudam)
print('Tipo do valor:', type(vizinhos_arad))


# ----- PASSO 4: pegar uma tupla e as partes dela ----
#
# aqui vamos mostramos a distancia de Arad e seu primeiro vizinho
#
# criando a variável PRIMEIRA e atribuindo os dados da
# LISTA 0 em VIZINHOS_ARAD (que se tornou uma LISTA com TUPLAS)
primeira = vizinhos_arad[0]

# mostra uma linha vazia, em branco. Serve para pular linha
print()

# aqui mostra a TUPLA toda que o dicionario
# trouxe na POSIÇÃO 0 (é o primeiro item da LISTA)
print('Primeira estrada que sai de Arad:', primeira)

# para mostrar as infos dentro de cada TUPLA dentro 
# das LISTAS do dicionário, utiliza a variavel que trouxe
# o dado junto com a POSIÇÃO do dado que quer exibir:
#
# primeira[0] - exibe o primeiro dado dentro da
# POSIÇÃO 0 da TUPLA, dentro da LISTA 0, 
# dentro da CHAVE Arad, dentro do dicionário mapa_romenia
# dentro do arquivo mapa.py que foi carregado no começo
# do código.

# aqui exibe o dado da PRIMEIRA POSIÇÃO da TUPLA vizinhos_arad[0]
print('  POSIÇÃO [0] -> cidade vizinha:', primeira[0])
# e aqui exibe o dado da SEGUNDA POSIÇÃO da TUPLA.
print('  POSIÇÃO [1] -> custo em km   :', primeira[1])


# ----- PASSO 5: percorrer a LISTA com for e desempacotar ----
# para "percorrer" a LISTA, usamos FOR para repetir o bloco
# identado uma vez para cada item da LISTA, que contém TUPLAS.
# Como cada item é uma TUPLA de duas posições, da pra "desempacotar"
# usando FOR VIZINHO, CUSTO IN ... o que coloca a POSIÇÃO 0 em
# VIZINHO e a POSIÇÃO 1 em CUSTO, a cada volta. Isso ira
# se repetir até percorrer todas as estradas de uma cidade.

print()
print('Estradas que saem de Arad:')
# para VIZINHO, CUSTO no MAPA_ROMENIA[item ARAD]
# aqui estamos criando as variavel vizinho e custo
# e atribuindo a elas os valores dentro da CHAVE ARAD
# que é uma TUPLA com 2 itens: NOME e NUMERO
for vizinho, custo in mapa_romenia['Arad']:
    # aqui exibe na tela ARAD -> VIZINHO = X km
    print('  Arad ->', vizinho, '=', custo, 'km')



# ----- PASSO 6: percorrer o mapa inteiro ----
# aqui vamos usar o LEN novamente, mas para calcular 
# quantas estradas (vizinhos) cada cidade tem
# além de usar o FOR para que isso possa rodar
# isso de forma automática.
print()
print('Número de estradas de cada cidade:')
for cidade in mapa_romenia:
    quantidade = len(mapa_romenia[cidade])
    print(f'  {cidade:<15} {quantidade} estrada(s)')


# ----- PASSO 7: consultar a heurística -----
# heurística, nesse caso, o DICIONÁRIO heuristica_bucareste
# utilizando os mesmos comandos acima, aplicando nesse caso
print()
print('h(Arad) =', heuristica_bucareste['Arad'], 'km em linha reta até Bucareste')
print('Para cada vizinho de Arad: custo da estrada e h(vizinho)')
for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    # f' é para declarar que F é uma etiqueta avisando que tudo que estiver
    # dentro de { } nesse texto deve ser trocado pelo valor da variárvel
    # e VIZINHO:<10 quer dizer para reservar 10 espaços de largura a esquerda,
    # para o texto da variavel
    # nos outros casos, reserva 3 espaços a direita da variável custo etc.
    print(f'  {vizinho:<10} estrada = {custo:>3} km   h = {h:>3} km')

