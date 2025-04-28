// Conectando ao banco de dados
const db = connect("mongodb://localhost:27017/Alura_Series");

// Definindo a coleção
const colecao = db.getCollection("series");

// Inserindo novos documentos (séries) na coleção
const dados = [
  {
    "Série": "Pataal Lok",
    "Ano lançamento": 2020,
    "Classificação": "16+",
    "IMDb Avaliação": 8.4
  },
  {
    "Série": "Upload",
    "Ano lançamento": 2020,
    "Classificação": "18+",
    "IMDb Avaliação": 8.0
  }
];

// Inserir os documentos na coleção
colecao.insertMany(dados);

// Buscar todas as séries com ano de lançamento 2020
const series2020 = colecao.find({ "Ano lançamento": 2020 }).toArray();
printjson(series2020);

// Atualizar a avaliação de uma série
colecao.updateOne(
  { "Série": "Pataal Lok" },
  { $set: { "IMDb Avaliação": 9.0 } }
);

// Exibir o documento atualizado
const serieAtualizada = colecao.find({ "Série": "Pataal Lok" }).toArray();
printjson(serieAtualizada);

// Deletar uma série
colecao.deleteOne({ "Série": "Upload" });
print("Série 'Upload' deletada com sucesso.");
