from flask import Flask, jsonify
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)


@app.route('/user/<int:id>', methods=['GET'])
def get_user_id(id):
    return jsonify({'msg': 'esta es una ruta get para un usuario especifico',
                    'id': id})

@app.route('/users', methods=['GET'])
def get_allusers():
    return jsonify({'msg':'esta es una ruta get para todos los usuarios'})

@app.route('/login', methods=['POST'])
def login():
    return jsonify({'msg':'esta es la ruta de login'})
    
@app.route('/signup', methods=['POST'])
def sign_up():
    return jsonify({'msg': 'esta ruta es para registrar un usuario'})

@app.route('/profile/<string:username>', methods=['GET'])
def get_profile_user(username):
    return jsonify({'msg':'esta ruta es para ir al perfil de un usuario'})

@app.route('/profile/<int:id>', methods=['GET'])
def get_profile_id(id):
    return jsonify({'msg':'esta ruta es para acceder a un perfil(id) desde el comentario que dejó en una publicación'})

@app.route('/post', methods=['POST'])
def post_content():
    return jsonify({'msg':'esta ruta es para subir contenido'})

@app.route('/comment', methods=['POST'])
def post_comment():
    return jsonify({'msg':'esta ruta es para postear un comentario'})

@app.route('/profile/setting/<int:id>', methods=['PUT'])
# @jwt_required()
def modificar_perfil(id):
    return jsonify({'msg':'esta ruta es para ',
                    'id':id})

@app.route('/searchAll/<string:search>', methods=['GET'])
def search(search):
    return jsonify({'msg':'esta ruta es para buscar usuarios post o comentarios',
                    'busqueda':search})

@app.route('/delete/post/<int:id>', methods=['DELETE'])
# @jwt_required()
def delete_post_by_id(id):
    return jsonify({'msg':'borrar la publicación(id) de un usuario',
                    'post id':id})

@app.route('/delete/comment/<int:id>', methods=['DELETE'])
# @jwt_required()
def delete_coment_by_id(id):
    return jsonify({'msg':'borrar el comentario(id) de un usuario',
                    'comment id':id})

####### Admin api #######

@app.route('/admin/load/<string:model>', methods=['GET'])
# @jwt_required()
def load_model(model):
    return jsonify({'msg': 'esta ruta carga los modelos?',
                    'modelo':model})

        ### Edit <model> <id> ###
@app.route('/admin/edit/<string:model>/<int:id>', methods=['PUT'])
# @jwt_required()
def edit_by_modelID(model,id):
    return jsonify({'msg': 'editar modelo?',
                    'modelo': model,
                    'id': id})



app.run('0.0.0.0')
