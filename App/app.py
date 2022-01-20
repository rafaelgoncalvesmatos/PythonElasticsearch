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

@app.route("all")
def all():
    resultsearch = es.search(index="prev_indice", query={"match_all" : {} })
    return resultsearch["hits"]

@app.route("/search/<word>")
def search_elastic(word):
    resultsearch = es.search(index="loja", query={ "query_string" : { "query" : busca } })
    return resultsearch["hits"]

@app.route("/inserir/<marca>/<produto>")
def inserir(marca, produto):
    doc = {
        "Marca" : marca,
        "Produto" : produto
        "timestamp" : datetime.now()
    }

    try:
        result = es.index(index="loja", document=doc)
        
        if "created" in result['result']:
            return result['result']
        else:
            return "Problem with insert data"
    except:
        return "<h1>Problem with connection or create index"