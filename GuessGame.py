from time import sleep
from MainGame import difficulty


def _generate_number():
    # Will generate automatic random number
    import random
    secret_number = int(random.uniform(1, difficulty))
    return secret_number


def _get_guess_from_user():
    # The user will choose a number
    number = int(input(f"You need to guess a number between 1 to {difficulty}: "))
    return number


def _compare_results(secret_number, number):
    # checking if the number the user chose equal to the random number
    if secret_number == number:
        return True


def play():
    # The start function, will start all functions and return false or true
    secret_number = _generate_number()
    print("Generating a Number....")
    sleep(2)
    print("Yeap! The number is ready. Now it is Your turn")
    sleep(1)
    number = _get_guess_from_user()
    if _compare_results(secret_number=secret_number, number=number):
        return True
    else:
        return False


play()
# Calling the start module
