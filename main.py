import random

print("Welcome to guess number game.💥")
print("I'm thinking of a number between 1 and 100.")

correct_number = random.randint(1,100)
number_is_correct = True

attempts = 0

while number_is_correct:
    try:
        user_guess = int(input("please enter your guess: "))
    except ValueError:
        print("Please enter a number.")
        continue

    attempts += 1

    if user_guess > 100 or user_guess <= 0:
        print("Please enter a number between 1 and 100.")
        continue
        

    if user_guess < correct_number:
        print("Too low! ⬇️")
    elif user_guess > correct_number:
        print("Too high! ⬆️")
    else:
        print(f"🎉 Correct! You got it in {attempts} attempts.")
        number_is_correct = False