# PythonElasticsearch

Este repositório tem como objetivo a integração do python com o Elasticsearch ( Docker ).

Tecnologia trabalhada:

> Docker,
> Elasticsearch,
> Kibana,
> Flask

## Docker

Necessario a instalação do docker já que o projeto pode ser executado com o docker-compose, para isso siga os proximo passo:

```
git clone [repositório]
cd PythonElasticsearch/Docker
docker-compose up
```

## Elasticsearch

Validando batendo diretamente na API do elasticsearch:

```
$ curl http://localhost:9200
{
  "name" : "es01",
  "cluster_name" : "es-docker-cluster",
  "cluster_uuid" : "sKv9-fNdSb6fORJ37p3f3Q",
  "version" : {
    "number" : "7.16.2",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "2b937c44140b6559905130a8650c64dbd0879cfb",
    "build_date" : "2021-12-18T19:42:46.604893745Z",
    "build_snapshot" : false,
    "lucene_version" : "8.10.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

Consultando os indices atuais no Elastic:

```
$ curl -X GET http://localhost:9200/_cat/indices
```

Deletando indice diretamente com o curl:

```
$ curl -X DELETE http://localhost:9200/[indice]
```

## Flask

Usando o flask é preciso fazer a instalação da lib via pip no meu caso estou usando o python 3:

```
$ python3 -m pip install flask
```

Execução é bem tranquila, apenas apontando a app como a variavel que vai ser lida pelo flask e na sequencia a execução.

```
$ export ES_LOCAL="http://localhost:9200"
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ python3 -m flask run
```

Para verificar o funcionamento segue a url:

> http://localhost:5000


Continua....