# -*- coding: utf-8 -*
# desafio1.py — Desafio 1: fazer um arquivo separado onde:
    # 1. Imprima as cidades que têm exatamente 1 estrada (resposta: Giurgiu, Eforie e Neamt).
    # 2. Imprima as cidades com h(n) menor que 200 km.
    #       Dica: for cidade in heuristica_bucareste:
    #           e um if.
    # 3. Descubra qual é a estrada mais longa do mapa (resposta: Fagaras–Bucharest, 211 km).

# começa importando o mapa e a heuristica, dentro do arquivo MAPA
from mapa import mapa_romenia, heuristica_bucareste
#---------------------------------------EXERCICIO 1---------------------------------------#
print("Que contem exatamente 1 estrada:")
for cidade in mapa_romenia:
    qtd_cidade = len(mapa_romenia[cidade])
    if qtd_cidade == 1:
        print(cidade)

print()

# sem usar variável adicional para receber o valor de LEN
print("Que contem exatamente 1 estrada:")
for cidade in mapa_romenia:
    if len(mapa_romenia[cidade]) == 1:
        print(cidade)

print()
#---------------------------------------EXERCICIO 2---------------------------------------#
print("Cidades com h(n) menor que 200 km")
for cidade in heuristica_bucareste:
    h = heuristica_bucareste[cidade]
    if h < 200:
        print(cidade)

print()

#---------------------------------------EXERCICIO 3---------------------------------------#
maior_custo = 0
origem_maior = ''
destino_maior = ''
for cidade in mapa_romenia:
    for vizinho, custo in mapa_romenia[cidade]:
        if custo > maior_custo:
            maior_custo = custo
            origem_maior = cidade
            destino_maior = vizinho
print('Estrada mais longa:')
print(f'saindo de {origem_maior} e indo para {destino_maior}, o custo é de {maior_custo} km')