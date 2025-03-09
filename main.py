import random

guess = random.randint(1, 10)
count = 0
while True :
    player = int(input("Enter a number between 1 to 10 : "))
    count+=1
    
    if player > guess :
        print("lower number please !")
    
    elif player < guess :
        print("Higher number please!")
        
    else :
        print("You Guessed Correctly !\n")
        print(f"Number of guesses : {count} ")
        break