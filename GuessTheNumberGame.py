import random

# generate a random number between 1 and 100
secret_number = random.randint(1, 100)
print(secret_number)

# set the number of guesses to zero
num_guesses = 0

# loop until the user guesses the number
while True:
    # ask the user to guess a number
    guess = int(input("Guess a number between 1 and 100: "))

    # increment the number of guesses
    num_guesses += 1

    # check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
