# -*- coding: utf-8 -*
# desafio1.py — Desafio 2: fazer um arquivo separado onde:
    # 1. Desafio 1: Calcule o custo do caminho
    #    Arad → Timisoara → Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest
    # 2. Desafio 2: Chame mostrar_g_h_f para esse mesmo caminho e descubra:
    #    em qual cidade o valor de f(n) passa de 418?

# começa importando o mapa e a heuristica, dentro do arquivo MAPA

from fase2_caminhos import custo_do_caminho, mostrar_g_h_f

arad_a_bucharest = ['Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 
                    'Craiova', 'Pitesti', 'Bucharest']

print('Arad -> Bucharest custa', custo_do_caminho(arad_a_bucharest), 'km')
print()
print("G (Já andado), H(Qnto falta) e F = G + H")
print()
print('Valores ao longo do caminho:')
mostrar_g_h_f(arad_a_bucharest)


#Ao rodar, da pra perceber que em Timisoara passa dos 418