# import dependencies

from flask import Flask, render_template, redirect
from cam import capturePredict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# Api call from client
# recieves image as data in byte 64 format, and sends the byte code for pre processing
#  gets emotion after preprocessing, and sends the output to the client
@app.route('/imagecapture/<data>', methods=['GET'])
def capture(data):
    finalValue=data.replace("SLASH","/")
    preditemotion = capturePredict(finalValue)
    print("My emo ", preditemotion)
    return preditemotion


# Start of the Flask Application
if __name__ == "__main__" :
    app.run(debug=True)