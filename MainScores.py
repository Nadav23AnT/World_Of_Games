from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        score = open(r"E:\MyGitRepo\World_Of_Games\scores.txt", "r")
        return render_template("score.html") # Open score details
    except FileNotFoundError or FileExistsError: # If the file didn't open for any reason
        return render_template("error.html") # Prints error message


app.run()
