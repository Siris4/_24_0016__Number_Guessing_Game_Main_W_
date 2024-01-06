#Number Guessing Game Objectives:

import random

from _24_0016__D12_v04_f01_Game_logo import logo
print(logo)

def play_Number_Guessing_game():

    turns_remaining = 0

    difficulty_level = int(input(f"Please choose between easy or hard (1 = easy, 2 = hard): "))
    if difficulty_level == 1:
        # global turns_remaining_for_easy
        # global turns_remaining
        turns_remaining += 10
    elif difficulty_level == 2:
        # global turns_remaining_for_hard
        # global turns_remaining
        turns_remaining += 5

    player_guessed_number = ""

    if difficulty_level == 1:
        print(f"You chose easy")
    else:
        print(f"You chose hard")


    continue_playing = True
    while continue_playing:

        # def base_number_determined():
        global base_number
        base_number = int(random.randint(1, 100))
        # print(f"The secret number is {base_number}")


        while turns_remaining > 0:
        # def player_guesses_number():
            player_guessed_number = int(input(f"Please guess a number between 1-100: "))

    # while continue_playing == True:

        # def redirect_higher_or_lower():
            if base_number > player_guessed_number:
                print(f"\nGuess higher")
            elif base_number < player_guessed_number:
                print(f"\nGuess lower")
            elif base_number == player_guessed_number:
                print("\nYou guessed it perfectly right!! Wow!")
                continue_playing = False
                break
            turns_remaining -= 1
            print(f"The number of turns remaining is: {turns_remaining}")
        else:
            print(f"Womp. You ran out of turns. Game Over. The number was {base_number}.")
            continue_playing = False
            break


    # base_number_determined()

    # player_guesses_number()

    # redirect_higher_or_lower()


#play again?
while True:
    play_Number_Guessing_game()
    play_again_option = input("Do you want to play again? (Y or N): ").upper()
    if play_again_option != "Y":
        print("Okay, thank you for playing! Have a great day then!")
        break