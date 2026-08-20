from flask import Flask, render_template, request
import requests
import csv
from datetime import datetime
import os

app = Flask(__name__)

def moeda_valida(moeda):
    try:
        url = "https://api.frankfurter.app/currencies"
        resposta = requests.get(url, timeout=20)
        if resposta.status_code != 200:
            return False
        moedas_disponiveis = resposta.json()
        return moeda in moedas_disponiveis
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        return False

def listar_moedas():
    try:
        url = "https://api.frankfurter.app/currencies"
        resposta = requests.get(url, timeout=20)
        if resposta.status_code == 200:
            return resposta.json()
        return {}
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        return {}

def converter(valor, de, para):
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={de}&to={para}"
    resposta = requests.get(url, timeout=20)

    if resposta.status_code != 200:
        return None, None

    dados = resposta.json()
    resultado = dados["rates"][para]
    taxa = resultado / valor
    return resultado, taxa

def salvar_historico(valor, de, para, resultado, taxa):
    with open("historico.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            valor, de, para, resultado, taxa
        ])

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None

    if request.method == "POST":
        try:
            valor = float(request.form.get("valor", 0))
            de = request.form.get("de", "").upper()
            para = request.form.get("para", "").upper()

            if valor <= 0:
                erro = "O valor precisa ser maior que zero."
            elif not moeda_valida(de):
                erro = f"Moeda de origem '{de}' inválida."
            elif not moeda_valida(para):
                erro = f"Moeda de destino '{para}' inválida."
            else:
                valor_convertido, taxa = converter(valor, de, para)
                if valor_convertido is not None:
                    resultado = {
                        "valor": valor,
                        "de": de,
                        "para": para,
                        "resultado": round(valor_convertido, 2),
                        "taxa": round(taxa, 4)
                    }
                    salvar_historico(valor, de, para, valor_convertido, taxa)
                else:
                    erro = "Erro ao consultar a API."

        except ValueError:
            erro = "Valor inválido. Digite um número."
        except requests.exceptions.Timeout:
            erro = "A API demorou muito para responder. Tente novamente."
        except requests.exceptions.ConnectionError:
            erro = "Sem conexão com a internet."
        except Exception:
            erro = "Ocorreu um erro inesperado. Tente novamente."

    moedas = listar_moedas()
    return render_template("index.html", resultado=resultado, erro=erro, moedas=moedas)

if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "False") == "True"
    app.run(debug=debug_mode, use_reloader=False)