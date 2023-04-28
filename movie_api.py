from flask import Flask
from flask_restful import Api
from flask_cors import CORS


app = Flask(__name__, static_url_path="")
CORS(app)
app.debug = False

api = Api(app)

api.add_resource(
    HolaMundoAPI,
    '/hola-mundo/<string:name>/<string:apellido>',
    endpoint='hola-mundo'
)

api.add_resource(
    MatematicasAPI,
    '/matematicas/',
    endpoint='matematicas'
)

if __name__ == "__main__":
    app.run(debug=False, port=5050)
