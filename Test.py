# dict = {'Emp': {'GK': {'ID': '001', 'Salary': '2000', 'Designation': 'ASE'},
#                 'KK': {'ID': '002', 'Salary': '2500', 'Designation': 'Tech-Lead'},
#                 'AK': {'ID': '003', 'Salary': '3000', 'Designation': 'Senior Tech-Lead'},
#                 'OK': {'ID': '004', 'Salary': '4000', 'Designation': 'Manager'}}}
# type(dict)
# print(dict)
# type(dict)
#
# import pandas
# asDF=pandas.DataFrame(dict['Emp'])
# print(asDF)

# def func(x):
#     return (lambda y: x + y)
# a = func(2)
# b = func(3)
# print(a(10))
# print(b(-1,9))

# my_list=[4,5,6,7,8,9]
# new_list=list(filter(lambda a:(a%2==0),my_list))
# print(new_list)

# my_list=[4,5,6,7,8,9]
# new_list=list(map(lambda a:(a%2==0),my_list))
# print(new_list)

# from functools import reduce
# my_list=[1,2,3,4,5]
# p=reduce(lambda a,b:a/b==0,my_list)
# print(p)
#-----------------------------------------------------------------------------------------------------------------------
def userinput1():
    n = int(input("Enter value for n:"))
    return n

def userinput2():
    k = int(input("Enter value for k:"))
    return k

def test(n, k):
    # Checking k is prime or not
    if k > 2:
        for i in range(2, k):
            if k % i == 0:
                print("Entered invalid 'k' value")
                break
        else:
            print("'k' is prime")
    elif k == 2:
        print("'k' is prime")
    else:
        print("Invalid 'k'")

    original_list = []

    for i in range(1, n + 1):
        if (i % k == 0):
            abc = i // k
            while (abc % k == 0):
                cba = abc // k
                abc = cba
            original_list.append(abc)
        else:
            original_list.append(i)
    #print("original_list is:", original_list)
    print(sum(original_list))

def result():
    input1 = userinput1()
    input2 = userinput2()
    primecheck = test(input1, input2)


result()
