#Getting the max number upto which we have to check
n = int(input("Enter a number:"))

#creating a range with the input number
num_range = set(range(2, n+1))

#creating an empty list, to which we append our values later
prime_list = []

#creating loop to iterate over the elements
while num_range:
    prime = num_range.pop() #Getting the lowest number from the range
    prime_list.append(prime) #Appending the value to the list
    multiples = set(range(prime*2, n+1, prime)) #Creating a range to get the multiples of number that resulted from prime variable and having a step count of the same
    num_range.difference_update(multiples) #removing the same elements from both the sets and having only the different values

total_count = len(prime_list) #Get count of values in the list
max_value = max(prime_list) #Get the maximum value in the list
print(f"There are {total_count} in the list from 2 to {n}. The largest of it is {max_value}")
