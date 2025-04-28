from pymongo import MongoClient
import json

#-----------------------------------------------------------------
# Conectando ao MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente['Alura_Series']
colecao = db['series']
#-----------------------------------------------------------------
# Deletando todos 
colecao.delete_many({})
#-----------------------------------------------------------------
# Abrindo e carregando o arquivo JSON
with open("./Base de dados.json", encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# Inserindo no MongoDB
colecao.insert_many(dados)

for documento in colecao.find():
    print(json.dumps(documento, indent=4, default=str))
#-----------------------------------------------------------------
# Atualizando um documento específico
colecao.update_one(
    {"Série": "Pataal Lok"},
    {"$set": {"IMDb Avaliação": 9.0}}
)

# Atualizando vários documentos
colecao.update_many(
    {"Classificação": "16+"},
    {"$set": {"Classificação": "16+"}}
)

#-----------------------------------------------------------------
# Deletando uma série específica
colecao.delete_one(
    {"Série": "Upload"},
)
#-----------------------------------------------------------------
# Buscar todos os documentos com "Ano lançamento" igual a 2020
documentos = list(colecao.find({"Ano de lançamento": 2020}))

# Converter o ObjectId para string
for doc in documentos:
    doc['_id'] = str(doc['_id'])

# Salvar em um arquivo JSON
with open('series_2020.json', 'w', encoding='utf-8') as f:
    json.dump(documentos, f, indent=4, ensure_ascii=False)

print("Arquivo 'series_2020.json' salvo com sucesso!")
