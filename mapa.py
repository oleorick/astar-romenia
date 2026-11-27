# -*- coding: utf-8 -*
# mapa.py — os DADOS do problema (Fase 1)
#
# Mapa rodoviário da Romênia (Figura 3.2 do Russell & Norvig) e a heurística
# h(n) = distância em linha reta até Bucareste (Figura 3.22).
# Este arquivo só guarda dados: ele não imprime nada quando é executado.
# Os outros arquivos do projeto fazem "from mapa import ..." para usá-los.
#
#
# ----- PASSO 1: o mapa como um dicionário ----
# Chave  = nome da cidade (texto)
# Valor  = lista de tuplas (vizinho, custo da estrada em km)
#
#
# O QUE EU ENTENDI:
# 'mapa_romenia =' é uma DICIONÁRIO que inicia com { } dentro dele contém as variáveis =
#{ 
# nome da cidade (do tipo texto) que contém: uma LISTA representada por COLCHETES
#   [e suas TUPLAS(LISTAS que não mudam) representado por 
#   PARÊNTES ('vizinho x', custo da estrada em KM), (...)]
#
# 'nome da cidade': [('nome do vizinho', custo da estrada em km), ('vizinho', custo da estrada em km), (...)],
#
# - Cada estrada é uma tupla (tuple) imutável com 2 itens: (nome_do_vizinho, custo_em_km).
#
#
#


mapa_romenia = {
    'Arad':           [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)], 
    'Zerind':         [('Arad', 75), ('Oradea', 71)],
    'Oradea':         [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu':          [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara':      [('Arad', 118), ('Lugoj', 111)],
    'Lugoj':          [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia':        [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta':        [('Mehadia', 75), ('Craiova', 120)],
    'Craiova':        [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras':        [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti':        [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest':      [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu':        [('Bucharest', 90)],
    'Urziceni':       [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova':        [('Urziceni', 98), ('Eforie', 86)],
    'Eforie':         [('Hirsova', 86)],
    'Vaslui':         [('Urziceni', 142), ('Iasi', 92)],
    'Iasi':           [('Vaslui', 92), ('Neamt', 87)],
    'Neamt':          [('Iasi', 87)],
}


#
#
#
#
# ----- PASSO 2: a heurística como outro dicionário ----
# Chave = cidade, Valor = distância em linha reta (km) daquela cidade até Bucareste
#
#
# O QUE EU ENTENDI:
# Heurística (pesquisei no Google) é uma estratégia de resolução
#   de problemas e tomada de decisão que utiliza atalhos
#   mentais ou regras práticas para encontrar soluções
#   satisfatórias de forma rápida.
# Então, o DICIONÁRIO heuristica_bucareste (que em outros ARQUIVOS
#   será representada por h(n), é a distancia em linha reta de cada
#   cidade até Bucareste. O que também a torna um dicionário com:
#   CHAVE = CIDADE, VALOR = UM NUMERO INTEIRO
# Como os dois dicionários usam exatamente os mesmos nomes de cidades, permite combinar os dois
#   em outros arquivos (códigos) do sistema
#
# heuristica_bucareste = {
#   'Arad': 366
# }
# Ou seja, 'Arad': 366 - de Bucareste (Bucharest) até Arad são 366 km

heuristica_bucareste = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100,
    'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80,
    'Vaslui': 199, 'Zerind': 374,
}