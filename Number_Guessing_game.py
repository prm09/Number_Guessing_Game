import random

MIN_GUESS = 1
MAX_GUESS = 10


def main():
    NPC_score = 0
    Player_score = 0

    name = input("Welcome, what is your first name? ")
    print("Hello " + name + ", Do you want to play a Number-Guessing Game?")
    while True:
        strikes = 0                                                                 # Sets initial number of strike to 0
        answer = input("Press [Enter] to play or [Q] to quit. ")                    # Lines 15-17 checks if user wants to continue playing
        if answer.upper() == "Q":
            print("Okay maybe another time.")
            if Player_score > NPC_score:                                            # Informs user he or she won more games than program
                print(f"Congratulations, You won {Player_score} to {NPC_score}.")
                break
            elif Player_score < NPC_score:                                          # Informs user he or she lost more games than program
                print(f"Sorry, You lost {NPC_score} to {Player_score}.")
                break
            else:
                print(f"You tied at {NPC_score}.")                                  # Informs user he or she tied the program
                break
        else:
            print("Here is the the leaderboard:")
            print("-------------------")
            print(f"  NPC: {NPC_score}")
            print(f"  {name}: {Player_score}")
            print("-------------------")
            print("You have 3 tries to guess a number,"
                  " I am thinking of a number 1 to 10.")

            random_number = random.randint(MIN_GUESS, MAX_GUESS)                  # Randomly generates number between the 1 to 10
            while True:                                         # Loop checks if user's guessed number is = to answer
                guess = number_game()
                if random_number == guess:
                    print("CORRECT!!")
                    Player_score += 1                           # Adds +1 to user's total score
                    break
                else:
                    print("I'm sorry that was not correct")
                    strikes += 1                                # Adds +1 to user's number of strikes
                    if guess < random_number:
                        print("Too Low.")
                    else:
                        print("Too High")
                    print(f"You have {strikes} strike(s).")
                    if strikes == 3:                            # User is capped at 3 strikes
                        NPC_score += 1                          # Adds +1 to program's total score
                        print(f"You Lose. The correct number was {random_number}.")
                        break
    return 0


def number_game():
    while True:
        amount = input("Your Answer: ")
        if amount.isdigit():                            # Checks if input is a digit
            amount = int(amount)
            if MIN_GUESS <= amount <= MAX_GUESS:        # Checks if guess is between number range
                break
            else:
                print(f"Amount must be between {MIN_GUESS} - {MAX_GUESS}.")
        else:
            print("Please enter a number.")
    return amount


main()