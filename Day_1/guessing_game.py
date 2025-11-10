import random

secret_number = random.randint(1, 100)

guess = ""




guess_counter = 0

while guess != secret_number:
    try:
        guess = int(input("What is your guess? "))
    except(ValueError):
        print("Please only enter numbers. Try again. \n")
        continue
    if guess > secret_number:
        print("Too high! Try again.")
        guess_counter += 1
        continue
    if guess < secret_number:
        print("Too low! Try again.")
        guess_counter += 1
        continue
    else:
        print("\nCongratulations, you won!")
        guess_counter += 1
        print("It took you", guess_counter, "tries. Try to get a lower score!\n")
        exit()