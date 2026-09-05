import random

print("Welcome to guess number game.💥")
print("I'm thinking of a number between 1 and 100.")

correct_number = random.randint(1, 100)
number_is_correct = True

attempts = 0

while number_is_correct:
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

        play_again = ""

        while play_again not in ("y", "n"):
            play_again = input(
                "Do you want to play again? (y/n): "
            ).lower()

            if play_again not in ("y", "n"):
                print("Please enter y or n.")

        if play_again == "y":
            attempts = 0
            correct_number = random.randint(1, 100)
            print("I'm thinking of a new number between 1 and 100.")
            continue

        else:
            print("Thanks for playing! 👋")
            break

    else:
        if attempts == 7:
            print("😢 Game over!")
            print(f"The correct number was {correct_number}.")

            play_again = ""

            while play_again not in ("y", "n"):
                play_again = input(
                    "Do you want to play again? (y/n): "
                ).lower()

                if play_again not in ("y", "n"):
                    print("Please enter y or n.")

            if play_again == "y":
                attempts = 0
                correct_number = random.randint(1, 100)
                print("I'm thinking of a new number between 1 and 100.")
                continue

            else:
                print("Thanks for playing! 👋")
                break

        if user_guess < correct_number:
            print("Too low! ⬇️")
        else:
            print("Too high! ⬆️")