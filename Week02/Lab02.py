import random

array = ["Rock", "Paper", "Scissors"]

score = 0
computer_score = 0

print("\nWelcome to Rock, Paper, Scissors! \n")

print("Rules: \n - Rock beats Scissors \n - Paper beats Rock \n - Scissors beats Paper \n - Each time you win, you get a point. \n - If you lose, the computer gets a point. \n - First to 3 points wins! \n")
print("")

loop = True
while loop:
    print("--------------------------------")
    player_choice = int(input("Enter your weapon 1 (Rock), 2 (Paper), or 3 (Scissors): \n"))

    computer_choice = random.choice([1, 2, 3])

    if player_choice not in [1, 2, 3]:
        print("Invalid choice! Please select a number between 1 and 3.\n")
    else:
        print("\n")
        print("Player chose: {}".format(array[player_choice - 1]))
        print("Computer chose: {}".format(array[computer_choice - 1]))
        print("\n")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
            print("You Win!")
            score += 1
        else:
            print("You Lose!")
            computer_score += 1
        
        print("\n")
        if player_choice != 1:
            print("You didn't pick the classic rock...\n")

        print("Score: Player {} - Computer {}".format(score, computer_score))
        print("\n")
        if score == 3:
            print("Congratulations! You reached 3 points and won the game!")
            loop = False
        elif computer_score == 3:
            print("The computer reached 3 points and won the game! Better luck next time.")
            loop = False

        
            