#Importing pandas library
import pandas as pd

#Importing our input data file
input_file = pd.read_csv('grocery_sales.csv')

#Filling up missing data in the input file
avg_value = input_file['sales'].mean()  #Getting mean value to fill the blanks
input_file['sales'].fillna(value = avg_value, inplace = True)

#Sum the column sales
sum_sales = input_file.groupby('transaction_date')['sales'].sum()

#plot the values in a graph
sum_sales.plot(rot = 45)
