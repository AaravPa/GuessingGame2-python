from random import randrange

randNum = randrange(1,9)
numOfTries=5
#print(randNum)
guess1=input("5 tries: Guess number here:")
guess1=int(float(guess1))
if guess1 == randNum :   
    print("Congratulations! You guessed the number!")
elif numOfTries>0 & guess1 != randNum:
    if guess1 > randNum :
        guess1 = "Less"
    else :
        guess1 = "Greater"
    numOfTries=numOfTries-1
    print(guess1,"than the number you guessed.",)
    guess2=input("4 tries left: Guess number here:")
    guess2=int(float(guess2))
    if guess2 == randNum :
        print("Congratulations! You guessed the number!")
    elif numOfTries>0 & guess2 != randNum:
        if guess2 > randNum :
            guess2 = "Less"
        else :
            guess2 = "Greater"
        numOfTries=numOfTries-1
        print(guess2,"than the number you guessed.",)
        guess3=input("3 tries left: Guess number here:")
        guess3=int(float(guess3))
        if guess3 == randNum :
            print("Congratulations! You guessed the number!")
        elif numOfTries>0 & guess3 != randNum:
            if guess3 > randNum :
                guess3 = "Less"
            else :
                guess3 = "Greater"
            numOfTries=numOfTries-1
            print(guess3,"than the number you guessed.",)
            guess4=input("2 tries left: Guess number here:")
            guess4=int(float(guess4))
            if guess4 == randNum :
                print("Congratulations! You guessed the number!")
            elif numOfTries>0 & guess4 != randNum:
                if guess4 > randNum :
                    guess4 = "Less"
                else :
                    guess4 = "Greater"
                numOfTries=numOfTries-1
                print(guess4,"than the number you guessed.",)
                guess5=input("1 tries left: Guess number here:")
                guess5=int(float(guess5))
                if guess5 == randNum :
                    print("Congratulations! You guessed the number!")
                elif numOfTries>0 & guess5 != randNum:
                    numOfTries=numOfTries-1
                    print("Out of tries: Better luck next time!")
    
    
    
    
    
    
    
