from flask import Flask, render_template

from cam import capturePredict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/imagecapture/<data>')
def capture(data):
    finalValue=data.replace("SLASH","/")
    preditemotion = capturePredict(finalValue)
    return "received "+preditemotion


if __name__ == "__main__" :
    app.run(debug=True)