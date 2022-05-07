import requests
import json

cotacao = requests.get(" https://economia.awesomeapi.com.br/last/BTC-BRL")
cotacao = cotacao.json()
cotacao_btc = cotacao['BTCBRL']["bid"]
date_cotacao = cotacao['BTCBRL']["create_date"]
print(cotacao_btc)
print(date_cotacao)