import random
import sys

print("Welcome \n Rock-Paper-Scissor")


def game():
    lst = ["rock", "paper", "scissor"]
    player_1 = input("Enter your name: ")
    player_2 = "Computer"
    p1_score = 0
    p2_score = 0
    count = 0
    print("---Game Begins---")
    while (count < 5):
        print("Press '1' for rock, '2' for paper, '3' for scissor\n\n")
        p1_turn = int(input("Your choice: "))
        p2_turn = random.randint(1, 3)
        print(player_1, "'s choice is ", lst[p1_turn - 1])
        print(player_2, "'s choice is ", lst[p2_turn - 1])
        if p1_turn == p2_turn:
            print("It's a tie")
        elif p1_turn == 1:
            if p2_turn == 2:
                print(player_2, " gets a point")
                p2_score += 1
            elif p2_turn == 3:
                print(player_1, " gets a point")
                p1_score += 1
        elif p1_turn == 2:
            if p2_turn == 1:
                print(player_1, " gets a point")
                p1_score += 1
            elif p2_turn == 3:
                print(player_2, " gets a point")
                p2_score += 1
        elif p1_turn == 3:
            if p2_turn == 1:
                print(player_2, " gets a point")
                p2_score += 1
            elif p2_turn == 2:
                print(player_1, " gets a point")
                p1_score += 1
        else:
            print("Invalid Input")
        count += 1
        print()
    if p1_score > p2_score:
        print(player_1, " wins the game")
    elif p1_score < p2_score:
        print(player_2, " wins the game")
    else:
        print("The match is a tie")
    print("Do you want to play again??? Yes(y) or No(n) ", end=" ")
    choice = input()
    if choice.lower() == "y":
        main()
    elif choice.lower() == "n":
        sys.exit()
    else:
        print("Invalid Input")
        main()

def main():
    print("---Menu---")
    print("Start Game (s)")
    print("Rules of the Game (r)")
    print("Quit Game (q)")
    choice = input("Select from the options: ")
    if choice.lower() == "q":
        sys.exit()
    elif choice.lower() == "r":
        print("For every win the player gets 1 point and no negative markings")
        print("The games runs for 5 turns for each player")
        print()
        print("Rock wins over Scissor")
        print("Paper wins over Rock")
        print("Scissor wins over Paper")
        print()
        main()
    elif choice.lower() == "s":
        game()
    else:
        print("Invalid Input")
        main()

main()
