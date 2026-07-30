import requests
import csv
from datetime import datetime

def moeda_valida(moeda):
    url = "https://api.frankfurter.app/currencies"
    resposta = requests.get(url)
    moedas_disponiveis = resposta.json()
    return moeda in moedas_disponiveis

def converter(valor, de, para):
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={de}&to={para}"
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        print(f"ERRO na API: status {resposta.status_code}")
        print(f"Resposta: {resposta.text}")
        return None, None
    
    dados = resposta.json()
    resultado = dados["rates"][para]
    taxa = resultado / valor  # taxa de câmbio unitária
    return resultado, taxa

def salvar_historico(valor, de, para, resultado, taxa):
    with open("historico.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            valor, de, para, resultado, taxa
        ])

def main():
    while True:
        try:
            valor = float(input("Valor: "))
            de = input("Moeda de origem (ex: USD): ").upper()
            para = input("Moeda de destino (ex: BRL): ").upper()

            if not moeda_valida(de):
                print(f"Moeda de origem '{de}' inválida.")
                continue
            if not moeda_valida(para):
                print(f"Moeda de destino '{para}' inválida.")
                continue

            resultado, taxa = converter(valor, de, para)
            if resultado is not None:
                print(f"{valor} {de} = {resultado:.2f} {para}  (taxa: 1 {de} = {taxa:.4f} {para})")
                salvar_historico(valor, de, para, resultado, taxa)

        except ValueError:
            print("Valor inválido. Digite um número.")
        except Exception as e:
            print("ERRO:", e)

        continuar = input("\nConverter outro valor? (s/n): ").lower()
        if continuar != "s":
            break

if __name__ == "__main__":
    main()