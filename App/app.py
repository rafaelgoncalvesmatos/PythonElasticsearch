import os

from flask import Flask
from elasticsearch import Elasticsearch
from datetime import datetime

connectionstring = os.getenv("ES_LOCAL")
es = Elasticsearch(connectionstring)
app = Flask(__name__)

@app.route("/")
def rootpage():
    resultado = es.search()
    return resultado
    # return "<b> Use da seguinte forma.</b> \
    #     Para buscar pela palavra chave  \
    #     /busca/[palavra] \
    #     Para inserir dados \
    #     /[marca]/[panela] "

@app.route("/inserir/<marca>/<produto>")
def inserir(marca, produto):
    doc = {
        "Marca" : marca,
        "Produto" : produto
    }

    try:
        result = es.index(index="loja", document=doc)
        return result['result']
    except:
        return "Erro ao inserir dados"