# DESAFIO API 
from flask import Flask, jsonify, request

app = Flask(__name__)

cancoes = [
    {
        'cancao': 'Black in Black',
        'autor': 'AC/DC'
    },

    {
        'cancao': 'timidez',
        'autor': 'Cvalo de Pau'
    },

    {
        'cancao': 'Mundo Inteiro',
        'autor': 'Desejo de Menina'
    }
]
#GET
#POST
#PUT
#DELETE

# Rota padrão
@app.route('/')
def cancao_postagens():
    return jsonify(cancoes)

#GET - com id - GET http://localhost:5000
@app.route('/cancoes/<int:indice>', methods=['GET'])
def obter_cancao_por_indice(indice):
    return jsonify(cancoes[indice])

# Criar uma nova postagem - POST - http://localhost:5000/postagem
@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem_cancao = request.get_json()
    cancoes.append(postagem_cancao)

    return jsonify(postagem_cancao, 200)

# Alterar uma postagem existente - PUT - http://localhost:5000/postagem/0
@app.route('/cancoes/<int:indice>', methods=['PUT'])
def alterar_cancao(indice):
    cancao_alterada = request.get_json()
    cancoes[indice].update(cancao_alterada)

    return jsonify(cancoes[indice]), 200


# Excluir uma postagem - DELETE - http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_cancao(indice):
    if 0 <= indice < len(cancoes):  # Verifica se o índice existe
        removida = cancoes.pop(indice)  # Remove a música e guarda o valor removido
        return jsonify({"mensagem": "Postagem excluída", "dados": removida}), 200
    
    return jsonify({"erro": "Não foi possível encontrar a postagem"}), 404

app.run(port=5000, host='localhost', debug=True)