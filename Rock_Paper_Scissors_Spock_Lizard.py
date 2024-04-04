import random
import json
from matplotlib import pyplot as plt

path = "data/Rock_Paper_Scissors_Spock_Lizard.json"

def write_file(data):
    with open(path, "w") as file:
        file.write(json.dumps(data, indent=4))

def statistics():
    with open(path, "r") as file:
        return json.load(file)

def save_selcted(selected):
    data = statistics()

    data["Rock"] = str(int(data["Rock"]) + (selected == 0))
    data["Paper"] = str(int(data["Paper"]) + (selected == 1))
    data["Scissors"] = str(int(data["Scissors"]) + (selected == 2))
    data["Spock"] = str(int(data["Spock"]) + (selected == 3))
    data["Lizard"] = str(int(data["Lizard"]) + (selected == 4))

    is_winner = game(selected)
    data["Draw"] = str(int(data["Draw"]) + (is_winner == 0))
    data["Player_won"] = str(int(data["Player_won"]) + (is_winner == 1))
    data["Computer_won"] = str(int(data["Computer_won"]) + (is_winner == 2))

    write_file(data)

def game(selected):
    computer = random.randint(0, 4)
    print(f"Computer Chose {computer}!")
    if (int(selected) + 2) % 5 == computer or (int(selected) - 1) % 5 == computer:
        print("You have Won!")
        print("-----------------------------------------------------")
        return 0
    elif(int(selected) == computer):
        print("It's a Draw!")
        print("-----------------------------------------------------")
        return 1
    else:
        print("You have Lost!")
        print("-----------------------------------------------------")
        return 2

def menu():
    print("Choose a or b!")
    print("a. play game")
    print("b. show statistics")
    input1 = input()
    if(input1 == "a"):
        print("choose a number between 0 and 4")
        print("Rock(0), Paper(1), Scissors(2), Spock(3), Lizard(4)")
        selected = input()
        if(selected.isdigit() and 0 <= int(selected) <= 4):
            print(f"You Chose {selected}!")
            save_selcted(int(selected))
        else:
            print("Invalid input. Please choose a number between 0 and 4")
            print("-----------------------------------------------------")
    elif (input1 == "b"):
        print(statistics())
        print("-----------------------------------------------------")
    else:
        print("Invalid choice. Please choose a or b")
        print("-----------------------------------------------------")

if __name__ == "__main__":
    while True:
        menu()