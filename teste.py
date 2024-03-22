quantidade_passos = int(input())
if quantidade_passos > 0:
    for passo_atual in range(1, quantidade_passos + 1):
        if passo_atual == 1:
            print(f"Explorador: {passo_atual} passo")
        else:
            print(f"Explorador: {passo_atual} passos")
elif quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")