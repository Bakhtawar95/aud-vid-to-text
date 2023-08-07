from flask import Flask, render_template, request, session
from IPython.display import Audio
from pytube import YouTube
import whisper



app = Flask(__name__)
app.secret_key = "hani"


@app.route("/")
def home():


    return "good morning"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
