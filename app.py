# importar librerias necesarias
# versiones utilizadas:
# spacy: 3.6.1
# flask: 2.3.2
import spacy
from flask import Flask, jsonify, request

# ruta del modelo preentrenado (cambiar la ruta donde está almacenada la carpeta del modelo)
model_path = "C:/Users/mike_/OneDrive/Escritorio/pruebas nlp/spacy/model"

# cargamos el modelo
modelo = spacy.load(model_path)


# función para el reconocimiento de entidades nombradas
def obtener_entidades(texto):
    """
    Función encargada de recibir texto y realizar reconocimiento de entidades nombradas (NER).

    argumento texto: lista de strings con el texto a procesar
    return resultado: diccionario con las entidades de cada oración
    """
    # diccionario de resultados de cada oración
    resultado = {"resultado": []}
    # Para cada oración
    for oracion in texto:
        # La oración es procesada por el modelo
        doc = modelo(oracion)
        # Se obtienen sus entidades
        entidades = {}
        for entidad in doc.ents:
            entidades[entidad.text] = entidad.label_
        # se almacenan en resultado
        resultado["resultado"].append(
            {
                "oración": oracion,
                "entidades": entidades
            }
        )
    return resultado


# creamos la aplicación
app = Flask(__name__)


@app.route("/")  # ruta inical
def index():
    return "NER"


@app.route("/ner", methods=['POST'])  # ruta para realizar petición NER
def ner():
    # obtenemos la petición POST (json)
    texto = request.get_json()
    # del archivo json obtenemos las oraciones (strings dentro de una lista)
    oraciones = texto.get('oraciones', [])
    # aplicamos la función para la obtención de las entidades para cada una de las oraciones
    entidades = obtener_entidades(oraciones)
    return jsonify(entidades)


# Inicializamos la aplicación
if __name__ == "__main__":
    app.run(debug=True)
