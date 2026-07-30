import requests

def converter(valor, de, para):
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={de}&to={para}"
    resposta = requests.get(url).json()
    return resposta["rates"][para]

try:
    valor = float(input("Valor: "))
    de = input("Moeda de origem (ex: USD): ").upper()
    para = input("Moeda de destino (ex: BRL): ").upper()

    resultado = converter(valor, de, para)
    print(f"{valor} {de} = {resultado} {para}")
except Exception as e:
    print("ERRO:", e)

input("Pressione Enter para sair...")
