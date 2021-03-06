import time
from ai_classes import Player, RandomAI

# This is the game with AI.
# You can create AI brains for this game.

def status(p1, p2):
    print(">>~`~`~`~`~`~`~`~`~`~`~<<")
    print("Status:")
    print(f"{p1.name}:\n    Bullets: {p1.bullets}\n    Guards: {p1.guards}\n    Score: {p1.score}")
    print(f"{p2.name}:\n    Bullets: {p2.bullets}\n    Guards: {p2.guards}\n    Score: {p2.score}")
    print(">>~`~`~`~`~`~`~`~`~`~`~<<")


def calculate(p1, p2):
    if p1.state == "shoot":
        if p1.bullets <= 0:
            p1.score = -1
            p2.score = -1
            print(f"{p1.name} shot an invisible bullet!")
        elif p2.state == "shoot":
            if p2.bullets <= 0:
                p1.score = -1
                p2.score = -1
                print(f"{p2.name} shot an invisible bullet!")
            else:
                p1.bullets -= 1
                p2.bullets -= 1
                print("The bullets hit each other!")
        elif p2.state == "guard":
            if p2.guards <= 0:
                p1.score = -1
                p2.score = -1
                print(f"{p2.name} guarded too much!")
            else:
                p1.bullets -= 1
                p2.guards -= 1
                print(f"{p2.name} blocked {p1.name}'s bullet!")
        elif p2.state == "reload":
            p1.bullets -= 1
            p1.score += 1
            p2.bullets += 1
            print(f"{p1.name} hit {p2.name}!")
    elif p1.state == "guard":
        if p1.guards <= 0:
            p1.score = -1
            p2.score = -1
            print(f"{p1.name} guarded too much!")
        elif p2.state == "shoot":
            if p2.bullets <= 0:
                p1.score = -1
                p2.score = -1
                print(f"{p2.name} shot an invisible bullet!")
            else:
                p1.guards -= 1
                p2.bullets -= 1
                print(f"{p1.name} blocked {p2.name}'s bullet!")
        elif p2.state == "guard":
            if p2.guards <= 0:
                p1.score = -1
                p2.score = -1
                print(f"{p2.name} guarded too much!")
            else:
                p1.guards -= 1
                p2.guards -= 1
                print("Nothing happened :\\")
        elif p2.state == "reload":
            p1.guards -= 1
            p2.bullets += 1
            print(f"{p2.name} prank'd {p1.name}")
    elif p1.state == "reload":
        if p2.state == "shoot":
            if p2.bullets <= 0:
                p1.score = 3
                print(f"{p2.name} shot an invisible bullet!")
            else:
                p1.bullets += 1
                p2.bullets -= 1
                p2.score += 1
                print(f"{p2.name} hit {p1.name}!")
        elif p2.state == "guard":
            if p2.guards <= 0:
                p1.score = 3
                print(f"{p2.name} guarded too much!")
            else:
                p1.bullets += 1
                p2.guards -= 1
                print(f"{p1.name} prank'd {p2.name}")
        elif p2.state == "reload":
            p1.bullets += 1
            p2.bullets += 1
            print(f"{p1.name} and {p2.name} decided to take a break.")

if __name__ == "__main__":
    p1 = Player("Broski")
    p2 = RandomAI("Rick")

    status(p1, p2)
    while True:
        current_turn = 1
        for i in range(2):
            if current_turn == 1:
                while True:
                    try:
                        move = int(input(f"{p1.name}'s Turn...\n  1. Reload\n  2. Guard\n  3. Shoot\n"))
                        if move > 3:
                            raise ValueError
                        break
                    except:
                        print("Please input an integer!")
                
                if move == 1:
                    p1.state = "reload"
                elif move == 2:
                    p1.state = "guard"
                else:
                    p1.state = "shoot"
                
                current_turn = 2

            else:
                move = p2.analyze()
                if move == 1:
                    p2.state = "reload"
                elif move == 2:
                    p2.state = "guard"
                else:
                    p2.state = "shoot"

        time.sleep(1)
        calculate(p1, p2)
        time.sleep(1)
        if p1.score == 3:
            print(f"{p1.name} won!")
            break
        elif p2.score == 3:
            print(f"{p2.name} won!")
            break
        elif p1.score == -1 and p2.score == -1:
            print("Someone Cheated :(")
            break
        status(p1, p2)
        
