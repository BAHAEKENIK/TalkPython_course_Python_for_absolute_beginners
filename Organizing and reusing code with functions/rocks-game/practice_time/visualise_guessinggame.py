import random


def main():
    show_header()
    play_game()


def show_header():
    print("--------------------------------------------------")
    print("                 M&M guessing game!               ")
    print("--------------------------------------------------")


def play_game():
    mm_count = random.randint(1, 100)
    attempt_limit = 5
    attempts = 0
    print("Guess the number of M&Ms and you get lunch on the house!")
    print()
    while attempts < attempt_limit:
        guess_text = input("How many M&Ms are in the jar? ")
        guess = int(guess_text)
        if mm_count == guess:
            print(f"You got a free lunch! It was {guess}.")
            break
        elif mm_count > guess:
            print("Sorry, that's too low!")
        else:
            print("That's too HIGH!")
        attempts += 1
    print(f"Bye,you're done in {attempts}")


if __name__ == "__main__":
    main()
