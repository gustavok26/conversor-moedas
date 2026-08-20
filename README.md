# Conversor de Moedas

Aplicação web simples para conversão de moedas em tempo real, construída com Python e Flask.

## Funcionalidades

- Conversão entre diversas moedas com cotação atualizada
- Validação de entrada (valor numérico maior que zero, moedas existentes)
- Tratamento de erros de rede (timeout, falta de conexão)
- Histórico de conversões salvo automaticamente
- Tabela com todas as moedas disponíveis para consulta

## Tecnologias utilizadas

- Python 3
- Flask
- Requests
- API [Frankfurter](https://www.frankfurter.app/) (cotações de câmbio, gratuita e sem necessidade de chave de acesso)

## Como executar localmente

1. Clone o repositório:
   git clone https://gustavok26/conversor-moedas.git
   cd conversor-moedas