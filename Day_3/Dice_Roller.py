#start with default die and how to roll it. 
import random
import sys
import time

try:
    Dice_default = [1, 2, 3, 4, 5, 6]
    dice_default_roll = random.choice(Dice_default)

    Number_Dice = 0
    Sides_of_Dice = 0

    while True:
        try:
            Number_Dice = int(input("\nHow many dice do you want to play with? "))
            if Number_Dice <= 0:
                print("Please only enter numbers between 1 and 100")
                continue
            if Number_Dice > 100:
                print("Please only enter numbers between 1 and 100")
                continue
            else:
                break
        except ValueError:
            print("Please only enter a number. No words, blank spaces, or characters allowed.")
            continue

    while True:
        try:
            Sides_of_Dice = int(input("\nHow many sides per die do you want? "))
            if Sides_of_Dice <= 0:
                print("Please only enter numbers between 1 and 100")
                continue
            if Sides_of_Dice > 100:
                print("Please only enter numbers between 1 and 100")
                continue
            else:
                break
        except ValueError:
            print("Please only enter a number. No words, blank spaces, or characters allowed.")
            continue

    Dice_List = list(range(1, Number_Dice + 1))
    Sides_List = list(range(1, Sides_of_Dice + 1))

    Dice_Result = [None] * len(Dice_List)

    print("\n")

    for i in Dice_List:
        Dice_Result[i-1] = random.choice(Sides_List)
        print(f"Roll {i}:", Dice_Result[i - 1])

    print(f"\nSum of all rolls: {sum(Dice_Result)}")
    print(f"Min Roll: {min(Dice_Result)}")
    print(f"Max Roll: {max(Dice_Result)}")

    while True:
        Sorted_YN = input("Would you like your rolls sorted from lowest to highest? Yes or No. ")
        Sorted_YN = Sorted_YN.upper()
        if Sorted_YN == "YES":
            print(sorted(Dice_Result))
            exit()
        if Sorted_YN == "NO":
            break
except KeyboardInterrupt:
    print("\nCanceled by user. ")
    sys.exit(130)

