from Live import load_game, _welcome


print(_welcome('Guy'))
difficulty, decision = load_game()

if decision == 1:
    from GuessGame import play
    play()
if decision == 2:
    from MemoryGame import play
    play()

