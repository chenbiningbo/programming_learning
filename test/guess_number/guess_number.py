serc_num = 9
guess_counts = 0
# guess_limit = 3
while guess_counts < 3:
    guess_num = int(input("Guess: "))
    guess_counts += 1
    if guess_num == serc_num:
        print("congratulations, You win the game")
        break
else:
    print("You failed game")