# Entrada dos valores da capacidade atual e do aumento percentual
capacidade_atual, aumento_percentual = map(int, input().split())
# Calcula a nova capacidade
nova_capacidade = capacidade_atual + (capacidade_atual * aumento_percentual / 100)
# Imprime a nova capacidade
print(int(nova_capacidade))

