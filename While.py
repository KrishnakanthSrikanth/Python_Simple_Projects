import random
n=10
to_be_guessed =int(n*random.random())+1
print (random.random())
print(to_be_guessed)
guess=0

while guess != to_be_guessed:
    guess = int(input("Number is:"))
    if guess>0:
        if guess > to_be_guessed:
            print("large")
        elif guess < to_be_guessed:
            print ("Small")
    else:
            print ("Done of trying")
            break
else:
        print("Congo")