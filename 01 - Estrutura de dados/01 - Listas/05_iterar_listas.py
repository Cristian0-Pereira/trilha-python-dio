carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro,end=" ")

for indice, carro in enumerate(carros):
    print(f"{indice+1}° {carro}")
