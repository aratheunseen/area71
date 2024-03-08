from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>/defination")
def defination(word):
    defination = "1. giving off light; bright or shining.\n2. very bright in colour.\n3. relating to light as it is perceived by the eye, rather than in terms of its actual energy."
    dictionary = {
        "word": word,
        "defination": defination
    }
    return dictionary

@app.route("/api/v1/<word>/case")
def text_transform(word):
    transform = {
        "word": word,
        "uppercase": word.upper(),
        "lowercase": word.lower(),
        "capitalize": word.capitalize()
    }
    return transform

app.run(debug=True, port=5001)