from pathlib import Path

SCORES_FILE_NAME = open(Path("Scores.txt"), "x")
# A string representing a file name. By default “Scores.txt”

BAD_RETURN_CODE = int(401)
# A number representing a bad return code for a function.


def _screen_cleaner():
    # A function to clear the screen.
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
