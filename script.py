#!bin/python3


from random import randint
def dice_rolling_simulator():
    dice = randint(1, 6)
    print ("This program is a simulator that rolls a six faced die and outputs the number of the side facing up")
    guess = input("Do you want to guess what side is facing up? ")
    
    if guess == "Yes" or guess == "yes" or guess == "y" or guess == "YES":
        test = input("What is your guess? ")
        if test == dice:
            print("You guessed right")
        else:
            print("You guessed wrong")
            print("The number was ", dice)
    else:
        print ("The number of the side of the die facing up is", dice)
    answer = input("Would you like to roll again?")
    
    while answer == "Yes" or answer == "yes" or answer == "YES" or answer == "y":
            dice = randint(1, 6)
            
            if guess == "Yes" or guess == "yes" or guess == "y" or guess == "YES":
                test = input("What is your guess? ")
                if test == dice:
                    print("You guessed right")
                else:
                    print("You guessed wrong")
                    print("The number was ", dice)
            else:
                print ("The number of the side of the die facing up is", dice)
            answer = input("Would you like to roll again?")
        
dice_rolling_simulator()

