from flask import Flask
from PIL import Image
imagen = Image.open("tower.png")
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route("/texto")
def text():
    return '<h1>Buenos días profe</h1>'

@app.route("/link")
def link():  
    return '<h1>https://www.youtube.com/watch?v=qU9mHegkTc4&list=PL9cIIcqvPNc4GnI69o0MlgrI5T5tRdz-R&index=9</h1>'
@app.route("/image")
def ima():
    return imagen.show()

app.run(debug=True)
