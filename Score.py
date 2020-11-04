

def add_score(difficulty):
    POINTS_OF_WINNING = str((difficulty * 3) + 5)
    # The function will read the current score in the scores file,
    # if it fails it will create a new one and will save the current score.
    try:
        score_file = open(r"E:\MyGitRepo\World_Of_Games\Scores.txt", "r")
        score = open(r"E:\MyGitRepo\World_Of_Games\Scores.txt", "a")
        score.write(f" ,{POINTS_OF_WINNING}")
    except FileNotFoundError:
        score = open(r"E:\MyGitRepo\World_Of_Games\Scores.txt", "x")
        score.write(POINTS_OF_WINNING)


