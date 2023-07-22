import random

def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def get_user_guess(min_num, max_num):
    while True:
        try:
            guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
            if min_num <= guess <= max_num:
                return guess
            else:
                print("Please enter a valid number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    print("Welcome to the Number Guessing Game!")
    min_num = 1
    max_num = 100  # You can change this range according to your preference.

    secret_number = generate_random_number(min_num, max_num)
    attempts = 0

    while True:
        attempts += 1
        user_guess = get_user_guess(min_num, max_num)

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    play_game()
