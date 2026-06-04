import random
SWG = ["snake","water","gun"]
computer = random.choice(SWG)
turns = 1
pwc = 0 #Player Win Count
cwc = 0 #Computer Win Count
while turns<=10:
    player = input("snake , water or gun?: ").lower()
    if player == computer:
        print("Tie")
        pwc+=1
        cwc+=1
    elif player == "gun":
        if computer == "water":
            print("You LOSE, because your gun drowned in the computer's water.")
            cwc+=1
        else:
            print("You WIN, because your gun killed the computer's snake.")
            pwc+=1
    elif player == "water":
        if computer == "snake":
            print("You LOSE, because the computer's snake drank up your water.")
            cwc+=1
        else:
            print("You WIN, because the computer's gun drowned in your water.")
            pwc+=1
    elif player == "snake":
        if computer == "gun":
            print("You LOSE, because the gun killed your snake.")
            cwc+=1
        else:
            print("You WIN, because your snake drank the computer's water.")
            pwc+=1
    else:
        print("Check your spelling !!!")
        turns+=1
        continue
    computer = random.choice(SWG)
    turns+=1

if turns > 10:
    print("\n==================================================")
    print("||                                              ||")
    print("||                 GAME OVER                    ||")
    print("||                                              ||")
    print("==================================================")

    print("\nPlayer Total Wins   --->", pwc)
    print("Computer Total Wins --->", cwc)

print("==================================================")

if pwc > cwc:
    print("**************************************************")
    print("*                                                *")
    print("*          CONGRATULATIONS! YOU WON!             *")
    print("*                                                *")
    print("**************************************************")

elif pwc == cwc:
    print("**************************************************")
    print("*                                                *")
    print("*               GAME TIED!                       *")
    print("*                                                *")
    print("**************************************************")

else:
    print("**************************************************")
    print("*                                                *")
    print("*            BETTER LUCK NEXT TIME!              *")
    print("*                YOU LOST!                       *")
    print("*                                                *")
    print("**************************************************")
