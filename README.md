# Alura Series - MongoDB Management

## 🚀 Descrição do Projeto

Este projeto tem como objetivo a **gerência de séries de TV** usando **MongoDB** para armazenar, atualizar, buscar e deletar informações de diversas séries. A partir de um arquivo JSON com dados das séries, o sistema é capaz de realizar **operações completas de CRUD (Create, Read, Update, Delete)**.

As funcionalidades incluem:
- Importação de dados de séries para o MongoDB.
- Busca e visualização das séries com base em critérios específicos, como **ano de lançamento**.
- Atualizações de informações, como a **avaliação do IMDb**.
- Deleção de dados, incluindo remoção de séries específicas ou de todas as séries de uma vez.

## 💻 Tecnologias Usadas

- **Python 3.x**
- **PyMongo** (Biblioteca Python para interação com MongoDB)
- **MongoDB** (Banco de dados NoSQL)
- **JSON** (Formato de dados utilizado para importar/exportar séries)

## 🔧 Funcionalidades

### 1. **Conexão com o MongoDB**
A aplicação conecta-se ao banco de dados MongoDB para realizar operações de leitura e escrita em tempo real.

### 2. **Importação de Dados**
Os dados das séries são importados de um arquivo **`Base de dados.json`** e inseridos na coleção **`series`** do MongoDB.

### 3. **Leitura de Dados**
O script permite listar todas as séries inseridas no banco de dados, exibindo-as em formato JSON com indentação legível.

### 4. **Atualização de Dados**
O sistema pode:
- Atualizar a **avaliação do IMDb** de uma série específica.
- Atualizar a **classificação** de várias séries simultaneamente.

### 5. **Deleção de Dados**
Você pode:
- Deletar uma série específica pelo nome.
- Deletar todas as séries de uma vez.

### 6. **Busca por Ano de Lançamento**
A funcionalidade de busca permite filtrar as séries por **ano de lançamento**, exportando os resultados para um arquivo **`series_2020.json`**.

## 📦 Pré-Requisitos

Certifique-se de ter as seguintes ferramentas instaladas no seu ambiente:

- **MongoDB** (servidor rodando na porta padrão 27017)
- **Python 3.x** instalado
- **Biblioteca PyMongo**: Instale via pip:
  ```bash
  pip install pymongo

```
alura-series/
│
├── Base de dados.json        # Arquivo JSON com dados das séries
├── mongosh.py                   # Script principal com operações MongoDB
├── series_2020.json          # Arquivo de saída com séries de 2020
├── README.md                 # Documentação do projeto
```