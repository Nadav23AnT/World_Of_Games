from flask import Flask

app = Flask(__name__)

def score_server():
    open(r"E:\MyGitRepo\World_Of_Games\Scores.txt", "r")
    @app.route("/")
