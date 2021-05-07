import os

from flask import Flask, render_template, redirect

from cam import capturePredict

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/static/images'


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/imagecapture/<data>', methods=['GET'])
def capture(data):
    finalValue=data.replace("SLASH","/")
    preditemotion = capturePredict(finalValue)
    print("My emo ", preditemotion)
    return preditemotion



if __name__ == "__main__" :
    app.run(debug=True)