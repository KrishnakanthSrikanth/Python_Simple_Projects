#ForLoopInsideWhile Example---Bulk Reservation of tickets

print("Hi there..!")
travelling=input("yes or no:")

while travelling == 'yes':
    num=int(input("Enter number of people:"))
    for num in range(1,num+1):
        name=input("Name is:")
        age=input("Age is:")
        sex=input("M or F:")
        print(name)
        print(age)
        print(sex)
    travelling=input("Oops! Forgot someone...??")