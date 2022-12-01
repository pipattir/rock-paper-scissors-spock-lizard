import random
# creating the game function


def game():
    # the possible actions
    user_action = input("Rock, Paper, Scissors, Lizard, Spock? (type exit to quit):\n")
    possible_actions = ["rock", "paper", "scissors", "lizard", "spock"]
    # giving the computer a random action
    computer_action = possible_actions[random.randint(0, 4)]
    # checking whether to play a round or quit the program
    if user_action.lower() == "exit":
        exit()
    elif user_action.lower() == "rock" or user_action.lower() == "paper" or user_action.lower() == "scissors"\
            or user_action.lower() == "lizard" or user_action.lower() == "spock":
        # if the actions are the same
        if user_action.lower() == computer_action:
            print(f"Both players selected", user_action + ". It's a tie!")
            game()
        # user chose rock
        elif user_action.lower() == "rock":
            if computer_action == "scissors":
                print("You won! Rock triumphs Scissors")
            elif computer_action == "lizard":
                print("You won! Rock triumphs Lizard")
            elif computer_action == "spock":
                print("You lost! Rock loses to Spock")
            else:
                print("You lost! Rock loses to Paper")
            game()
        # user chose paper
        elif user_action.lower() == "paper":
            if computer_action == "rock":
                print("You won! Paper triumphs rock")
            elif computer_action == "lizard":
                print("You lost! Paper loses to Lizard ")
            elif computer_action == "spock":
                print("You won! Paper triumphs Spock")
            else:
                print("You lost! Paper loses to Scissors")
            game()
        # user chose scissors
        elif user_action.lower() == "scissors":
            if computer_action == "paper":
                print("You won! Scissors triumphs Paper")
            elif computer_action == "lizard":
                print("You won! Scissors triumphs Lizard")
            elif computer_action == "spock":
                print("You lost! Scissors loses to Spock")
            else:
                print("You lost! Scissors loses to Rock")
            game()
        # user chose lizard
        elif user_action.lower() == "lizard":
            if computer_action == "scissors":
                print("You lost! Lizard loses to Scissors")
            elif computer_action == "rock":
                print("You lost! Lizard loses to Rock")
            elif computer_action == "paper":
                print("You won! Lizard triumphs Paper")
            else:
                print("You won! Lizard triumphs Spock")
            game()
        # user chose spock
        elif user_action.lower() == "spock":
            if computer_action == "scissors":
                print("You won! Spock triumphs scissors")
            elif computer_action == "rock":
                print("You won! Spock triumphs rock")
            elif computer_action == "paper":
                print("You lost! Spock loses to Paper")
            else:
                print("You lost! Spock loses to Lizard")
            game()
    # in case answer is none of the actions nor exit
    else:
        print("That's not a valid play. Check your spelling!")
        game()
# calling the game function


game()
