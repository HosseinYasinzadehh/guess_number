import random


def play_game():
    correct_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if user_guess > 100 or user_guess <= 0:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if user_guess == correct_number:
            print(f"🎉 Correct! You got it in {attempts} attempts.")
            return

        if attempts == 7:
            print("😢 Game over!")
            print(f"The correct number was {correct_number}.")
            return

        if user_guess < correct_number:
            print("Too low! ⬇️")
        else:
            print("Too high! ⬆️")


def ask_play_again():
    play_again = ""

    while play_again not in ("y", "n"):
        play_again = input(
            "Do you want to play again? (y/n): "
        ).lower()

        if play_again not in ("y", "n"):
            print("Please enter y or n.")

    return play_again

while True:
    play_game()

    play_again = ask_play_again()

    if play_again == "n":
        print("Thanks for playing! 👋")
        break