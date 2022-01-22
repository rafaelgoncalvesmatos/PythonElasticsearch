import os

from flask import Flask
from elasticsearch import Elasticsearch
from datetime import datetime

connectionstring = os.getenv("ES_LOCAL")
es = Elasticsearch(connectionstring)
app = Flask(__name__)

@app.route("/")
def rootpage():
    return "<b> Use da seguinte forma.</b><br> \
        Para mostrar tudo <br>  \
        /api/all <br><br> \
        Para buscar pela palavra chave <br>  \
        /api/search/[palavra] <br><br> \
        Para inserir dados <br> \
        /api/insert/[marca]/[panela] <br>"

@app.route("/api/all")
def all_elastic():
    resultsearch = es.search(index="loja", query={"match_all" : {} })
    return resultsearch["hits"]

@app.route("/api/search/<word>")
def search_elastic(word):
    resultsearch = es.search(index="loja", query={ "query_string" : { "query" : word } })
    return resultsearch["hits"]

@app.route("/api/insert/<marca>/<produto>")
def insert_elastic(marca, produto):
    doc = {
        "Marca" : marca,
        "Produto" : produto,
        "timestamp" : datetime.now(),
    }

    try:
        result = es.index(index="loja", document=doc)
        
        if "created" in result['result']:
            return result['result']
        else:
            return "Problem with insert data"
    except:
        return "<h1>Problem with connection or create index"