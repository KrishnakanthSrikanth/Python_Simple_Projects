#For loop example--- To find Factorial of a number

number=int(input("Number is"))
fact=1

if number < 0:
    print ("Value must be positive")
elif number ==0:
    print ("Factorial is 1")
else:
    for i in range(1, number+1):
        fact =fact*i
print(fact)

