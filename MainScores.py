from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        score = open(Path("Scores.txt"), "r")
        return render_template("score.html", SCORE=score)  # Open score details
    except FileNotFoundError or FileExistsError:  # If the file didn't open for any reason
        return render_template("error.html", ERROR="Unknown Error")  # Prints error message


app.run()
