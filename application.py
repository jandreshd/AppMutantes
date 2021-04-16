from flask import Flask, request
from apiMutants.mutants import *
from conexionDB.dbMutants import consultarEstadisticasDia
from conexionDB.dbMutants import guardarSecuenciaAdn

application = Flask(__name__)
# add a rule for the index page.
@application.route('/')
def hello_world():
    return "Por fin lo lograste"

def index():
    return "Hola"

@application.route('/mutant', methods=['POST'])
def mutant():
    esUnMutante = False
    request_data = request.get_json()
    dna = request_data['dna']
    if (esAdnValido(dna) == True):
        if (esMutante(dna) == True):
            esUnMutante = True
            guardarSecuenciaAdn(dna, esUnMutante)
        if esUnMutante == True:
            return "Es un Mutante"
        else:
            return "No es un Mutante", 403
    else:
        return {"codigoRespuesta": 999, "mensajeRepuesta": "El valor enviado no es una secuencia de AND Valida"}

@application.route('/stats', methods=['GET'])
def consultar():
    return consultarEstadisticasDia()

if __name__ == "__main__":
 # Setting debug to True enables debug output. This line should be
 # removed before deploying a production app.
 application.debug = True
 application.run()