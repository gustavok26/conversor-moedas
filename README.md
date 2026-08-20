# Conversor de Moedas

Aplicação web simples para conversão de moedas em tempo real, construída com Python e Flask.

🔗 **Acesse a aplicação:** [conversor-moedas-gustavo.onrender.com](https://conversor-moedas-gustavo.onrender.com/)

> Nota: o serviço gratuito do Render "dorme" após um período de inatividade. Se o link demorar 30-50 segundos para carregar no primeiro acesso, é normal — a aplicação está sendo reativada.

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
- Gunicorn (servidor de produção)
- API [Frankfurter](https://www.frankfurter.app/) (cotações de câmbio, gratuita e sem necessidade de chave de acesso)
- Deploy: [Render](https://render.com/)

## Como executar localmente

1. Clone o repositório:
   git clone https://gustavok26/conversor-moedas.git
   cd conversor-moedas