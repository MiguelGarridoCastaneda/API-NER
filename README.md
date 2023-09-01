# API-NER

Versiones de librerias utilizadas:
  - spacy: 3.6.1
  - flask: 2.3.2

Este repositorio cuenta con una API para realizar peticiones a un modelo NER, para la clasificación (etiquetado) de entidades en texto.
Para la realización de este trabajo se utilizó un modelo NLP preentrenado de la librería spacy, el modelo utilizado fue ´es_core_news_sm´, se descargó, almacenó y posteriormente se cargó en una API creada en el lenguaje de programación Python con ayuda del framework Flask. Los pasos de descarga y almacenamiento del modelo se realizaron en el archivo model.ipynb, mientras que la API se encuentra en el archivo app.py de donde se carga el modelo desde la carpeta ´model´ para realizar el reconocimiento de entidades nombradas al recibir una petición POST, las pruebas de esta API se realizaron en el software de testeo Insomnia. Para probar la API se ejecuta el archivo app.py asegurándose de modificar la ruta de la carpeta del modelo y posteriormente se pega la ruta que proporciona flask (http://127.0.0.1:5000/ner) en Insomnia aplicando el método POST, se le hace una petición json como viene estructurada en las indicaciones de la prueba y arrojará el resultado obtenido.
