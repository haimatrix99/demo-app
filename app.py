from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world from GCP v2!</p>"
