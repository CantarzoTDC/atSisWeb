from flask import Flask, render_template, request
import requests
import json

''' Instruções
A) Construir um webapp de conversão monetária (USD ~ BRL)[feito em aula]

B) Faça um webapp que calcule o custo de uma viagem baseado nos seguintes dados:
    1 - Consumo do carro / L ($/L?)
    2 - Distancia em KM da viagem
    3 - Preço do combustivel

        -- Etapas:
        1- Formar dupla [?]
        2- Repositório GHub [https://github.com/CantarzoTDC/atSisWeb]
        3- Consumo da API [?]
        4 -Frontend [?]
        5- Backend [?]
        6- Testes [?]
        7- Commit no Repositório [v]
'''

app = Flask(__name__)


@app.route('/')
def xtra():
    return render_template('index.html')

    #https://internet.sefaz.es.gov.br/informacoes/combustivel/index.php


@app.route('/converter')
def converter():
    '''
    https://www.layoutit.com/ (build bootstrap, p/ pegar conteudo da pasta static [css, fonts, js])
    https://docs.awesomeapi.com.br/api-de-moedas (doc api)
    https://wordpad.cc/DipLtFmH (app.py e converter.html)
    '''
    valueJ = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    value = float(valueJ.json()['USDBRL']['high'])
    toConvert = request.args.get('valor')
    resultado = {}
    if toConvert:
        try:
            toConvert = float(toConvert)
            converted = round(toConvert*value,2)
            converted = str(converted).replace('.',',')
            resultado = {
                'valor_original':toConvert,
                'valor_convertido':converted,
                'dolar_diario':value
            }
        except ValueError:
            resultado = {}
    return render_template('converter.html', resultado=resultado)


@app.route('/tripData/data/')
def consumeData():
    distJ,priceJ,perfJ  = requests.get('')
    dist = float(distJ.json()['USDBRL']['high'])
    price = float(priceJ.json()['USDBRL']['high'])
    perf = float(perfJ.json()['USDBRL']['high'])
    toConvert = request.args.get('valor')
    resultado = {}
    if toConvert:
        try:
            toConvert = float(toConvert)
            converted = round(toConvert*value,2)
            converted = str(converted).replace('.',',')
            resultado = {
                'valor_original':toConvert,
                'valor_convertido':converted,
                'dolar_diario':value
            }
        except ValueError:
            resultado = {}
    return render_template('tripCalc.html',''' data=data''')


@app.route('/tripData/calc/')
def calcData():
    return render_template('tripCalc.html', '''data=data''')


@app.route('/tripData/res/')
def distRes():
    return render_template('tripCalc.html', '''data=data''')

if __name__ == "__main__":
    app.run(debug=True)