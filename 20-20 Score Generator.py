#20-20 Score Generator

import random
n = 250
score_to_be_guessed = int(n * random.random()) + 1
print(score_to_be_guessed)
score_guess = 0

while score_guess != score_to_be_guessed:
    score_guess = int(input("Enter your guess value:"))
    diff = score_to_be_guessed - score_guess
    if diff!=0:
        if score_guess<1 or score_guess>250:
            print("Reduce your expection for 20-20 cricket")
        elif abs(diff)<=10:
            print("Close by,You are a True Indian Fan")
        elif abs(diff)>10:
            print("You don't watch that much!")
else:
    print("You guessed it right champ..!!")