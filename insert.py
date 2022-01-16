from datetime import datetime
from elasticsearch import Elasticsearch
from pprint import pprint

import time
import inflect 
import random


# Conexao com o elasticsearch
es = Elasticsearch("http://localhost:9200")
hora = datetime.now()

def insert( number ):
  n = random.random()
  doc = {
    "Autor" : number,
    "Livro" : "",
    "Ano"   : "",
    "timestamp" : datetime.now(),
  }

  response = es.index(index=n, document=doc)

  pprint(f"Realizando INSERT {hora}")
  # pprint(response)

  if "created" in response['result']:
    pprint(f"Status do documento: {response['result']} - {hora}")
  else:
    loop()

def loop():
  while(True):
    for i in range(1,500):
      p = inflect.engine()
      p.number_to_words(i)
      insert(i)
      # time.sleep(2)

loop()