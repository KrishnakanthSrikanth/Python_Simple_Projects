# NestedWhileLoopExample---Simulation of an ATM

print("Welcome..!")
restart = 'Y'
bal = 22.22
chances = 3
while chances >= 0:
    pin = int(input("Enter pin:"))
    if pin == (1234):
        print("Entered pin is Correct\n")
        while restart not in ('N', 'NO', 'n', 'no'):
            print("Press 1 for knowing available balance \n")
            print("Press 2 for withdraw \n")
            print("Press 3 for pay in \n")
            print("Press 4 for return card \n")
            option = int(input("Enter value"))
            if option == 1:
                print("Your balance is: ", bal)
                restart = input("Go back?")
                if restart in ('n', 'N', 'NO', 'no'):
                    print("Thank You!")
                    break
            elif option == 2:
                option2 = 'y'
                withdrawal = float(input("How much?\n"))
                if withdrawal in [10, 20, 40, 60, 80, 100]:
                    bal = bal - withdrawal
                    print("\nYour current balance is: ", bal)
                    restart = input("Go back?")
                    if restart in ('n', 'N', 'NO', 'no'):
                        print("Thank You!")
                        break
                elif withdrawal != [10, 20, 40, 60, 80, 100]:
                    print("Incorrect value.. please re-try!\n")
                    restart = 'y'
                elif withdrawal == 1:
                    withdrawal = float(input("Enter amount:"))
            elif option == 3:
                Pay_in = float(input("Enter amount:"))
                bal = bal + Pay_in
                print("\nYour current balance is: ", bal)
                restart = input("Go back?")
                if restart in ('n', 'N', 'NO', 'no'):
                    print("Thank You!")
                    break
            elif option == 4:
                print("Please wait your card will be returned shortly..\n")
                print("Thank you for the service..!")
                break
            else:
                print("Enter correct pin\n")
                restart = 'y'
    elif pin != ('1234'):
        print("Incorrect pin")
        chances = chances - 1
        if chances == 0:
            print("\n No more tries sorry..")
            print("Thank you for your cooperation ")
            break
