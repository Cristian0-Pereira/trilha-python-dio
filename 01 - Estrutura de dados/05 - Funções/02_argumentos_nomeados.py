# def salvar_carro(marca, modelo, ano, placa):
#     # salva carro no banco de dados...
#     print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
data = datetime.datetime.now()
data_atual = data.strftime("%A").capitalize() + data.strftime(", %d de %B de %Y - %H:%M")
print(data_atual)