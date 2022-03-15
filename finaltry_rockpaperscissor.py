import random

cards = ["rock", "paper", "scissor"]

def point(i):
    while i >= -2 <= 2:
        u = input()
        comp = random.choice(cards)
        print(u)
        print(comp)
        if (u == 'rock' and comp == 'scissor') or (u == 'paper' and comp == 'rock') or (
                u == 'scissor' and comp == 'paper'):
            print("user gets +1")
            i += 1
        elif u == comp:
            print("user gets 0")
            i += 0
        else:
            print("user gets -1!")
            i += -1
        print(i)
        if i == 2:
            print("You won!!")
        if i == -2:
            break
    print("Game over")


print(point(i=0))
